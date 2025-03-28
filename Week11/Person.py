class Person:
    def __init__(self, p_name, p_age, p_height):
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        print("Constructing the Person Object")
        self.public_prop = "I'm Public"
        self.private_prop = "I'm Private"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")


person_instance = Person("Sahand", 20, 6)
print("Public property:", person_instance.public_prop)

try:
    print(person_instance.__name)
except AttributeError as e:
    print("AttributeError:", e)
print("Name via magic getter:", person_instance.name)
person_instance.name = "Anna"
print("Updated name via magic getter:", person_instance.name)