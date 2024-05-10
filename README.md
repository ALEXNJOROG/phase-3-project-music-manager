# phase-3-project-music-manager - Alex Njoroge

### PROJECT DESCRIPTION
Music Manager is a program that enables the user to organize a list of their favorite music on the basis of the artists and the particular songs.
The program's features facilitate creation of new enitites as well as deletion of unwanted already existing entities.

The Artiste class represents an artist, and the Song class represents a song, with a one-to-many relationship between them (one artist can have multiple songs).

The models.py file defines the Artiste and Song model classes, including property methods to validate the data, and ORM methods for creating, getting, and deleting objects.

The app.py file contains the CLI logic, with the menus updated to reflect the Artiste and Song models.

Running the app.py file will create the database file music.db (if it doesn't exist) and user can interact with the application through the CLI menus to manage artists and songs.


### EXAMPLE USAGE
