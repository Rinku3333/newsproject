import requests
import json

def speaks(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speaks("new for today...lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3c7a8707f1624b74a976f1d88710fa7d"
    news = requests.get(url).text
    news_dic = json.loads(news)
    print(news_dic["articles"])
    arts = news_dic['articles']
    for article in arts:
        speaks(article["title"])
        speaks("moving on to the next news..Listen carefully ")