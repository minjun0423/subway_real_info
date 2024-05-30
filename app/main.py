from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

"""
API_KEY = "427a53796b6d696e37344f6451594a"  # 서울시 오픈API 키
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

class ArrivalInfo(BaseModel):
    열차번호: str
    호선: str
    상하행선구분: str
    지하철_위치: str
    지하철_도착까지: str
"""

@app.get("/")
def read_root():
    return {"message": "Subway Info"}

"""
@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()  # JSON 형식 변환 데이터
        
        processed_data = []  # 데이터 가공
        for arrival_info in data.get("realtimeArrivalList", []):
            processed_data.append(ArrivalInfo(
                열차번호=arrival_info.get("btrainNo", ""),
                호선=arrival_info.get("subwayId", ""),
                상하행선구분=arrival_info.get("updnLine", ""),
                지하철_위치=arrival_info.get("arvlMsg3", ""),
                지하철_도착까지=arrival_info.get("arvlMsg2", "")
            ))
        return processed_data
    except Exception as e:
        return {"error": str(e)}
"""
