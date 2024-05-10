from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Artiste, Song

engine = create_engine('sqlite:///music.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    print('Welcome to the Music CLI!')
    print('1. Artiste Menu')
    print('2. Song Menu')
    print('3. Exit')
    choice = input('Enter your choice: ')
    return choice

def artiste_menu(session):
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
            try:
                artiste = Artiste.create(session, name)
                print(f'Artiste created: {artiste}')
            except ValueError as e:
                print(f'Error: {e}')

        elif choice == '2':
            artistes = Artiste.get_all(session)
            for artiste in artistes:
                print(artiste)

        elif choice == '3':
            id = int(input('Enter artiste ID: '))
            artiste = Artiste.get_by_id(session, id)
            if artiste:
                print(artiste)
            else:
                print(f'Artiste with ID {id} not found')

        elif choice == '4':
            id = int(input('Enter artiste ID: '))
            Artiste.delete(session, id)
            print(f'Artiste with ID {id} deleted')

        elif choice == '5':
            id = int(input('Enter artiste ID: '))
            artiste = Artiste.get_by_id(session, id)
            if artiste:
                print(f'Songs by {artiste.name}:')
                for song in artiste.songs:
                    print(song)
            else:
                print(f'Artiste with ID {id} not found')

        elif choice == '6':
            break

        else:
            print('Invalid choice')

def song_menu(session):
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
            try:
                song = Song.create(session, title, artiste_id)
                print(f'Song created: {song}')
            except ValueError as e:
                print(f'Error: {e}')

        elif choice == '2':
            songs = Song.get_all(session)
            for song in songs:
                print(song)

        elif choice == '3':
            id = int(input('Enter song ID: '))
            song = Song.get_by_id(session, id)
            if song:
                print(song)
            else:
                print(f'Song with ID {id} not found')

        elif choice == '4':
            id = int(input('Enter song ID: '))
            Song.delete(session, id)
            print(f'Song with ID {id} deleted')

        elif choice == '5':
            break

        else:
            print('Invalid choice')

def main():
    session = Session()

    while True:
        choice = main_menu()

        if choice == '1':
            artiste_menu(session)

        elif choice == '2':
            song_menu(session)

        elif choice == '3':
            print('Goodbye!')
            break

        else:
            print('Invalid choice')

    session.close()

if __name__ == '__main__':
    main()