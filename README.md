# Book Store App - Django

## Description

The project has one application `books` that has two models `Author` and `Book` with a relationship one to many (an `Auther` has many `Books`)

The app allows to `add`, `edit` or `delete` `Authors` and `Books`

### The app has four pages:

- Home page that displays the books
- Book details page that displays a book details
- Author details that displays a specific author books
- Book form page that allows to add or edit a book

## Installing

### Clone the project

```sh
git clone https://github.com/AhmedHafez13/ITI-Book-Store-Django.git
```

### Change the directory to the the application directory

```sh
cd ITI-Book-Store-Django
```

### Create a virtual environment `venv`

```sh
python -m venv venv
```

### Activate the virtual environment `venv`

```sh
source venv/Scripts/activate
```

### Install the requirements

```sh
pip install -r requirements.txt
```

### Run the application

```sh
python manage.py runserver
```

Or using git-bash in windows

```sh
winpty python manage.py runserver
```
