import requests
import pprint
import pandas as pd
import csv
#ライブラリの導入

REQUEST_URL = "https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426?"
APP_ID = "1020456938647513185"
#API情報を定数に代入

large = str(input("国などを示すコード(lrgeClassCode)を入力してください>>(例：japan)"))
middle = str(input("都道府県などを示すコード(middleClassCode)を入力してください>>(例：tokyo)"))
small = str(input("市などを示すコード(smallClassCode)を入力してください>>(例：shibuya)"))
#宿泊施設の地域を選択(入力)

params={
    "applicationId":APP_ID,
    "format":"json",
    "largeClassCode":large,
    "middleClassCode":middle,
    "smallClassCode":small
}
#パラメータの設定

res = requests.get(REQUEST_URL,params)
result = res.json()
#jsonファイルに変換

df = pd.DataFrame()
hotels = result["hotels"]
for i,hotel in enumerate(hotels):
    hotel_info = hotel["hotel"][0]["hotelBasicInfo"]
    _df = pd.DataFrame(hotel_info,index=[i])
    df = df.append(_df)
#データの収集とpandasで表に変換

df[['hotelName', 'hotelInformationUrl','hotelMinCharge','telephoneNo','reviewAverage']].to_csv("hotel.csv",index=False)
#pandasで表化したファイルをcsvファイルに変換