from .teacher import Teacher

class Course:
    def __init__(self,course_code:str, course_title:str, teacher:Teacher):
        self._course_code = course_code
        self._course_title = course_title
        self._teacher = teacher

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
        return f"Course Code: {self._course_code}, Course Title: {self._course_title}, {self._teacher}"