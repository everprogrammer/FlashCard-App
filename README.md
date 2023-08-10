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
git clone https://github.com/your-username/flashcard-app.git
```

Create a Virtual Environment
Navigate to the project directory and create a virtual environment:

cd flashcard-app
python -m venv venv


Install Dependencies
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
Usage
Running the Application
Activate your virtual environment if it's not already activated:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Navigate to the project directory containing the manage.py file and run the development server:

bash
Copy code
python manage.py runserver
Access the app in your web browser at http://127.0.0.1:8000/.

Features
All Cards Page
The "All Cards" page displays a list of all flashcards available in the app.

Learning Session
The learning session employs spaced repetition to review cards at specific intervals: today, 3 days after the previous revision, 7 days after the last revision, 14 days, and 30 days. Mark a card as remembered or forgotten to adjust its deck.

Completed Words
Access the "Completed Words" page to see words that have reached the 6th deck, signifying their completion. You can also reset a word's progress to the first deck.

Fast Search
Utilize the search button to quickly find specific flashcards based on keywords or definitions.

Contributing
Contributions are welcome! To contribute to the Flashcard App, follow these steps:

Fork the repository.
Create a new branch.
Make your changes and commit them.
Push the changes to your fork.
Create a pull request detailing your changes.
License
This project is licensed under the MIT License.