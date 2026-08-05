# How To Run

## 1. Open this project folder

Open a terminal in the project folder.

If you are not already inside the project folder, use `cd` to move into it:

```powershell
cd path\to\background-remover
```

## 2. Create a virtual environment

```powershell
python -m venv .venv
```

## 3. Activate it

```powershell
.venv\Scripts\activate
```

## 4. Install the required packages

```powershell
pip install -r requirements.txt
```

This installs:

- Flask
- rembg with CPU support
- Pillow

The `rembg` package may also install extra dependencies like `onnxruntime`.

If you already installed the packages before this file was updated, run this once:

```powershell
pip install --upgrade -r requirements.txt
```

## 5. Start the app

```powershell
python app.py
```

## 6. Open it in your browser

Go to:

```text
http://127.0.0.1:5000
```
