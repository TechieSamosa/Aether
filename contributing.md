# Contributing to AETHER 🌌

Welcome to AETHER. This framework processes heavy multi-modal lunar data from Chandrayaan-2. Our primary engineering challenges involve managing massive datasets and training deep learning models in compute-constrained environments.

## ⚠️ Academic Authorship & Intellectual Property Notice
The core maintainers are currently preparing a formal scientific research paper based on the AETHER framework. 

By contributing to this repository, you acknowledge and agree to the following:
*   **Publication Acknowledgements:** External contributions (such as data scrapers, pipeline optimizations, bug fixes, and tooling) will be formally recognized in the **Acknowledgements** section of any resulting academic publications. 
*   **Co-Authorship:** Academic co-authorship is strictly reserved for the core research team. 
*   **Repository Recognition:** Contributors who make significant, impactful engineering contributions (excluding minor typo fixes or basic README changes) will be explicitly recognized in the project's `README.md` contributors section. GitHub will also automatically track you as a repository contributor.

## 🎯 What We Need Help With (GSSoC '26)
We have a vast amount of lunar data but limited compute power. We need contributors who can help us move data efficiently and optimize our Python pipelines.

**What you CAN work on:**
*   **Data Ingestion:** Writing robust Python scripts to scrape/download bulk data from ISRO's archives safely and reliably.
*   **Memory Optimization:** Refactoring our PyTorch `DataLoader` classes to load image patches dynamically from disk rather than crashing RAM.
*   **Code Quality:** Adding type hinting, docstrings, and writing unit tests (pytest).
*   **Optional C++ Optimizations:** If you are highly skilled in C++, we welcome PRs that port heavy bottleneck functions (like geospatial tensor stacking) to `libtorch` or C++ OpenCV.

---

### 🛑 The Research Red Line
Do not alter the fundamental mathematical architecture, loss functions, or network topology of the GAN/SSL models in the `src/` directory. These files are strictly locked for our ongoing research, and any Pull Requests modifying the core math will be rejected.

**Suggestions via Issues:** We welcome theoretical suggestions and architectural ideas via GitHub Issues. The core research team retains full discretion to review, accept, or reject these proposals.

**Agreement:** Please note that even if a theoretical suggestion is adopted and implemented by the team, it does not qualify the suggester for academic co-authorship. By submitting any issue, comment, or Pull Request to this repository, you automatically agree to these terms.

---

## 🛠️ How to Contribute
1. **Fork & Clone:** Fork the repo and set up your local environment.
2. **Claim an Issue:** Look for issues tagged `good first issue` or `help wanted`. Comment to be assigned.
3. **Branch:** Create a branch (`feature/your-feature`).
4. **Code:** Write clean, memory-efficient code.
5. **PR:** Submit your Pull Request explaining exactly what you optimized or fixed.
