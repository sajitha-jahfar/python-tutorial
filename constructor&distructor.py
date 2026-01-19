class person:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} has been created")
    def __del__(self):
        print(f"{self.name} has been destroyed")
p=person("john")
del p
