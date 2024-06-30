import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Josaa_project.settings')
django.setup()

from analysis.load_data import load_data

load_data()
