from person import Person

class Teacher(Person):
    def __init__(self, specialization, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__specialization = specialization
        
    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        self.specialization = specialization
        
    def can_use_services(self):
        return True