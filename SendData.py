import urllib, urllib.request

BASE_URL = 'https://api.thingspeak.com/update.json'
WRITE_KEY = 'KZ34WHKW50OY83HS'

def send_hcho(hcho):
    data = urllib.parse.urlencode({'api_key' : WRITE_KEY, 'field1' : hcho}).encode(encoding='UTF8')
    try:
        response = urllib.request.urlopen(url=BASE_URL, data=data, timeout=10)
    except Exception as ex:
        print (ex)
        return

    print (response.read())

def send_air_data(HCHO = None, Temperature=None, Humidity=None, TVOC=None, CO2=None):
    values={}
    values['api_key'] = WRITE_KEY
    if HCHO is not None:
        values['field1'] = HCHO
    if Temperature is not None:
        values['field2'] = Temperature
    if Humidity is not None:
        values['field3'] = Humidity
    if TVOC is not None:
        values['field4'] = TVOC
    if CO2 is not None:
        values['field5'] = CO2

    data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    try:
        response = urllib.request.urlopen(url=BASE_URL, data=data, timeout=10)
    except Exception as ex:
        print (ex)
        return

    print (response.read())