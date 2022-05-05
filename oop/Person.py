class Person:
    def __init__(self, person_name: str, age: int, hight: float = None):
        self.__name = person_name
        self.__age = age
        self.__hight = hight

    def summery(self):
        pass
        # return f"Your name is : {self.__name} . Your age is : {self.__age} . Hieght is {self.__hight if self.__hight is not None else '5.5 inch'} inch"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
