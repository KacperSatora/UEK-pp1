def month(n):
    months = ["Styczen", "Luty", "Marzec", "Kwiecien",
              "Maj", "Czerwiec", "Lipiec", "Sierpien",
              "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]
    return months[n - 1]


print(month(7))