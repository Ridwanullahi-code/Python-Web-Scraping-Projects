import requests
import pandas as pd 
from bs4 import BeautifulSoup
import re

pages = {'page1':'&vjk=a7582f2fbff00739',		
		'page2':'10&vjk=f9ebc1df67369bdb',
		'page3':'20&vjk=d6ee12cbcf2b59bd',
		'page4':'30&vjk=dd7e8254afa5c3d1',
		'page5':'40&vjk=a8c9891fda808680',
		'page6':'50&vjk=d7734a35247151e2',
		}

class JobSearch:
	url = 'https://ng.indeed.com/jobs?q=data%20analyst&l=anywhere&start='

	def parse(self):
		job_list = []

		for key,value in pages.items():
			respond = requests.get(self.url+value)
			soup = BeautifulSoup(respond.content, 'lxml')
			job_descrip = soup.find_all('td',{'class':'resultContent'})

			for job in job_descrip:
				
				job_dict = {
				"JobTitle":job.h2.span.text,
				"CompanyName":job.find('span',{'class':'companyName'}).text,
				"Location":job.find('div',{'class':'companyLocation'}).text.replace('+5 locations','').strip(),
				"Salary": str(job.find(string = re.compile(r'^₦\d+'))).replace('a month','').strip() 

				}

				if job_dict["Salary"] == "None":
					job_dict["Salary"] = "0"

				job_list.append(job_dict)
		
		return job_list
		
	def DataFrame(self):
		data = self.parse()

		dataframe = pd.DataFrame(data)

		dataframe.to_csv("JobSearch.csv",index=None)
		return "Successfully done"


project = JobSearch()
print(project.DataFrame())

