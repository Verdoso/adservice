from demo_pb2 import Ad

camera = Ad( redirect_url='/product/2ZYFJ3GM2N', text='Film camera for sale. 50% off.')
lens = Ad( redirect_url='/product/66VCHSJNUP', text='Vintage camera lens for sale. 20% off')
recordPlayer = Ad( redirect_url='/product/0PUK6V6EV0"', text='Vintage record player for sale. 30% off.')
bike = Ad( redirect_url='/product/9SIQT8TOJO"', text='City Bike for sale. 10% off.')
baristaKit = Ad( redirect_url='/product/1YMWWN1N4O"', text='Home Barista kitchen kit for sale. Buy one, get second kit for free')
airPlant = Ad( redirect_url='/product/6E92ZMYYFZ"', text='Air plants for sale. Buy two, get third one for free')
terrarium = Ad( redirect_url='/product/L9ECAV7KIM"', text='Terrarium for sale. Buy one, get second one for free')

ads_by_category = {
    "photography": [ camera, lens ],
    "vintage": [ camera, lens, recordPlayer ],
    "cycling": [ bike ],
    "cookware": [ baristaKit ], 
    "gardening": [ airPlant, terrarium]
}

from itertools import chain

add_by_url = dict()
for ad in chain(*ads_by_category.values()):
    if ad.redirect_url not in add_by_url:
        add_by_url[ad.redirect_url] = ad
all_ads = list(add_by_url.values())