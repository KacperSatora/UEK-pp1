film_titles = ["Interstellar", "Star Wars", "No rest for the wicked", "Good, Bad and Ugly", "Woolf of Walstreet"]
file = open("t11.txt", "w")
for title in film_titles:
    file.write(f"{title}\n")