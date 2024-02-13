import json
import requests
import urllib.request
from pprint import pprint


url = "https://instagram-downloader.p.rapidapi.com/index"
post = "https://www.instagram.com/reel/C07TX_ZL29J/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="

querystring = {"url": post}

headers = {"X-RapidAPI-Key": "TOKEN",
           "X-RapidAPI-Host": "instagram-downloader.p.rapidapi.com"}

response = requests.get(url, headers=headers, params=querystring)
url_link = json.loads(response.text)
video_link = url_link["result"]["video_url"]
video_name = url_link["result"]["username"]

video = urllib.request.urlretrieve(video_link, f"{video_name}.mp4")

pprint(response.text)


# import requests
# from pprint import pprint
# url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/"
# post = "https://www.instagram.com/reel/C07TX_ZL29J/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
#
# querystring = {"url": post}
#
# headers = {"X-RapidAPI-Key": "48ec87fe45mshecb35adf6cb2136p11cf43jsn838685d94fd2",
#            "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"}
#
# response = requests.get(url, headers=headers, params=querystring)
#
# pprint(response.json())
#
text = [{
            "thumb": 'https://proxy.mediadownloader.app/get?__sig=Zf3kQFqa1TFPIszM0Ol7aA&__expires=1704626881&uri'
                     '=https%3A%2F%2Finstagram.fkwi4-3.fna.fbcdn.net%2Fv%2Ft51.2885-15'
                     '%2F411153552_888180802971491_492231579977556614_n.jpg%3Fstp%3Ddst-jpg_e15%26_nc_ht%3Dinstagram'
                     '.fkwi4-3.fna.fbcdn.net%26_nc_cat%3D111%26_nc_ohc%3DwCfOvW0dXkkAX99fORU%26edm%3DAP_V10EBAAAA'
                     '%26ccb%3D7-5%26oh%3D00_AfDuqiGTzkRJsVuUvffxM8n-UtvdP2kaa0zmcBd2M9zbyA%26oe%3D659AEBBC%26_nc_sid'
                     '%3D2999b8&__srvid=instagram&__cid=mTY2wLHa1yPMcXBdrchsqQ',
            'title': 'Jingle bellll  '
            '.......@neymarjr#neymar2020#neymar_jr#neymarsantos....#neymar '
            '#neymarjr #Neymarskills #Neymar10 #Neymar11#neymarzete '
            '#neymarprime #neymarjunior #neymarpsg #neymarzetes #nutmeg '
            '#neymarfans #neymarbrasil #trend #new #neymarjr10 #neymaredits #',
            'type': 'video',
            'url': "https"}]


