# import requests
# from pprint import pprint
# from api_key import key
#
#
# model = input("Enter your favorite car: ")
# api_url =
# response = requests.get(api_url, headers={'X-Api-Key': key})
# if response.status_code == requests.codes.ok:
#     pprint(response.text)
# else:
#     print("Error:", response.status_code, response.text)

# import requests
# from api_key import key
# from pprint import pprint
#
# model = input("Mashinaning modelini kiriting: ")
# api_url = f'https://api.api-ninjas.com/v1/cars?model={model}'
# response = requests.get(api_url, headers={"X-Api-Key": key})
# if response.status_code == requests.codes.ok:
#     pprint(response.text)
# else:
#     print("Error:", response.status_code, response.text)


# bmw = ('[{"city_mpg": 14, "class": "compact car", "combination_mpg": 15, '
# '"cylinders": 6, "displacement": 2.5, "drive": "rwd", "fuel_type": "gas", '
#  '"highway_mpg": 17, "make": "import trade services", "model": "bmw 325i", '
#  '"transmission": "a", "year": 1992}, {"city_mpg": 12, "class": "midsize car", '
#  '"combination_mpg": 14, "cylinders": 6, "displacement": 3.4, "drive": "rwd", '
#  '"fuel_type": "gas", "highway_mpg": 18, "make": "j.k. motors", "model": '
#  '"bmw535i", "transmission": "a", "year": 1992}, {"city_mpg": 12, "class": '
#  '"midsize car", "combination_mpg": 14, "cylinders": 6, "displacement": 3.4, '
#  '"drive": "rwd", "fuel_type": "gas", "highway_mpg": 18, "make": "j.k. '
#  'motors", "model": "bmw635csi", "transmission": "a", "year": 1992}, '
#  '{"city_mpg": 12, "class": "midsize car", "combination_mpg": 14, "cylinders": '
#  '6, "displacement": 3.4, "drive": "rwd", "fuel_type": "gas", "highway_mpg": '
#  '18, "make": "j.k. motors", "model": "bmw635l6", "transmission": "a", "year": '
#  '1992}, {"city_mpg": 12, "class": "midsize car", "combination_mpg": 14, '
#  '"cylinders": 6, "displacement": 3.4, "drive": "rwd", "fuel_type": "gas", '
#  '"highway_mpg": 18, "make": "j.k. motors", "model": "bmw735i", '
#  '"transmission": "a", "year": 1992}]')


# import requests

# name = input("Name: ")
# api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
# response = requests.get(api_url, headers={'X-Api-Key': key})
# if response.status_code == requests.codes.ok:
#     pprint(response.text)
# else:
#     print("Error:", response.status_code, response.text)
# print(type(json.loads(response.text)))


# import requests
# from api_key import key
# from pprint import pprint
# import json
# name = input(">>>>")
# api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(name)
# response = requests.get(api_url, headers={'X-Api-Key': key})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)


from pprint import pprint
# a = input(">>>>>>>")
# api_url = f'https://api.api-ninjas.com/v1/country?name={a}'
# response = requests.get(api_url, headers={'X-Api-Key': key})
# if response.status_code == requests.codes.ok:
#     pprint(response.text)
# else:
#     print("Error:", response.status_code, response.text)

# weather = ('{"cloud_pct": 99, "temp": 3, "feels_like": -1, "humidity": 83, "min_temp": '
#             '1, "max_temp": 4, "wind_speed": 3.76, "wind_degrees": 229, "sunrise": '
#             '1699938110, "sunset": 1699968368}')


# city = input("City: ")
# api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
# response = requests.get(api_url, headers={'X-Api-Key': key})
# if response.status_code == requests.codes.ok:
#     pprint(type(json.loads(response.text)))
# else:
#     print("Error:", response.status_code, response.text)

# city = 'london'
# api_url = 'https://api.api-ninjas.com/v1/worldtime?city={}'.format(city)
# response = requests.get(api_url, headers={'X-Api-Key': key})
# if response.status_code == requests.codes.ok:
#     pprint(response.text)
# else:
#     print("Error:", response.status_code, response.text)

# import requests
# from PIL import Image, ImageDraw, ImageFont
#
# font = ImageFont.truetype("arial.ttf", size=30)
# comm = input("Message")
#
# url = f"https://al-quran1.p.rapidapi.com/{comm}"
# headers = {
#     "X-RapidAPI-Key": "48ec87fe45mshecb35adf6cb2136p11cf43jsn838685d94fd2",
#     "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
# }
# response = requests.get(url, headers=headers)
# data = response.json()
# dic1 = data['verses']
# for i in dic1:
#     img = Image.new("RGBA", (640, 640), "white")
#     draw = ImageDraw.Draw(img)
#     draw.text((400, 400), text=dic1[i]["content"], fill="black", font=font)
#     img.show()

import requests
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
from pprint import pprint

comm = int(input("Sura raqamini kiriting: "))

url = f"https://al-quran1.p.rapidapi.com/{comm}"

headers = {
  "X-RapidAPI-Key": "TOKEN",
  "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()
# pprint(data["surah_name"])
pprint(data)