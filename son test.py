"""il=int(input("Il daxi edin: "))
def yoxla(_il):
    if _il % 4 == 0  or _il % 400==0:
        return "True"

    else:
        return "False"
netice=yoxla(il)
print(netice)"""


"""def is_leap(_year):
    leap=False
    if _year % 4 == 0 or _year % 400 == 0:
        return "True"

    else:
        return "False"
    return leap

year = int(input())
print(is_leap(year))"""


"""def is_leap(year):
    if year % 4 == 0 or year % 400 == 0:
        return "True"
    else:
        return "False"


year = int(input())
print(is_leap(year))"""


def is_leap(year):
    if year % 4 == 0 or year / 400 == 0:
        return "True"
    elif year % 100 == 0:
        return ("False")

    else:
        return ("False")


year = int(input())
print(is_leap(year))












