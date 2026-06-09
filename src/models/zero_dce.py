"""
Zero-DCE: Zero-Reference Deep Curve Estimation
===============================================
Self-supervised low-light image enhancement — no paired data required.

The network estimates pixel-wise light-enhancement curve maps A(t)
that are iteratively applied to brighten dark images:

    Î(t) = Î(t-1) + A(t) · Î(t-1) · (1 - Î(t-1))

This is a monotonic mapping in [0,1] — dark pixels get brighter,
already-bright pixels barely change. No clipping, no inversion.

Architecture: 7-layer CNN with symmetric skip connections, ~80K params.
              Input: (B, 1, H, W) → Output: (B, 1, H, W) enhanced

Reference:
    Guo, C. et al. (2020). "Zero-Reference Deep Curve Estimation
    for Low-Light Image Enhancement." CVPR 2020.
    plan.pdf, Chapter 5.3
"""
from typing import Tuple, Optional, Dict, Any
import torch
import torch.nn as nn


class ZeroDCE(nn.Module):
    """Zero-Reference Deep Curve Estimation Network.

    Lightweight CNN (~80K parameters) that estimates n_iter curve maps
    for iterative image enhancement. Works on single-channel panchromatic
    images (adapted from the original 3-channel RGB version).

    Args:
        n_iter: Number of curve iterations (default: 8).
                More iterations = finer control but more curve maps to estimate.
        in_channels: Input channels (1 for panchromatic OHRC, 3 for RGB).
        base_channels: Base filter count (32 in original paper).
    """

    def __init__(
            self,
            n_iter: int = 8,
            in_channels: int = 1,
            base_channels: int = 32,
    ) -> None:
        super().__init__()
        self.n_iter = n_iter
        ch = base_channels

        # Encoder path (layers 1-4)
        self.conv1 = nn.Conv2d(in_channels, ch, 3, padding=1, padding_mode='replicate', bias=True)
        self.conv2 = nn.Conv2d(ch, ch, 3, padding=1, padding_mode='replicate', bias=True)
        self.conv3 = nn.Conv2d(ch, ch, 3, padding=1, padding_mode='replicate', bias=True)
        self.conv4 = nn.Conv2d(ch, ch, 3, padding=1, padding_mode='replicate', bias=True)

        # Decoder path with skip connections (layers 5-7)
        # Skip: layer5 gets concat(layer3, layer4) → 2*ch input
        # Skip: layer6 gets concat(layer2, layer5) → 2*ch input
        # Skip: layer7 gets concat(layer1, layer6) → 2*ch input
        self.conv5 = nn.Conv2d(ch * 2, ch, 3, padding=1, padding_mode='replicate', bias=True)
        self.conv6 = nn.Conv2d(ch * 2, ch, 3, padding=1, padding_mode='replicate', bias=True)

        # Output: n_iter curve maps per input channel
        self.conv7 = nn.Conv2d(
            ch * 2, n_iter * in_channels, 3, padding=1, padding_mode='replicate', bias=True
        )

        self.relu = nn.ReLU(inplace=True)
        self.in_channels = in_channels

        # Initialize weights
        self._init_weights()

    def _init_weights(self) -> None:
        """Xavier initialization for stable training."""
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_uniform_(m.weight)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    

    def forward(
           self,
           x: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Forward pass: estimate curve maps and apply enhancement.

        Args:
            x: Input image tensor, shape (B, C, H, W), values in [0, 1]

        Returns:
            enhanced: Enhanced image, shape (B, C, H, W), values in [0, 1]
            curve_maps: All curve maps, shape (B, n_iter*C, H, W)
        """
        # Encoder
        x1 = self.relu(self.conv1(x))    # (B, ch, H, W)
        x2 = self.relu(self.conv2(x1))   # (B, ch, H, W)
        x3 = self.relu(self.conv3(x2))   # (B, ch, H, W)
        x4 = self.relu(self.conv4(x3))   # (B, ch, H, W)

        # Decoder with symmetric skip connections
        x5 = self.relu(self.conv5(torch.cat([x3, x4], dim=1)))  # (B, ch, H, W)
        x6 = self.relu(self.conv6(torch.cat([x2, x5], dim=1)))  # (B, ch, H, W)

        # Curve maps via tanh → values in (-1, 1)
        A = torch.tanh(self.conv7(torch.cat([x1, x6], dim=1)))
        # A shape: (B, n_iter * C, H, W)

        # Apply iterative curve adjustment
        enhanced = x.clone()
        for i in range(self.n_iter):
            # Extract curve map for this iteration
            curve = A[:, i * self.in_channels:(i + 1) * self.in_channels, :, :]
            # Apply the light-enhancement curve
            enhanced = enhanced + curve * enhanced * (1 - enhanced)

        # Clamp to valid range
        enhanced = torch.clamp(enhanced, 0.0, 1.0)

        return enhanced, A

    def count_parameters(self) -> int:
        """Count total trainable parameters."""
        return sum(p.numel() for p in self.parameters() if p.requires_grad)



def build_zero_dce(
    config: Optional[Dict[str, Any]] = None
) -> ZeroDCE:
    """Factory function to build Zero-DCE from config dict.

    Args:
        config: Dict with optional keys: n_iter, in_channels, base_channels

    Returns:
        Initialized ZeroDCE model
    """
    if config is None:
        config = {}

    model = ZeroDCE(
        n_iter=config.get('n_iter', 8),
        in_channels=config.get('in_channels', 1),
        base_channels=config.get('channels', 32),
    )

    return model


if __name__ == '__main__':
    """Quick sanity check: verify model shapes and parameter count."""
    print("Zero-DCE Model Sanity Check")
    print("=" * 40)

    model = ZeroDCE(n_iter=8, in_channels=1, base_channels=32)
    print(f"Parameters: {model.count_parameters():,}")

    # Test forward pass
    x = torch.randn(2, 1, 64, 64)  # Batch of 2, single-channel, 64x64
    x = torch.clamp(x * 0.1 + 0.05, 0, 1)  # Simulate dark PSR image

    enhanced, A = model(x)
    print(f"Input shape:    {x.shape}")
    print(f"Output shape:   {enhanced.shape}")
    print(f"Curve maps:     {A.shape}")
    print(f"Input range:    [{x.min():.3f}, {x.max():.3f}]")
    print(f"Output range:   [{enhanced.min():.3f}, {enhanced.max():.3f}]")
    print(f"Mean brightness: {x.mean():.3f} → {enhanced.mean():.3f}")

    # Verify gradient flow
    loss = enhanced.mean()
    loss.backward()
    grad_ok = all(p.grad is not None for p in model.parameters())
    print(f"Gradient flow:  {'✅ OK' if grad_ok else '❌ BROKEN'}")
    print("=" * 40)
