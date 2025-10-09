from models import *

class App:
    def __init__ ( self ):
        self.studentlist = StudentList ()
        self._courselist = CourseList ()

    def run (self):
        MisssHumera = Teacher ("Miss MsHumera", "007")
        SirBari = Teacher ("Sir Bari", "001")
        MissMariam = Teacher ("Miss Mariam", "054")
        SirHuzaifa = Teacher ("Sir Huzaifa", "111")

        oop = Course ("CS-352","Object Oriented Programming", MisssHumera)
        dld = Course ("CS-354", "Digital Logic Design", SirBari)
        ds = Course ("CS-358", "Discrete Structure", MissMariam)
        la = Course ("CS-356", "linear Algebra", SirHuzaifa)

        self._courselist.add_course (oop)
        self._courselist.add_course (dld)
        self._courselist.add_course (la)
        self._courselist.add_course (ds)

        self._courselist.remove_course (ds)

        self._courselist.search_by_title ("linear Algebra")

        a = Student ("Asad", "87", 1, self._courselist)
        h = Student ("Hasnain", "50", 1, self._courselist)
        d = Student ("Daniyal", "39", 1, self._courselist)

        self.studentlist.add_student (a)
        self.studentlist.add_student (h)
        self.studentlist.add_student (d)

        self.studentlist.removeStudent (d)

        self.studentlist.search_by_name ("Asad")
        self.studentlist.search_by_seat ("50")
        self.studentlist.search_by_semester (1)

    @property
    def show_all_students ( self ):
        return self.studentlist.get_students

    @property
    def show_all_courses ( self ):
        return f"{self._courselist.get_course}"
