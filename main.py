from abc import ABC, abstractmethod

class Department:
 
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    def __init__(self, code, name, salary, department):
        self.__department = department
        self.code = code
        self.name = name
        self.salary = salary
        self.workDay = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.workDay

    def get_department(self):
        return self.__department.name

    def set_department(self, department, department_code):
        self.__departament = Department(department, department_code)


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def calc_bonus(self):
        return self.__sales * 0.15

    def put_sales(self, sale):
        self.__sales += sale