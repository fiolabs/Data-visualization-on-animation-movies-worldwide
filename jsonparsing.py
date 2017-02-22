import urllib2
import json
import csv
import re
from bs4 import BeautifulSoup
i = 0;
directedBy = "NA"
producedBy = "NA"
screenplayBy = "NA"
storyBy = "NA"
starring = "NA"
musicBy = "NA"
editedBy = "NA"
productioncompanies = "NA"
distributionBy = "NA"
runningTime = "NA"
country = "NA"
language = "NA"
budget = "NA"
boxoffice = "NA"
count = 0;
with open('animdump2.csv', 'w') as csvfile:
    fieldnames = ['title','directed by','produced by','screenplay by','story by','starring','music by','edited by','companies','distributed by','running time','country','Language','Budget','Boxoffice']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    with open('movies.csv', 'rU') as csvfile:
    	reader = csv.reader(csvfile)
    	for row in reader:
			count=count+1
			if "nimat" in str(row[2]):
				title = str(row[1])[:-7]
			else:
				continue
			print(title+"   "+str(count))
			try:
				directedBy = "NA"
				producedBy = "NA"
				screenplayBy = "NA"
				storyBy = "NA"
				starring = "NA"
				musicBy = "NA"
				editedBy = "NA"
				productioncompanies = "NA"
				distributionBy = "NA"
				runningTime = "NA"
				country = "NA"
				language = "NA"
				budget = "NA"
				boxoffice = "NA"
				##print("came here in try 1")
				response = urllib2.urlopen('https://en.wikipedia.org/wiki/'+title)
				##print("came here in try 2")
				html = response.read()
				##print("came here in try 3")
				soup = BeautifulSoup(html,'html.parser')
				table2 = str(soup.table)
				##print(table2)
				soup = BeautifulSoup(table2,'html.parser')
				data = soup.find_all('tr')
				i = 0
				del (data[0])
				del (data[0])
				for strs in data:
					soup2 = BeautifulSoup(str(strs),'html.parser')
					data = str(soup2.td)
					##print(str(data)+"===")
					headData = "lol"
					for head in soup2.find_all('th'):
						headData = str(head.string)	
						##print(headData)
						soup3 = BeautifulSoup(str(data),'html.parser')
						tdata = str(soup3.td.text.encode('utf-8'))
						if "rodu" in headData:
							producedBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+producedBy)
							continue
						if "tory" in headData:
							storyBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+storyBy)
							continue
						if "arr" in headData:
							starring = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+starring)
							continue
						if "usic" in headData:
							musicBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+musicBy)
							continue
						if "dit" in headData:
							editedBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+editedBy)
							continue
						if "reen" in headData:
							screenplayBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+screenplayBy)
							continue
						if "nemato" in headData:
							screenplayBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+screenplayBy)
							continue
						if "rect" in headData:
							directedBy = str(soup3.td.text.encode('utf-8')).strip(" ")
							#print(headData+"---->"+directedBy)
							continue
						if "ountry" in headData:
							country = tdata
							#print(headData+"---->"+country)
							continue
						if "Box" in headData: 
							boxoffice = tdata
							#print(headData+"---->"+boxoffice)
							continue 	
						if "get" in headData:
							budget = tdata
							#print(headData+"---->"+budget)
							continue
						if "None" in headData:
							data = str(soup2.div.text)
							if "nnin" in data:
								runningTime = tdata
								#print(data+"---->"+runningTime)
							if "duct" in data:
								productioncompanies = str(soup3.td.text.encode('utf-8'))
								#print(data+"---->"+productioncompanies)
							continue
					#print("\n\n\n")
			except Exception:
				#print("came as exception!")
				pass
			writer.writerow({'title' : title,'directed by' : directedBy,'produced by': producedBy,'screenplay by' : screenplayBy,'story by':storyBy,'starring':starring,'music by' : musicBy,'edited by' : editedBy,'companies' : productioncompanies,'distributed by' : distributionBy,'running time' : runningTime,'country':country,'Language':language,'Budget':budget,'Boxoffice':boxoffice})
			