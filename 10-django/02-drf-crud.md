## **5. Add DRF and Create a CRUD API**

**Objective:** Build a full CRUD API using DRF’s serializers and views.

**Teacher Notes:**

- Define a simple model (e.g., `Book` with fields `title` and `author`).
- Use DRF serializers to map models to JSON.
- Create a `ModelViewSet` for CRUD operations.

**Code Example:**
`api/models.py`

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```


This creates a file which shows the diffs between the database and the code.
```bash
python manage.py makemigations
```

This updates the database to match the code - applying the migrations to the database
```bash
python manage.py migrate
```

`api/serializers.py`

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

`api/views.py`

```python
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

`myapi/urls.py`

```python
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns += router.urls
```

**Test CRUD:**

- Use Postman to test `GET`, `POST`, `PUT`, `DELETE` on `/api/books/`.
