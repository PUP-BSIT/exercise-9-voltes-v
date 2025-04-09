def display_menu():
    print("\n===================")
    print("  Movie Main Menu  ")
    print("===================")
    print("1. List all movies")
    print("2. Add a new movie")
    print("3. Update a movie")
    print("4. Delete a movie")
    print("5. Search for a movie")
    print("6. Exit")
    print("===================")

def list_all_movies(movie_list):
    if not movie_list:
        print("\nNo movies found.")
        return

    for index, movie in enumerate(movie_list, start=1):
        print(f"\nMovie {index}:")
        for key, value in movie.items():
            print(f"  {key.capitalize()}: {value}")

def add_movie(movie_list):
    print("\nAdd New Movie")

    title = input("Enter title: ")

    while True:
        director = input("Enter director: ")
        if any(char.isdigit() for char in director):
            print("Director name should not contain numbers.")
        else:
            break

    while True:
        genre = input("Enter genre: ")
        if any(char.isdigit() for char in genre):
            print("Genre should not contain numbers.")
        else:
            break

    while True:
        release_year_input = input("Enter release year: ")
        if release_year_input.isdigit():
            release_year = int(release_year_input)
            break
        else:
            print("Release year must be a number.")

    while True:
        rating_input = input("Enter rating (1 - 10): ")
        try:
            rating = float(rating_input)
            if rating_input.replace('.', '', 1).isdigit() and 1 <= rating <= 10:
                break
            else:
                print("Rating must be a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Rating must be a number.")

    movie = {
        "title": title,
        "director": director,
        "genre": genre,
        "release year": release_year,
        "rating": rating
    }
    movie_list.append(movie)
    print("\nMovie added successfully.")

def update_movie(movie_list):
    title_to_update = input("\nEnter the title of the movie to update: ")

    for movie in movie_list:
        if movie["title"].lower() == title_to_update.lower():
            print("\nMovie found. Leave input blank to keep current value.")

            new_title = input(
                f"Enter new title [{movie['title']}]: "
            ) or movie["title"]

            new_director = input(
                f"Enter new director [{movie['director']}]: "
            ) or movie["director"]

            new_genre = input(
                f"Enter new genre [{movie['genre']}]: "
            ) or movie["genre"]

            new_year = input(
                f"Enter new release year [{movie['release year']}]: "
            ) or movie["release year"]

            new_rating = input(
                f"Enter new rating [{movie['rating']}]: "
            ) or movie["rating"]

            movie.update({
                "title": new_title,
                "director": new_director,
                "genre": new_genre,
                "release year": new_year,
                "rating": new_rating
            })

            print("Movie details updated successfully!.")
            return

    print("Movie not found.")

def delete_movie(movie_list):
    title_to_delete = input("\nEnter the title of the movie to delete: ")

    for movie in movie_list:
        if movie["title"].lower() == title_to_delete.lower():
            movie_list.remove(movie)
            print("\nMovie deleted successfully.")
            return

    print("\nMovie not found.")

def search_movie(movie_list):
    title_to_search = input("\nEnter the title to search for: ")

    found = False
    for movie in movie_list:
        if movie["title"].lower() == title_to_search.lower():
            print("\nMovie found:")
            for key, value in movie.items():
                print(f"  {key.capitalize()}: {value}")
            found = True
            break

    if not found:
        print("\nMovie not found.")

def main():
    movie_list = []

    while True:
        display_menu()
        choice = input("Select an option (1-6): ")


        if choice == '1':
            list_all_movies(movie_list)
        elif choice == '2':
            add_movie(movie_list)
        elif choice == '3':
            update_movie(movie_list)
        elif choice == '4':
            delete_movie(movie_list)
        elif choice == '5':
            search_movie(movie_list)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()