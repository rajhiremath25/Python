class Employee:

    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Salary : ", self.salary)
        print("Gender :", self.gender)


employee = Employee("Ajinkya Rahane", 35, 2000000, "M")
employee.employee_details()