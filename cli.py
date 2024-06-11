import click 
from helpers import SessionLocal, Movie, Review, Category
from models import Base 
from sqlalchemy.exc import OperationalError

class MovieWatchlistCLI:
    def __init__(self):
        self.session = SessionLocal()
        self.database_initialized = False