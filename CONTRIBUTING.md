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

## 🛑 Zero-Tolerance AI Copy-Paste Policy

> **This is not optional. Violations result in immediate PR closure.**

We fully encourage contributors to use Large Language Models (LLMs) such as ChatGPT, Gemini, Claude, or GitHub Copilot as **learning and debugging tools**. However, this project involves real scientific data from an active space mission, and every line of code has consequences for data integrity.

### What is ALLOWED:
- Using an LLM to **understand** how `pds4-tools` parses XML metadata.
- Asking an LLM to **explain** a PyTorch loss function or debug a syntax error.
- Using Copilot for **autocompletion** of boilerplate code you fully understand.

### What is STRICTLY FORBIDDEN:
- Blindly copy-pasting an entire PR from an LLM without understanding the mathematical or structural context.
- Submitting code that references **hallucinated libraries** (e.g., `from lunar_enhance import PSRProcessor` — this does not exist).
- Submitting code with **broken logical loops**, off-by-one errors in sliding window implementations, or incorrect tensor reshaping that would silently corrupt scientific data.
- Submitting obvious **AI boilerplate** (e.g., `# TODO: Implement this function` repeated across files, generic docstrings that don't match the actual function signature).

### Consequences:
PRs that exhibit clear signs of unreviewed AI generation will be:
1. **Immediately closed** without merge.
2. Labeled as `invalid`.
3. The contributor will receive a warning. Repeat offenders will be blocked from the repository.

**Bottom line:** Use AI to learn. Don't let AI submit your homework.

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
