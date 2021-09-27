from movie import Movie
import csv

movies_file = open("movies.csv", "r")
movies_csv = csv.reader(movies_file, delimiter=',')

movies = []

for row in movies_csv:
    m = Movie(row[1], row[3], row[5], row[9])
    movies.append(m)

while True:
    # display menu
    print("1. By genre")
    print("2. By year")
    print("3. By director")
    print("0. Exit")

    choice = input("Select: ")

    if choice == "1":
        genre = input("Genre: ")
        for m in movies:
            if m.has_genre(genre):
                print(m, m.genre)
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("Wrong choice")
