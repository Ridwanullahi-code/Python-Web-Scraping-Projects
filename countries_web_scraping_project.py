import requests
from bs4 import BeautifulSoup
import pandas as pd


class Myproject:


    def get_data(self,url):
        respond = requests.get(url)
        soup = BeautifulSoup(respond.text,"html.parser")
        return soup

    def parse(self):

    	country_list = []

    	soup = self.get_data("https://www.scrapethissite.com/pages/simple/")
    	country_info = soup.find_all('div',{'class':'col-md-4 country'})
    
    	for country in country_info:

    		country_dict = {

    				"Name": country.h3.text.strip(),
    				"Capital": country.div.span.text.strip(),
    				"Population": country.div.find('span',{'class':'country-population'}).text.strip()
    		}
    		country_list.append(country_dict)

    	return country_list


    def create_dataframe(self):
    	data = self.parse()
    	dataframe = pd.DataFrame(data)
        dataframe.to_csv("Country.csv",index=None)

    	return 'Successfully Done'

project = Myproject()
print(project.create_dataframe())


	