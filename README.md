# TaskMate.ai - AI-Powered Task Management System

## Overview

TaskMate.ai is an AI-driven task management system that helps users generate concise code-related solutions for tasks using AI models. This platform integrates Google Gemini AI to provide efficient, 5-point solutions, making task management faster and more productive.
## Project Demo

[![TaskMate.ai Demo](https://www.loom.com/share/50dab6879ec14e76874fb79684474c5e?sid=6c51a16f-bbef-4807-ad9c-ca71aa255fa6)

*Click the image to watch the demo.*
## Features

- **User Authentication**: Secure login and registration system.
- **Task Management**: Users can create, update, and delete tasks.
- **AI-Powered Solutions**: Automatically generates concise solutions (in 5 bullet points) for tasks related to coding using Google Gemini AI.
- **Task Status Tracking**: Track tasks with a status indicator (Pending or Completed).
- **Task Assignment**: Each task is assigned to an authenticated user (optional).
- **REST API**: Full task management and AI response features are exposed via REST API using Django Rest Framework.

## Tech Stack

- **Backend**: Django, Django Rest Framework
- **AI Integration**: Google Gemini AI API (gemini-1.5-flash)
- **Database**: SQLite
- **Frontend**: Angular (Optional if you're building a frontend)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- Google Gemini AI API access
- SQLite (default with Django)
- Postman (for API testing)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/saurabh-giri/taskmate-ai.git
    cd taskmate-ai
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # For Windows: myenv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the project root directory and add your Google Gemini API key:

    ```bash
    GEMINI_API_KEY=your_google_gemini_api_key
    ```

5. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the server**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- `/api/auth/login/` - User login
- `/api/auth/register/` - User registration

### Tasks

- `/api/tasks/` - List all tasks (GET), Create new task (POST)
- `/api/tasks/<id>/` - Retrieve, Update, or Delete a task (GET, PUT, DELETE)

### AI Response

- Automatically generated after task creation.

## AI Integration

Upon task creation, TaskMate.ai communicates with Google Gemini AI to generate a concise solution in 5 bullet points. These points are stored and linked to the task in the database.

