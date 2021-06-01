from courses import Course
from service import Service
from busy import Busy
from classroom import Classroom
from day import Day
from scheduler import Scheduler

import csv


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

course_list = []
service_list = []
busy_list = []
class_list = []
days_list = []
schedule_list = []
big_class_list = []
small_class_list = []
intersection_compare_list = []
display_curriculum = []
temporary_list = []


def is_busy(instructor, day, time):
    for busy in busy_list:
        if(instructor == busy.get_instructor() and day == busy.get_busy_day() and time == busy.get_busy_time()):
            return True


def get_semester(course_code):
    for course in intersection_compare_list:
        if(course.get_course_code() == course_code):
            year_of_the_semester = course.get_course_semester()
            return year_of_the_semester


def is_intersection(day, time, course_code):
    input_semester = get_semester(course_code)

    for schedule in schedule_list:
        if(day == schedule.get_day_name() and time == schedule.get_day_time() and input_semester == get_semester(schedule.get_course_code())):
            return True


with open('Courses.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        course = Course(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        course_list.append(course)


with open('service.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        service = Service(row[0], row[1], row[2])
        service_list.append(service)


with open('busy.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        busy = Busy(row[0], row[1], row[2])
        busy_list.append(busy)


with open('classroom.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        classroom = Classroom(row[0], row[1])
        class_list.append(classroom)


for day in days:
    day_ = Day(day, class_list)
    days_list.append(day_)

intersection_compare_list = list(course_list)

for service in service_list:
    for day in days_list:
        if(service.get_course_day() == day.get_name()):
            if(service.get_course_time() == "Morning"):
                day.morning.append(service.get_course_code())
            else:
                day.afternoon.append(service.get_course_code())

for day in days_list:
    if(day.get_morning()):
        for course_code in day.morning:
            for course in course_list:
                if(course_code == course.get_course_code() and course.get_course_type() == 'C'):
                    schedule = Scheduler(
                        day.get_name(), "Morning", day.get_morning_big_class().pop(0), course_code)
                    schedule_list.append(schedule)
                elif(course_code == course.get_course_code() and course.get_course_type() == 'E'):
                    schedule = Scheduler(
                        day.get_name(), "Morning", day.get_morning_small_class().pop(0), course_code)
                    schedule_list.append(schedule)

    if(day.get_afternoon()):
        for course_code in day.afternoon:
            for course in course_list:
                if(course_code == course.get_course_code() and course.get_course_type() == 'C'):
                    schedule = Scheduler(
                        day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(0), course_code)
                    schedule_list.append(schedule)
                elif(course_code == course.get_course_code() and course.get_course_type() == 'E'):
                    schedule = Scheduler(
                        day.get_name(), "Afternoon", day.get_afternoon_small_class().pop(0), course_code)
                    schedule_list.append(schedule)

for service_lesson in service_list:
    for course in course_list:
        if(service_lesson.get_course_code() == course.get_course_code()):
            course_list.remove(course)

for day in days_list:
    for course in course_list:
        if(day.get_morning_small_class()):
            if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Morning")) and not(is_intersection(day.get_name(), "Morning", course.get_course_code()))):
                schedule = Scheduler(
                    day.get_name(), "Morning", day.get_morning_small_class().pop(0), course.get_course_code())
                schedule_list.append(schedule)
                course_list.remove(course)

for day in days_list:
    for course in course_list:
        if(day.get_afternoon_small_class()):
            if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Afternoon")) and not(is_intersection(day.get_name(), "Afternoon", course.get_course_code()))):
                schedule = Scheduler(
                    day.get_name(), "Afternoon", day.get_afternoon_small_class().pop(0), course.get_course_code())
                schedule_list.append(schedule)
                course_list.remove(course)

for day in days_list:
    for course in course_list:
        if(day.get_morning_big_class()):
            if(course.get_course_type() == 'C' and not(is_busy(course.get_course_instructor(), day.get_name(), "Morning")) and not(is_intersection(day.get_name(), "Morning", course.get_course_code()))):
                schedule = Scheduler(
                    day.get_name(), "Morning", day.get_morning_big_class().pop(0), course.get_course_code())
                schedule_list.append(schedule)
                course_list.remove(course)

for day in days_list:
    for course in course_list:
        if(day.get_afternoon_big_class()):
            if(course.get_course_type() == 'C' and not(is_busy(course.get_course_instructor(), day.get_name(), "Afternoon")) and not(is_intersection(day.get_name(), "Afternoon", course.get_course_code()))):
                schedule = Scheduler(
                    day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(0), course.get_course_code())
                schedule_list.append(schedule)
                course_list.remove(course)

for day in days_list:
    for course in course_list:
        if(day.get_morning_big_class()):
            if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Morning")) and not(is_intersection(day.get_name(), "Morning", course.get_course_code()))):
                schedule = Scheduler(
                    day.get_name(), "Morning", day.get_morning_big_class().pop(len(day.get_morning_big_class()) - 1), course.get_course_code())
                schedule_list.append(schedule)
                course_list.remove(course)

for day in days_list:
    for course in course_list:
        if(day.get_afternoon_big_class()):
            if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Afternoon")) and not(is_intersection(day.get_name(), "Afternoon", course.get_course_code()))):
                schedule = Scheduler(
                    day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(len(day.get_afternoon_big_class()) - 1), course.get_course_code())
                schedule_list.append(schedule)
                course_list.remove(course)

repeat = int(class_list[0].get_number()) if int(class_list[0].get_number()) > int(
    class_list[1].get_number()) else int(class_list[1].get_number())

while(repeat > 0):
    for day in days_list:
        for item in day.get_morning_big_class():
            schedule = Scheduler(
                day.get_name(), "Morning", day.get_morning_big_class().pop(0), "--------")
            schedule_list.append(schedule)
        for item in day.get_morning_small_class():
            schedule = Scheduler(
                day.get_name(), "Morning", day.get_morning_small_class().pop(0), "--------")
            schedule_list.append(schedule)
        for item in day.get_afternoon_big_class():
            schedule = Scheduler(
                day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(0), "--------")
            schedule_list.append(schedule)
        for item in day.get_afternoon_small_class():
            schedule = Scheduler(
                day.get_name(), "Afternoon", day.get_afternoon_small_class().pop(0), "--------")
            schedule_list.append(schedule)
    repeat -= 1

big_class_substring = "bigClass"
small_class_substring = "smallClass"

if(len(course_list) != 0):
    print("There is no way to make a schedule for the department.")
else:
    for day in days_list:
        for item_morning in schedule_list:
            if(day.get_name() == item_morning.get_day_name() and item_morning.get_day_time() == "Morning" and item_morning.get_class_type().find(big_class_substring) != -1):
                display_curriculum.append(item_morning)
        for item_morning in schedule_list:
            if(day.get_name() == item_morning.get_day_name() and item_morning.get_day_time() == "Morning" and item_morning.get_class_type().find(small_class_substring) != -1):
                display_curriculum.append(item_morning)
        for item_afternoon in schedule_list:
            if(day.get_name() == item_afternoon.get_day_name() and item_afternoon.get_day_time() == "Afternoon" and item_afternoon.get_class_type().find(big_class_substring) != -1):
                display_curriculum.append(item_afternoon)
        for item_afternoon in schedule_list:
            if(day.get_name() == item_afternoon.get_day_name() and item_afternoon.get_day_time() == "Afternoon" and item_afternoon.get_class_type().find(small_class_substring) != -1):
                display_curriculum.append(item_afternoon)

    for item in display_curriculum:
        print(item.get_day_name(), item.get_day_time(),
              item.get_class_type(), item.get_course_code())
