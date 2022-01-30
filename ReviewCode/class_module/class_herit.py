class A():
    def __init__(self, a=None, b=None, *args, **kwargs):
        print('Init {} with arguments {}'.format(self.__class__.__name__, (a, b)))


class B():
    def __init__(self, q=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Init {} with arguments {}'.format(self.__class__.__name__, (q)))


class C(A, B):
    def __init__(self):
        super().__init__(a=1, b=2, q=3)


cs = C()
