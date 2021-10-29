'''docstring'''


class Student:
    '''docring'''

    def __init__(self, name, age):
        '''docsring'''
        self.name = name
        self.age = age

    def add_school(self, school_name):
        '''docstring'''
        self.school_name = school_name

    def add_subjects(self, subjects):
        '''docstring'''
        self.subjects = subjects

    def introduce(self):
        '''docstring'''
        return "Student " + self.name + " is " + self.age + " years old"


class MiddleSchool(Student):
    '''docstring'''

    def __init__(self, name, age, school_name, grade):
        super().__init__(name, age)
        self.school = school_name
        self.grade = grade

    def introduce(self):
        return (super().introduce() + " in grade " +
                self.grade + "th of school " + self.school)


student_Kimi = Student('Kimi', '9')
student_Kimi.add_subjects = ['English', 'Math', 'Science', 'Coding']
print(student_Kimi.introduce())
student_Peggy = MiddleSchool('Peggy', '12', 'Brette Heart', '6')

print(student_Peggy.introduce())
