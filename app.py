from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re
import unicodedata 
import pandas as pd

def slugify(text):    
    text = unicodedata.normalize("NFKD", text)      
    text = text.replace("“", "").replace("”", "").replace("’", "'").replace("‘", "'")      
    text = text.replace("'", "")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text)       
    return text.strip("-").lower()

def get_data( name):
    driver = webdriver.Chrome()
    url = slugify(name)
    driver.get(f"https://www.concertarchives.org/bands/{url}?date=upcoming")  
    time.sleep(1)
    concerts = []
    rows = driver.find_elements(By.XPATH, '//*[@id="band-show-table-condensed"]/tbody/tr[@style="cursor: pointer;" and not(contains(@class, "expand-duplicates"))]')
    
    
    for row in rows:
        try:
            date = row.find_element(By.XPATH, './/td[1]/span').text.strip()
            concert = row.find_element(By.XPATH, './/td[2]/span/strong/a')
            concert_link = concert.get_attribute('href')
            concert = concert.text.strip()
            venue = row.find_element(By.XPATH, './/td[3]').text.strip()
            location = row.find_element(By.XPATH, './/td[4]').text.strip().split(',')
            city = location[0]
            state = location[1]
            country = location[2]
            
            concerts.append({
                'Name':name,
                'Date': date,
                'Concert': concert,
                'ConcertLink' : concert_link,
                'Venue': venue,
                'City':city,
                'State':state,
                'Country': country
            })
        except Exception as e:
            print(f"Skipping row due to error: {e}")
    driver.quit()
    return concerts

def main():   
    
    df = pd.read_excel('artist_names.xlsx')
    data = []
    for name in df['artist_name'].iloc[0:200].values:
        data.extend(get_data(name))
        print("Finished!! ",name)
    out_df = pd.DataFrame(data)
    out_df.to_csv('Output.csv')
   
    

if __name__ == "__main__":
    main()