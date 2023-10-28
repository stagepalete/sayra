
# Sayra


# Deployment
### To set up backend API:

1) Create virtual env for python inside project folder
```Bash
python -m venv venv
```
2) Activate virtual env
```Bash
venv\Scripts\activate
```
3) Install all requirement libs
```Bash
pip install -r requirements.txt
```

### To run backend API:
1) Create postgresql database called sayra

2) Migrate
```Bash
python manage.py makemigrations
python manage.py migrate
```
3) Run
```Bash
python manage.py runserver
```



# Authors
- [@stagepalete](https://www.github.com/stagepalete)
