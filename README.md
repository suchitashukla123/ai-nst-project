# 🎨 AI Neural Style Transfer

An AI-powered web application for **Neural Style Transfer**, built using **Python, PyTorch, Flask, VGG, and Adaptive Instance Normalization (AdaIN)**.

The application allows users to upload a **content image** and a **style image**, and generates a stylized image that preserves the content of the original image while applying the artistic style of the selected style image.

---

## 🌐 Live Demo

🚧 **Coming Soon**

The live demo link will be added after deployment.

---

## 📌 Project Overview

Neural Style Transfer is a deep learning technique that combines the **content of one image** with the **artistic style of another image**.

This project implements **Arbitrary Neural Style Transfer using Adaptive Instance Normalization (AdaIN)**.

### Input

- 🖼️ Content Image
- 🎨 Style Image
- 🎚️ Alpha value for controlling style strength

### Output

- ✨ AI-generated stylized image

The project uses a pretrained **VGG encoder** to extract feature representations, **Adaptive Instance Normalization (AdaIN)** to transfer style information, and a trained **decoder network** to reconstruct the final stylized image.

---

## ✨ Features

- 🖼️ Upload a content image
- 🎨 Upload a style image
- 🤖 AI-based Neural Style Transfer
- 🧠 VGG-based feature extraction
- 🎨 Adaptive Instance Normalization (AdaIN)
- 🎚️ Adjustable style strength using the Alpha parameter
- ⚡ Automatic CPU/GPU detection
- 📂 Example images for testing
- 🌐 Flask-based web interface
- 💾 Generated stylized image output

---

## 🧠 How It Works

The Neural Style Transfer pipeline works as follows:

```text
              Content Image
                    │
                    ▼
               VGG Encoder
                    │
                    ▼
             Content Features
                    │
                    │
                    ▼
              ┌───────────┐
              │   AdaIN   │
              └─────┬─────┘
                    ▲
                    │
               Style Features
                    ▲
                    │
               VGG Encoder
                    ▲
                    │
                Style Image
                    │
                    ▼
            Stylized Features
                    │
                    ▼
             Decoder Network
                    │
                    ▼
             Stylized Image