class C:
    def __init__(self, students):
        self.students = dict(students)

    def m(self, n):
        names = []
        for student in self.students:
            if sum(self.students[student]) / len(self.students[student]) >= n:
                names.append(student)
        names.sort()
        return ",".join(names)