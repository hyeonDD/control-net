from backend_app.core.config import settings
import aiohttp
import random
import uuid


async def fetch_image_data(session, url):
    """
    이미지 데이터 메타데이터 가져오기
    """
    async with session.get(url) as response:
        return await response.json()


async def download_image(query):
    """
    dir에 저장
    """
    url = f'https://pixabay.com/api/?key={settings.PIXABAY_API_KEY}&q={query}&image_type=photo'

    async with aiohttp.ClientSession() as session:
        data = await fetch_image_data(session, url)

        if 'hits' in data and len(data['hits']) > 0:
            image = random.choice(data['hits'])
            image_url = image['largeImageURL']
            # 다운로드 이미지 하드코딩
            unique_prefix = uuid.uuid4().hex
            os.makedirs('./result_images', exist_ok=True)
            file_path = f'./result_images/random_{query}_{unique_prefix}.jpg'

            async with session.get(image_url) as response:
                with open(file_path, 'wb') as file:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        file.write(chunk)

            return file_path
        else:
            return False
