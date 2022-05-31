# 引用requests模組 (# 快速註解 ctrl + / )
# 一種用來發送 HTTP requests的模組
import requests
import json

# 空氣品質報告API網址
url = "https://data.epa.gov.tw/api/v2/aqx_p_488?offset=0&api_key=f229005f-00b4-4796-be01-19f352289290"

# 透過requests模組對指定網址發送HTTP Request
# 取得對方伺服器(行政院環保署的伺服器)的回應
res = requests.get(url)

# 出現[200]表示正常  出現[4xx]表示網址錯誤  出現[5xx]表示伺服器錯誤
# print(res)

# 伺服器回傳的資料
data = res.json()
# print(json.dumps(data, indent=2, ensure_ascii=False)) 
records = data['records']
for i in records:
    # print(i)
    report = f"{i['sitename']} 縣市:{i['county']} 空氣品質:{i['aqi']} 狀態:{i['status']} 時間:{i['datacreationdate']}"
    print(report)
    print("=================")


search_term = str(input("請數入ㄧ個查詢地標\n"))
report = f"你所輸入的{search_term}並不存在於資料庫"
for r in records:
    if r["sitename"] == search_term:
        report = f"{r['sitename']} 縣市:{r['county']} 空氣品質:{r['aqi']} 狀態:{r['status']} 時間:{r['datacreationdate']}"
print(report)