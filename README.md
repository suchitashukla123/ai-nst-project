# 🎨 AI Neural Style Transfer

An AI-powered web application that transfers the artistic style of one image onto another using **PyTorch, VGG, and Adaptive Instance Normalization (AdaIN)**.

Users can upload a content image, upload a style image, adjust the style strength, and generate a stylized image.

## 🚀 Features

- Upload content and style images
- AI-based Neural Style Transfer
- VGG-based feature extraction
- Adaptive Instance Normalization (AdaIN)
- Adjustable style strength using Alpha
- Automatic CPU/GPU detection
- Flask-based web interface
- Example images for testing

## 🧠 How It Works

Content Image → VGG Encoder → Content Features  
Style Image → VGG Encoder → Style Features  
Content + Style Features → AdaIN → Decoder → Stylized Image

## 🛠️ Technologies

- Python
- PyTorch
- Torchvision
- Flask
- VGG
- AdaIN
- Pillow
- NumPy

## 📂 Project Structure

ai-nst-project/  
├── NST_Code/  
│   ├── app.py  
│   ├── train.py  
│   ├── vgg_normalised.pth  
│   ├── experiment/  
│   │   └── final_exp/  
│   │       └── decoder_final.pth  
│   ├── examples/  
│   ├── templates/  
│   └── utils/  
├── Demo_IO_Images/  
├── code.ipynb  
├── requirements.txt  
├── .python-version  
└── README.md

## 💻 Run Locally

### 1. Clone the Repository

    git clone https://github.com/suchitashukla123/ai-nst-project.git
    cd ai-nst-project

### 2. Create and Activate Virtual Environment

**Windows:**

    python -m venv .venv
    .venv\Scripts\activate

**macOS / Linux:**

    python3 -m venv .venv
    source .venv/bin/activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run the Application

    cd NST_Code
    python app.py

### 🌐 Open in Browser

    http://127.0.0.1:5000

## 🎨 How to Use

1. Upload a content image.
2. Upload a style image.
3. Adjust the Style Strength.
4. Click **Transfer Style**.
5. View the generated stylized image.

## 🧠 Model

The project uses:

- **VGG Encoder** for feature extraction
- **AdaIN** for style transfer
- **Trained Decoder** for generating the stylized image

Required model files:

    NST_Code/vgg_normalised.pth
    NST_Code/experiment/final_exp/decoder_final.pth

## 🌐 Live Demo

**Live App:**  
https://ai-nst-project-smw2.onrender.com

> The live deployment runs on a limited CPU-based hosting environment. For the most reliable experience, clone the repository and run the application locally.

