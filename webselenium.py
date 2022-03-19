from selenium import webdriver
import urllib.request
import json
from datetime import datetime
import requests

PATH = "D:\python\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/hot-100/")

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time)
ListIMBD = []


for rich in driver.find_elements_by_class_name("o-chart-results-list-row-container"):
    print(rich.text)
    for img in rich.find_elements_by_class_name("c-lazy-image__img"):
        print(img.get_attribute("src"))
   
        ListIMBD.append(
        {"No": rich.text.split("\n")[0],
        "Judul": rich.text.split("\n")[1],
        "Penyanyi": rich.text.split("\n")[2],
        "Lama":rich.text.split("\n")[5],
        "Image": img.get_attribute("src"),
        "Waktu_Scrapping":now.strftime("%Y-%m-%d %H:%M:%S")
        }
        )

hasil_scraping = open("hasilscraping.json", "w")
json.dump(ListIMBD, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()