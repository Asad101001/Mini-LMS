from .student import Student

class StudentList:
    def __init__(self):
        self._students = []
        self._list_of_students = []

    def add_student( self, student:Student):

         if isinstance(student, Student):
             self._students.append(student)
             self._list_of_students=[str(stud) for stud in self._students]
         else:
             raise TypeError("Only students can be added to StudentList")

    def removeStudent( self, student:Student):

         if isinstance(student, Student):
             self._students.remove(student)
             self._list_of_students=[str(stud) for stud in self._students]
         else:
             raise TypeError("Only students can be removed from StudentList")

    @property
    def get_students( self ):
        return f"------Complete list of the students------\n\n{self._list_of_students}\n"

    def search_by_name ( self, key: str ):
        found_students = [ student for student in self._students if student.name == key ]

        if found_students:
            print (f"\nFound results based on: {key}: {len (found_students)} \n\n")
            for student in found_students:
                print (student)
        else:
            print (f"\nNo student found with the name:'{key}'\n")

    def search_by_seat ( self, key ):
        found_seat = [ student for student in self._students if student.seat_no == key ]

        if found_seat:
            print (f"\nFound results based on seat number: {key}: {len (found_seat)} \n\n")
            for student in found_seat:
                print (student)
        else:
            print (f"\nNo student found with the same seat number:'{key}'\n")

    def search_by_semester ( self, key ):
        found_semester = [ student for student in self._students if student.semester == key ]

        if found_semester:
            print (f"\nFound results based on semester {key}: {len (found_semester)} \n\n")
            for student in found_semester:
                print (student)
        else:
            print (f"\nNo student found with the semester:'{key}'\n")

    def __str__ ( self ):

        return f"\n{self._list_of_students}\n"