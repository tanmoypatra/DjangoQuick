# DjangoQuick
Quick Start to django rest framework

# Curl usage:
```
curl -H 'Accept: application/json; indent=4' -u tanmoy:awesome http://127.0.0.1:8000/users/
```
# Httpie usage:
```
http -a tanmoy:awesome --json POST http://127.0.0.1:8000/snippets/ code="print 456"
```

# Delete all migration files
```
rm -f tmp.db db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate

```
# Create SuperUser
```
python manage.py createsuperuser
```


