class Student(object):
    def __init__(self):
        self.name = '22'

    def __getattr__(self, attr):
        return lambda :"22"

    # def __repr__(self):
    #     return self.name

    # def __call__(self):
    #     print('My name is %s.' % self.name)


s = Student()
print s.age()
