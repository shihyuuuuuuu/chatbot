from transitions.extensions import GraphMachine
import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.chatbot
schedule = db.schedule

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'hi'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'schedule'

    def is_going_to_state3(self, update):
        text = update.message.text
        if text.lower() == 'yu':
            return 1

    def on_enter_state1(self, update):
        update.message.reply_text("Bello!我可以為你做什麼呢？")

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("你想要查那一隊呢～？")

    def on_exit_state2(self, update):
        print('Leaving state2')
    
    def on_enter_state3(self, update):
        for document in schedule.find({"$or": [{"Team1":"裕隆"}, {"Team2":"裕隆"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
			#print(document[date+8:date+13], document[time+6, time+11])
            update.message.reply_text("這是裕隆隊接下來的比賽：\n"+document[date+8:date+13] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
