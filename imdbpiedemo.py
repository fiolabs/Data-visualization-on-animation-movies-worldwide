import urllib2
import json
import csv
f = open('missingMovies.txt', 'w')
with open('omdbdump.csv','w') as csvfile1:
	fieldnames=['title','year','rated','released','runtime','genre','director','writer','actors','language','country','awards','metascore','imdbrating','imdbvotes','imdbid']
	writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
	writer.writeheader()
	with open('animdumpdup.csv', 'rU') as csvfile:
		reader = csv.reader(csvfile)
		
		for row in reader:
			try:
				title = str(row[8])
				response = urllib2.urlopen("http://www.omdbapi.com/?t="+title+"&y=&plot=short&r=json")
				#print(response)
				data = json.load(response)
				print(title+":\n")
				print(data["Response"])
				if str(data["Response"]) == "True":
					writer.writerow({'title' : data["Title"].encode('utf-8'),'year' : data["Year"],'rated':data["Rated"],'released':data["Released"],'runtime':data["Runtime"],'genre':data["Genre"],'director':data["Director"].encode('utf-8'),'writer':data["Writer"].encode('utf-8'),'actors':data["Actors"].encode('utf-8'),'language':data["Language"],'country':data["Country"],'awards':data["Awards"],'metascore':data["Metascore"],'imdbrating':data["imdbRating"],'imdbvotes':data["imdbVotes"],'imdbid':data["imdbID"]})
				else:
					f.write(title+" ^ bad response"+"\n")
			except Exception:
				print("\n$$$$$$$$$\n")
				f.write(title+" ^ connection time out"+"\n")
			print("\n")
