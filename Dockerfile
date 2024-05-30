# ���̽� �̹����� Python 3.9 ���
FROM python:3.9

# �۾� ���丮�� �����մϴ�
WORKDIR /app

# �ʿ��� ��Ű���� ��ġ�մϴ�
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ���ø����̼� �ҽ� �ڵ带 �����մϴ�
COPY ./app /app

# Uvicorn�� ����Ͽ� ���ø����̼��� �����մϴ�
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
