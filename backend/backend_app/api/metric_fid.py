import torch
import numpy as np
from scipy import linalg
from torchvision import models, transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import os

# Custom dataset to load images from directory
class ImageFolderDataset(Dataset):
    def __init__(self, image_dir, transform=None):
        self.image_dir = image_dir
        self.image_paths = [os.path.join(image_dir, file) for file in os.listdir(image_dir)]
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image

def calculate_fid(real_features, generated_features):
    mu1, sigma1 = np.mean(real_features, axis=0), np.cov(real_features, rowvar=False)
    mu2, sigma2 = np.mean(generated_features, axis=0), np.cov(generated_features, rowvar=False)

    if sigma1.ndim == 0:
        sigma1 = np.atleast_2d(sigma1)
    if sigma2.ndim == 0:
        sigma2 = np.atleast_2d(sigma2)

    diff = mu1 - mu2
    covmean, _ = linalg.sqrtm(sigma1 @ sigma2, disp=False)

    if np.iscomplexobj(covmean):
        covmean = covmean.real

    fid = diff.dot(diff) + np.trace(sigma1 + sigma2 - 2 * covmean)
    return fid

# Function to extract features from images using a pre-trained InceptionV3 model
def get_features(dataset, model, batch_size=32, device='cuda'):
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    features = []

    with torch.no_grad():
        for images in dataloader:
            images = images.to(device)
            outputs = model(images).view(images.size(0), -1)
            features.append(outputs.cpu().numpy())

    features = np.concatenate(features, axis=0)
    return features

# Main function to compute FID between two image directories
def compute_fid(real_image_dir, generated_image_dir, batch_size=32, device='cuda'):
    # Transformation to apply to images
    transform = transforms.Compose([
        transforms.Resize((299, 299)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Create datasets
    real_dataset = ImageFolderDataset(real_image_dir, transform=transform)
    generated_dataset = ImageFolderDataset(generated_image_dir, transform=transform)

    # Load pre-trained InceptionV3 model
    inception_model = models.inception_v3(pretrained=True, transform_input=False).to(device)
    inception_model.eval()

    # Get features from the real and generated images
    real_features = get_features(real_dataset, inception_model, batch_size=batch_size, device=device)
    generated_features = get_features(generated_dataset, inception_model, batch_size=batch_size, device=device)

    # Calculate FID
    fid_score = calculate_fid(real_features, generated_features)
    return fid_score

# Example usage
real_image_dir = 'real'
generated_image_dir = 'output'
fid_score = compute_fid(real_image_dir, generated_image_dir)
print(f'FID Score: {fid_score}')