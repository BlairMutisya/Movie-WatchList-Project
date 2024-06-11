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

    def initialize_database(self):
        """Initialize the database by creating all necessary tables."""
        click.echo("Initializing the database...")
        Base.metadata.create_all(self.session.bind)
        self.database_initialized = True
        click.echo("Database initialized successfully.")

    def check_initialization(self):
        """Check if the database is initialized."""
        if self.database_initialized:
            return True
        try:
            # Check if any table exists
            self.session.execute('SELECT 1 FROM movies LIMIT 1')
            self.database_initialized = True
            return True
        except OperationalError:
            click.echo("Database not initialized. Please initialize the database first.")
            return False
    def movie_management_menu(self):
        """Display the movie management menu."""
        click.echo("1. Add a new movie to the watchlist.")
        click.echo("2. Delete a movie from the watchlist by ID.")
        click.echo("3. List all movies in the watchlist.")
        click.echo("4. Show details for a specific movie by ID.")
        click.echo("5. List all movies in a specific category.")
        click.echo("6. Mark a movie as watched.")
        click.echo("7. Mark a movie as not watched.")
        click.echo("8. Return to main menu")
