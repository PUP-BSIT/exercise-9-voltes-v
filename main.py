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

#TODO(Pineda): Update movie details
def update_movie():
    pass

#TODO(Morales): Delete a movie from the list
def delete_movie():
    pass

#TODO(Gulles): Search for a movie by title
def search_movie():
    pass

#TODO(Caculitan): Handle Program Loop and User Interface
def main():
    pass
