# AI Model Response API

## Overview
This project implements a simple Django REST API that allows users to manage and process AI-generated responses using the OpenAI API. It supports creating responses by sending prompts to the AI model, retrieving specific responses, and listing all available responses.

---

## Features
- Create and retrieve AI-generated responses from models like gpt-3.5-turbo.
- Store AI responses in a database with metadata, such as model type, timestamp, and processing time.
- Input validation and error handling.
- Pagination for large response lists.
- Basic caching for efficient response management.

---

## Technologies Used
- Backend Framework: Django, Django REST Framework  
- Database:* SQLite (or PostgreSQL for production)  
- API Integration: OpenAI API  
- Environment Management: Virtualenv  
- Testing: Django Test Framework  

---

## Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/your-username/ai-response-api.git
cd ai-response-api

### 2. Create a Virtual Environment
python3 -m venv env
.\env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Up the OpenAI API Key
#### Open Window cmd :
set OPENAI_API_KEY=your-api-key-here
     
### 5. Run Database Migrations
python manage.py migrate

### 6. Start the Development Server

python manage.py runserver

The API will be accessible at:

http://127.0.0.1:8000



