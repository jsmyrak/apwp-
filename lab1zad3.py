class AccessLogger:
    def __set_name__(self, owner, name):
        self.public_name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        value = instance.__dict__.get(self.public_name)
        print(f"[LOG ODCZYTU] Odczytano atrybut '{self.public_name}'. Wartość: {value}")
        return value

    def __set__(self, instance, value):
        print(f"[LOG ZAPISU] Zmiana atrybutu '{self.public_name}'. Nowa wartość: {value}")
        instance.__dict__[self.public_name] = value


class Uzytkownik:
    imie = AccessLogger()
    wiek = AccessLogger()

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

if __name__ == "__main__":
    print("--- Tworzenie użytkownika ---")
    user1 = Uzytkownik("Jan", 30)
    
    print("\n--- Odczyt atrybutów ---")
    obecne_imie = user1.imie
    obecny_wiek = user1.wiek
    
    print("\n--- Zmiana atrybutów ---")
    user1.imie = "Adam"
    user1.wiek = 31