# KHU Mobweb Django Assignments

Assignments deployed with Django for PythonAnywhere.

- Root page: Chapter 17, `Django 템플릿과 CSS 꾸미기`
- Root page now also includes Chapter 18 image-blog output from pages 6-13.
- `/html5/`: Chapter 16 실습 과제 09, `HTML5 문서 구조와 멀티미디어 태그`
- `submission/ch19_fixed_game.html`: Chapter 19 JavaScript corrected game code.

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
git clone https://github.com/ysbc1247/mobweb.git
cd mobweb
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

In the PythonAnywhere Web tab:

1. Create a manual web app.
2. Set the virtualenv path to `/home/ystc1247/mobweb/venv`.
3. Replace the WSGI file contents with:

```python
import os
import sys

path = '/home/ystc1247/mobweb'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())
```

Chapter 17 submission text:

```text
GitHub URL: https://github.com/ysbc1247/mobweb
PythonAnywhere URL: https://ystc1247.pythonanywhere.com/
Capture image: screenshots/ch17_capture.jpg
```

If the repository is already cloned on PythonAnywhere:

```bash
cd ~/mobweb
git pull
source venv/bin/activate
python manage.py migrate
```

Then reload the web app from the PythonAnywhere Web tab.

```text
https://ystc1247.pythonanywhere.com/
```

## Current Submission Files

```text
submission/ch18_urls.txt
submission/ch18_images/ch18_01_post_list.png
submission/ch18_images/ch18_02_post_detail.png
submission/ch18_images/ch18_03_media_image.png
submission/ch19_fixed_game.html
submission/ch19_images/ch19_game_01_start.png
submission/ch19_images/ch19_game_02_playing.png
submission/ch19_images/ch19_game_03_finished.png
submission/submission_checklist.txt
```
