import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim

def calculate_ssim(img1, img2):
    """Calculates the SSIM between two images."""
    img1 = np.array(img1)
    img2 = np.array(img2)
    
    # SSIM 계산을 위해 이미지의 최소 크기에 맞춰 win_size 설정
    min_side = min(img1.shape[0], img1.shape[1])
    win_size = min(7, min_side)  # win_size는 최소 크기 7과 이미지 최소 크기의 작은 값을 사용
    ssim_value, _ = compare_ssim(img1, img2, full=True, win_size=win_size, channel_axis=2)
    return ssim_value

def load_image(image_path, target_size=None):
    """Loads an image, resizes it if a target size is provided, and converts it to RGB."""
    image = Image.open(image_path).convert('RGB')
    if target_size:
        image = image.resize(target_size, Image.Resampling.LANCZOS)
    return image

def compute_average_ssim(real_image_dir, generated_image_dir):
    """Computes the average SSIM between two directories of images."""
    real_images = sorted(os.listdir(real_image_dir))
    generated_images = sorted(os.listdir(generated_image_dir))
    
    ssim_values = []
    
    for real_img_name, gen_img_name in zip(real_images, generated_images):
        real_img_path = os.path.join(real_image_dir, real_img_name)
        gen_img_path = os.path.join(generated_image_dir, gen_img_name)
        
        real_img = load_image(real_img_path)
        gen_img = load_image(gen_img_path, target_size=real_img.size)
        
        ssim_value = calculate_ssim(real_img, gen_img)
        ssim_values.append(ssim_value)
        print(f"SSIM for {real_img_name} and {gen_img_name}: {ssim_value}")

    average_ssim = np.mean(ssim_values)
    return average_ssim

# Example usage
real_image_dir = 'real'
generated_image_dir = 'output'
average_ssim = compute_average_ssim(real_image_dir, generated_image_dir)
print(f'Average SSIM: {average_ssim}')
