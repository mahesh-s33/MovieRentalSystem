from Model.User import User

if __name__ == '__main__':
    print("Welcome to Movie Rental Systems")
    print("+++++++++++++++++++++++++++++++")
    choice = ''
    user = User('mahesh')
    while choice!='q':
        print("Enter your choice \nShow List: s \nAdd Movie: a \nDelete Movie: d " +
              "\nWatched Movies: w \nMark as watched: m\nQuit: q")
        choice = input()
        if choice=='a':
            name = input("Enter movie name: ")
            genre = input("Enter genre: ")
            user.addMovie(name, genre)
        if choice=='s':
            print(f"{user}")
        if choice=='d':
            name = input("Enter movie name to be deleted: ")
            user.deleteMovie(name)
        if choice=='m':
            print(f"{user}")
            num = int(input("Enter the movie no to set as watched."))
            user.markWatched(num)
        if choice=='w':
            print(user.watchedMovies())


