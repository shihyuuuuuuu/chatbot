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

    def bye_to_user(self, update):
        text = update.message.text
        if text.lower() == 'bye':
            update.message.reply_text("ㄅㄅ")
            return 1

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '嗨' or text.lower() == '返回'

    def is_going_to_state2(self, update):
        text = update.message.text
        if text.lower() == '查賽程':
            return 1

    def is_going_to_state3(self, update):
        text = update.message.text
        if text.lower() == '裕隆':
            return 1

    def is_going_to_state4(self, update):
        text = update.message.text
        if text.lower() == '台啤':
            return 1
    def is_going_to_state5(self, update):
        text = update.message.text
        if text.lower() == '璞園':
            return 1

    def is_going_to_state6(self, update):
        text = update.message.text
        if text.lower() == '達欣':
            return 1
    def is_going_to_state7(self, update):
        text = update.message.text
        if text.lower() == '富邦':
            return 1

    def is_going_to_state8(self, update):
        text = update.message.text
        if text.lower() == '台銀':
            return 1
    def is_going_to_state9(self, update):
        text = update.message.text
        if text.lower() == '金酒':
            return 1

    def is_going_to_state10(self, update):
        text = update.message.text
        if text.lower() == '查戰績':
            return 1
    
    def on_enter_state1(self, update):
        update.message.reply_text("你好!我可以為你做什麼呢？")

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("你想要看那一隊的比賽？")
    
    def on_exit_state2(self, update):
        print('Leaving state2')
    
    def on_enter_state3(self, update):
        update.message.reply_text("這是裕隆隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"裕隆"}, {"Team2":"裕隆"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
			#print(document[date+8:date+13], document[time+6, time+11])
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
    
    def on_enter_state4(self, update):
        update.message.reply_text("這是台啤隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"台啤"}, {"Team2":"台啤"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
    
    def on_enter_state5(self, update):
        update.message.reply_text("這是璞園隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"璞園"}, {"Team2":"璞園"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
            #print(document[date+8:date+13], document[time+6, time+11])
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')
    
    def on_enter_state6(self, update):
        update.message.reply_text("這是達欣隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"達欣"}, {"Team2":"達欣"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
    
    def on_enter_state7(self, update):
        update.message.reply_text("這是富邦隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"富邦"}, {"Team2":"富邦"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
            #print(document[date+8:date+13], document[time+6, time+11])
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')
    
    def on_enter_state8(self, update):
        update.message.reply_text("這是台銀隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"台銀"}, {"Team2":"台銀"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')

    def on_enter_state9(self, update):
        update.message.reply_text("這是金酒隊接下來的比賽：")
        for document in schedule.find({"$or": [{"Team1":"金酒"}, {"Team2":"金酒"}]}):
            document = str(document)
            date = document.find("Date")
            time = document.find("Time")
            team1 = document.find("Team1")
            team2 = document.find("Team2")
            place = document.find("Place")
            #print(document[date+8:date+13], document[time+6, time+11])
            update.message.reply_text(document[date+8:date+14] + " " + document[time+8:time+13] + " " + document[team1+9:team1+11] + ":" + document[team2+9:team2+11] + " " + document[place+9:place+11])
        self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')

    def on_enter_state10(self, update):
        update.message.reply_text("1 台灣銀行\n2 桃園璞園建築\n3 富邦勇士\n4 台北達欣工程\n5 金門酒廠\n6 裕隆納智捷\n7 台灣啤酒")
        self.go_back(update)
    
    def on_exit_state10(self, update):
        print('Leaving state10')
