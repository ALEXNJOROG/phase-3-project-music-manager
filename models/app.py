from models import Artiste, Song

def main_menu():
    print('Welcome to the Music CLI!')
    print('1. Artiste Menu')
    print('2. Song Menu')
    print('3. Exit')
    choice = input('Enter your choice: ')
    return choice

def artiste_menu():
    while True:
        print('\nArtiste Menu')
        print('1. Create Artiste')
        print('2. View All Artistes')
        print('3. Find Artiste by ID')
        print('4. Delete Artiste')
        print('5. View Songs by Artiste')
        print('6. Return to Main Menu')
        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter artiste name: ')
            artiste = Artiste()
            artiste.create(name)
            print(f'Artiste created with name: {name}')

        elif choice == '2':
            artiste = Artiste()
            artistes = artiste.get_all()
            for artiste_data in artistes:
                print(f"ID: {artiste_data[0]}, Name: {artiste_data[1]}")

        elif choice == '3':
            id = int(input('Enter artiste ID: '))
            artiste = Artiste()
            artiste_data = artiste.get_by_id(id)
            if artiste_data:
                print(f"ID: {artiste_data[0]}, Name: {artiste_data[1]}")
            else:
                print(f'Artiste with ID {id} not found')

        elif choice == '4':
            id = int(input('Enter artiste ID: '))
            artiste = Artiste()
            artiste.delete(id)
            print(f'Artiste with ID {id} deleted')

        elif choice == '5':
            id = int(input('Enter artiste ID: '))
            artiste = Artiste()
            artiste_data = artiste.get_by_id(id)
            if artiste_data:
                songs = artiste.get_songs(id)
                print(f'Songs by {artiste_data[1]}:')
                for song_data in songs:
                    print(f"ID: {song_data[0]}, Title: {song_data[1]}")
            else:
                print(f'Artiste with ID {id} not found')

        elif choice == '6':
            break

        else:
            print('Invalid choice')

def song_menu():
    while True:
        print('\nSong Menu')
        print('1. Create Song')
        print('2. View All Songs')
        print('3. Find Song by ID')
        print('4. Delete Song')
        print('5. Return to Main Menu')
        choice = input('Enter your choice: ')

        if choice == '1':
            title = input('Enter song title: ')
            artiste_id = int(input('Enter artiste ID: '))
            song = Song()
            song.create(title, artiste_id)
            print(f'Song created with title: {title}')

        elif choice == '2':
            song = Song()
            songs = song.get_all()
            for song_data in songs:
                print(f"ID: {song_data[0]}, Title: {song_data[1]}, Artiste ID: {song_data[2]}")

        elif choice == '3':
            id = int(input('Enter song ID: '))
            song = Song()
            song_data = song.get_by_id(id)
            if song_data:
                print(f"ID: {song_data[0]}, Title: {song_data[1]}, Artiste ID: {song_data[2]}")
            else:
                print(f'Song with ID {id} not found')

        elif choice == '4':
            id = int(input('Enter song ID: '))
            song = Song()
            song.delete(id)
            print(f'Song with ID {id} deleted')

        elif choice == '5':
            break

        else:
            print('Invalid choice')

def main():
    while True:
        choice = main_menu()

        if choice == '1':
            artiste_menu()

        elif choice == '2':
            song_menu()

        elif choice == '3':
            print('Goodbye!')
            break

        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()