employee_list = []

class Employee:

    def add_employee(self, emp_id, name, place):
        employee = {
            "name": name,
            "emp_id": emp_id,
            "place": place
        }
        employee_list.append(employee)

    def print_employee(self):
        for i in range(len(employee_list)):
            print(" employee : ", employee_list[i])

    def delete(self,emp_id):
        #del employee_list[0]
        print("size : ", len(employee_list))
        for i in range(len(employee_list)):
            print("iterator : ",employee_list[i], "emp_id : ", emp_id)
            emp  = employee_list[i]
            if emp["emp_id"] == emp_id:
                del employee_list[i]
                print("size : ", len(employee_list))

    def search(self,emp_id):
        for i in range(len(employee_list)):
            emp = employee_list[i]
            if emp["emp_id"] == emp_id:
                print("found: ",employee_list[i])

    def main(self):
        number = input(" How many emp do you want ?? ")
        print (number)
        for j in range(int(number)):
            name = input("Enter name : ")
            emp_id = input(" Enter emp id : ")
            place = input (" Enter place : ")
            emp.add_employee(emp_id, name, place)

        emp.print_employee()
        id = input(" emp to delete id : ")
        #emp.delete(id)
        emp.search(id)

emp = Employee();
emp.main();