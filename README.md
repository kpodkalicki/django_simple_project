1. Utworzenie bazy danych
```bash
python manage.py migrate
```
2. Utworzenie administratora
```bash
python manage.py createsuperuser
```
3. Uruchomienie aplikacji
```bash
python runserver 
```
4. Utworzenie aplikacji __notes__
```bash
python manage.py startapp notes
```
5. Instalacja aplikacji __notes__ 

6. Model __Note__ oraz migracja bazy danych
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Dodanie modelu __Note__ do panelu admnistratora

8. ListView na podstawie [http://misztal.edu.pl/logs/listview-w-django/](http://misztal.edu.pl/logs/listview-w-django/)

9. DetailView na podstawie [http://misztal.edu.pl/logs/detailview-w-django/](http://misztal.edu.pl/logs/detailview-w-django/)

10. Korzystając z [https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/) przygotuj odpowiednie widoki umożliwiające dodawanie, aktualizację i usuwanie notatek.
 
11. [Dodaj użytkownika](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/#models-and-request-user) - autora notatki - do modelu __Note__. Pamietaj o [migracji bazy danych](https://docs.djangoproject.com/en/1.10/topics/migrations/).
 
12. Zatroszcz się, aby tylko [zalogowany użytkownik](https://docs.djangoproject.com/en/1.10/topics/auth/default/#django.contrib.auth.decorators.login_required) mógł dodawać notatki. Zapewnij aby w momencie tworzenia notatki użytkowniek wypełniany był [automatycznie](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/#models-and-request-user).