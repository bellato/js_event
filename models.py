import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, mapper


engine = create_engine('sqlite:///js_event.db', echo=False)

metadata = MetaData()
event_table = Table('events', metadata,
                    Column('id_event', Integer, primary_key=True),
                    Column('date', String),
                    Column('title', String),
                    Column('link', String))

metadata.create_all(engine)


class Event:
    def __init__(self, date, title, link):
        self.date = date
        self.title = title
        self.link = link

    def __repr__(self):
        return "<Event('%s','%s', '%s')>" % (self.date, self.title, self.link)


if __name__ == '__main__':
    conn = sqlite3.connect("js_event.db")
    cursor = conn.cursor()

    cursor.execute('create table if not exists events(id_event integer primary key unique, '
                   'event_link text, title text, date text)')
