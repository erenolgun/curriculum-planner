class Busy:
    def __init__(self, instructor, busy_day, busy_time):
        self.instructor = instructor
        self.busy_day = busy_day
        self.busy_time = busy_time

    def get_instructor(self):
        return self.instructor

    def get_busy_day(self):
        return self.busy_day

    def get_busy_time(self):
        return self.busy_time
