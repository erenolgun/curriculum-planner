class Course:
    def __init__(self, course_code, course_name, course_semester, course_credit, course_type, course_departmant, course_instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.course_semester = course_semester
        self.course_credit = course_credit
        self.course_type = course_type
        self.course_departmant = course_departmant
        self.course_instructor = course_instructor

    def get_course_code(self):
        return self.course_code

    def get_course_name(self):
        return self.course_name

    def get_course_semester(self):
        return self.course_semester

    def get_course_credit(self):
        return self.course_credit

    def get_course_type(self):
        return self.course_type

    def get_course_department(self):
        return self.course_departmant

    def get_course_instructor(self):
        return self.course_instructor
