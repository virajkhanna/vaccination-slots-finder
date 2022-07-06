# Made by Viraj Khanna
# Copyright ©️ 2022-Present Viraj Khanna

import json
import requests
from time import sleep
from datetime import datetime, date

pins = []
i2 = 0

while i2 < 7:
    pins.append(input("Enter the pincode to search (You will be asked 7 times): "))
    i2 = i2 + 1

headers={'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586', "Upgrade-Insecure-Requests": "1", "Connection": "keep-alive"}
today = date.today()
tdate = today.strftime("%d/%m/%Y")
pin = 110001
i = 0
i3 = 0

while i3 < int(len(pins)):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(int(pins[i3]), tdate)
    x1= requests.get(url, headers=headers)
    y = json.loads(x1.text)

    sessions = y["sessions"]

    cen = None

    now = datetime.now()

    print("Check: " + pins[i3])

    for session in sessions:
        cen = sessions[i]
        if(cen["min_age_limit"] == 18 and cen["vaccine"] == "COVISHIELD" and cen["fee_type"] == "Free"):
            time = now.strftime("%H:%M:%S")
            f = "\n---------------------------------------------------------\n" + str(time) + ": "+ "Name: " + cen["name"] + "\nPincode: " + str(cen["pincode"]) + "\n---------------------------------------------------------"
            print(f)
            break
        if(cen == None):
            print("Empty")
            break

        sleep(3)
            
    i3 = i3 + 1

    sleep(2)
