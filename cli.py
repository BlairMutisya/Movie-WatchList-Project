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
    
    def run(self):
        """Run the CLI application."""
        while True:
            self.display_menu()
            choice = click.prompt("Enter your choice", type=int)

            if choice == 1:
                self.initialize_database()
            elif choice == 2:
                if self.check_initialization():
                    self.movie_management()
            elif choice == 3:
                if self.check_initialization():
                    self.review_management()
            elif choice == 4:
                if self.check_initialization():
                    self.category_management()
            elif choice == 5:
                click.echo("Exiting...")
                break
            else:
                click.echo("Invalid choice. Please try again.")
