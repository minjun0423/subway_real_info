from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# 서울시 지하철 실시간 도착정보 Open API 키
API_KEY = 'YOUR_API_KEY'

@app.get("/")
def read_root():
    return {"message": "서울시 지하철 실시간 도착 정보 API. /subway/{station} 경로를 통해 검색하세요."}

@app.get("/subway/{station}")
def get_subway_info(station: str):
    url = f"http://swopenAPI.seoul.go.kr/api/subway/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    response = requests.get(url)
    data = response.json()

    if 'errorMessage' in data:
        raise HTTPException(status_code=404, detail=data['errorMessage']['message'])

    results = []
    for item in data['realtimeArrivalList']:
        result = {
            '열차번호': item['trainNo'],
            '지하철호선ID': item['subwayId'],
            '첫번째도착메세지': item['arvlMsg2'],
            '두번째도착메세지': item['arvlMsg3']
        }
        results.append(result)

    return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
