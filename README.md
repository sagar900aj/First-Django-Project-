# Sagar's Portfolio (Django)

A personal portfolio website built with Django, featuring home, about, contact, and gallery pages.

## What's included

- Personal portfolio website with multiple pages
- Built using Django web framework
- Includes templates and static files for styling

## How to run this project

### Step 1: Clone the repository

```powershell
# Using HTTPS (easiest method)
git clone https://github.com/sagar900aj/Django.git
cd Django\Sagar_portfolio
```

### Step 2: Set up Python environment

```powershell
# Create virtual environment
python -m venv env

# Activate virtual environment (PowerShell)
..\env\Scripts\Activate.ps1
# OR for Command Prompt use:
# ..\env\Scripts\activate.bat

# Install required packages
pip install -r requirements.txt
```

### Step 3: Start the website

```powershell
# Set up database
python manage.py migrate

# Run development server
python manage.py runserver
```

### Step 4: View the website

Open your browser and go to: http://127.0.0.1:8000/

## Project structure

```
Sagar_portfolio/       # Main project folder
├── home_page/        # Main app
│   ├── templates/    # HTML templates
│   └── static/       # CSS, JavaScript, images
└── manage.py         # Django management script
```

## Troubleshooting

- If `Activate.ps1` fails, try using Command Prompt with: `..\env\Scripts\activate.bat`
- Make sure Python and Git are installed on your computer
- Virtual environment must be activated before running any `python manage.py` commands
