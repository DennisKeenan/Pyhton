class Vehicle:
    def __init__(self,brand:str,year:int,color:str) -> None:
        self.brand=brand
        self.year=year
        self.color=color

    def move(self,distance:int):
        print(self.brand,"moving",distance)

class Car(Vehicle):
    def __init__(self, brand: str, year: int, color: str, enginetype: str, hp: int, type: str) -> None:
        self.enginetype=enginetype
        self.hp=hp
        self.type=type
        super().__init__(brand, year, color)
        
class Plane(Vehicle):
    def __init__(self, brand: str, year: int, color: str, engines: int, classes: str, passengers: int) -> None:
        self.engines=engines
        self.classes=classes
        self.passengers=passengers
        super().__init__(brand, year, color)

    def fly(self, no:str, departure:str, arrival:str):
        print(self.brand,self.classes,"-",self.passengers,"passengers, with flight number",no,"Depart from",departure,"to",arrival)

bmw_i4=Car("BMW",2023,"White","Electric",340,"Luxury EV")
innova_diesel=Car("Toyota",2021,"White","Combustion Diesel",147,"MPV")
airbus_a380=Plane("Airbus",2007,"White",4,"Private Jet",830)
boeing_737=Plane("Boeing",2020,"Blue",2,"Commercial",220)

bmw_i4.move(4000)
innova_diesel.move(3000)
airbus_a380.move(200000)
boeing_737.move(500000)

airbus_a380.fly("2AXDF3","Jakarta","Turkey")
boeing_737.fly("3DFASW5","Surabaya","Lombok")
