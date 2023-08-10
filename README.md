# Flashcard App

The Flashcard App is a Django-based application designed to help users learn and review vocabulary effectively using spaced repetition techniques.

## Table of Contents

- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
- [Features](#features)
  - [All Cards Page](#all-cards-page)
  - [Learning Session](#learning-session)
  - [Completed Words](#completed-words)
  - [Fast Search](#fast-search)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to get the Flashcard App up and running on your local machine.

### Clone the Repository

Clone the repository using Git:

```bash
https://github.com/everprogrammer/FlashCard-App.git
```

### Create a Virtual Environment

Create a Virtual Environment
Navigate to the project directory and create a virtual environment:

```bash
cd flashcard-app
python -m venv venv
```

### Install Dependencies

Install Dependencies
Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
On macOS and Linux:
```
On macOS and Linux:

```bash
source venv/bin/activate
```
Install the required packages using pip

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application
Activate your virtual environment if it's not already activated:

On Windows:

```bash
venv\Scripts\activate
```
On macOS and Linux:

```bash
source venv/bin/activate
```

Navigate to the project directory containing the manage.py file and run the development server:

```bash
python manage.py runserver
Access the app in your web browser at http://127.0.0.1:8000/.
```

## Features

First You must create decks of cards from 1 to 6 in order, using the admin panel. Then you can continue using the application.
```bash
localhost:8000/admin
username: admin
password:admin
```

### All Cards Page
The "All Cards" page displays a list of all flashcards available in the app.

### Learning Session
The learning session employs spaced repetition to review cards at specific intervals: today/ tomorrow, 3 days after first revision, 7, 14 days, and 30 days after the last revision. Mark a card as I know this word or I do not know this word to move the card between the decks. If a card is remembered it moves to next deck if not it goes back to deck number one regardless of current deck it sits in. There are 6 decks available.

### Completed Words
Access the "Completed Words" page to see words that have reached the 6th deck, signifying their completion. You can also reset a word's deck to the first if the meaning is forgotten. Revision for words at 6th deck is after one year from previous revision. 

### Fast Search
Utilize the search button to quickly find specific flashcards based on keywords or definitions.

## Contributing
Contributions are welcome! To contribute to the Flashcard App, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push the changes to your fork.
5. Create a pull request detailing your changes.

## License
This project is licensed under the MIT License.
