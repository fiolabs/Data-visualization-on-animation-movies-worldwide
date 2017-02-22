import csv
import urllib2
import json



with open('animdump.csv', 'w') as csvfile:
    fieldnames = ['poster_path','adult','overview','release_date','genre_ids','id','original_title','original_language','title','backdrop_path','popularity','vote_count','vote_average']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for pages in range(1,610):
        urlvar = "https://api.themoviedb.org/3/discover/movie?api_key=a444fb5e98813e49013125a0b6e14dcf&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(pages)+"&with_genres=16"
        response = urllib2.urlopen(urlvar)
        data = json.load(response)
        for i in range(0,20):
            print(str(pages)+"->"+str(i))
            #writer.writerow({'original_title' :data["results"][i]["original_title"].encode('utf-8')})
            writer.writerow({'poster_path' :data["results"][i]["poster_path"] ,'adult' :data["results"][i]["adult"],'overview' :data["results"][i]["overview"].encode('utf-8'),'release_date' :data["results"][i]["release_date"],'genre_ids' :data["results"][i]["genre_ids"],'id' :data["results"][i]["id"],'original_title' :data["results"][i]["original_title"].encode('utf-8'),'original_language' :data["results"][i]["original_language"],'title' :data["results"][i]["title"].encode('utf-8'),'backdrop_path' :data["results"][i]["backdrop_path"],'popularity' :data["results"][i]["popularity"],'vote_count' :data["results"][i]["vote_count"],'vote_average' :data["results"][i]["vote_average"]})
