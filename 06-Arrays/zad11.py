def month(n):
    monthDict = {
        1: "Styczen",
        2: "Luty",
        3: "Marzec",
        4: "Kwiecien",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpien",
        9: "Wrzesien",
        10: "Październik",
        11: "Listopad",
        12: "Grudzień"
    }
    return monthDict[n]

print(month(1) + "\n" + month(2) + "\n" + month(11) + "\n" + month(12))