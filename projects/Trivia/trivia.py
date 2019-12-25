import pandas as pd
import random
import re
from html import unescape

from user import User
from enums import Difficulty
from statistics import Statistics
from json_handler import JsonHandler
from db_handler import DBHandler

class Trivia:

    def __init__(self):

        self.__category = ""
        self.__difficulty = ""
        self.__current_user = ""
        self.__dict_users = {}
        self.__df_questions = pd.DataFrame()

        self.__df_categories = JsonHandler.req_categories()

        db_handler = DBHandler('odbc')
        db_handler.fillCategory(self.__df_categories)

        self.__cls_statistics = Statistics(self.__df_categories)


    def play(self):

        self.get_params()

        if (self.__df_questions.empty):
            print("There are no questions that meet the criteria")
            return


        start = "\033[1m"
        end = "\033[0;0m"
        pattern = "^[1-9]\d*$"

        correct = 0
        wrong = 0

        for index, row in self.__df_questions.iterrows():
            selected_ans = ""
            print(start + unescape(row.loc['question']) + end)

            answers = unescape(row.loc['incorrect_answers'])
            answers.append(unescape(row.loc['correct_answer']))
            random.shuffle(answers)
            for ind,ans in enumerate(answers):
                print(ind+1,ans)

            while (len(re.findall(pattern, selected_ans)) == 0) or \
                    ( not (len(re.findall(pattern, selected_ans)) == 0) and not ((int(selected_ans) > 0) and (int(selected_ans) <= len(answers)))):
                selected_ans = input(">>> ")

            selected_ans = int(selected_ans)

            chosen_ans = answers[selected_ans - 1]
            correct_ans = unescape(row.loc['correct_answer'])

            if correct_ans == chosen_ans:
                print("correct")
                correct += 1
            else:
                print("wrong. choose:", chosen_ans, "correct:", correct_ans)
                wrong += 1

        self.__cls_statistics.save(self.__category,self.__difficulty,correct,wrong)

    def show_statistics(self):
        self.__cls_statistics.show()

    def get_params(self):

        self.__category = ""
        self.__difficulty = ""
        num_questions = ""

        pattern = "^[1-9]\d*$"
        while len(re.findall(pattern, num_questions)) == 0:
            num_questions = input("number of questions\n")
        num_questions = int(num_questions)

        print(self.__df_categories)
        while (len(re.findall(pattern, self.__category)) == 0) or\
                (not (len(re.findall(pattern, self.__category)) == 0) and (int(self.__category) not in self.__df_categories.index)):
            self.__category = input("choose category from the list \n")
        self.__category = int(self.__category)

        for difficulty in Difficulty:
            print( difficulty.value + 1, '.', difficulty.name)

        while (len(re.findall(pattern, self.__difficulty)) == 0) or \
                (not (len(re.findall(pattern, self.__difficulty)) == 0) and (
                        (int(self.__difficulty)-1) not in list(map(int, Difficulty)))):
            self.__difficulty = input("Which difficulty level to choose \n")

        self.__difficulty = Difficulty(int(self.__difficulty)-1).name.lower()

        self.__df_questions = JsonHandler.req_questions(num_questions,self.__category,self.__difficulty)

    def set_user(self):
        login_name = ""
        while login_name == "":
            login_name = input("enter login name \n")

        if login_name == self.__current_user:
            print(f"user {login_name} already logged in ")
        else:
            if login_name in self.__dict_users.keys():
                user = self.__dict_users[login_name]
            else:
                user = User(login_name)
                self.__dict_users[login_name] = user

            self.__current_user = login_name
            self.__cls_statistics.user = user

    def insert_question(self):
        login_name = input("enter login name \n")