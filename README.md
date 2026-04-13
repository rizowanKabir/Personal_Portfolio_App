# Portfolio v2

A personal portfolio website built with **Django**, featuring dynamic content management through the Django admin panel. The site includes sections for skills, services, portfolio projects, work experience, education, and a contact form.

---

## Features

- **Home** — Overview with featured projects, skills, and services
- **About** — Work experience and education timeline
- **Skills** — Skills grouped by category (Languages, Frameworks, Databases, etc.)
- **Services** — Services offered with icons and descriptions
- **Portfolio** — Project showcase with technology tags and GitHub/live links
- **Contact** — Contact form with message storage in the database

---

## Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Django 4.2              |
| Frontend  | HTML, CSS (custom), Font Awesome |
| Database  | SQLite (default)        |
| Images    | Pillow                  |

---

## Project Structure

```
portfolio_v2/
├── portfolio_project/       # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/               # Main app
│   ├── models.py            # Skill, Service, Portfolio, Experience, Education, Contact
│   ├── views.py             # View functions for each page
│   ├── urls.py              # App URL routing
│   ├── forms.py             # Contact form
│   ├── admin.py             # Admin panel config
│   └── management/
│       └── commands/
│           └── seed_data.py # Command to populate sample data
├── templates/               # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── skills.html
│   ├── services.html
│   ├── portfolio.html
│   └── contact.html
├── static/
│   └── css/
│       └── style.css
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/portfolio_v2.git
   cd portfolio_v2
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Seed sample data** *(optional)*

   ```bash
   python manage.py seed_data
   ```

6. **Create a superuser** (for admin access)

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. Open your browser and go to `http://127.0.0.1:8000/`

---

## Admin Panel

Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials to manage all content — projects, skills, services, experience, education, and contact messages.

---

## Environment & Security Notes

> ⚠️ Before deploying to production, make sure to:

- Replace the `SECRET_KEY` in `settings.py` with a secure random key
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS` with your actual domain
- Configure a production-ready database (e.g., PostgreSQL)
- Set up proper static file serving (e.g., WhiteNoise or a CDN)

---

## Models Overview

| Model       | Description                                      |
|-------------|--------------------------------------------------|
| `Skill`     | Technical skills grouped by category             |
| `Service`   | Services offered with icon and description       |
| `Portfolio` | Projects with tech stack, GitHub and live URLs   |
| `Experience`| Work history with company, role, and bullet points |
| `Education` | Academic background with institution and CGPA    |
| `Contact`   | Messages submitted through the contact form      |

---


