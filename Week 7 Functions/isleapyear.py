def isleapyear(year):
    if year%100==0:
        if year%400==0:
            return True
    elif year%4==0:
        return True
    return False
