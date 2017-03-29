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
4. Utworzenie apliacji __notes__
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