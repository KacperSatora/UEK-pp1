import re


class C:

    @staticmethod
    def m1(n):
        oddNumbers = re.findall(r"[24680]", str(n))
        return "".join(oddNumbers)
    @staticmethod
    def m2(n):
        digits = list(str(n))
        for i in range(1, len(digits)):
            if digits[i] < digits[i - 1]:
                return False
        return True
    @staticmethod
    def m3(n):
        modelSet = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        digits = set(list((str(n))))
        result = list(modelSet - digits)
        result.sort()
        return "".join(result)
