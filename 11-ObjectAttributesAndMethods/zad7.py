class Student:
    currentid = 100000
    university = "UEK Kraków"

    def __init__(self, name, surname, fieldOfStudy):
        self.name = name
        self.surname = surname
        self.id = Student.currentid
        Student.currentid += 1
        self.fieldOfStudy = fieldOfStudy


    def __str__(self) -> str:
        return f'{self.name} {(self.surname).upper()} ({self.id}), {self.fieldOfStudy}, {self.university}'


print(Student('Kacper', 'Satora', 'Applied Informatics',))
print(Student('Jan', 'Kowalski', 'Philosophy',))
print(Student('Piotr', 'Nowak', 'Economy',))
