
import pyttsx3
import requests
import json
class News:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.getNews()
    def speak(self, str):
        self.engine.say(str)
        self.engine.runAndWait()
    def getNews(self):
        apiKey = 'f9da9cefd5c54983a49ed363e07d279d'
        str = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}')
        str = str.text
        dictstr = json.loads(str)
        results = len(dictstr['articles'])
        i = 0
        self.engine.say("starting the news...")
        while i<results-1:
            art = dictstr['articles']
            print(art[i]['title'])
            self.speak(art[i]['title'])
            print("click to know more: ", art[i]['url'])
            print()
            self.speak("Moving on to the next News...")
            i+=1
        art = dictstr['articles']
        print(art[i]['title'])
        self.speak(art[i]['title'])
        print("click to know more: ", art[i]['url'])
        print()
        self.speak("Moving on to the next News...")
        
News()
