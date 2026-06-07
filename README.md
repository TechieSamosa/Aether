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

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details. This permissive license allows for wide use and collaboration.



***

### 2. Updated `CONTRIBUTING.md`
Copy and paste this to replace your entire CONTRIBUTING guide:


# Contributing to AETHER 🌌

Welcome to AETHER! We are thrilled to be a part of **GirlScript Summer of Code 2026**. 

We are using Deep Learning to peer into the darkest places in our solar system: the Permanently Shadowed Regions (PSRs) of the Lunar South Pole. This guide outlines our technical roadmap, how our data pipeline works, our current engineering bottlenecks, and the strict academic rules governing this repository.

---

## ⚠️ Academic Authorship & Intellectual Property Notice
The core maintainers are currently preparing a formal scientific research paper based on the AETHER framework. By contributing to this repository, you acknowledge and agree to the following:

* **Publication Acknowledgements:** External contributions (such as data scrapers, pipeline optimizations, bug fixes, and tooling) will be formally recognized in the **Acknowledgements** section of any resulting academic publications. 
* **Co-Authorship:** Academic co-authorship is strictly reserved for the core research team (Aditya, Tushar, and Nitin). 
* **Repository Recognition:** Contributors who make significant, impactful engineering contributions will be explicitly recognized in the project's `README.md` contributors section.

### 🛑 The Research Red Line
Do not alter the fundamental mathematical architecture, loss functions, or network topology of the Zero-DCE models in the `src/models/` directory. These files are strictly locked for our ongoing research, and any Pull Requests modifying the core math will be rejected. 

*(Note: We welcome theoretical suggestions via GitHub Issues. However, even if a suggested issue is highly impactful and implemented by the core team, it does not grant the suggester academic co-authorship).*

---

## 🗺️ Part 1: Technical Roadmap & How AETHER Works

To contribute effectively, you need to understand how we source and process our data.

### 1. How We Source Our Data (The PRADAN Portal)
Our primary data source is the **Chandrayaan-2 Orbiter High Resolution Camera (OHRC)** ($0.25$ meters/pixel).
1.  We use the [ISRO PRADAN Map Browse](https://chmapbrowse.issdc.gov.in) interface.
2.  We target the floors of known PSR craters (e.g., Shackleton, Cabeus). 
3.  We download the **Calibrated Product ZIP**, which contains the raw `.img` file (usually ~1.2 GB) and the `.xml` PDS4 label.

### 2. How the Pipeline Processes Images
Working with 1.2 Billion pixel planetary images requires a specialized pipeline:
* **Data Ingestion:** We use `pds4-tools` to parse metadata and load raw `.img` binaries into NumPy arrays. 
* **Patch Extraction:** We use a sliding-window algorithm to extract 64x64 patches, automatically categorizing them into `psr` (dark) or `sunlit` (bright) to avoid overloading the GPU.
* **The Model:** We utilize a Zero-Reference Deep Curve Estimation (Zero-DCE) approach. Instead of predicting pixels directly, it predicts exposure curves to stretch the faint secondary light hidden in the shadows.
* **Inference & Denoising:** Enhanced tiles are stitched back together. We apply Non-Local Means (NLM) spatial denoising to clean up amplified sensor noise before mapping.

---

## 🎯 Part 2: What We Need Help With (GSSoC '26)

We have a vast amount of lunar data but limited compute power. We need contributors who can help us move data efficiently and optimize our Python pipelines.

**We are actively seeking Pull Requests for:**

* **Data Automation (Web Scraping):** PRADAN downloads are currently manual. We need Python scripts (using `requests`, `BeautifulSoup`, or `Selenium`) to automate downloading the massive `.zip` products based on a list of coordinates.
* **Memory Optimization:** We are running out of RAM. We need help refactoring our PyTorch `DataLoader` classes to dynamically load image patches from the disk using `rasterio` windowed reading, rather than loading the whole image at once.
* **GIS Integration & Map Stitching:** AETHER outputs enhanced image strips. We need scripts using `GDAL` or `Rasterio` to read the embedded spatial metadata (`geometry.csv`) and stitch these overlapping tiles back into a single, cohesive GeoTIFF map.
* **Code Quality & Testing:** Adding strict Python type hinting, writing Google-style docstrings, and building unit tests using `pytest` for our data ingestion functions.
* **Optional C++ Optimizations:** If you are highly skilled in C++, we welcome PRs that port heavy bottleneck functions (like geospatial tensor stacking) to `libtorch` or C++ OpenCV.

---

## 🛠️ Part 3: How to Contribute

Ready to write some code? Here is the standard workflow:

1.  **Fork & Clone:** Fork the repository to your GitHub account and clone it to your local machine.
2.  **Find an Issue:** Check the **Issues** tab. Look for tags like `good first issue`, `help wanted`, or `gssoc-26`.
3.  **Claim it:** Comment on the issue asking to be assigned. **Do not start working until you are assigned.**
4.  **Create a Branch:** Create a new branch for your feature (`git checkout -b feature/your-feature-name`).
5.  **Write Clean Code:** Ensure your code is memory-efficient and well-documented.
6.  **Submit a PR:** Push your branch to your fork and submit a Pull Request to our `main` branch. Provide a clear description of what you optimized or fixed.

We review PRs frequently. Please be patient, respectful, and welcome to the team!
