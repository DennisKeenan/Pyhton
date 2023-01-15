class Person:
    def __init__(self,name:str,age:int,gender:bool) -> None:
        self.name=name
        self.age=age
        self.gender=gender

    def talk(self,words:str):
        print(self.name,":",words)

    def interaction(self,person,type:str):
        print(self.name,type,"with",person.name)