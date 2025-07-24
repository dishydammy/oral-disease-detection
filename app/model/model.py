import torch
from torchvision import transforms
from PIL import Image

# Class labels the model predicts
CLASS_NAMES = ['OSCC', 'with_dysplasia', 'without_dysplasia']

# Transform used for preprocessing images during inference
inference_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                         std=[0.229, 0.224, 0.225])
])

# Load the full model object saved with torch.save(model)
def load_model(model_path: str = "model.pth"):
    model = torch.load(model_path, map_location=torch.device("cpu"), weights_only=False)
    model.eval()
    return model

# Optional utility function to test prediction locally (not used in API)
def predict_image(model, image_path: str):
    image = Image.open(image_path).convert("RGB")
    img_tensor = inference_transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        outputs = model(img_tensor)
        predicted_idx = torch.argmax(outputs, dim=1).item()
        return CLASS_NAMES[predicted_idx]