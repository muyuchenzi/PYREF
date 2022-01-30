class Work(object):
    def __init__(self, work_class, *args, **kwargs):
        print('---', *args, '----')
        super().__init__(*args, **kwargs)
        self.work_class = work_class
