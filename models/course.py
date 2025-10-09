from .teacher import Teacher

class Course(Teacher):
    def __init__(self,name, teacher_id, course_code:str, course_title:str):
        super().__init__(name, teacher_id)
        self._course_code = course_code
        self._course_title = course_title

    @property
    def course_code(self):
        return self._course_code
    @course_code.setter
    def course_code( self, val ):
        self._course_code = val

    @property
    def course_title( self ):
        return self._course_title
    @course_title.setter
    def course_title( self, val ):
        self._course_title = val

    def __str__(self):
        return f"Course Code: {self._course_code}, Course Title: {self._course_title}, {super().__str__()}"