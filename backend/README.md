# ControlNet

backend 코드

- fastapi의 lifespan을 처음 써봄 (이전의 on_event의 startup과shutdown를 좀더 확장한 느낌)
- lifespan으로 앱이 시작전 미리 ml model을 불러오고 앱이 종료시엔 종료할 수 있도록 하여 OOM 문제를 해결함
