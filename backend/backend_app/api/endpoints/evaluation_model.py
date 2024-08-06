import uuid
import cv2
import time

from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
import numpy as np
from annotator.canny import CannyDetector
from cldm.model import create_model, load_state_dict
from cldm.ddim_hacked import DDIMSampler
from backend_app.api.utils_process import process
from backend_app.core.config import settings

router = APIRouter()

apply_canny = CannyDetector()

model = create_model(settings.PATH_BASE_MODEL_V10).cpu()
model.load_state_dict(load_state_dict(settings.WEIGHT_PATH_BASE_MODEL_V10, location='cuda'))
model = model.cuda()
ddim_sampler = DDIMSampler(model)


@router.post("/process")
async def process_image(
    input_image: UploadFile = File(...),
    prompt: str = Form(...),
    a_prompt: str = Form('best quality, extremely detailed'),
    n_prompt: str = Form('longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality'),
    num_samples: int = Form(1),
    image_resolution: int = Form(512),
    ddim_steps: int = Form(20),
    guess_mode: bool = Form(False),
    strength: float = Form(1.0),
    scale: float = Form(9.0),
    seed: int = Form(-1),
    eta: float = Form(0.0),
    low_threshold: int = Form(100),
    high_threshold: int = Form(200)
):
    input_image = np.fromstring(await input_image.read(), np.uint8)
    input_image = cv2.imdecode(input_image, cv2.IMREAD_COLOR)
    
    # process가 실행되는 시간 측정
    process_start_time = time.time()

    result_images = process(
        apply_canny, model, ddim_sampler,
        input_image, prompt, a_prompt, n_prompt, num_samples, image_resolution, ddim_steps,
        guess_mode, strength, scale, seed, eta, low_threshold, high_threshold
    )

    process_end_time = time.time()
    # process가 실행된 시간
    process_time = process_end_time - process_start_time

    unique_prefix = uuid.uuid4().hex

    output_paths = []

    for i, image in enumerate(result_images):
        output_path = f'./result_images/result_{unique_prefix}_{i}.png'
        output_paths.append(output_path)
        cv2.imwrite(output_path, image)

    return {
        'output_paths' : output_paths,
        'process_time': process_time
    }
