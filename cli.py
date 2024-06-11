import click 
from helpers import SessionLocal, Movie, Review, Category
from models import Base 
from sqlalchemy.exc import OperationalError

class MovieWatchlistCLI:
    def __init__(self):
        self.session = SessionLocal()
        self.database_initialized = False

    def display_menu(self):
        """Display the main menu."""
        click.echo("1. Initialize Database")
        click.echo("2. Movie Management")
        click.echo("3. Review Management")
        click.echo("4. Category Management")
        click.echo("5. Exit")
    
    