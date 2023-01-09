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


s = C({"Peter": [4, 5, 4], "Harry": [2, 5], "Barbara": [3, 3, 3, 5, 5, 5]})
print(s.m(4))
print(s.m(3))
print(s.m(5))
