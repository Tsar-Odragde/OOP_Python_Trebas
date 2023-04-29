class Employee:
    def _init_(self, name, hourly_rate, hours_worked, experience):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.experience = experience

    def calculate_salary(self):
        if self.experience < 8:
            base_salary = self.hourly_rate * self.hours_worked * 30
            tax_deduction = base_salary * 0.13
            net_salary = base_salary - tax_deduction
            yearly_salary = net_salary * 12
            salary_without_tax = base_salary * 12
            return f"{self.name}'s base salary is ${base_salary:.2f}, yearly salary is ${yearly_salary:.2f}, and their net salary after tax deduction is ${net_salary:.2f} per month."
        elif self.experience > 15:
            base_salary = self.hourly_rate * self.hours_worked * 30
            bonus = 2000
            total_salary = base_salary + bonus
            tax_deduction = total_salary * 0.13
            net_salary = total_salary - tax_deduction
            yearly_salary = net_salary * 12
            salary_without_tax = total_salary * 12
            return f"{self.name}'s base salary is ${base_salary:.2f} with a bonus of ${bonus:.2f}, yearly salary is ${yearly_salary:.2f}, and their net salary after tax deduction is ${net_salary:.2f} per month."
        else:
            print("The input for experience is not defined in this range (It should be smaller than 8 or greater than 15)")

    def display_employee_details(self):
        print(f"Name: {self.name}")
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Hours Worked: {self.hours_worked:.2f}")
        print(f"Experience: {self.experience} years")

    def display_salary_details(self):
        salary_details = self.calculate_salary()
        print(salary_details)

name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
experience = int(input("Enter experience in years: "))

employee = Employee(name, hourly_rate, hours_worked, experience)

employee.display_employee_details()

employee.display_salary_details()
