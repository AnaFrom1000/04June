Students_list = []
Lecturer_list = []


class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.marks = {}
        self.marks_List = []
        self.average_mark = 0
        Students_list.append(self)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.dict:
                lecturer.dict[course] += [grade]
            else:
                lecturer.dict[course] = [grade]
          
        else:
            print("Ошибка")
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_mark}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент!")
            return
        return self.average_mark < other.average_mark


Alex = Student("Alexey", "Petrov", "men")
Alex.courses_in_progress.append("Math")
Alex.courses_in_progress.append("IT")
Alex.courses_in_progress.append("English")
Alex.courses_in_progress.append("Russian")

Olga = Student("Olga", "Ivanova", "women")
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
   
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.dict = {}
        self.marks = {}
        self.marks_List = []
        self.average_mark = 0
        Lecturer_list.append(self)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_mark}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор!")
            return
        return self.average_mark < other.average_mark


Antony = Lecturer("Anton", "Ptushkin")
Antony.courses_attached.append("IT")
Antony.courses_attached.append("English")
print(Antony.dict, Antony.name)

Oleg = Lecturer("Oleg", "Popov")
Oleg.courses_attached.append("Russian")
Oleg.courses_attached.append("Math")


class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
         
        else:

            return 'Ошибка'


Peter = Reviewer("Peter", "Volkov")
Peter.courses_attached.append("Math")
Peter.courses_attached.append("IT")
Polina = Reviewer("Polina", "Tur")
Polina.courses_attached.append("Math")
Polina.courses_attached.append("Russian")

Peter.rate_hw(Alex, "Math", 5)
Peter.rate_hw(Alex, "Math", 4)
Peter.rate_hw(Alex, "Math", 2)
Peter.rate_hw(Alex, "IT", 5)
Peter.rate_hw(Alex, "IT", 2)
Polina.rate_hw(Alex, "Math", 3)
Polina.rate_hw(Alex, "Russian", 2)
Polina.rate_hw(Olga, "Russian", 5)
Polina.rate_hw(Olga, "Russian", 4)
Polina.rate_hw(Olga, "Russian", 4)
Polina.rate_hw(Olga, "Math", 3)
print(Alex.grades)
print(Alex.marks)
print(Alex.average_mark)

print(Peter.courses_attached)
Alex.rate_lect(Antony, "IT", 10)
Alex.rate_lect(Antony, "IT", 8)
Alex.rate_lect(Antony, "IT", 10)
Alex.rate_lect(Antony, "English", 5)
print(Antony.dict)
print()




print(Olga > Alex)




def average_rate_stud(group, course): # функция на определение средней оценки студентов за курс 
  Mark_list=[]
  flag=True
  if group==Student:
    Mark_list=[]
    flag=True
    for i in range(len(Students_list)):
      if course in Students_list[i].grades:
        flag=False
        Mark_list+=Students_list[i].grades[course]
        
    
    if flag==True:
      print("Такой курс студенты не проходили или нет ни одной оценки")

    else:
      average_mark = sum(Mark_list) / len(Mark_list)
      print(f'Средняя оценка за курс {course} составляет {average_mark}')


  elif group==Lecturer:
    
    for i in range(len(Lecturer_list)):
      if course in Lecturer_list[i].dict:
        flag=False
        Mark_list+=Lecturer_list[i].dict[course]
   
    
    if flag==True:
      print("Такой курс не преподается или у лекторов нет ни одной оценки")

    else:
      average_mark = sum(Mark_list) / len(Mark_list)
      print(f'Средняя оценка за курс {course} составляет {average_mark}')


average_rate_stud(Student, "Math")