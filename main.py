from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def int_float_procces(data):
        return data*2

    @process.register(str)
    @staticmethod
    def str_procces(data):
        return data.upper()

    @process.register(list)
    @process.register(tuple)
    @staticmethod
    def _from_list_or_tuple(data):
        return data.__class__(sorted(data))






print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
try:
    print(Processor.process({3, 2, 1}))
except Exception as e:
    print(e)


