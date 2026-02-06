class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print(f"name : {self.name} , age :{self.age}")

class student(person):
    school_name="ABCD school"

    def __init__ (self,name,age,class_name,roll,marks=0):
        super().__init__(name,age)
        self.class_name=class_name
        self.roll=roll
        self.__marks = marks #private

    def set_marks(self,marks):
        self.__marks= marks
    def get_marks(self):
        return self.__marks
    def grade(self):
        if self.__marks >= 80 and self.__marks<=100:
            return "A+"
        elif self.__marks >= 70 and self.__marks<=79:
            return "A"
        elif self.__marks >= 65 and self.__marks<=69:
            return "A-"
        elif self.__marks >= 60 and self.__marks<=64:
            return "B+"
        elif self.__marks >= 55 and self.__marks<=59:
            return "B"
        elif self.__marks >= 50 and self.__marks<=54:
            return "C+"
        elif self.__marks >= 45 and self.__marks<=49:
            return "D+"
        elif self.__marks >= 33 and self.__marks<=44:
            return "D"
        elif self.__marks < 33:
            return "F"
        else:
            return"invalid grade"
    def show_info(self):
        super().show_info()
        print(f"class : {self.class_name} , Roll: {self.roll} marks: {self.__marks} grade: {self.grade()}")
        
    def __del__(self):
        print(f"student{self.name} , Roll {self.roll} has beeen removed")

class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def show_info(self):
        super().show_info()
        print(f"subject:  {self.subject}")
        
class admin(teacher):
    def add_student(self,student_list,student):
        student_list.append(student)
        print(f"{student.name} added sucessfully!")
    def remove_student(self,student_list,roll):
        for s in student_list:
            if s.roll==roll:
                student_list.remove(s)
                print("removed student")
                del s
                break
    def update_marks(self,student_list,roll,new_marks):
        for s in student_list:
            if s.roll == roll:
                s.set_marks(new_marks)
                print("marks updated")
                break




students=[] 

admin1= admin("mr rahim" , 32 , "match")


while(True):
    print("\n  -- student Manegment System")
    print("1. Add student")
    print("2. Show all Students")
    print("3. Update Marks")
    print("4. Remove Student")
    print("5. PLEASE LEAVE")


    choice=input("enter your choice: ")

    if choice=="1":
        name=input("Student Name: ")
        age=float(input("age: "))
        class_name=input("class: ")
        roll=float(input("roll: "))
        marks=float(input("mark: "))

        st=student(name,age,class_name,roll, marks)


        admin1.add_student(students,st)
    elif choice== "2":
        for s in students:
            s.show_info()
            print("-----------")
    elif choice== "3":
        roll=int(input("Enter student roll: "))
        new_marks=float(input("Enter the new marks: "))

        admin1.update_marks(students,roll,new_marks)
    elif choice== "4":
        roll=int(input("Enter student roll: "))

        admin1.remove_student(students,roll)
    elif choice== "5":
        print("Removing you from the system")
        break
    else:
        print("ERROR 404 NOT FOUND")