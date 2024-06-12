# Movie Watchlist Project

The Movie Watchlist Project is a command-line application designed to help users manage their list of movies. With this tool, you can add movies to your watchlist, categorize them, review them, and update their watch status.

## Features

- **Movie Management**: Add, list, update, and delete movies from your watchlist.
- **Category Management**: Organize movies into different categories.
- **Review Management**: Add and view reviews for movies.
- **Database Initialization**: Easily set up the database with required tables.

## Project Structure
```
Movie-Watchlist-Project/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    ├── init_db.py
    ├── main.py
    ├── cli.py
    └── helpers.py
```

### Files Description

- **Pipfile**: Lists project dependencies.
- **Pipfile.lock**: Locks the versions of dependencies.
- **README.md**: Project documentation.
- **lib/**: Contains the source code.
  - **models/**: Directory for ORM models (contains `__init__.py` for package initialization).
  - **init_db.py**: Script to initialize the database schema.
  - **main.py**: The main entry point for the CLI application.
  - **cli.py**: The core CLI application logic.
  - **helpers.py**: Helper functions for database operations and other utilities.

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/Movie-Watchlist-Project.git
cd Movie-Watchlist-CLI
```
### 2. Install Pipenv
If you don't have Pipenv installed, you can install it using pip:
```
pip install pipenv
```
### 3. Install Project Dependencies
Navigate to the project directory and use Pipenv to install the required dependencies:
```
pipenv install
```
### 4. Activate the Virtual Environment
Activate the Pipenv virtual environment with:
```
pipenv shell
```
### 5. Initialize the Database
Run the lib/init_db.py script to set up the database:
```
python lib/init_db.py
```
## Usage
After setting up, you can use the CLI to manage your movie watchlist.
### Running the CLI
```
python lib/cli.py
```
### Main Menu Options

1. **Initialize Database**: Set up the database schema.
2. **Movie Management**: Access the movie management menu.
3. **Review Management**: Manage movie reviews.
4. **Category Management**: Manage categories for organizing movies.
5. **Exit**: Exit the CLI application.

### Movie Management Options

- **Add a new movie to the watchlist**: Input the title, director, genre, and optionally, a category ID.
- **Delete a movie from the watchlist by ID**: Remove a movie by its ID.
- **List all movies in the watchlist**: Display all movies in your watchlist.
- **Show details for a specific movie by ID**: View detailed information about a specific movie.
- **List all movies in a specific category**: Show all movies in a chosen category.
- **Mark a movie as watched**: Update a movie's status to "watched".
- **Mark a movie as not watched**: Update a movie's status to "not watched".
- **Return to main menu**: Go back to the main menu.

### Review Management Options

- **Add a review for a movie**: Enter review details for a specific movie.
- **View reviews for a movie**: Display all reviews for a specified movie.
- **Return to main menu**: Go back to the main menu.

### Category Management Options

- **List all categories**: Display all categories used for organizing movies.
- **Return to main menu**: Go back to the main menu.
### Additional Commands

- **To Install a New Dependency**:
  
```
  pipenv install <package-name>
```
### Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.
