from Week11.Person import Person


class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        super().__init__(p_name, p_age, p_height)
        self.major = p_major
        print("This time it's a Student object")


student_instance = Student("Shayan", 23, 6, "Computer Science T177")

print("Student name :", student_instance.name)
print("Student major:", student_instance.major)
