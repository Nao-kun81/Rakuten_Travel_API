import requests
import pprint
import pandas as pd
import csv
import time

#API情報を定数に代入
REQUEST_URL = "https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426?"
APP_ID = "発行されたAPP_ID"

#宿泊施設の地域を選択(入力)
large = str(input("国などを示すコード(largeClassCode)を入力してください(例：japan)>>"))
middle = str(input("都道府県などを示すコード(middleClassCode)を入力してください(例：tokyo)>>"))
small = str(input("市などを示すコード(smallClassCode)を入力してください例：shibuya)>>"))

#パラメータの設定
params={
    "applicationId":APP_ID,
    "format":"json",
    "largeClassCode":'国を示すコード(例:japan)',
    "middleClassCode":'都道府県を示すコード(例:tokyo)',
    "smallClassCode":'市を示すコード(例:shibuya)',
    "hits":'検索件数(int)'
}

#jsonファイルに変換
res = requests.get(REQUEST_URL,params)
result = res.json()

#データの収集とpandasで表に変換
df = pd.DataFrame()
hotels = result["hotels"]
for i,hotel in enumerate(hotels):
    hotel_info = hotel["hotel"][0]["hotelBasicInfo"]
    _df = pd.DataFrame(hotel_info,index=[i])
    df = df.append(_df)

#同じディレクトリ内にcsvファイルを保存する
df[['hotelName', 'hotelInformationUrl','hotelMinCharge','telephoneNo','reviewAverage']].to_csv("hotel.csv",index=False)
