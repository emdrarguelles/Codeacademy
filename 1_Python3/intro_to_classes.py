class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
    else:
      pass
  
  def get_average(self):
    if not self.grades:
        return 0
    return sum(self.grades)/len(self.grades)
  
  def add_attendance(self, date, was_present):
    self.attendance[date] = was_present

  def get_attendance(self):
    return self.attendance

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score
  
  def is_passing(self):
    if self.score >= 65:
      return "Pass"
    else:
      return "Fail"


grade_100 = Grade(100)
pieter.add_grade(grade_100)

