import pandas as pd
from enums import Diffculty
import numpy as np
import matplotlib.pyplot as plt

class Statistics():

    def __init__(self,categories):

        self.user_id = 0

        self.__df_category = pd.DataFrame(np.zeros([2,len(categories.index)]) ,columns = categories.index ,index=['wrong','correct'])
        self.__df_difficulty = pd.DataFrame(np.zeros([2,len(Diffculty)]),columns = [e.name.lower() for e in Diffculty] ,index=['wrong','correct'])
        self.__df_score = pd.DataFrame(columns=['score'] ,dtype=np.int)

        #self.__df_games = pd.DataFrame(columns=['user_id','category','difficulty','correct','wrong'])

        pd.options.display.max_columns = None

        print(self.__df_score)


    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id



    def stat(self,category,difficulty,ans: bool):

        if ans:
            self.__df_category.loc['correct',category] += 1
            self.__df_difficulty.loc['correct', difficulty] += 1
            if self.__user_id not in self.__df_score.index:
                self.__df_score.loc[self.__user_id] = 0
            self.__df_score.loc[self.__user_id] += 1
        else:
            self.__df_category.loc['wrong', category] += 1
            self.__df_difficulty.loc['wrong', difficulty] += 1

        # print(self.__df_category)
        # print(self.__df_difficulty)
        # print(self.__df_score)

    def show_statistics(self):
        self.__df_category = self.__df_category.T
        self.__df_difficulty = self.__df_difficulty.T

        df_cat = self.__df_category[(self.__df_category.wrong > 0) | self.__df_category.correct > 0]
        df_diff = self.__df_difficulty[(self.__df_difficulty.wrong > 0) | self.__df_difficulty.correct > 0]

        fig , ax = plt.subplots(1,2)

        df_cat.plot.bar(ax= ax[0],title="category")
        df_diff.plot.bar(ax=ax[1],title="difficulty")

        plt.show()


