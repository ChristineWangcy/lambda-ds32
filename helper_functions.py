import pandas as pd

<<<<<<< HEAD
def null_count(df):
    return df.isnull().sum().sum()
=======
>>>>>>> eb5c007e1e4e3dc79cac5400f5be569c58ba7bdb

def split_dates(date_series):
    months = date_series.apply(lambda x: x[:2])
    days = date_series.apply(lambda x: x[3:5])
    years = date_series.apply(lambda x: x[6:])
    return(pd.DataFrame({'month': months, 'day': days, 'year': years}))


def list_2_series(list_2_series, df):
    df['list'] = list_2_series
<<<<<<< HEAD
    return(df)

=======
    print(df)


print(list_2_series([1, 2], pd.DataFrame()))
split_dates(pd.Series(['09/12/2018', '11/23/2017']))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_school(self, school_name):
        self.school_name = school_name

    def add_subjects(self, subjects):
        self.subjects = subjects

    def introduce(self):
        return "Student " + self.name + " is " + self.age + " years old"


class MiddleSchool(Student):
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
>>>>>>> eb5c007e1e4e3dc79cac5400f5be569c58ba7bdb
