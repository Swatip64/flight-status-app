# Real-Time Flight Status and Notifications System

A full-stack application providing real-time flight status updates and notifications to passengers. The system includes features for tracking flight delays, cancellations, gate changes, and more. It integrates with airport systems, sends notifications via SMS, email, or app notifications, and has a user-friendly interface.

## Features

- **Real-time Flight Updates:** Displays current flight status including delays, cancellations, gate changes, arrival time, and boarding time.
- **Push Notifications:** Sends notifications for flight status changes via SMS, email, or app notifications using Firebase Cloud Messaging and RabbitMQ.
- **Integration with Airport Systems:** Fetches accurate flight data from airport databases.
- **Interactive UI:** Provides an attractive and user-friendly interface with animations and responsive design.

## Technologies Used

- **Frontend:** HTML, CSS, React.js
- **Backend:** Python (Flask)
- **Database:** PostgreSQL
- **Notifications:** Firebase Cloud Messaging, RabbitMQ

## Setup and Installation

### Prerequisites

- Node.js
- Python
- PostgreSQL
- Firebase account
- RabbitMQ server

### Frontend Setup

1. Navigate to the `frontend` directory:
    cd frontend

2. Install the required npm packages:
    npm install

3. Start the React development server:
     npm start

## Backend Setup

 1. Navigate to the backend directory:
    cd backend

2. Create a virtual environment and activate it:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required Python packages:
   pip install -r requirements.txt

4. Set up the PostgreSQL database and run migrations:
   python manage.py db upgrade

5. Start the Flask server:
    python run.py

## Notifications Setup

  Configure Firebase Cloud Messaging and RabbitMQ as per their respective documentation.

## Usage

> Search Flights: Use the search bar on the homepage to find flights by flight number or airline.
> View Flight Details: Click on a flight to see more details about its status, gate, arrival time, and boarding time.
> Receive Notifications: Set up your notification preferences to receive updates via SMS, email, or app notifications.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

   > Fork the repository.
   > Create a new branch for your changes.
   > Make your changes and test them.
   > Submit a pull request with a clear description of your changes.




1. **Initial Setup:**
  
   git commit -m "Initial commit: Set up project structure with frontend and backend" -m "Created basic project structure with separate frontend and backend directories. Included initial setup files and configuration."

## Add Real-Time Flight Updates:

git commit -m "Add real-time flight status updates" -m "Implemented functionality to fetch and display real-time flight status updates including delays, cancellations, gate changes, arrival time, and boarding time."

## Enhance UI with Animations:

git commit -m "Enhance UI with animations and improved styling" -m "Updated the user interface to include animations for flight status updates. Improved styling for better user experience and visual appeal."

## Integrate Notifications:

git commit -m "Integrate Firebase Cloud Messaging and RabbitMQ for notifications" -m "Set up Firebase Cloud Messaging and RabbitMQ to handle push notifications for flight status changes. Configured notification preferences and tested functionality."

## Fix API Integration Issues:

git commit -m "Fix API integration issues and update flight data handling" -m "Resolved issues with

This is my Presentation link "https://my.visme.co/view/q69d8g1r-untitled-project"
   git clone https://github.com/Swatip64/flight-status-app.git
