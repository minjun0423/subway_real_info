# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉토리를 설정합니다
WORKDIR /app

# 필요한 패키지를 설치합니다
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드를 복사합니다
COPY ./app /app

# Uvicorn을 사용하여 애플리케이션을 실행합니다
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
