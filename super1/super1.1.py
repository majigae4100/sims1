class Town:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, audience):
        self.audience = audience


class Student(Town, School):
    student_name = "Petro"

    def __init__(self, name, audience, age):
        super(Town, self).__init__(name)
        super(Student, self).__init__(audience)
        self.age = age


student = Student(name='Kyiv', audience="17", age='18')
print(f"Audience: {student.name}")
print(f"City: {student.audience}")
print(f"Age: {student.age}")
