class Fernandes:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def introduction(self):
        print(f"Hi I'm {self.name} I'm {self.age} years old and my hoby is playing {self.hobby}.")
         
x = Fernandes("Nelfer", 18, "Football")
x.introduction()
