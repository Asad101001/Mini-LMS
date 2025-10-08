from person import Person

class Student(Person):

    def __init__(self, name, seat_no:str, semester:int):
        super().__init__(name)
        self._seat_no = seat_no
        self._semester = semester

    def __str__(self):
        return f"Student's {super().__str__()} , Seat #: {self._seat_no} , Semester: {self._semester}"    
    
a=Student("asad", "087", 2)
print(a)    

    