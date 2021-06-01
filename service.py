class Service:
    def __init__(self, course_code, course_day, course_time):
        self.course_code = course_code
        self.course_day = course_day
        self.course_time = course_time

    def get_course_code(self):
        return self.course_code

    def get_course_day(self):
        return self.course_day

    def get_course_time(self):
        return self.course_time
