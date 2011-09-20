import os

#DEBUG
#=====
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

#TODO : Installation script should ask the timezone
TIME_ZONE = 'Europe/Madrid'

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2','postgresql','mysql','sqlite3','oracle'
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': APPLICATION_DIR + '/test.db',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
                                         # Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default.
                                         # Not used with sqlite3.
    }
}
