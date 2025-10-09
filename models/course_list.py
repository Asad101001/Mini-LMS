from .course import Course


class CourseList:
    def __init__ ( self ):
        self._courses = [ ]
        self._list_of_courses = [ ]

    def add_course ( self, course: Course ):

        if isinstance (course, Course):
            self._courses.append (course)
            self._list_of_courses = [ str (course) for course in self._courses ]

        else:
            return TypeError ("\nCan only add courses!")

    def remove_course ( self, course: Course ):

        if isinstance (course, Course):

            self._courses.remove (course)
            self._list_of_courses = [ str (course) for course in self._courses ]

        else:
            return TypeError ("\nCan Only Remove courses!")

    @property
    def get_course ( self ):
        return f"------Course List------\n\n{self._list_of_courses}\n"

    def search_by_title ( self, key ):

        found_course = [ course for course in self._courses if course.course_title == key ]

        if found_course:
            print (f"\nFound results based on title {key}: {len (found_course)}\n\n")
            for i in found_course:
                print (i)

        else:
            print (f"\nNo courses found with the same name:'{key}'\n")

    def __str__ ( self ):

        return f"{self._list_of_courses}"





