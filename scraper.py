import requests
import csv
import tweepy

from datetime import date
from datetime import timedelta


URL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"


consumer_key = "TBJX0j4eA4v5esovpLy6k8HkS"
consumer_secret = "OUNIJdjZOO6h0SAPmGMTOI00AfnJ41rBHyUiVZmALLuiwNiMMp"
access_token = "1262245023388753920-JOLV0oyfoe4HkotzHk0pd4OFun07R4"
access_token_secret = "u1UxmVj9eo8ukWk13bKvaoGgwWbXldtBHBwh8sBh0VIs0"



def getCSV():
    r = requests.get(URL)
    content = r.content


    file = open("case.csv","w") 
    file.write(content)


def readCSV():
    with open("case.csv", mode = "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        yesterday = date.today() - timedelta(days = 1)
        # print(yesterday)

        cases = 0
        deaths = 0

        for row in csv_reader:
            # print(row['date'])
            if str(row["date"]) == str(yesterday):
                case = int(row["cases"])
                death = int(row["deaths"])

                cases += case
                deaths += death
        
        tweetContent(cases, deaths)



def tweetContent(cases, deaths):
     tweetOut("Until yesterday, there are {0} cases and {1} deaths total in the U.S".format(cases, deaths))


def tweetOut(tweetContent):
    oauth = OAuth()
    api = tweepy.API(oauth)
    api.update_status(tweetContent)



def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None



def main():
    getCSV()
    readCSV()



if __name__ =='__main__':
    main()


