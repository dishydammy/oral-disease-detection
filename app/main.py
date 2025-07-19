from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import torch
import torch.nn.functional as F
from app.model.model import load_model, CLASS_NAMES, inference_transform

# Initialize FastAPI app
app = FastAPI(title="Oral Disease Detection API")

# Load model on startup using full model object
model = load_model("app/model/model.pth")

# Define prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Check if uploaded file is an image
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(content={"error": "Only JPEG or PNG images are supported"}, status_code=400)

    try:
        # Read and convert image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Preprocess image
        tensor = inference_transform(image).unsqueeze(0)  # Add batch dimension

        # Inference
        with torch.no_grad():
            outputs = model(tensor)  # Raw scores (logits)
            probs = F.softmax(outputs, dim=1)  # Convert to probabilities
            predicted_idx = torch.argmax(probs, dim=1).item()
            predicted_label = CLASS_NAMES[predicted_idx]
            confidence = round(probs[0][predicted_idx].item(), 4)

        # Return result
        return {
            "prediction": predicted_label,
            "confidence": confidence
        }

    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to process image: {str(e)}"},
            status_code=500
        )