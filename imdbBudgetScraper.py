from bs4 import BeautifulSoup
import csv
import urllib2
budget = "NA"
openingWeekend = "NA"
gross = "NA"
supercount = 0
f = open('timeoutids.txt','w')
with open('imdbbudget.csv','w') as csvfile1:
	fieldnames = ['imdbid','budget','opening weekend simple','gross simple','opening weekend','gross']
	writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
	writer.writeheader()
	with open('omdbdump.csv', 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if len(row) > 1:
					try:
						count = 3
						budget = "NA"
						openingWeekend = "NA"
						gross = "NA"
						id = row[15]
						print supercount
						supercount = supercount + 1
						urls = 'http://www.imdb.com/title/'+id+'/business?ref_=tt_dt_bus'
						print(urls)
						response = urllib2.urlopen(urls)
					
						html = response.read()
						soup = BeautifulSoup(html,'html.parser')
						content = soup.find(id="tn15content")
						#print(content)
						x = str(content)
						soup2 = BeautifulSoup(x,'html.parser')
						data = soup2.get_text().encode('utf-8')
						lines = data.splitlines()
						i = 0
						while True:
							if lines[i] == "Budget":
								i = i+1
								budget = lines[i]
								count = count-1
							if lines[i] == "Opening Weekend":
								i = i+1
								openingWeekend = lines[i]
								count = count-1
							if lines[i] == "Weekend Gross":
								i = i+1
								gross = lines[i]
								count = count-1
							i = i+1
							if i == len(lines):break
							if count == 0:break
						writer.writerow({'imdbid':id,'budget':budget,'opening weekend simple':openingWeekend.split(" ")[0],'gross simple':gross.split(" ")[0],'opening weekend':openingWeekend,'gross':gross})
						print budget+" "+openingWeekend+" "+gross
					except Exception:
						print "came here"
						f.write(id+"\n")
						pass