import pandas as pd
from enums import Diffculty
import numpy as np
import matplotlib.pyplot as plt

class Statistics():

    def __init__(self,categories):
        self.user_id = 0
        self.__df_games = pd.DataFrame(columns=['user_id','category','difficulty','correct','wrong'])
        pd.options.display.max_columns = None

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    def save(self,category,difficulty,correct,wrong):
        self.__df_games = self.__df_games.append({'user_id':self.__user_id,'category':category,'difficulty':difficulty,'correct':correct,'wrong':wrong},ignore_index=True)
        #print(self.__df_games)


    def show(self):
        if self.__df_games.empty:
            return

        df_cat = self.__df_games.groupby('category')[['correct','wrong']].sum()
        print("df_cat")
        print(df_cat)

        df_diff = self.__df_games.groupby('difficulty')[['correct','wrong']].sum()
        print("df_diff")
        print(df_diff)

        df_score = self.__df_games.groupby('user_id')[['correct']].sum()
        df_score.sort_values(by=['correct'],inplace=True,ascending = False)
        df_score = df_score.head(3)
        print("df_score")
        print(df_score)

        # fig , ax = plt.subplots(1,2)
        #
        # df_cat.plot.bar(ax= ax[0],title="category")
        # df_diff.plot.bar(ax=ax[1],title="difficulty")

        fig = plt.figure(figsize=(6, 6))
        grid = plt.GridSpec(3, 4, hspace=0.9, wspace=0.5)

        cat_ax = fig.add_subplot(grid[0:2,2:])
        diff_ax = fig.add_subplot(grid[0:2,0:2],sharey=cat_ax)
        score_ax = fig.add_subplot(grid[2,:])

        df_cat.plot.bar(ax=cat_ax,title="category")
        cat_ax.xaxis.label.set_visible(False)

        df_diff.plot.bar(ax=diff_ax,title="difficulty" )
        diff_ax.xaxis.label.set_visible(False)
        diff_ax.set_xticklabels(diff_ax.get_xticklabels(), rotation=45)


        # score_ax.table(cellText=df_score.values, colColours=['grey'] * df_score.shape[1], bbox=[0, 0, 1, 1],
        #                colLabels=df_score.columns,rowLabels=df_score.index)
        #colors = plt.cm.BuPu(np.linspace(0, 0.5, len(df_score.index)))
        # score_ax.table(cellText=df_score.values, colLabels=df_score.columns, rowLabels=df_score.index,
        #                colColours=['red'] * df_score.shape[1],
        #                rowColours=['red'] * df_score.shape[1],
        #                loc="center")

        #score_ax.table(cellText=high_scores, colLabels="", loc="center")
        #score_ax.plot(high_scores)]
        #score_ax.set(title='three users with the highest score');

        # print('*********************************')
        # df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
        # score_ax.table(cellText=df.values, colLabels=df.columns, loc='center')

        # df = pd.DataFrame(np.random.randn(2, 2), columns=list('AB'))
        # score_ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index,loc='center')


        #rowColours  =['grey']  df_score.columns
        score_ax.table(cellText=df_score.values, colLabels=['score'], rowLabels=df_score.index,
                       cellLoc='center',colLoc='center',
                       loc='center', colColours=['C1'],
                       rowColours=['C1' for x in df_score.index],colWidths=[0.3])
        score_ax.set_title("3 users with the highest score",fontsize=12,fontweight='bold')

        # df2 = pd.DataFrame(np.random.randn(2, 2), columns=['user','score'])
        # print("df2")
        # print(df2.values)
        # # df = pd.DataFrame(np.array([[high_scores]]), columns=['three users with the highest score'])
        # #
        # print('*df_score.T.values ***')
        # print(df_score.T.values)
        # print(df_score.values)
        # print(df_score.index.tolist())
        # print([df_score.T.index.tolist()])
        # score_ax.table(cellText=df2.values, colLabels=df2.columns,colColours=['grey'] ,loc='top')
        #score_ax.table(cellText=[df_score.T.index.tolist()], colLabels=['user_id'], colColours=['grey'],loc='top')
        #score_ax.set_title("three users with the highest score")

        #plt.plot(high_scores,ax=score_ax,title="three users with the highest score")
        score_ax.axis('off')
        score_ax.get_xaxis().set_visible(False)
        score_ax.get_yaxis().set_visible(False)

        # df_score.plot(ax=score_ax, table=np.round(df_score.T, 2), legend=False,title="three users with the highest score")
        # score_ax.xaxis.set_visible(False)

        plt.show()


