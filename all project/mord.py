# Example of Method Overriding in Python

class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Testing method overriding
if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()

    print(animal.speak())  # Output: Animal makes a sound
    print(dog.speak())     # Output: Dog barks
    print(cat.speak())     # Output: Cat meows
