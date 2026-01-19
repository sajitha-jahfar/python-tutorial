class Engine:
    def start_engine(self):
        print("engine started")
class Wheel:
    def rotate_wheel(self):
        print("wheel rotating")
class car(Engine,Wheel):
    def driving(self):
        print("car moving")
c=car()
c.start_engine()
c.rotate_wheel()
c.driving()