# Background Remover

A simple starter project for a website that will remove the background from PNG and JPG images.

## What This Uses

- HTML
- CSS
- Bootstrap 5
- Python
- Flask
- rembg

## How To Run

Open a terminal in this project folder.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

Start the app:

```powershell
python app.py
```

Open this link in your browser:

```text
http://127.0.0.1:5000
```

## How To Stop The App

Go back to the terminal where the app is running and press:

```text
Ctrl + C
```

## Project Files

- `app.py` - Python Flask app
- `templates/index.html` - Upload page
- `static/styles.css` - Custom styles
- `requirements.txt` - Python packages
- `uploads/` - Folder for uploaded images
- `outputs/` - Folder for finished images
