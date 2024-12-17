import os
import subprocess


VENV_NAME = os.environ.get('VENV_NAME')
GUNICORN_SERVICE = os.environ.get('GUNICORN_SERVICE')


if not VENV_NAME or not GUNICORN_SERVICE:
    print("Error: VENV_NAME or GUNICORN_SERVICE environment variable is not set.")
    exit(1)

try:
    subprocess.run('git pull origin main', shell=True, check=True)
    subprocess.run(f'source {VENV_NAME}/bin/activate && pip install -r requirements.txt', shell=True, executable='/bin/bash', check=True)
    subprocess.run(f'source {VENV_NAME}/bin/activate && python manage.py migrate', shell=True, executable='/bin/bash', check=True)
    subprocess.run(f'source {VENV_NAME}/bin/activate && python manage.py collectstatic --noinput', shell=True, executable='/bin/bash', check=True)
    subprocess.run(["sudo", "systemctl", "restart", GUNICORN_SERVICE], check=True)
    print("Done!")
except Exception as ex:
    print(ex)