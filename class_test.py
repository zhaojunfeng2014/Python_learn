class A:
    explanation = 'this is my programs'

    def normal_method(self, name):
        print(self.explanation)

    @classmethod
    def class_method(cls, explanation):
        print(cls.explanation)

    @staticmethod
    def static_method(explanation):
        print(explanation)


a = A()
a.explanation = 'this is new'
a.normal_method('explanation')
