# curriculum-planner
This project has been implemented to learn Python from scratch for CENG206 - Programming Languages lesson. In this project, I have implemented an automatic course planner for a curriculum semester of a department with using Python. In the
curriculum, there are several courses for each year of the curriculum. The program assign a classroom and a time slot
for each course in the curriculum. Courses in the same year should not be intersected with each other. 
There can be some intersection between courses of different years. There are 2 different types of the
classroom: big and small. Mandatory courses in the curriculum must be assigned to a big classroom. Elective courses can
be assigned to a big or small classroom according to the availability of them. There is a limited number of dedicated
classrooms for the department. The number of each type of classroom have been read from a file. Besides, for each
weekday there are 2-time slots available, morning and afternoon.
In the department curriculum, there are some service courses which are given by another department at the university.
The time slot of these courses is fixed and predefined. Therefore, these lessons can not be assigned different time slots for those courses
other than the requested time slot. Furthermore, some instructors may not be available for some time slots. Thus, the
program should respect these busy time slots for the respective courses. The all data were obtained by reading from the given files mentioned.
In the end, the program will print the course schedule for the department. In this schedule, there is no
intersection between courses for a year of the curriculum and respect to all constraints. If the program can not find any
possible schedule it will print a message “There is no way to make a schedule for the department.” To fit the course
schedule, the number of classrooms must be increased via editing the file.
