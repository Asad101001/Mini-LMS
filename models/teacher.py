from person import Person

class Teacher(Person):

    def __init__(self, name, teacher_id:str):
        super().__init__(name)
        self._teacher_id = teacher_id

    def __str__(self):
        return f"Teacher's {super().__str__()} , Teacher's I.D: {self._teacher_id}" 
