import requests

URL = "https://realpython.github.io/fake-jobs/"
URL = "https://www.hankyung.com/"
page = requests.get(URL)

print(page.text)
