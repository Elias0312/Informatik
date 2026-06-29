from enum import Enum

class DeviceType(Enum):
    CAMERA = "camera"
    MICROPHONE = "microphone"
    LIGHT = "light"

class Device:
    _count = 0

    def __init__(self, name: str, serialnumber: str, type: DeviceType):
        self.name = name
        self.serialnumber = serialnumber
        self.type = type
        Device._count += 1

class Camera(Device):
    def __init__(self, name, serialnumber, type, resolution):
        super().__init__(name, serialnumber, type)
        self.resolution = resolution

    def info(self):
        print(f"{self.type}('{self.name}'({self.resolution}), serialnumber: {self.serialnumber})")

class Microphone(Device):
    def __init__(self, name, serialnumber, type, sensitivity):
        super().__init__(name, serialnumber, type)
        self.sensitivity = sensitivity

    def info(self):
        print(f"{self.type}('{self.name}', sensitivity: {self.sensitivity}, serialnumber: {self.serialnumber})")

class Light(Device):
    def __init__(self, name, serialnumber, type, power):
        super().__init__(name, serialnumber, type)
        self.power = power

    def info(self):
        print(f"{self.type}('{self.name}', power: {self.power}, serialnumber: {self.serialnumber})")