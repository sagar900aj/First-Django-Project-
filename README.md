# Sagar_portfolio (Django)

A small Django portfolio project (personal site) with a `home_page` app. This repository demonstrates a typical Django project structure with templates and static files split correctly.

## What this project contains

- Django project: `Sagar_portfolio/`
- App: `home_page/`
- SQLite database: `db.sqlite3`
- Virtual environment: `env/` 

The app provides these pages (mapped in `home_page/urls.py`): home, about, contact, gallery, and a sample `blog_users` view.

## Why this README

This file explains how to run the project locally, where templates and static files live, and best practices for adding CSS/JS.

---

## Quick setup (Windows / PowerShell)

Open PowerShell and run the following commands from the repository root (`C:\Django\Sagar_portfolio`):

```powershell
# Change to project directory
cd C:\Django\Sagar_portfolio

# Activate the project's virtual environment (PowerShell)
..\env\Scripts\Activate.ps1

# Optional: install dependencies if you have a requirements.txt
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Notes:
- If `Activate.ps1` fails due to PowerShell execution policy, you can run PowerShell as Administrator and allow script execution, or use the `Activate.bat` file from Command Prompt: `..\env\Scripts\activate.bat`.
- In development (DEBUG=True) Django's `runserver` will serve app static files automatically.

### Collect static files (for production)

If you deploy or want to collect static files into a single folder:

```powershell
# Ensure STATIC_ROOT is set in settings.py (example: BASE_DIR / 'staticfiles')
python manage.py collectstatic --noinput
```

---

## Project structure (important parts)

Recommended structure for templates and static assets in this app (`home_page`):

```
home_page/
  templates/
    base.html              # shared site layout (nav, footer, css/js includes)
    home/
      home.html            # page-specific template
      about_me.html
      contact_me.html
      gallery.html
  static/
    home/
      css/
        style.css
      js/
        main.js
```

Why this layout?
- Put HTML templates in `templates/` (Django's template loader finds them).
- Put CSS/JS in `static/` (Django collects and serves these; templates should NOT contain CSS/JS files).
- Use `{% load static %}` and `{% static 'home/css/style.css' %}` in templates to reference static files.

Example in `base.html` header:

```django
{% load static %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="{% static 'home/css/style.css' %}">
```

And at the bottom of `base.html`:

```django
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="{% static 'home/js/main.js' %}"></script>
```

---

## Views: how to render templates

Prefer `render()` for simplicity and context passing. Example in `home_page/views.py`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')
```

If you namespace templates under `home/`, reference them with that path (as above). If you place `home.html` directly under `templates/` (not recommended), you would use `'home.html'`.

---

## Settings notes (`Sagar_portfolio/settings.py`)

Recommended static settings (you already have `STATIC_URL`):

```python
STATIC_URL = 'static/'
# Optional during development if you want a central project static dir
# STATICFILES_DIRS = [ BASE_DIR / 'static' ]
# For production (collectstatic):
# STATIC_ROOT = BASE_DIR / 'staticfiles'
```

Keep `DEBUG = True` while developing.

---

## Common issues & troubleshooting

- "Templates not found": Make sure `APP_DIRS=True` is set in `TEMPLATES` (it is) and templates live under `home_page/templates/`.
- "Static files not loading": Ensure you used `{% load static %}` and pointed to the correct path (e.g. `home/css/style.css`). In production, run `collectstatic` and serve `STATIC_ROOT`.
- "Django not found" when running manage.py: Activate the virtual environment before running commands.

---

## Contributing / Next steps

- Add or edit templates in `home_page/templates/home/`.
- Add CSS/JS to `home_page/static/home/css/` and `home_page/static/home/js/`.
- If you add new Python deps, update `requirements.txt` with `pip freeze > requirements.txt` while the virtualenv is active.

---


If you want me to also generate or update `base.html`, `home/home.html`, or the static files (`style.css`, `main.js`), tell me which files to create or overwrite and I'll add them.
