#roiyeho@gmail.com

import requests
import random
from enums import Diffculty
import pandas as pd
from html import unescape
from statistics import Statistics

class Trivia():

    def __init__(self):

        self.__user_id = 0
        self.__category = 0
        self.__difficulty = 0

        self.__df_categories = pd.DataFrame()
        self.__df_questions = pd.DataFrame()

        self.req_categories()

        self.__cls_statistics = Statistics(self.__df_categories)


    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id
        self.__cls_statistics.user_id = user_id


    def req_categories(self):
        url = "https://opentdb.com/api_category.php"
        r = requests.get(url=url)
        data = r.json()
        self.__df_categories = pd.DataFrame(data['trivia_categories'])
        self.__df_categories.set_index('id',inplace=True)

    def req_questions(self):

        num_questions = int(input("number of questions\n"))

        print(self.__df_categories)
        self.__category = int(input("Which category to choose \n"))

        for difficulty in Diffculty:
            print( difficulty.value + 1, '.', difficulty.name)
        selected_idx = int(input("Which difficulty level to choose \n"))
        self.__difficulty = Diffculty(selected_idx-1).name.lower()

        print("************** REQUESTED URL ********************************")
        url = f"https://opentdb.com/api.php?amount={num_questions}&category={self.__category}&difficulty={self.__difficulty}"
        print(url)
        r = requests.get(url=url)
        data = r.json()
        self.__df_questions = pd.DataFrame(data['results'])

    def play(self):
        self.req_questions()

        start = "\033[1m"
        end = "\033[0;0m"

        for index, row in self.__df_questions.iterrows():
            print(start + unescape(row.loc['question']) + end)

            answers = row.loc['incorrect_answers']
            answers.append(row.loc['correct_answer'])
            random.shuffle(answers)
            for ind,ans in enumerate(answers):
                print(ind+1,ans)
            selected_ans = int(input(">>> "))

            chosen_ans = ''
            if (selected_ans > 0) & (selected_ans <= len(answers)):
                chosen_ans = answers[selected_ans - 1]
            correct_ans = unescape(row.loc['correct_answer'])

            if correct_ans == chosen_ans:
                print("correct")
                self.__cls_statistics.stat(self.__category, self.__difficulty, True)
            else:
                print("wrong. choose:", chosen_ans, "correct:", correct_ans)
                self.__cls_statistics.stat(self.__category, self.__difficulty, False)



    def show_statistics(self):
        self.__cls_statistics.show_statistics()



