def kvadratAlma_decerator(_func):
    def wrapper():
        funcResult=_func()
        newResult=funcResult**2
        print(newResult)
        return newResult
    return wrapper
@kvadratAlma_decerator
def someFunc():
    x=int(input("Eded daxil edin:"))
    return x


someFunc()