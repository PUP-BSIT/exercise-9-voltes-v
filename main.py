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

#TODO(CORPUS): Ensure that the Director and Genre fields do not accept numbers,
# and the Release Year and Rating fields do not accept letters."

def add_movie(movie_list):
    print("\nAdd New Movie")
    movie = {
        "title": input("Enter title: "),
        "director": input("Enter director: "),
        "genre": input("Enter genre: "),
        "release_year": input("Enter release year: "),
        "rating": input("Enter rating (1 - 10): ")
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
                f"Enter new release year [{movie['release_year']}]: "
            ) or movie["release_year"]

            new_rating = input(
                f"Enter new rating [{movie['rating']}]: "
            ) or movie["rating"]

            movie.update({
                "title": new_title,
                "director": new_director,
                "genre": new_genre,
                "release_year": new_year,
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