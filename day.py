from copy import deepcopy


class Day:
    def __init__(self, name, class_list):
        self.name = name
        self.morning = []
        self.afternoon = []
        self.big_class_list = []
        self.small_class_list = []

        for classroom in class_list:
            if(classroom.size == "big"):
                size = list(range(int(classroom.number)))
                for s in size:
                    x = "bigClass" + str(s + 1)
                    self.big_class_list.append(x)
            if(classroom.size == "small"):
                size = list(range(int(classroom.number)))
                for s in size:
                    x = "smallClass" + str(s + 1)
                    self.small_class_list.append(x)

        self.morning_big_class = list(self.big_class_list)
        self.morning_small_class = list(self.small_class_list)

        self.afternoon_big_class = list(self.big_class_list)
        self.afternoon_small_class = list(self.small_class_list)

    def get_name(self):
        return self.name

    def get_morning(self):
        return self.morning

    def get_afternoon(self):
        return self.afternoon

    def get_big_class_list(self):
        return self.big_class_list

    def get_small_class_list(self):
        return self.small_class_list

    def get_morning_big_class(self):
        return self.morning_big_class

    def get_morning_small_class(self):
        return self.morning_small_class

    def get_afternoon_big_class(self):
        return self.afternoon_big_class

    def get_afternoon_small_class(self):
        return self.afternoon_small_class
