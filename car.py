#Car Class with Encapsulation
class Car:
    #CONSTRUCTOR
    def __init__(self, year_model, make):

        # Private Attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # METHODS
    def accelerate(self):
        self.__speed += 5

    def brake(self):

        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

    def get_make(self):
        return self.__make

    def get_year_model(self):
        return self.__year_model