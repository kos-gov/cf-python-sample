 #!/bin/bash
 
  echo "make migrations"
 python manage.py makemigrations

 echo "migrate"
 python manage.py migrate

 echo [$0] Starting Django Server...
 python manage.py runserver --noreload
