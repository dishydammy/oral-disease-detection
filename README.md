# 🦷 Oral Disease Detection API

An image classification API powered by a fine-tuned ResNet50 model that helps detect and classify oral diseases from medical images. This project aims to assist clinicians and researchers in early screening and diagnosis of common oral conditions using deep learning.

---

## 🩺 Problem Statement

Oral diseases are among the most prevalent non-communicable diseases globally and are often left undiagnosed in early stages. Delays in diagnosis may lead to severe complications including cancer progression, loss of teeth, and overall poor quality of life.

This model is trained to classify medical images into one of three categories:

1. **OSCC (Oral Squamous Cell Carcinoma)**  
   A type of cancer that arises in the squamous cells lining the oral cavity. Early detection is critical as untreated OSCC can metastasize and become life-threatening.

2. **With Dysplasia**  
   Refers to abnormal but non-cancerous changes in oral tissues. Dysplasia is considered precancerous, and identifying it early helps monitor progression or regression over time.

3. **Without Dysplasia**  
   Refers to normal or benign tissue without signs of dysplasia or carcinoma. Important for establishing healthy baselines or post-treatment monitoring.

---

## 🧠 Model and Dataset

- **Model**: A fine-tuned [ResNet50](https://arxiv.org/abs/1512.03385) model from PyTorch’s `torchvision.models`.
- **Training Details**: The model was trained on a medical image dataset with high-quality oral cavity scans.
- **Dataset Source**: The dataset was obtained from a medical research source. A Google Drive download link will be included here soon.

---

## ⚙️ API Overview

This project uses **FastAPI** to serve the model for inference.

- **Endpoint**: `POST /predict`
- **Input**: PNG image of an oral cavity
- **Output**: Predicted class label (`OSCC`, `with_dysplasia`, `without_dysplasia`) and probability scores
- **Documentation**: Swagger UI available at `/docs`

---

## 🧪 How to Use

### Run Locally (Setup Instructions Coming Soon)
> Instructions for setting up with virtual environment and dependencies will be added later.

### Docker Deployment (Planned)
Deployment using Docker and AWS (Elastic Beanstalk or EC2) is currently in progress. Once live, the public API endpoint will be shared.

---

## 🧵 Project Structure

```
oral-disease-image-classification/
│
├── app/
│   ├── main.py                 # FastAPI application
│   └── model/
│       ├── model.py            # Model loading and prediction logic
│       └── model.pth           # Trained PyTorch model
│
├── Dockerfile                  # Docker container definition
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files/folders to ignore in git
└── README.md                   # Project documentation (this file)
```