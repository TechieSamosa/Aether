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

-----

## 🚀 Overview

**AETHER** is a deep learning framework designed to solve one of the most significant challenges in planetary science: visualizing the **Permanently Shadowed Regions (PSRs)** of the Moon. These areas, which haven't seen sunlight in billions of years, are prime locations for water ice but are notoriously difficult to image. Using a rich suite of data from ISRO's **Chandrayaan-2** mission, AETHER employs **Self-Supervised Learning** to enhance faint signals, transforming noisy, low-light patches into scientifically valuable maps.

-----

## ✨ Key Features

* **Self-Supervised Enhancement**: Leverages a novel pretext task to teach the model lunar topology from unlabeled data, eliminating the need for hand-annotated training sets.
* **Multi-Modal Data Fusion**: Intelligently integrates optical (OHRC), radar (DFSAR), elemental (CLASS), and spectral (IIRS) data to create a holistic and information-rich view of the lunar surface.
* **High-Fidelity Generative Model**: Utilizes a fine-tuned Generative Adversarial Network (GAN) to reconstruct shadowed terrain with plausible details, maximizing the Signal-to-Noise Ratio (SNR).
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

Our pipeline transforms raw, heterogeneous data into clear, scientifically-valuable maps. The cornerstone of AETHER is its ability to fuse diverse data sources, providing our model with a rich, multi-faceted understanding of the lunar surface.

### 1\. Multi-Modal Data Ingestion & Fusion

We treat the lunar surface as a multi-layered dataset. Each instrument provides a unique layer of information, and by combining them, we create a "super-image" that offers far more context than a simple photograph.

* 🛰️ **Primary Optical Data (OHRC):** This is the high-resolution visual canvas we aim to enhance. It provides the base imagery, which suffers from low signal in shadowed regions.
* 🪨 **Structural & Texture Data (DFSAR):** The radar data acts as our structural blueprint. Unaffected by shadows, it reveals surface roughness and physical topography, telling the model the *shape* of the ground.
* 🧪 **Elemental Composition Data (CLASS):** This provides the chemical fingerprint. By mapping elements like Silicon, Iron, and Magnesium, CLASS tells the model *what the ground is made of*, allowing it to connect chemistry to texture.
* 💧 **Mineralogical & Volatile Data (IIRS):** The infrared spectrometer is key for identifying specific minerals and, crucially, the spectral signature of water ice and hydroxyl molecules. This layer guides the model toward areas of high scientific interest.
* 🗺️ **Geometric & Navigational Data (SPICE):** The essential Rosetta Stone. SPICE kernels provide the precise position, orientation, and timing data required to take all the above layers and align them perfectly into a single, cohesive coordinate system.

> **The Fusion Process:** All data layers are georeferenced using SPICE and stacked into a multi-channel tensor. Instead of a 3-channel (RGB) image, our model processes a rich data cube, enabling an informed, context-aware enhancement.

### 2\. Self-Supervised Pre-training (The Core Engine)

The model learns the fundamental patterns of lunar terrain without labels.

* **Pretext Task**: We employ a "masked autoencoder" approach. The model is fed a multi-channel data tensor with random patches masked out and is trained to reconstruct the missing information. To succeed, it must learn the intrinsic relationships between radar texture, optical shadows, and chemical composition.

### 3\. Generative Fine-Tuning

The pre-trained encoder from the SSL phase is used as the backbone of a custom Generative Adversarial Network (GAN).

* This GAN is specifically fine-tuned on the task of **low-light enhancement**. It takes a noisy OHRC image as input and generates a clean, high-SNR version, guided by the deep contextual understanding from the fused data.

### 4\. Map Synthesis & Visualization

The enhanced image tiles are stitched together and projected into a polar stereographic map.

* The final output is a high-resolution map highlighting previously unseen details within the Moon's Permanently Shadowed Regions.

-----

## 🌍 Impact & Applications

AETHER directly contributes to the next era of lunar exploration by:

* **Enabling Safer Landings**: Providing mission planners with clear, detailed views of potential landing sites for robotic and crewed missions.
* **Accelerating Scientific Discovery**: Unlocking vast, unexplored regions for geological analysis and the search for water ice.
* **Advancing Planetary AI**: Pioneering the use of self-supervised techniques for low-data, extreme-environment scenarios in space exploration.

-----
## 📂 Repository Structure

```text
aether/
│
├── data/                  # Utilities for ISRO PRADAN data scraping and bulk downloading
├── notebooks/             # Jupyter notebooks for Exploratory Data Analysis (EDA)
├── models/                # Pre-trained model weights (Zero-DCE, GANs)
│
├── src/                   # 🔒 Core Research Modules (Restricted for Open Source PRs)
│   ├── data_io/           # PDS4 XML metadata parsing and raw .img ingestion
│   ├── models/            # Deep learning architectures (Zero-DCE, GAN, SSL)
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

1.  Clone the repository:
    ```bash
    git clone [https://github.com/TechieSamosa/AETHER.git](https://github.com/TechieSamosa/AETHER.git)
    cd AETHER
    ```
2.  Create and activate a conda environment:
    ```bash
    conda env create -f environment.yml
    conda activate aether
    ```
3.  Run inference on a sample image:
    ```bash
    python scripts/enhance.py --input /path/to/sample.img --output /path/to/enhanced.png --model models/aether_v1.pth
    ```

-----

## 🎯 How to Contribute (GSSoC '26)

We are thrilled to be a part of **GirlScript Summer of Code 2026**! We welcome contributions from the global community, specifically focusing on data engineering, memory optimization, and pipeline automation.

### ⚠️ Important: Academic IP & Authorship
The AETHER framework is the foundation of an upcoming scientific research paper. **The core mathematical architecture and deep learning models in the `src/` directory are strictly locked.** Before making any pull requests, you **must** read our [CONTRIBUTING.md](CONTRIBUTING.md) to understand the strict boundaries between open-source engineering contributions and academic co-authorship. By interacting with this repository, you automatically agree to these terms.

### Getting Started:
1. **Read the Docs:** Review our [Contributor Guide & Technical Roadmap](CONTRIBUTING.md) to understand how we source Chandrayaan-2 data.
2. **Find an Issue:** Look for issues tagged `good first issue`, `gssoc-26`, or `help wanted`.
3. **Focus Areas:** We are actively looking for PRs related to:
   * Automated web-scraping for ISRO PRADAN data.
   * PyTorch DataLoader memory optimization.
   * GIS map stitching using GDAL/Rasterio.
   * Unit testing and code documentation.

-----

## 📚 References & Acknowledgements

This work builds upon the state-of-the-art in deep learning and planetary science. We gratefully acknowledge the data provided by the **ISRO Science Data Archive (ISDA)**.

* **"Masked Autoencoders Are Scalable Vision Learners"** (He et al., 2021)
* **"SinGAN: Learning a Generative Model from a Single Natural Image"** (Shaham et al., 2019)
* **Chandrayaan-2 Mission Data Handbook**, ISRO
* **"Analysis of Permanently Shadowed Regions of the Moon using LRO and Chandrayaan-2 Data"**

-----

## 🔬 Core Research Team

AETHER’s core architecture, deep learning methodology, and academic research are developed and maintained by:
* **Aditya Sachin Khamitkar** (Lead Architect & Researcher)
* **Tushar** (Core Researcher)
* **Nitin** (Core Researcher)

-----

## 🏅 Open Source Contributors

A huge thank you to the global developers and GSSoC '26 mentees who have optimized our pipelines, improved our data ingestion, and helped scale AETHER! Impactful engineering contributions are automatically recognized here.

<a href="https://github.com/TechieSamosa/Aether/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TechieSamosa/Aether" />
</a>

-----

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details. This permissive license allows for wide use and collaboration.
