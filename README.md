Marks_for_course ={} # Оценки студентов
Marks_for_course_lect={} # Оценки лекторов

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.marks={}
        self.marks_List=[]
        self.average_mark=0
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.dict:
                lecturer.dict[course] += [grade]
            else:
                lecturer.dict[course] = [grade]
            if course in Marks_for_course_lect:
                Marks_for_course_lect[course]+=[grade]
            else:
                Marks_for_course_lect[course] = [grade]
            lecturer.marks[course] = sum(lecturer.dict[course]) / len(lecturer.dict[course])
            lecturer.marks_List = list(lecturer.marks.values())
            lecturer.average_mark = sum(lecturer.marks_List) / len(lecturer.marks_List)
        else:
            print("Ошибка")
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_mark}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res
Alex=Student("Alexey", "Petrov", "men")
Alex.courses_in_progress.append("Math")
Alex.courses_in_progress.append("IT")
Alex.courses_in_progress.append("English")
Alex.courses_in_progress.append("Russian")

Olga=Student("Olga", "Ivanova", "women")
Olga.courses_in_progress.append("Math")
Olga.courses_in_progress.append("Russian")
Olga.courses_in_progress.append("English")

print(Alex.courses_in_progress)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    dict={}
    marks = {}
    marks_List = []
    average_mark = 0
    def __str__(self):
        res=f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_mark}'
        return res

def __lt__(Lecturer, Student):
    return Lecturer.average_mark<Student.average_mark



Antony=Lecturer("Anton", "Ptushkin")
Antony.courses_attached.append("IT")
Antony.courses_attached.append("English")
print(Antony.dict, Antony.name)

Oleg=Lecturer("Oleg", "Popov")
Oleg.courses_attached.append("Russian")
Oleg.courses_attached.append("Math")

class Reviewer(Mentor):
    def __str__(self):
        res=f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
            # print(sum(student.grades[course])/len(student.grades[course]))
            if course in Marks_for_course:
                Marks_for_course[course]+=[grade]
            else:
                Marks_for_course[course] = [grade]
            print(Marks_for_course)
            student.marks[course]=sum(student.grades[course])/len(student.grades[course])
            student.marks_List = list(student.marks.values())
            student.average_mark=sum(student.marks_List)/len(student.marks_List)
        else:

            return 'Ошибка'
Peter=Reviewer("Peter", "Volkov")
Peter.courses_attached.append("Math")
Peter.courses_attached.append("IT")
Polina=Reviewer("Polina", "Tur")
Polina.courses_attached.append("Math")
Polina.courses_attached.append("Russian")

Peter.rate_hw(Alex, "Math", 5)
Peter.rate_hw(Alex, "Math", 4)
Peter.rate_hw(Alex, "IT", 5)
Peter.rate_hw(Alex, "IT", 2)
Polina.rate_hw(Alex, "Math", 3)
Polina.rate_hw(Alex, "Russian", 2)
Polina.rate_hw(Olga, "Russian", 5)

print(Alex.grades)
print(Alex.marks)
print(Alex.average_mark)

print(Peter.courses_attached)
Alex.rate_lect(Antony, "IT", 10)
Alex.rate_lect(Antony, "IT", 8)
Alex.rate_lect(Antony, "IT", 10)
Alex.rate_lect(Antony, "English", 5)
print(Antony.dict)
print(Antony.average_mark)
print(Antony<Alex)
print(Alex)
print(Antony)
print(Peter)

print(Marks_for_course)
def Average_mark_stud(course):
    print (sum(Marks_for_course[course])/len(Marks_for_course[course]))
Average_mark_stud('IT')

def Average_mark_lect(course):
    print (sum(Marks_for_course_lect[course])/len(Marks_for_course_lect[course]))
Average_mark_lect('IT')