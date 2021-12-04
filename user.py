class User():
    def __init__(self, username="", password="", firstName="", lastName="", emailAddress="", permission=""):
        self.__username = username
        self.__password = password
        self.__firstName = firstName
        self.__lastName = lastName
        self.__emailAddress = emailAddress
        self.__permission = permission

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @property
    def emailAddress(self):
        return self.__emailAddress

    @emailAddress.setter
    def emailAddress(self, emailAddress):
        self.__emailAddress = emailAddress

    @property
    def permission(self):
        return self.__permission

    @permission.setter
    def permission(self, permission):
        self.__permission = permission