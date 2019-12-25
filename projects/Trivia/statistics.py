import pandas as pd
import matplotlib.pyplot as plt

class Statistics:

    def __init__(self,categories):
        self.__user = None
        self.__df_games = pd.DataFrame(columns=['login_name','category','difficulty','correct','wrong'])

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    def save(self,category,difficulty,correct,wrong):
        self.__df_games = self.__df_games.append({'login_name':self.__user.login_name,'category':category,
                                                  'difficulty':difficulty,'correct':correct,'wrong':wrong},ignore_index=True)

    def show(self):
        if self.__df_games.empty:
            return

        df_cat = self.__df_games.groupby('category')[['correct','wrong']].sum()
        df_diff = self.__df_games.groupby('difficulty')[['correct','wrong']].sum()
        df_score = self.__df_games.groupby('login_name')[['correct']].sum()
        df_score.sort_values(by=['correct'],inplace=True,ascending = False)
        df_score = df_score.head(3)

        fig = plt.figure(figsize=(6, 6))
        grid = plt.GridSpec(3, 4, hspace=0.9, wspace=0.5)

        cat_ax = fig.add_subplot(grid[0:2,2:])
        diff_ax = fig.add_subplot(grid[0:2,0:2],sharey=cat_ax)
        score_ax = fig.add_subplot(grid[2,:])

        df_cat.plot.bar(ax=cat_ax,title="category")
        cat_ax.xaxis.label.set_visible(False)

        df_diff.plot.bar(ax=diff_ax,title="difficulty")
        diff_ax.xaxis.label.set_visible(False)
        diff_ax.set_xticklabels(diff_ax.get_xticklabels(), rotation=45)

        score_ax.table(cellText=df_score.values, colLabels=['score'], rowLabels=df_score.index,
                       cellLoc='center',colLoc='center',
                       loc='center', colColours=['C1'],
                       rowColours=['C1' for x in df_score.index],colWidths=[0.3])
        score_ax.set_title("3 users with the highest score",fontsize=12,fontweight='bold')
        score_ax.axis('off')
        score_ax.get_xaxis().set_visible(False)
        score_ax.get_yaxis().set_visible(False)

        plt.show()


