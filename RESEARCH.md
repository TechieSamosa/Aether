# 🔬 AETHER Research Contributor Guide

This document defines the boundaries between **open-source engineering contributions** and **academic research contributions** for the AETHER project.

---

## 🔒 Core Architecture: Protected

The following components constitute the intellectual property of the AETHER core research team and are **locked from external modification**:

| Protected Component | Location | Reason |
|---|---|---|
| Zero-DCE Network Architecture | `src/models/zero_dce.py` | Novel adaptation for panchromatic lunar imagery |
| Self-Supervised Loss Functions | `src/losses/zero_ref.py` | Custom-tuned loss weights for PSR noise floor |
| Two-Phase Training Curriculum | `notebooks/kaggle_training.ipynb` | Core methodological contribution of the paper |
| Inference Tile-Blending Pipeline | `src/inference/pipeline.py` | Bartlett-window reconstruction algorithm |

> **Why?** These components form the basis of a scientific research paper currently in preparation. Unauthorized modifications could compromise the reproducibility and academic integrity of the published results. We must be able to point to a single, canonical implementation.

Pull Requests that modify any of the above files will be **rejected without review**.

---

## 🧪 The Research Contributor Path

We recognize that some contributors possess deep expertise in Machine Learning, Computer Vision, or Planetary Science that goes beyond standard engineering contributions. For these individuals, we offer the **Research Contributor Path**.

### Who Qualifies?

To be considered for the Research Contributor Path, you must demonstrate verifiable expertise through **at least one** of the following:

- 📄 **Published work** (conference papers, journal articles, preprints on arXiv) in Computer Vision, Image Processing, or Remote Sensing.
- 🏆 **Kaggle rankings** (Competitions Expert or higher, or a top-10% finish in a relevant image processing competition).
- 🔧 **Open-source ML history** (maintainer or significant contributor to an established ML library or research codebase).

### How to Apply

1. Open a **GitHub Issue** with the title format: `[Research Proposal] <Your Topic>`.
2. Include:
   - A brief description of your proposed research direction.
   - Links to your credentials (publications, Kaggle profile, GitHub repos).
   - A rough technical approach (1–2 paragraphs).
   - Expected deliverables (code, benchmarks, report).
3. The core team will review and respond within 7 days.

---

## 🎯 Open Research Directions

The following areas are **explicitly open** for Research Contributors. These do not touch the core model architecture but can significantly improve the overall pipeline quality.

### 1. Deep Learning Alternatives to Classical NLM Denoising
**Current state:** We use Non-Local Means (NLM) as a post-processing denoiser. It works, but it's slow and has fixed parameters.  
**Opportunity:** Implement and benchmark a learned denoiser such as **DnCNN**, **FFDNet**, or **Restormer** as a drop-in replacement. The denoiser must:
- Accept single-channel (grayscale) float32 input.
- Be lightweight enough to run on a single GPU with the existing tile-based inference pipeline.
- Preserve scientific features (crater rims, boulders) without hallucinating texture.

### 2. Adaptive CLAHE Parameter Optimization
**Current state:** CLAHE is applied with fixed `clipLimit=2.0` and `tileGridSize=(8,8)`.  
**Opportunity:** Build an adaptive parameter selector that analyzes the local noise statistics and terrain type of each tile to dynamically choose optimal CLAHE parameters. This could be rule-based or a small learned model.

### 3. Native PyTorch No-Reference Image Quality Assessment
**Current state:** We rely on `pyiqa` for NIQE, BRISQUE, and PIQE metrics, which introduces a heavy dependency tree.  
**Opportunity:** Implement **BRISQUE**, **NIQE**, and **PIQE** as standalone PyTorch modules (no external dependencies) that can be used both as evaluation metrics and as differentiable loss functions during training.

### 4. Learned PSR-vs-Sunlit Patch Classifier
**Current state:** We classify patches as `psr`, `sunlit`, or `mixed` using a simple photometric threshold (mean pixel brightness).  
**Opportunity:** Train a lightweight binary classifier (e.g., a small ResNet or EfficientNet) that can more accurately distinguish PSR patches from sunlit patches, especially in the ambiguous "mixed" boundary regions. This classifier would replace the heuristic in `scripts/extract_patches.py`.

### 5. SAR-Optical Fusion Module
**Current state:** We only use optical (OHRC) data.  
**Opportunity:** Design a fusion module that combines DFSAR (Dual-Frequency Synthetic Aperture Radar) data with enhanced OHRC imagery to provide sub-surface context. This is a significant research undertaking and would likely result in co-authorship consideration.

---

## 📜 Intellectual Property & Co-Authorship

- **Standard Engineering PRs** (data scrapers, memory optimization, testing, documentation): Recognized in the **Acknowledgements** section of publications and in the repository's Hall of Fame.
- **Research Contributor PRs** (novel denoiser, learned classifier, SAR fusion): Evaluated on a case-by-case basis for potential **co-authorship** on subsequent publications, depending on the significance and novelty of the contribution.

This distinction is made transparently and in good faith. We want to reward meaningful intellectual contributions appropriately.
