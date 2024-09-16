class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

# Create an instance of Dog
dog = Dog()

# Call the make_sound method
dog.make_sound()  # Output: Dog barks
