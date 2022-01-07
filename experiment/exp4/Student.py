class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return max(self.score)


if __name__ == '__main__':
    stu1 = Student("abs", 18, (65, 29, 13))
    stu2 = Student("bell", 19, (39, 39, 78))

    msg = stu1.get_name() + "," + str(stu1.get_age()) + "," + str(stu1.get_score())
    print(msg)

    msg = stu2.get_name() + "," + str(stu2.get_age()) + "," + str(stu2.get_score())
    print(msg)
