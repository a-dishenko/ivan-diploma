"""
WSGI config for mck_samolet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# -*- coding: utf-8 -*-

import os
import sys
import platform

#activate_this = os.path.expanduser('~/venv/bin/activate_this.py')
#exec(open(activate_this).read(), {'__file__': activate_this})


from django.core.wsgi import get_wsgi_application

# путь к проекту
sys.path.insert(0, '/home/c/ch82151/django_kxnx4/public_html')
# путь к фреймворку
sys.path.insert(0, '/home/c/ch82151/django_kxnx4/public_html/mck_samolet')
# путь к виртуальному окружению
python_version = ".".join(platform.python_version_tuple()[:2])
sys.path.insert(0, '/home/c/ch82151/django_kxnx4//django/lib/python{0}/site-packages'.format(python_version))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mck_samolet.settings')

application = get_wsgi_application()
