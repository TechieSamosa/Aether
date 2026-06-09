# Zero-DCE: DCE-Net Architecture Diagram

This document provides a visual diagram of how the 7-layer CNN (DCE-Net)
produces the 8 curve parameter maps used in the Zero-DCE low-light
image enhancement process.

## Architecture Overview

```mermaid
flowchart TD
    A["🖼️ Low-light input image\nH × W × 3 (RGB)"]

    A --> L1["Conv Layer 1\n32 filters · 3×3 · stride 1 · ReLU"]
    L1 --> L2["Conv Layer 2\n32 filters · 3×3 · stride 1 · ReLU"]
    L2 --> L3["Conv Layer 3\n32 filters · 3×3 · stride 1 · ReLU"]
    L3 --> L4["Conv Layer 4 — Bottleneck\n32 filters · 3×3 · stride 1 · ReLU"]
    L4 --> L5["Conv Layer 5 + skip from L3\n32 filters · 3×3 · ReLU · concat"]
    L5 --> L6["Conv Layer 6 + skip from L2\n32 filters · 3×3 · ReLU · concat"]
    L6 --> L7["Conv Layer 7 — Output\n24 filters · 3×3 · Tanh"]
    L7 --> OUT["✅ 8 curve parameter maps α₁…α₈\n3 RGB maps × 8 iterations = 24 channels"]

    L2 -.->|"skip connection"| L6
    L3 -.->|"skip connection"| L5

    style A   fill:#185FA5,color:#fff
    style L4  fill:#0F6E56,color:#fff
    style L7  fill:#993C1D,color:#fff
    style OUT fill:#854F0B,color:#fff
```

## Key Design Decisions

| Property | Value | Reason |
|---|---|---|
| Layers | 7 conv layers | Lightweight (~79K params) |
| Filters (L1–L6) | 32, kernel 3×3 | Capture local features |
| Activation (L1–L6) | ReLU | Non-linearity without vanishing gradients |
| Activation (L7) | Tanh | Constrains output to [-1, 1] |
| Skip connections | L2→L6, L3→L5 | Symmetrical, preserves spatial detail |
| Output channels | 24 (3 × 8) | One α map per RGB channel per iteration |
| No pooling / BN | Intentional | Preserves neighboring pixel relationships |

## How the Curve Parameters Work

Each of the **8 iterations** applies a Light-Enhancement (LE) curve:
LE(I; α) = I + α · I · (1 - I)
Where `α` is the pixel-wise curve parameter map predicted by DCE-Net.
The curve is applied **iteratively** to progressively brighten the image
without clipping highlights.

## References

- Paper: [Zero-Reference Deep Curve Estimation (CVPR 2020)](https://arxiv.org/abs/2001.06826)
- Authors: Chunle Guo et al.