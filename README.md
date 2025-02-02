# BharatFD
# Creative FAQ Management API

A Django-based multilingual FAQ system with dynamic translation,
WYSIWYG rich text support, and caching via Redis.

## Features
- **Dynamic Translation:** Auto-translate FAQs into multiple languages.
- **Rich Text Answers:** Powered by django-ckeditor.
- **REST API:** Query FAQs with a language selector (`?lang=`).
- **Caching:** Redis caching for fast API responses.
- **Optional Asynchronous Translation:** (Powered by Celery)
- **Admin Panel:** User-friendly interface for FAQ management.
- **Unit Tested:** Using Django’s test framework.

## Installation

1. **Clone the repository:**
   git clone <repository-url>
   cd creative_faq
2. Create and activate a virtual environment:
python -m venv env
source env/bin/activate

3.Install dependencies:
pip install -r requirements.txt

4.Run migrations:
python manage.py migrate

5.Run the development server:
python manage.py runserver

6.(Optional) Start Celery worker:
celery -A creative_faq worker --loglevel=info

7.Admin Panel
Create a superuser:
python manage.py createsuperuser
Access: http://127.0.0.1:8000/admin/
