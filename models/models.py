from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Artiste(Base):
    __tablename__ = 'artistes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    songs = relationship('Song', back_populates='artiste')

    def __repr__(self):
        return f'Artiste(id={self.id}, name="{self.name}")'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Artiste name cannot be blank')
        self._name = value.strip()

    @classmethod
    def create(cls, session, name):
        artiste = cls(name=name)
        session.add(artiste)
        session.commit()
        return artiste

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def delete(cls, session, id):
        artiste = cls.get_by_id(session, id)
        if artiste:
            session.delete(artiste)
            session.commit()

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artiste_id = Column(Integer, ForeignKey('artistes.id'))
    artiste = relationship('Artiste', back_populates='songs')

    def __repr__(self):
        return f'Song(id={self.id}, title="{self.title}", artiste_id={self.artiste_id})'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError('Song title cannot be blank')
        self._title = value.strip()

    @classmethod
    def create(cls, session, title, artiste_id):
        song = cls(title=title, artiste_id=artiste_id)
        session.add(song)
        session.commit()
        return song

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def delete(cls, session, id):
        song = cls.get_by_id(session, id)
        if song:
            session.delete(song)
            session.commit()