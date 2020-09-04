def layout_decerator(_func):
    def localFunc():
        dinamikhisse=_func()
        txt=f"Header hissesine aid kodlar:\n {dinamikhisse} \n Footer hissesine aid kodlar:"
        return  txt
    return localFunc
@layout_decerator
def Home():
    return ("---Ana sehifeye aid olan kodlar:")
@layout_decerator
def About():
    return ("---Haqqimizda sehifesine aid olan kodlar:")
@layout_decerator
def Contact():
    return ("---Kontakt hissesine aid olan kodlar:")
print(Home())
print(About())
print(Contact())