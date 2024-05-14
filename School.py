from abc import ABC,abstractmethod

class School(ABC):   
    def __init__(self,name,surname,age,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.number_of_floors = 5
    @abstractmethod
    def show(self):
        return f"Name:{self.name} \nSurname : {self.surname} \nAge : {self.age} \nGender : {self.gender}"

    @abstractmethod
    def __del__(self):
        return f"{self.name} {self.surname} has left the school."  
   
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_age(self):
        return self.age
  
    def get_gender(self):
        return self.gender

class Student(School):
    def __init__(self,name,surname,age,gender,number,time,grade):
        School.__init__(self,name,surname,age,gender)
        self._number = number
        self.time = time
        self.grade= grade

    def show(self):
        return School.show(self) + f"\nNumber : {self._number} \nTime : {self.time} \nGrade : {self.grade}"
    
    def __del__(self):
        return f"{self.name} {self.surname} has graduated from school."

    def get_number(self):
        return self._number

    def get_time(self):
        return self.time

    def set_time(self,new_time):
        if new_time != "Morning" or new_time != "Day":
            return "Enter a valid time => 'Day' or 'Morning'"
        else:
            self.time = new_time
    
    def get_grade(self):
        return self.grade

    def grade_up(self):
        if self.grade == 8:
            return f"{self.name} {self.surname} graduated from school."
        else:
            self.grade += 1

    def enter_lesson(self):
        return "The lesson has started."

    def leave_lesson(self):
        return "The lesson has finished."

    def study(self):
        return f"{self.name} {self.surname} has started to study."

class Teacher(School):
    def __init__(self,name,surname,age,gender,field,work_time,salary):
        School.__init__(self,name,surname,age,gender)
        self.field = field
        self.work_time = work_time
        self.__salary = salary

    def show(self):
        return School.show(self) + f"\nField : {self.field} \nWork Time : {self.work_time} \nSalary : {self.__salary}"

    def __del__(self):
        return f"{self.name} {self.surname} has stopped giving lecture."

    def get_field(self):
        return self.field
        
    def add_field(self,new_field):
        self.field.append(new_field)

    def get_work_time(self):
        return self.work_time

    def change_work_time(self,new_work_time):
        if new_work_time != "Day" or "Night":
            return f"Enter a valid time => 'Day' or 'Morning"
        else:
            self.work_time = new_work_time

    def give_lecture(self):
        return f"{self.name} {self.surname} is giving {self.field[0]}"

    def is_senior(self):
        if self.work_time > 10:
            return f"{self.name} {self.surname} is a senior teacher"
        else:
            return f"{self.name} {self.surname} is not a senior teacher."

    def get_salary(self):
        return self.__salary

    def raise_salary(self,ratio):
        if ratio < 0:
            return f"Enter a positive value to raise salary"
        else:
            if self.work_time < 10:
                self.__salary += self.__salary * ratio * 1.80
            else:
                self.__salary += self.__salary * ratio

    def raise_work_time(self):
        self.work_time += 1

class Janitor(School):
    def __init__(self,name,surname,age,gender,shift,salary,floor):
        School.__init__(self,name,surname,age,gender)
        self.shift = shift
        self.__salary = salary
        self.floor = floor

    def show(self):
        return School.show(self) + f"\nShift : {self.shift} \nSalary : {self.__salary} \nFloor : {self.floor}"

    def __del__(self):
        return f"{self.name} {self.surname} has left the job."

    def get_shift(self):
        return self.shift

    def set_shift(self,new_shift):
        if new_shift != "Day" or "Night":
            return "Enter a valid shift => Day or Night"
        else:
            if self.shift == "Day":
                self.shift = "Night"
                return "Janitor is now working at night shift"
            else:
                self.shift = "Day"
                return "Janitor is now working at day shift"

    def get_salary(self):
        return self.__salary

    def raise_salary(self,ratio):
        if ratio < 0:
            return "Enter a positive value for ratio"
        else:
            self.__salary += self.__salary * ratio

    def get_floor(self):
        return self.floor

    def change_floor(self,new_floor):
        if new_floor > self.number_of_floors or new_floor <0:
            return f"Enter a value between 0 and {self.number_of_floors}"
        else:
            self.floor = new_floor

    def clean_bathrooms(self):
        return "Bathrooms has been cleaned"


class Principal(School):
    def __init__(self,name,surname,age,gender,salary,work_time):
        School.__init__(self,name,surname,age,gender)
        self.__salary = salary
        self.work_time = work_time

    def show(self):
        return School.show(self) + f"\nSalary : {self.__salary} \nWork Time : {self.work_time}"

    def __del__(self):
        return f"{self.name} {self.surname} has resigned from school as principal"

    def get_salary(self):
        return self.__salary

    def raise_salary(self,ratio):
        if ratio < 0:
            return "Enter a positive value for ratio"
        else:
            self.__salary += self.__salary * ratio

    def get_work_time(self):
        return self.work_time

prin = Principal("Nazlı","Aydın",21,"FeMale",15000,5)
print(prin.show())
print(prin._Principal__salary)
            

    
        