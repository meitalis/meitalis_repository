class User:

    def __init__(self, login_name):
        self.__login_name = login_name

    @property
    def login_name(self):
        return self.__login_name

    @login_name.setter
    def login_name(self,login_name):
        self.__login_name = login_name

