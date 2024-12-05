## **4. Explore the Value Add of DRF**

**Objective:** Highlight the productivity benefits of Django REST Framework (DRF).

**Teacher Notes:**

- Install DRF and discuss its purpose.
- Compare a simple DRF-based view to the custom view built earlier.

**Code Example:**
Install DRF:

```bash
pip install djangorestframework
```

`api/views.py`

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def drf_view(request):
    if request.method == 'GET':
        return Response({"message": "Hello from DRF!"})
    elif request.method == 'POST':
        return Response({"data": request.data})
```

Update `urls.py`:

```python
urlpatterns += [
    path('api/drf-view/', drf_view),
]
```

**Test Endpoint:**

- Test `GET` and `POST` requests via Postman.
