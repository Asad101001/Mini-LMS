from .person import Person
from .course_list import CourseList

class Student(Person):
    def __init__(self, name: str, seat_no: str, semester: int, courses: CourseList):
        super().__init__(name)
        self._seat_no = seat_no
        self._semester = semester
        self._courses = courses

    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, val):
        self._seat_no = val

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, val):
        self._semester = val

    def __str__(self):
        return (
            f"Student's {super().__str__()} , "
            f"Seat #: {self._seat_no} , "
            f"Semester: {self._semester}"
        )
