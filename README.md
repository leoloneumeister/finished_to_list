# Setup

1. Clone the repository

```bash
git clone https://github.com/leoloneumeister/finished_to_list
```

2. Go into directory

```bash
cd finished_to_list
```

3. Create venv

```bash
python -m venv venv
```

4. Activate venv

macos:
```bash
source venv/bin/acitve
```

windows:
```bash
source venv\Scripts\activate
```

5. install requirements

```bash
pip install -r requirements.txt
```

6. Create .env file and enter secrets

```bash
echo 'DATABASE_URL=sqlite:///database.db
FLASK_APP=run.py
FLASK_DEBUG=True' > .env
```

7. Run locally

Macos/linux
```bash
gunicorn run:app
```

windows
```bash
python run.py
```

8. Open on port:

http://localhost:8000
