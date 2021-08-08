class Message:

    def __init__(self, device_id, thing, datetime, humidity_soil):
        self.device_id = device_id
        self.thing = thing
        self.datetime = datetime
        self.humidity_soil = humidity_soil
        print("Registering data: {}".format(self.__dict__))
