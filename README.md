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

13. Korzystają z [Managing static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/1.10/howto/static-files/) dodaj do projektu jego ostylowanie.

14. Wykorzystując klasę bazową [UserPassesTestMixin](https://docs.djangoproject.com/en/1.10/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin) zadbaj o to, aby tylko twórca mógł aktualizować notatkę oraz aby admin i twórca mogli je usuwać.

15. Utwórz model __Topic__, który będzie reprezentował temat notatek. Wykorzystaj modele bazowe TitleSlugDescriptionModel oraz TimeStampedModel  z aplikacji [django-extensions](https://github.com/django-extensions/django-extensions), którą musisz zainstalować.

16. Zmień model __Note__ tak aby dziedziczył po TimeStampedModel  z aplikacji [django-extensions](https://github.com/django-extensions/django-extensions). Pamietaj o migracji bazy danych.
 
17. Utwórz drzewiastą zależność dla tematów wykorzystujac aplikację [django-mptt](https://github.com/django-mptt/django-mptt) (dodatkowo zainstaluj również [django-mptt-admin](https://github.com/mbraak/django-mptt-admin)). Zobacz jak to działa w panelu administratora.

18. Dodaj pole _public_ do modelu Topic. Zadbaj o to, aby była możliwość edycji pola public z poziomu listy w panelu administratora wykorzystując [list_editable](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_editable) w modelu administratora. Uwaga: Aby to zobaczyc trzeba przejść do 'Grid view'.

19. Przenieś model Topic do nowej aplikacji. Dodaj widoki listy, szczegółowy, tworzenia, aktualizacji i usuwania dla modelu Topic. W wydoku szczegółowym wyświetl notaki podpięte do aktualnego tematu. Popraw działanie aplikacji tak, aby możliwie było automatyczne wypełnianie odpowiedniego tematu przy tworzeniu notatki.