from selenium import webdriver
from bs4 import BeautifulSoup
import time

#START_URL= "https://www.jamiatimes.in/search?updated-max=2020-06-28T07%3A34%3A00-07%3A00&max-results=7#PageNo=7"
START_URL="https://www.jamiatimes.in/search?updated-max=2022-07-05T02%3A41%3A00-07%3A00&max-results=7#PageNo=2"
#START_URL= "https://www.indiatoday.in/science"
                
driver = webdriver.Chrome("./chromedriver")
driver.get(START_URL)
time.sleep(10)
def scrape():
    
    temp_l=[]
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    for div_tag in soup.find_all("div", attrs={"class", "blog-post hentry index-post"}):
        
        temp_l.append(str(div_tag))
    print(temp_l)   

    enclosing_start= "<html><head><link rel='stylesheet' " +  "href='styles.css'></head> <body>" 
    enclosing_end= "</body></html>"

    with open('restructured2.html', 'w+',  encoding='utf-16') as f:
        f.write(enclosing_start)
        f.write('\n' + '<p> EXTRACTED CONTENT START </p>'+'\n')
        for items in temp_l: 
            f.write('%s' %items)
        f.write('\n' + enclosing_end)    
                   
    print("File written successfully")
    f.close()

scrape()
