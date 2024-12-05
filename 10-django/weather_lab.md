### **Lab: Create an Endpoint That Fetches Weather Data and Returns JSON**

#### **Objective**

Extend the basic "Hello World" API to fetch real-time weather data from a public API (e.g., OpenWeatherMap) and return the data as JSON. This lab helps students practice:

1. Working with external APIs using the `requests` library.
2. Handling query parameters.
3. Returning dynamic JSON responses.

---

### **Lab Steps**

#### **Step 1: Install Required Library**

Install the `requests` library if not already installed:

```bash
pip install requests
```

---

#### **Step 2: Sign Up for OpenWeatherMap**

1. Go to [OpenWeatherMap](https://openweathermap.org/api) and create a free account.
2. Obtain your API key from the dashboard.
   - Example: `YOUR_API_KEY`

---

#### **Step 3: Create the Endpoint**

Update the `api/views.py` file to include a new view that fetches weather data:

```python
import requests
from django.http import JsonResponse

def get_weather(request):
    # Get the city from the query parameters (default to "London")
    city = request.GET.get("city", "London")

    # OpenWeatherMap API URL and your API key
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Fetch weather data from OpenWeatherMap
    response = requests.get(url)

    # Handle API response
    if response.status_code == 200:
        data = response.json()
        # Extract key information
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return JsonResponse(weather)
    else:
        # Handle errors (e.g., invalid city name)
        return JsonResponse({"error": "Unable to fetch weather data"}, status=400)
```

---

#### **Step 4: Add the Route**

Update `myapi/urls.py` to include the new endpoint:

```python
from django.urls import path
from api.views import hello_world, get_weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_world),
    path('api/weather/', get_weather),  # Add the weather endpoint
]
```

---

#### **Step 5: Test the Endpoint**

1. **Access the Default City (London):**
   Open in a browser or Postman:

   ```
   http://127.0.0.1:8000/api/weather/
   ```

   **Response Example:**

   ```json
   {
     "city": "London",
     "temperature": 15.5,
     "description": "clear sky"
   }
   ```

2. **Specify a City Using Query Parameters:**
   Open in a browser or Postman:

   ```
   http://127.0.0.1:8000/api/weather/?city=Paris
   ```

   **Response Example:**

   ```json
   {
     "city": "Paris",
     "temperature": 17.2,
     "description": "few clouds"
   }
   ```

3. **Test Error Handling:**
   Try an invalid city name:
   ```
   http://127.0.0.1:8000/api/weather/?city=InvalidCity
   ```
   **Response Example:**
   ```json
   {
     "error": "Unable to fetch weather data"
   }
   ```

---

### **Extensions**

- **Support Multiple Cities:** Accept a list of cities and return weather data for all.
- **Cache Results:** Use Django’s caching framework to avoid redundant API calls for the same city.
