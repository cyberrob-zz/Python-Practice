import requests
from bs4 import BeautifulSoup

url = "https://iplay.sa.gov.tw/odata/Gym(9453)?$format=application/json;odata.metadata=none"

payload = {}
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
  'Cookie': '__RequestVerificationToken=I1poRqnJEzb6LCEjPz4fDZQjQrfZgKXb5Vndg9d4qAlmJlwNseoPfNTh8gl-C8rt12xendi2FF8isEukT1f9aJ13VjFr43BASflL_U0oViQ1'
}

response = requests.request("GET", url, headers=headers, data = payload)
soup = BeautifulSoup(response.content, "html.parser")

print(soup)
