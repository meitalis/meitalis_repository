class Category():

  def __init__(self, id, name):
    self.__name = name
    self.__id = id

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, id):
    self.__id = id

  @classmethod
  def from_json(cls, json_dict):

     return cls(json_dict['id'],json_dict['name'])

#*******************************************************
 #self.__df_games.append({'Name': self.user_id, 'category': category,'difficulty': difficulty,'correct': category,'wrong': category}, ignore_index=True)

# if category not in self.__df_category.columns:
#     self.__df_category[category] = [[0, 0]]
        # if self.user_id not in self.__df_category.index:
        #     self.__df_category.at[self.user_id, 'total'] = [0, 0]
        #     self.__df_category.at[self.user_id, category] = [0, 0]
        #
        # self.__df_category.at[self.user_id, 'total'][int(ans)] += 1
        # self.__df_category.at[self.user_id, category][int(ans)] += 1

        # if self.user_id in self.__df_category.index:
        #     self.__df_category.at[self.user_id, 'total'][int(ans)] += 1
        #     if category not in self.__df_category.columns:
        #         self.__df_category[category] = [[0, 0]]
        #     self.__df_category.at[self.user_id, category][int(ans)] += 1
        # else:
        #     # ans = false(0) = wrong ans = true(1) = correc
        #     self.__df_category.at[self.user_id,'total'] = [0,0]
        #     self.__df_category.at[self.user_id, 'total'][int(ans)] += 1
        #     if category not in self.__df_category.columns:
        #         self.__df_category[category] = [[0, 0]]
        #     self.__df_category.at[self.user_id, category][int(ans)] += 1



        # if self.user_id in self.__df_difficulty.index:
        #     srs_d = self.__df_difficulty.loc[self.user_id]
        # else:
        #     srs_d = pd.Series()
        #     self.__df_difficulty.loc[self.user_id] = srs_d
        #
        # print(srs_d)
        # srs_d.loc[difficulty][int(ans)] += 1
        # srs_d.loc['total'][int(ans)] += 1
        #
        # print(self.__df_difficulty)


    # difficulty_dict = {'1': [2, 4],
    #                    '2': [3, 4],
    #                    '3': [4, 5],
    #                    '4': [6, 14],
    #                    '5': [22, 24]}
    #
    # difficulty_srs = pd.Series(difficulty_dict)
    # difficulty_srs
    #
    # category_dict = {'1': [2, 4],
    #                  '2': [3, 4],
    #                  '3': [4, 5],
    #                  '4': [6, 14],
    #                  '5': [22, 24]}
    #
    # category_srs = pd.Series(category_dict)
    # category_srs
    #
    # df = pd.DataFrame({'category': category_srs,
    #                    'difficulty': difficulty_srs
    #
    #                    })
    #
    # df
    #
    # df['total'] = 5


    #         cat1        cat2     cat3    total score
    # id 1    [T:2,F:3]   [1,4]               2 + 1
    # id 2
    # id 3


# from html.parser import HTMLParser
# pd.options.display.max_columns = None
# print(self.df_questions.loc[:,['correct_answer','incorrect_answers','question']])
# parser = HTMLParser()