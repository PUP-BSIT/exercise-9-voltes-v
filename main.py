#TODO(Gulles): Display the Main Menu Options
def display_menu():
    pass

def list_all_movies(movie_list):
    if not movie_list:
        print("No movies found.")
        return

    for index, movie in enumerate(movie_list, start=1):
        print(f"\nMovie {index}:")
        for key, value in movie.items():
            print(f"  {key.capitalize()}: {value}")

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
    print("Movie added successfully.")

def update_movie(movie_list):
    title_to_update = input("Enter the title of the movie to update: ")

    for movie in movie_list:
        if movie["title"].lower() == title_to_update.lower():
            print("Movie found. Leave input blank to keep current value.")

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

#TODO(Morales): Delete a movie from the list
def delete_movie():
    pass

#TODO(Caculitan): Search for a movie by title
def search_movie(movie_list):
    title_to_search = input("Enter the title to search for: ")

    found = False
    for movie in movie_list:
        if movie["title"].lower() == title_to_search.lower():
            print("\nMovie found:")
            for key, value in movie.items():
                print(f"  {key.capitalize()}: {value}")
            found = True
            break

    if not found:
        print("Movie not found.")

#TODO(Gulles): Handle Program Loop and User Interface
def main():
    pass
