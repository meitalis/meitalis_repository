import requests
import pandas as pd


class JsonHandler:

    category_url = "https://opentdb.com/api_category.php"
    questions_url = "https://opentdb.com/api.php?"

    def __init__(self):
       pass

    @staticmethod
    def req_categories():
        r = requests.get(url=JsonHandler.category_url)
        data = r.json()
        df_categories = pd.DataFrame(data['trivia_categories'])
        df_categories.set_index('id',inplace=True)

        return df_categories

    @staticmethod
    def req_questions(num_questions,category,difficulty):
        url = JsonHandler.questions_url + f"amount={num_questions}&category={category}&difficulty={difficulty}"

        r = requests.get(url=url)
        data = r.json()
        df_questions = pd.DataFrame(data['results'])

        return df_questions

