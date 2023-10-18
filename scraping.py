import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div",class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text:"python" in text.lower()    
)
