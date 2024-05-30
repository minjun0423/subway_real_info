from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = "427a53796b6d696e37344f6451594a"  # ����� ����API Ű
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

class ArrivalInfo(BaseModel):
    ������ȣ: str
    ȣ��: str
    �����༱����: str
    ����ö_��ġ: str
    ����ö_��������: str

@app.get("/")
def read_root():
    return {"message": "Subway Info"}

@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()  # JSON ���� ��ȯ ������
        
        processed_data = []  # ������ ����
        for arrival_info in data.get("realtimeArrivalList", []):
            processed_data.append(ArrivalInfo(
                ������ȣ=arrival_info.get("btrainNo", ""),
                ȣ��=arrival_info.get("subwayId", ""),
                �����༱����=arrival_info.get("updnLine", ""),
                ����ö_��ġ=arrival_info.get("arvlMsg3", ""),
                ����ö_��������=arrival_info.get("arvlMsg2", "")
            ))
        return processed_data
    except Exception as e:
        return {"error": str(e)}
