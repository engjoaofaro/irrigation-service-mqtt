class Message:

    def __init__(self, device_id, thing, datetime, humidity_soil):
        self.__device_id = device_id
        self.__thing = thing
        self.__datetime = datetime
        self.__humidity_soil = humidity_soil
        print("Registering data: {}".format(self.__dict__))
