import random


class Arrays:
    @staticmethod
    def f1(numOfElements, values):
        list = []
        for i in range(numOfElements):
            list.append(values)
        return list

    @staticmethod
    def f2(numOfElements, start, end):
        list = []
        for i in range(numOfElements):
            list.append(random.randint(start, end))
        return list

    @staticmethod
    def f3(arr, start, end):
        count = 0
        for num in arr:
            if num >= start and num <= end:
                count += 1
        return count


print(Arrays.f1(10, 4))
print(Arrays.f2(20, -7, 8))
print(Arrays.f3(Arrays.f2(20, -7, 8), -1, 1))
