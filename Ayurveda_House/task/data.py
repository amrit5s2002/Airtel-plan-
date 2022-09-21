
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

def Data():
    data = []
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.minimize_window()
    driver.get('https://www.airtel.in/myplan-infinity/')
    elements = driver.find_elements(By.XPATH, "//span[contains(@class,'price')]")
    # print(type(elements))
    for p in elements:
        # print(p.text)
        plan = p.text
        
        if p.text != "":
            data.append(p.text)
        

    for d in plan:
        if d == "":
            print("blank")
            del(d)
    # print(data)

    filename = 'data.csv'
    with open(filename, 'w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(plan)
        
    return data
