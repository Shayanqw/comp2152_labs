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

# Print the public attribute public_prop (should work)
print("Public property:", person_instance.public_prop)

# Try printing the private name property directly (this should cause an AttributeError)
try:
    print(person_instance.__name)
except AttributeError as e:
    print("AttributeError:", e)

# Access the name via the magic getter
print("Name via magic getter:", person_instance.name)

# Modify the name using the magic setter (set the new name to Anna)
person_instance.name = "Anna"

# Print again to confirm the change
print("Updated name via magic getter:", person_instance.name)