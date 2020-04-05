import codecs
import os, sys

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, City, Language, Error

User = get_user_model()

parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D0%B5%D0%B2&category=Python'),
    (djinni, 'https://djinni.co/jobs/?location=%D0%9A%D0%B8%D0%B5%D0%B2&primary_keyword=Python'),
    (rabota, 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2')
)


def get_settings():
    qs = User.objects.filter(send_email=True).values()
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst

q = get_settings()

city = City.objects.filter(slug='kiev').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass
if errors:
    er = Error(data=errors).save()

# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()
