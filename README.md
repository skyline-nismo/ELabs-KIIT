# Handwritten Digit Recognition (Linear SVC)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: Open Source](https://img.shields.io/badge/License-Open_Source-green.svg)](https://opensource.org/licenses/)
[![ML: Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

A robust, end-to-end Python pipeline for real-time handwritten digit recognition. This system bridges the gap between digital drawing and machine learning by capturing live screen data, performing binary feature extraction, and classifying digits using a high-performance **Linear Support Vector Classifier (SVC)**.

---

## 🚀 Features

- **Live Inference**: Instant prediction as you draw in any application (MS Paint, Whiteboard, etc.).
- **Data Pipeline**: Full suite for image capture, binary thresholding, and CSV dataset generation.
- **Optimized Model**: Pre-trained Linear SVC achieving **96%+ accuracy** on processed screen-captured data.
- **Validation Tools**: Interactive dataset previewer to verify image-to-pixel conversion.

---

## 🎬 Demo

*Place a GIF or Screenshot here showing the drawing canvas and prediction window!*
<!-- Example: ![Demo](assets/demo.gif) -->

---

## 📊 Technical Specification

| Feature | Details |
| :--- | :--- |
| **Classifier** | SVC with Linear Kernel (Scikit-Learn) |
| **Input Feature Vector** | 784-dimensional (28x28 flattened grayscale) |
| **Preprocessing** | Gaussian Blur + Binary Thresholding (100) |
| **Sampling Rate** | ~1000ms per inference loop (configurable) |
| **Dataset Size** | 100 samples per digit (0-9) |
| **Accuracy** | Typically 96%+ on self-collected datasets |

---

## 🛠️ Installation & Setup

### 1. Prerequisites
- **Python 3.7 or higher**
- A drawing canvas (MS Paint is recommended for Windows users).

### 2. Fast Setup
```bash
# Clone the repository
git clone https://github.com/skyline-nismo/ELabs-KIIT.git
cd ELabs-KIIT

# Setup Virtual Environment (Highly Recommended)
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/macOS

# Install Dependencies
pip install -r HandwrittenRecognitionUsingCNN/requirements.txt
```

---

## 🖥️ Usage Guide

### ⚡ Quick Start: Live Prediction
The project includes a pre-trained model. You can start immediately:
1.  Open your drawing application.
2.  Position your canvas within the default capture area: **(100, 300)** to **(950, 1000)**.
3.  Execute:
    ```bash
    python HandwrittenRecognitionUsingCNN/final_model.py
    ```

### 🧠 Advanced: Custom Training
To train the model on your own unique handwriting:

1.  **Collect Raw Data**: Run `image_collection.py`. Update the `images_folder` path for each digit (0-9).
2.  **Generate CSV**: Run `dataset_generation.py`. This processes raw `.png` files into the `Dataset.csv` pixel map.
3.  **Train Model**: Run `train_and_test.py`. This generates a new `model/digit_recognizer` file.

---

## 📂 Project Structure

```text
HandwrittenRecognitionUsingCNN/
├── final_model.py        # Core application for live prediction
├── train_and_test.py     # ML pipeline: Train, test, and save model
├── dataset_generation.py # Image-to-pixel CSV converter
├── dataset_loading.py    # Data loader & shuffler utility
├── image_collection.py   # Screen capture tool for data gathering
├── preview.py            # Dataset inspector (Matplotlib based)
├── requirements.txt      # Dependency manifest
├── Dataset.csv           # Final processed feature matrix
└── model/                # Persistent storage for trained weights
```

---

## 💡 Pro-Tips & Troubleshooting
- **Coordinates**: If the prediction window shows the wrong part of your screen, adjust the `bbox` variable in `final_model.py`.
- **Contrast**: The model performs best with dark ink on a light background.
- **Accuracy**: For best results, ensure the digit fills at least 70% of the capture region.

---

## 🧪 Tech Stack
- **OpenCV**: Vision processing & real-time UI.
- **Scikit-Learn**: Machine Learning implementation.
- **PyScreenshot**: Cross-platform screen capture.
- **Pandas/NumPy**: Large-scale data manipulation.

---

## 🛠️ Future Improvements

- **CNN Implementation**: Transition from Linear SVC to a Convolutional Neural Network (CNN) for even higher robustness.
- **Dynamic Region Selection**: Support for custom screen region selection via a GUI.
- **Confidence Scoring**: Display probability/confidence scores for each prediction.
- **Logging**: Export predictions and captured data to local logs for analysis.
- **Extended Training**: Train on larger, more diverse datasets (e.g., MNIST) to improve generalization.

---

## 📜 License
Distributed under the Open Source license. See `LICENSE` for more information.
