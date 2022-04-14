from person import Person
class Student(Person):
    def sayhello(self):
        return(f"Hola mi nombre es {self.name} {self.lastname}")