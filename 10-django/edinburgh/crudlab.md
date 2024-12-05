### **Lab: Build a CRUD API for a Custom Resource**

#### **Objective**

Guide participants in creating a CRUD API for a resource of their choice using DRF’s serializers and viewsets. The resource could be anything relevant, such as `Movie`, `Product`, or `Task`.

---

### **Lab Steps**

#### **Step 1: Define Your Model**

1. **Choose a Resource**:

   - Participants will define a simple model with at least two fields.
   - Example: A `Task` model with `title`, `description`, and `is_completed` fields.

2. **Create the Model in `api/models.py`:**

   ```python
   from django.db import models

   class Task(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       is_completed = models.BooleanField(default=False)

       def __str__(self):
           return self.title
   ```

---

#### **Step 2: Generate and Apply Migrations**

1. Run the following commands to create and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

#### **Step 3: Create the Serializer**

1. Create a `serializers.py` file in the `api` app (if it doesn’t exist).
2. Add the serializer for the `Task` model:

   ```python
   from rest_framework import serializers
   from .models import Task

   class TaskSerializer(serializers.ModelSerializer):
       class Meta:
           model = Task
           fields = '__all__'
   ```

---

#### **Step 4: Create the ViewSet**

1. Add a `TaskViewSet` to `api/views.py`:

   ```python
   from rest_framework.viewsets import ModelViewSet
   from .models import Task
   from .serializers import TaskSerializer

   class TaskViewSet(ModelViewSet):
       queryset = Task.objects.all()
       serializer_class = TaskSerializer
   ```

---

#### **Step 5: Register the ViewSet with a Router**

1. Update `myapi/urls.py` to include the new resource:

   ```python
   from rest_framework.routers import DefaultRouter
   from api.views import TaskViewSet

   router = DefaultRouter()
   router.register('tasks', TaskViewSet)

   urlpatterns += router.urls
   ```

---

#### **Step 6: Test the CRUD API**

1. Use Postman or a similar tool to test the following endpoints:

   - **Create a Task (POST):**

     ```json
     {
       "title": "Complete Django Lab",
       "description": "Work on CRUD API lab",
       "is_completed": false
     }
     ```

   - **List Tasks (GET):**  
     `GET http://127.0.0.1:8000/tasks/`

   - **Retrieve a Task by ID (GET):**  
     `GET http://127.0.0.1:8000/tasks/1/`

   - **Update a Task (PUT):**

     ```json
     {
       "title": "Complete Django Lab",
       "description": "CRUD lab completed successfully",
       "is_completed": true
     }
     ```

   - **Delete a Task (DELETE):**  
     `DELETE http://127.0.0.1:8000/tasks/1/`

---

### **Extensions**

1. **Add Search or Filtering**:

   - Enable filtering tasks by `is_completed` using DRF’s filtering backends.
   - Example:

     ```python
     from rest_framework.filters import SearchFilter

     class TaskViewSet(ModelViewSet):
         queryset = Task.objects.all()
         serializer_class = TaskSerializer
         filter_backends = [SearchFilter]
         search_fields = ['title']
     ```

2. **Implement Pagination**:
   - Add pagination to the `TaskViewSet` by configuring `DEFAULT_PAGINATION_CLASS` in `settings.py`.

---
