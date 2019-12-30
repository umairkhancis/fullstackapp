# fullstackapp
Full stack app in python django-rest-framework and react js.

## Services
- Django App - For APIs and displaying some pages.
- React App - For LPV and DPV.
- MySQL database - For persistent storage.
- Redis - In memory database, for storing and reading the count of user visits to home page.
- Redis Banner - Visualization for redis.

## Run in docker
```python
$ docker-compose up --build
```

## Urls
- [Django Template based LPV Page](http://localhost:8000/movie/lpv/)
- [Api to get all articles](http://localhost:8000/api/movie/article/)
- [Api to get sepecific article](http://localhost:8000/api/movie/article/1)
- [React based LPV page](http://localhost:3000/)
- [React based DPV page](http://localhost:3000/1)
