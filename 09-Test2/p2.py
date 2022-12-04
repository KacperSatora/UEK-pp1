def f(human_age):
    if human_age > 2:
        return ((human_age * 10) - ((human_age - 2) * 10) + ((human_age - 2) * 4))
    else:
        return human_age * 10