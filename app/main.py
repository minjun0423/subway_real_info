from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = "427a53796b6d696e37344f6451594a"  # ����� ����API Ű
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

@app.get("/")
def read_root():
    return {"message": "Subway Info"}


#@app.get("/")
#def read_root(station: str = Query(..., title="Subway Station", description="Enter the subway station name to get real-time arrival information")):
    # ����ڰ� �Է��� ������ �޾ƿͼ� �ش� ������ �����̷�Ʈ
#    return RedirectResponse(url=f"/subway/{station}")

@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json() #JSON ���� ��ȯ ������
        
    processed_data = [] # ������ ����
    for arrival_info in data["realtimeArrivalList"]:
        station = arrival_info["statnNm"]
        train_line = arrival_info["trainLineNm"] #������ ���
        arvlMsg2 = arrival_info["arvlMsg2"] #ù��°�����޼���, (����, ��� , ���� ��)
        arvlMsg3 = arrival_info["arvlMsg3"] #�ι�°�����޼���, (���տ�� ����,12�� �� (�����Ÿ�) ��)
        updownline = arrival_info["updnLine"]
        barvlDt = arrival_info["barvlDt"]
        btrainNo = arrival_info["btrainNo"]
        subwayId = arrival_info["subwayId"]
        #cur_time = r.json()['datetime']
        #ordkey = arrival_info["ordkey"]

        processed_data.append({"������ȣ": btrainNo, "ȣ��": subwayId, "�����༱����": updownline, "����ö ��ġ": arvlMsg3, "����ö ��������": arvlMsg2})
    return processed_data