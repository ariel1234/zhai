import os
if(not os.system("py manage.py runserver --settings=debug.settings")):
    os.system("python manage.py runserver --settings=debug.settings")
