from django.http import HttpResponse
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from sea.models import Project
from datetime import datetime
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the sea index.")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicia el webdriver con el chromedriver como parametro
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# 1) Se dirige a la página web
driver.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php#")
id = driver.find_element(By.ID,"info_resultado")
max_pages = int(id.text[-5:].replace(",",""))

for page_index in range(1,10): #Change 10 to max_pages+1 
    print("Processing page : ",page_index)
    if page_index > 1:
        dropdown = driver.find_element(By.NAME, "pagina_offset")
        dropdown.find_element(By.XPATH, f"//option[. = '{page_index}']").click()

    table_id = driver.find_element(By.CLASS_NAME, 'tabla_datos')
    rows = table_id.find_elements(By.TAG_NAME, "tr") 
    for row in rows:
        col = row.find_elements(By.TAG_NAME, "td") 
        if(len(col)>1):
            Project.objects.create(name=col[1].text,
                                   document_type=col[2].text,
                                   region=col[3].text,
                                   typology=col[4].text,
                                   owner=col[5].text,
                                   investment=col[6].text,
                                   presentation_date=datetime.strptime(col[7].text,"%d/%m/%Y"),
                                   status=col[8].text)
driver.quit()

def projects(request):
   projects = Project.objects.all()
   return render(request, "home.html", {'projects':projects})