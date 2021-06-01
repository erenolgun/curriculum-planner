class Scheduler:
    def __init__(self, day_name, day_time, class_type, course_code):
        self.day_name = day_name
        self.day_time = day_time
        self.class_type = class_type
        self.course_code = course_code

    def get_day_name(self):
        return self.day_name

    def get_day_time(self):
        return self.day_time

    def get_class_type(self):
        return self.class_type

    def get_course_code(self):
        return self.course_code
