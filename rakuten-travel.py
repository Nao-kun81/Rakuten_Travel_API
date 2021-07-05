import requests
import pprint
import pandas as pd
import csv
import time

#API情報を定数に代入
REQUEST_URL = "https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426?"
APP_ID = "1020456938647513185"

#起動説明
print("\r\n\r\n【楽天トラベル施設検索】\r\n\r\n")
print("：注意説明：")
print("""
    ・入力内容はすべて半角英数字で入力してください。
    ・入力内容にエラーがある場合プログラムが停止します。
    ・検索結果は同じディレクトリ内にCSVファイル(hotel.csv)として保存します。
""")

#宿泊施設の地域を選択(入力)
large = str(input("国などを示すコード(largeClassCode)を入力してください(例：japan)>>"))
middle = str(input("都道府県などを示すコード(middleClassCode)を入力してください(例：tokyo)>>"))
small = str(input("市などを示すコード(smallClassCode)を入力してください例：shibuya)>>"))

#入力確認
print("\r\n\r\n=======入力内容の確認=======")
print(">　国は【",large,"】を指定中")
print(">　都道府県は【",middle,"】を指定中")
print(">　市は【",small,"】を指定中")
print("============================")
menu_check = str(input("\r\n\r\n【確認】こちらの内容でお間違いないですか？＜はい：1 / いいえ：２＞(番号を選択)>>"))

#入力内容に不備または間違いがある場合
if menu_check == "2":
    while True:
        large = str(input("\r\n\r\n国などを示すコード(lrgeClassCode)を入力してください(例：japan)>>"))
        middle = str(input("都道府県などを示すコード(middleClassCode)を入力してください(例：tokyo)>>"))
        small = str(input("市などを示すコード(smallClassCode)を入力してください例：shibuya)>>"))
        print("\r\n\r\n=======入力内容の確認=======")
        print(">　国は【",large,"」を指定中")
        print(">　都道府県は【",middle,"】を指定中")
        print(">　市は【",small,"】を指定中")
        print("============================")
        menu_check = str(input("\r\n\r\n【確認】こちらの内容でお間違いないですか？＜はい：1 / いいえ：２＞(番号を選択)>>"))
        if menu_check == "1":
            break

hit = int(input("\r\n\r\n検索結果を何個取得しますか？(1以上30以下：半角数字を入力)>>"))
if 1>hit or 30<hit:
    while True:
        print("\r\n\r\n検索結果は1以上30以下しか指定できません。")
        hit = int(input("検索結果を何個取得しますか？(1以上30以下：半角数字を入力)>>"))
        if 1<=hit<=30:
            break

#パラメータの設定
params={
    "applicationId":APP_ID,
    "format":"json",
    "largeClassCode":large,
    "middleClassCode":middle,
    "smallClassCode":small,
    "hits":hit
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

#pandasで表化したファイルをcsvファイルに変換
df[['hotelName', 'hotelInformationUrl','hotelMinCharge','telephoneNo','reviewAverage']].to_csv("hotel.csv",index=False)

#csvファイルの保存が完了
print("\r\n\r\n同じディレクトリ内にcsvファイルが生成されました")
print("\r\n\r\n【楽天トラベル施設検索】を終了します")
time.sleep(1)