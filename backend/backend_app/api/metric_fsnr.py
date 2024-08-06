import os
import numpy as np
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

def calculate_psnr(img1, img2):
    """Calculates the PSNR between two images."""
    return compare_psnr(np.array(img1), np.array(img2), data_range=255)

def load_image(image_path, target_size=None):
    """Loads an image, resizes it if a target size is provided, and converts it to RGB."""
    image = Image.open(image_path).convert('RGB')
    if target_size:
        image = image.resize(target_size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsampling
    return image

def compute_average_psnr(real_image_dir, generated_image_dir):
    """Computes the average PSNR between two directories of images."""
    real_images = sorted(os.listdir(real_image_dir))
    generated_images = sorted(os.listdir(generated_image_dir))
    
    psnr_values = []
    
    for real_img_name, gen_img_name in zip(real_images, generated_images):
        real_img_path = os.path.join(real_image_dir, real_img_name)
        gen_img_path = os.path.join(generated_image_dir, gen_img_name)
        
        real_img = load_image(real_img_path)
        gen_img = load_image(gen_img_path, target_size=real_img.size)  # Resize generated image to match real image size
        
        psnr_value = calculate_psnr(real_img, gen_img)
        psnr_values.append(psnr_value)
        print(f"PSNR for {real_img_name} and {gen_img_name}: {psnr_value}")

    average_psnr = np.mean(psnr_values)
    return average_psnr

# Example usage
real_image_dir = 'path_to_real_images'
generated_image_dir = 'path_to_generated_images'
average_psnr = compute_average_psnr(real_image_dir, generated_image_dir)
print(f'Average PSNR: {average_psnr}')
