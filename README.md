# KHU Blog Django Assignment

Chapter 14 assignment: `HTML 시작하기 - 맞춤형 템플릿 만들기`.

## Local Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## PythonAnywhere

After pushing this folder to GitHub, use a PythonAnywhere Bash console:

```bash
git clone https://github.com/<your-github-username>/<your-repo-name>.git
cd <your-repo-name>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

In the PythonAnywhere Web tab:

1. Create a manual web app.
2. Set the virtualenv path to `/home/<your-pythonanywhere-username>/<your-repo-name>/venv`.
3. Replace the WSGI file contents with:

```python
import os
import sys

path = '/home/<your-pythonanywhere-username>/<your-repo-name>'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())
```

Your submission URL will be:

```text
https://<your-pythonanywhere-username>.pythonanywhere.com/
```
