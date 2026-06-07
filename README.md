# 🌌 AETHER: Illuminating the Unseen 🌗

<div align='center'>
  <img src="https://img.shields.io/badge/GirlScript_Summer_of_Code-2026-F96F59?style=for-the-badge&logo=girlscript" alt="GSSoC 26">
  <img src="https://img.shields.io/badge/Project%20Status-Active-brightgreen?style=for-the-badge" alt="Project Status">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blueviolet?style=for-the-badge" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-PyTorch-orange?style=for-the-badge" alt="Framework">
</div>

<div align='center'>
  <img src="https://img.shields.io/github/contributors/TechieSamosa/Aether?style=for-the-badge&color=blue" alt="GitHub contributors">
  <img src="https://img.shields.io/github/last-commit/TechieSamosa/Aether?style=for-the-badge&color=brightgreen" alt="GitHub last commit">
  <img src="https://img.shields.io/github/issues-pr/TechieSamosa/Aether?style=for-the-badge&color=aqua" alt="GitHub PR Open">
  <img src="https://img.shields.io/github/repo-size/TechieSamosa/Aether?style=for-the-badge&color=lightgrey" alt="Repo Size">
</div>

<div align='center'>
  <br>
  <img src="docs/images/before_after_sample.png" alt="AETHER Enhancement Results" width="90%">
  <br>
  <em>Left: Raw OHRC telemetry of a Permanently Shadowed Region (pitch black). Right: AETHER-enhanced output revealing hidden crater topography.</em>
  <br><br>
</div>

-----

## 🚀 Overview

**AETHER** is a deep learning framework designed to solve one of the most significant challenges in planetary science: visualizing the **Permanently Shadowed Regions (PSRs)** of the Moon. These areas, which haven't seen sunlight in billions of years, are prime locations for water ice but are notoriously difficult to image. Using a rich suite of data from ISRO's **Chandrayaan-2** mission, AETHER employs **Zero-Reference Deep Curve Estimation (Zero-DCE)** to enhance faint signals, transforming noisy, low-light patches into scientifically valuable maps without synthesizing fake details.

-----

## ✨ Key Features

* **Zero-Reference Enhancement**: Utilizes a highly efficient, lightweight CNN to dynamically estimate pixel-wise exposure curves, completely eliminating the need for paired ground-truth lunar imagery.
* **Multi-Modal Data Fusion**: Intelligently integrates optical (OHRC), radar (DFSAR), elemental (CLASS), and spectral (IIRS) data to create a holistic and information-rich view of the lunar surface.
* **Scientific Integrity**: Rejects hallucination-prone generative models in favor of physically grounded exposure scaling combined with Non-Local Means (NLM) spatial denoising, maximizing the Signal-to-Noise Ratio (SNR).
* **Mission-Ready Outputs**: Produces high-resolution, georeferenced polar maps critical for landing site selection, resource prospecting, and geomorphological studies.

-----

## 🛠️ Technical Architecture

AETHER is built with a modern, research-focused tech stack designed for high-performance computing and reproducibility.

* **Core Framework**: **PyTorch** for its flexibility and dynamic computation graphs.
* **Data Handling**: **GDAL** & **Rasterio** for geospatial data processing, **Pandas** for metadata management.
* **Image Processing**: **OpenCV** and **Scikit-Image** for preprocessing and classical enhancement algorithms.
* **Models & Training**: **Hugging Face Accelerate** for distributed training and **Weights & Biases** for experiment tracking.
* **Hardware**: Designed for **NVIDIA GPUs** using **CUDA** for accelerated model training.

-----

## 🧠 Methodology

Our pipeline transforms raw, heterogeneous data into clear, scientifically-valuable maps. The cornerstone of AETHER is its two-phase training curriculum designed specifically for the extreme noise floor of lunar PSRs.

### 1\. Multi-Modal Data Ingestion & Fusion

We treat the lunar surface as a multi-layered dataset. Each instrument provides a unique layer of information, and by combining them, we create a "super-image" that offers far more context than a simple photograph.

* 🛰️ **Primary Optical Data (OHRC):** This is the high-resolution visual canvas we aim to enhance.
* 🪨 **Structural & Texture Data (DFSAR):** The radar data acts as our structural blueprint, revealing physical topography unaffected by shadows.
* 🧪 **Elemental Composition Data (CLASS):** Provides the chemical fingerprint, mapping elements like Silicon, Iron, and Magnesium.
* 💧 **Mineralogical & Volatile Data (IIRS):** The infrared spectrometer identifies specific minerals and the spectral signature of water ice.
* 🗺️ **Geometric & Navigational Data (SPICE):** SPICE kernels align all layers perfectly into a single, cohesive coordinate system.

### 2\. Phase 1: Synthetic Adaptation

Because true "bright" ground-truth images of PSRs do not exist, we simulate them. We take sunlit OHRC patches, synthetically darken them, and inject them with mixed Poisson-Gaussian noise to match the sensor's noise floor. The model is supervised on these synthetic pairs to learn basic feature recovery.

### 3\. Phase 2: Zero-Reference Fine-Tuning

The pre-trained model is fine-tuned on actual pitch-black PSR patches. Using mathematical loss functions (Spatial Consistency, Exposure Control, and Illumination Smoothness), the model learns to enhance the true secondary scattered light without relying on a reference image.

### 4\. Inference & Denoising

The massive OHRC images are processed in overlapping tiles to manage memory. Because enhancing a faint signal amplifies existing sensor noise, the raw Zero-DCE output is passed through a Non-Local Means (NLM) spatial denoiser and CLAHE to clean the image and reveal the physical topography before final map synthesis.

-----

## 🌍 Impact & Applications

AETHER directly contributes to the next era of lunar exploration by:

* **Enabling Safer Landings**: Providing mission planners with clear, detailed views of potential landing sites for robotic and crewed missions.
* **Accelerating Scientific Discovery**: Unlocking vast, unexplored regions for geological analysis and the search for water ice.
* **Advancing Planetary AI**: Pioneering the use of zero-reference techniques for low-data, extreme-environment scenarios in space exploration.

-----
## 📂 Repository Structure

```text
aether/
│
├── data/                  # Utilities for ISRO PRADAN data scraping and bulk downloading
├── notebooks/             # Jupyter notebooks for Exploratory Data Analysis (EDA)
├── models/                # Pre-trained model weights (Zero-DCE)
│
├── src/                   # 🔒 Core Research Modules (Restricted for Open Source PRs)
│   ├── data_io/           # PDS4 XML metadata parsing and raw .img ingestion
│   ├── models/            # Deep learning architectures (Zero-DCE, NLM Denoiser)
│   └── projection/        # GDAL/Rasterio geospatial mapping and map synthesis
│
├── scripts/               # Executable pipeline scripts
│   ├── extract_patches.py # Sliding-window patch extraction and categorization
│   └── infer.py           # Model inference, NLM spatial denoising, and blending
│
├── tests/                 # Unit and integration tests (pytest)
├── CONTRIBUTING.md        # Vital guidelines, IP rules, and GSSoC roadmap
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

```

## 🚀 Getting Started

### **Prerequisites**

* Python 3.10+
* Anaconda or Miniconda
* NVIDIA GPU with CUDA 11.8+

### **Installation**

1. Clone the repository:
```bash
git clone [https://github.com/TechieSamosa/AETHER.git](https://github.com/TechieSamosa/AETHER.git)
cd AETHER

```


2. Create and activate a conda environment:
```bash
conda env create -f environment.yml
conda activate aether

```


3. Run inference on a sample image:
```bash
python scripts/enhance.py --input /path/to/sample.img --output /path/to/enhanced.png --model models/aether_v1.pth

```



---

## 🎯 How to Contribute (GSSoC '26)

We are thrilled to be a part of **GirlScript Summer of Code 2026**! We welcome contributions from the global community, specifically focusing on data engineering, memory optimization, and pipeline automation.

### ⚠️ Important: Academic IP & Authorship

The AETHER framework is the foundation of an upcoming scientific research paper. **The core mathematical architecture and deep learning models in the `src/` directory are strictly locked.** Before making any pull requests, you **must** read our [CONTRIBUTING.md](https://www.google.com/search?q=CONTRIBUTING.md) to understand the strict boundaries between open-source engineering contributions and academic co-authorship. By interacting with this repository, you automatically agree to these terms.

### Getting Started:

1. **Read the Docs:** Review our [Contributor Guide & Technical Roadmap](https://www.google.com/search?q=CONTRIBUTING.md) to understand how we source Chandrayaan-2 data.
2. **Find an Issue:** Look for issues tagged `good first issue`, `gssoc-26`, or `help wanted`.
3. **Focus Areas:** We are actively looking for PRs related to:
* Automated web-scraping for ISRO PRADAN data.
* PyTorch DataLoader memory optimization.
* GIS map stitching using GDAL/Rasterio.
* Unit testing and code documentation.



---

## 📚 References & Acknowledgements

This work builds upon the state-of-the-art in deep learning and planetary science. We gratefully acknowledge the data provided by the **ISRO Science Data Archive (ISDA)**.

* **"Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement"** (Guo et al., 2020)
* **"Peering into lunar permanently shadowed regions with deep learning"** (Bickel et al., 2021)
* **Chandrayaan-2 Mission Data Handbook**, ISRO
* **"Analysis of Permanently Shadowed Regions of the Moon using LRO and Chandrayaan-2 Data"**

---

## 🔬 Core Research Team

AETHER’s core architecture, deep learning methodology, and academic research are developed and maintained by:

* **Aditya Sachin Khamitkar** (Lead Architect & Researcher)
* **Tushar** (Core Researcher)
* **Nitin** (Core Researcher)

---

## 🏅 Open Source Contributors

A huge thank you to the global developers and GSSoC '26 mentees who have optimized our pipelines, improved our data ingestion, and helped scale AETHER! Impactful engineering contributions are automatically recognized here.

### 🏆 AETHER Hall of Fame

| Contributor (GitHub Handle) | Tier | Specific Contribution |
|---|---|---|
| `@example-contributor` | 🥇 Gold | Implemented automated PRADAN data scraper, reducing manual download time by 95% |
| | | |

> **How to get listed:** Make a meaningful, merged PR. Tiers are assigned by the core team based on impact: 🥇 Gold (architectural/high-impact), 🥈 Silver (significant feature/optimization), 🥉 Bronze (bug fixes, docs, tests).

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details. This permissive license allows for wide use and collaboration.



