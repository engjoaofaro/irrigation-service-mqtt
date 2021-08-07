class Message:

    def __init__(self, thing, humidity_soil, irrigation_count):
        self.__thing = thing
        self.__humidity_soil = humidity_soil
        self.__irrigation_count = irrigation_count
        print("Registering data: {}".format(self.__dict__))
