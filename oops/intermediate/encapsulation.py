class Employee:
    def __init__(self, username):
        self.__username = username      # __ makes the field private

    def get_username(self):
        return self.__username
    
emp = Employee("Jack")
print(emp.get_username())