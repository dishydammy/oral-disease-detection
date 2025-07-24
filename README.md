# 🦷 Oral Disease Detection 

## 🧠 Project Overview

An image classification API powered by a fine-tuned ResNet50 model that helps detect and classify oral diseases from histopathological images. This project aims to assist clinicians and researchers in early screening and diagnosis of oral conditions using deep learning and accessible APIs.

The dataset used consists of histopathological images and accompanying clinical and sociodemographic data collected between 2010 and 2021 from patients managed at the Oral Diagnosis Project (NDB) of the Federal University of Espírito Santo (UFES), Brazil. It includes samples from individuals with Oral Squamous Cell Carcinoma (OSCC) and Leukoplakia, represented as with or without epithelial dysplasia. A supplementary dataset of image patches from the original samples was also provided.

---

## 🩺 Problem Statement

Oral diseases are among the most common non-communicable diseases globally and often go undiagnosed during their early stages, especially in low-resource settings. Late detection can lead to serious complications such as cancer progression, functional impairment, tooth loss, and reduced quality of life.

This model was trained to classify oral histopathological images into one of three categories:

* OSCC (Oral Squamous Cell Carcinoma)
A malignant neoplasm arising in the squamous cells of the oral cavity. Early and accurate diagnosis is crucial because OSCC can metastasize, making it life-threatening if left untreated.

* With Dysplasia
Represents tissue with abnormal cellular changes that are not yet cancerous. Dysplasia is a known precancerous condition and detecting it early helps guide timely monitoring or intervention to prevent progression to carcinoma.

* Without Dysplasia
Normal or benign tissue without signs of abnormality. This class provides a healthy baseline for comparison and supports clinicians in ruling out malignancy.

While the model currently focuses on image-based predictions, the original dataset also includes rich metadata (such as age, gender, tobacco/alcohol use, lesion type, and more), which presents opportunities for future multi-modal analysis combining image and clinical data for even more accurate predictions.

---

## 🧠 Model and Dataset

- **Model**: A fine-tuned [ResNet50](https://arxiv.org/abs/1512.03385) model from PyTorch’s `torchvision.models`.
- **Training Details**: The model was trained on high-resolution oral cavity images with three target classes.
- **Dataset Source**: Download available from [Mendeley Data Repository](https://data.mendeley.com/datasets/bbmmm4wgr8/4).

---

## ⚙️ API Overview

This project uses **FastAPI** to serve the trained model for inference.

- **Endpoint**: `POST /predict`
- **Input**:  A histopathological PNG/JPG image file extracted from an oral tissue biopsy
- **Output**:  
  - Predicted class label: one of `OSCC`, `with_dysplasia`, or `without_dysplasia`  
  - Confidence scores for each class
- **Interactive Documentation**: Visit `http://localhost:8000/docs` when running locally.

---

## 🚀 Running with Docker

You can containerize and run the API locally using Docker:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/oral-disease-image-classification.git
cd oral-disease-image-classification
```

### 2. Build the Docker Image

```bash
docker build -t oral-disease-detector .
```

### 3. Run the Container

```bash
docker run -p 8000:8000 oral-disease-detector
```

### 4. Access the API
* Swagger Docs: http://localhost:8000/docs
* Click on "Try it out", then upload an image for prediction

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
├── Image_Sort_Notebook.ipnyb   # Notebook for sorting images into class folder
├── Model_Training.ipnyb        # Notebook for training model
├── Dockerfile                  # Docker container definition
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation (this file)
```

---

##  Disclaimer

This tool is built for educational and research purposes only and is not a substitute for professional medical diagnosis. Always consult qualified healthcare professionals for clinical decisions.