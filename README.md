# MUSIC MANAGER - Alex Njoroge

## PROJECT DESCRIPTION
Music Manager is a program that enables the user to organize a list of their favorite music on the basis of the artists and their particular songs.
The program's features facilitate creation of new enitites as well as deletion of unwanted already existing entities.

This application uses a custom ORM to interact with a SQLite database. It defines two model classes, Artiste and Song, with a one-to-many relationship between them (one artist can have multiple songs).

The Database class is a context manager that handles the connection to the SQLite database. It provides methods to execute SQL queries and fetch results.

The Model class is a base class that defines common CRUD operations for models. It uses the Database class to interact with the database.

The Artiste and Song classes inherit from the Model class and define their respective table names and additional methods.

The app.py file contains the CLI logic, with the menus updated to reflect the Artiste and Song models.
Running the app.py file, it will create the database file music.db (if it doesn't exist) and user can interact with the application through the CLI menus to manage artists and songs.


## PROJECT SETUP
1. Fork and Clone this repository to a local environment.
2. To install required dependancies run : pipenv install
3. To use the shell rurn : pipenv shell



## FEATURES
1. Create an artist and update the music database.
2. Create a song and update the music database.
3. Get all the artists and songs in the music database.
4. Get specific artist and song by id.


## EXAMPLE USAGE
### Creating an artist
artiste1 = Artiste.create(session, 'Santan Dave')
print(artiste1) 

### Creating a song
song1 = Song.create(session, 'Professor X', artiste1.id)

### Getting all artists
artistes = Artiste.get_all(session)
print('All Artistes:')
for artiste in artistes:
    print(artiste)

### Getting all songs
songs = Song.get_all(session)
print('\nAll Songs:')
for song in songs:
    print(song)

### Getting an artiste by ID
artiste = Artiste.get_by_id(session, 1)
print(f'\nArtiste with ID 1: {artiste}')

### Getting songs by an artiste
print(f'\nSongs by {artiste.name}:')
for song in artiste.songs:
    print(song)

### Delete a song
Song.delete(session, song1.id)
print(f'Deleted song with ID {song1.id}')


## CONTRIBUTORS
1. Alex Njoroge.

