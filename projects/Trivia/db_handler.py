import pyodbc


class DBHandler:

    drivers = {'odbc': {'conn_str': "Driver={ODBC Driver 13 for SQL Server};" \
                                "Server=localhost;" \
                                "Database=Trivia;" \
                                "Trusted_Connection=yes;"
                    }
                }


    def __init__(self,driver):

        self.driver = DBHandler.drivers.get(driver, DBHandler.drivers.get('odbc'))

        self.conn = pyodbc.connect(self.driver.get('conn_str'))

        self.cursor = self.conn.cursor()

        self.createTriviaTables()

    def __del__(self):
        self.conn.close()

    def createTriviaTables(self):

        self.cursor.execute("{CALL [sp_CreateDifficulties]}")
        self.cursor.execute("{CALL [sp_CreateTypesQuestion]}")
        self.cursor.execute("{CALL [sp_CreateCategories]}")
        self.cursor.execute("{CALL [sp_CreateQuestions]}")
        self.cursor.execute("{CALL [sp_CreateAnswers]}")

        self.conn.commit()

    def fillCategory(self,df_categories):

        insert = "INSERT INTO [Categories] VALUES"

        for cat_id, row in df_categories.iterrows():

            cat_name = row['name']
            sql = insert + f"({cat_id}, '{cat_name}')"
            self.cursor.execute(sql)

        self.conn.commit()

