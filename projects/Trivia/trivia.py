import requests
import random
from enums import Diffculty
import pandas as pd
#from html.parser import HTMLParser
from html import unescape

class Trivia():

    def __init__(self):

        self.__df_categories = pd.DataFrame()
        self.__df_questions = pd.DataFrame()

        self.req_categories()
        self.req_questions()

        self.play()

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
            print(difficulty.__repr__())
        difficulty = input("Which difficulty level to choose \n")

        try:
            difficulty = Diffculty(difficulty)
        except:
            print("illegal difficulty. set difficulty to 'easy")
            difficulty = Diffculty.Easy

        url = f"https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty.value}"
        r = requests.get(url=url)
        data = r.json()
        self.df_questions = pd.DataFrame(data['results'])


    def play(self):
        # pd.options.display.max_columns = None
        #print(self.df_questions.loc[:,['correct_answer','incorrect_answers','question']])
        #parser = HTMLParser()

        for index, row in self.df_questions.iterrows():
            #print(parser.unescape(row.loc['question']))
            print(unescape(row.loc['question']))
            print(row.loc['incorrect_answers'])
            print(row.loc['correct_answer'])


            print("**********************************************")
            answers = unescape(row.loc['incorrect_answers'])
            answers.append(unescape(row.loc['correct_answer']))
            random.shuffle(answers)
            for ind,ans in enumerate(answers):
                print(ind+1,ans)
            #ans = input(parser.unescape(row.loc['correct_answer']))








