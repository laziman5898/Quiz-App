import requests
import random
class QuizApi():
    def __init__(self):
        self.response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
        self.response.raise_for_status()
        self.data = self.response.json()["results"]
        self.datalength = len(self.data)-1

    def randomQuestion(self):
        return self.data[random.randint(0,self.datalength)]
