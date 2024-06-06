from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# ����� ����ö �ǽð� �������� Open API Ű
API_KEY = 'YOUR_API_KEY'

@app.get("/")
def read_root():
    return {"message": "����� ����ö �ǽð� ���� ���� API. /subway/{station} ��θ� ���� �˻��ϼ���."}

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
            '������ȣ': item['trainNo'],
            '����öȣ��ID': item['subwayId'],
            'ù��°�����޼���': item['arvlMsg2'],
            '�ι�°�����޼���': item['arvlMsg3']
        }
        results.append(result)

    return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
