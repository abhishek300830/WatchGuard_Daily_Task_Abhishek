MENU_PROMPT = "\nEnter 'a' to add a movie \nEnter 'l' to see your movies\nEnter 'f' to find a movie by title\nEnter 'q' to quit: "
movies = []


def list_length():
    return len(movies)


def user_input_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    return [title,director,year]


def add_movie():
    title,director,year = user_input_movie()
    movies.append({
    'title': title,
    'director': director,
    'year': year
    })


def listing_movie():
    print("Movies present in Collection are...")
    if(list_length()==0):
        print("No Movie Present")
        return
    
    for index,movie in enumerate(movies):
        print_movie(index,movie)
        

def print_movie(index,movie):
    print(f"{index}. Title : {movie['title']}")
    print(f"    Released in ({movie['year']})")
    print(f"    Director by : {movie['director']}")


def searching_in_list(movie_name):
    for movie in movies:
        if movie['title'].lower() == movie_name.lower():
            print(f"{movie_name} is Present in the Collection.")
            return
        
    print("Movie not Found in Collection.")


def finding_movie():
    movie_name = input("Enter Movie Name you want to search  : ")
    searching_in_list(movie_name)


user_options= {
    'a':add_movie,
    'l':listing_movie,
    'f':finding_movie
}


def user_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_fun = user_options[selection]
            selected_fun()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


user_menu()