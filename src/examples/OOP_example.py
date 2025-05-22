
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f'My name is {self.name} and I am a {self.breed}'


my_dog = Dog("Rhea", "Tibetan Mastiff")
print(my_dog.bark())

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled = []

    def enroll(self, course):
        self.enrolled.append(course)

    def get_courses(self):
        return self.enrolled
    def __str__(self): #When printing object
        return f"{self.name} ({self.student_id}) - Courses: {', '.join(self.enrolled)}"
    
    def __repr__(self): #When debugging
        return f"Student(name='{self.name}', student_id='{self.student_id}', courses={self.enrolled})"

    
s1 = Student("Lucas", "IE2029")
s1.enroll("Programming_II")
s1.enroll('Calc_II')
print(s1.get_courses())
print(s1)  
print(repr(s1))


