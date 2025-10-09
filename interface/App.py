from models import *

class App:
    def __init__ ( self ):
        self.studentlist = StudentList ()
        self._courselist = CourseList ()


      # a = Student("Asad", "87", 2)
      # print(a)
      # print(a.seat_no)
      # a.seat_no= "5"
      # print(a.seat_no)
      # a.semester = 69
      # print(a.semester)
      #
      #
      # c= Course("Dr. Humera Tariq", "007", "CS-352", "OOPs")
      # print(c)


    def run (self):
        Humera = Teacher ("Mis Humera","007")
        Bari = Teacher ("Sir Bari", "001")
        Mariam = Teacher ("Mis Mariam", "054")
        Huzaifa = Teacher ("Sir Huzaifa", "111")

        oop = Course ("Humera", "007","CS-352","Object Oriented Programming", )
        dld = Course (" Bari","001","CS-354", "Digital Logic Design")
        ds = Course ("Mariam","054","CS-358", "Discrete Structure")
        la = Course ("Huzaifa","111","CS-356", "linear Algebra")

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
        return f"{self.studentlist.get_students}"

    @property
    def show_all_courses ( self ):
        return f"{self._courselist.get_course}"
