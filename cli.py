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

    def movie_management(self):
        """Handle movie management operations."""
        while True:
            self.movie_management_menu()
            choice = click.prompt("Enter your choice", type=int)

            if choice == 1:
                self.add_movie()
            elif choice == 2:
                self.delete_movie()
            elif choice == 3:
                self.list_movies()
            elif choice == 4:
                self.show_movie_details()
            elif choice == 5:
                self.list_movies_by_category()
            elif choice == 6:
                self.mark_movie_watched()
            elif choice == 7:
                self.mark_movie_not_watched()
            elif choice == 8:
                break
            else:
                click.echo("Invalid choice. Please try again.")

    def add_movie(self):
        """Add a new movie to the watchlist."""
        title = click.prompt("Enter the title of the movie")
        director = click.prompt("Enter the director of the movie")
        genre = click.prompt("Enter the genre of the movie")
        category_id = click.prompt("Enter the category ID for the movie (optional)", type=int, default=None)

        movie = Movie.create(self.session, title, director, genre, category_id)
        click.echo(f"Movie added: {movie}")
    def delete_movie(self):
        """Delete a movie from the watchlist by ID."""
        movie_id = click.prompt("Enter the ID of the movie to delete", type=int)
        success = Movie.delete(self.session, movie_id)
        if success:
            click.echo("Movie deleted successfully.")
        else:
            click.echo("Movie not found.")

    def list_movies(self):
        """List all movies in the watchlist with their IDs and watched status."""
        movies = Movie.get_all(self.session)
        if movies:
            click.echo("List of movies in the watchlist:")
            for movie in movies:
                watched_status = "Watched" if movie.watched else "Not Watched"
                click.echo(f"ID: {movie.id}, Title: {movie.title}, Director: {movie.director}, Genre: {movie.genre}, Watched: {watched_status}, Category ID: {movie.category_id}")
        else:
            click.echo("No movies found in the watchlist.")

    def show_movie_details(self):
        """Show details for a specific movie by ID."""