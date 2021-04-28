class Pc:
    def __init__(self):
        self.mb=None
        self.kb=None
        self.mn=None
        self.power=False
    def poweron(self):
        self.power=True
    def poweroff(self):
        self.power=False

class Motherboard:
    def __init__(self,name):
        self.name=name

class Cpu:
    def __init__(self,brand="INTEL"):
        self.brand=brand

class Keyboard:
    def __init__(self,keys):
        self.keys=keys

class Monitor:
    def __init__(self,size):
        self.size=size

asus=Pc()
asus.mb=Motherboard("華碩")
asus.kb=Keyboard(104)
asus.mn=Monitor(27)
