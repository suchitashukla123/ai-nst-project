# 🎨 AI Neural Style Transfer

An AI-powered web application that transfers the artistic style of one image onto another using **PyTorch, VGG, and Adaptive Instance Normalization (AdaIN)**.

Users can upload a content image, a style image, adjust style strength, and generate a stylized image.

## 🚀 Features

- Upload content and style images
- AI-based Neural Style Transfer
- VGG-based feature extraction
- Adaptive Instance Normalization (AdaIN)
- Adjustable style strength using Alpha
- CPU/GPU automatic detection
- Flask web interface
- Example images for testing

## 🧠 How It Works

```text
Content Image ──► VGG Encoder ──► Content Features
                                      │
                                      ▼
                                    AdaIN
                                      ▲
                                      │
Style Image ─────► VGG Encoder ──► Style Features
                                      │
                                      ▼
                              Decoder Network
                                      │
                                      ▼
                              Stylized Image
🛠️ Technologies
Python
PyTorch
Torchvision
Flask
VGG
AdaIN
Pillow
NumPy
📂 Project Structure
ai-nst-project/
│
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
│
├── Demo_IO_Images/
├── code.ipynb
├── requirements.txt
├── .python-version
└── README.md
💻 Run Locally
1. Clone the repository
git clone https://github.com/suchitashukla123/ai-nst-project.git
cd ai-nst-project
2. Create virtual environment

Windows:

python -m venv .venv
.venv\Scripts\activate

Mac/Linux:

python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
cd NST_Code
python app.py

Open:

http://127.0.0.1:5000
🎨 How to Use
Upload a content image.
Upload a style image.
Adjust Style Strength.
Click Transfer Style.
View the generated stylized image.
🧠 Model

The project uses:

VGG Encoder for feature extraction
AdaIN for transferring style statistics
Trained Decoder for generating the final stylized image

Model files:

NST_Code/vgg_normalised.pth
NST_Code/experiment/final_exp/decoder_final.pth
🌐 Live Demo

Live App:
https://ai-nst-project-smw2.onrender.com

The live deployment runs on a limited CPU-based hosting environment. For the complete and reliable experience, running the project locally is recommended.
