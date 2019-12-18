import requests
import random
from enums import Diffculty
import pandas as pd
from html import unescape

class Trivia():

    def __init__(self):

        self.__df_categories = pd.DataFrame()
        self.__df_questions = pd.DataFrame()

        self.req_categories()

    @property
    def n_questions (self):
        return self.__n_questions

    @n_questions .setter
    def n_questions (self, n_questions ):
        self.__n_questions  = n_questions

    @property
    def df_questions(self):
        return self.__df_questions

    @df_questions.setter
    def df_questions(self, df_questions):
        self.__df_questions = df_questions

    @property
    def df_categories(self):
        return self.__df_categories

    @df_categories.setter
    def df_categories(self, df_categories):
        self.__df_categories = df_categories

    def req_categories(self):
        url = "https://opentdb.com/api_category.php"
        r = requests.get(url=url)
        data = r.json()
        self.df_categories = pd.DataFrame(data['trivia_categories'])
        self.df_categories.set_index('id',inplace=True)

    def req_questions(self):

        num_questions = int(input("number of questions\n"))

        print(self.df_categories)
        category = input("Which category to choose \n")

        for difficulty in Diffculty:
            print( difficulty.value + 1, '.', difficulty.name)
        selected_idx = int(input("Which difficulty level to choose \n"))
        difficulty = Diffculty(selected_idx-1).name.lower()

        print("************** REQUESTED URL ********************************")
        url = f"https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}"
        print(url)
        r = requests.get(url=url)
        data = r.json()
        self.df_questions = pd.DataFrame(data['results'])

    def play(self):
        self.req_questions()

        start = "\033[1m"
        end = "\033[0;0m"

        for index, row in self.df_questions.iterrows():
            print(start + unescape(row.loc['question']) + end)

            answers = unescape(row.loc['incorrect_answers'])
            answers.append(unescape(row.loc['correct_answer']))
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
            else:
                print("wrong. choose:", chosen_ans, "correct:", correct_ans)

    def statistics(self):
                cat1        cat2     cat3    total score
        id 1    [T:2,F:3]   [1,4]               2 + 1
        id 2
        id 3

        category_statistics = {'userid1' :
                               'userid1':

                            }

        difficulty_statistics

#from html.parser import HTMLParser
# pd.options.display.max_columns = None
#print(self.df_questions.loc[:,['correct_answer','incorrect_answers','question']])
#parser = HTMLParser()
