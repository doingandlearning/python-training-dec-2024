### Lab: Managing Users and Permissions with Classes in Python

**Objective:**  
Build a Python class to represent users in a university system. This will involve defining attributes such as usernames, roles, and permissions, and implementing methods to manage user behaviors like granting and revoking permissions.

---

### Scenario:  
You are tasked with developing a Python program to manage user accounts for a university's IT system. Each user has attributes like username, role, and permissions. Your goal is to create a `User` class and implement functionality for managing user behaviors.

---

### Task 1: Define the `User` Class  
1. Create a class named `User`.  
2. Add the following attributes:
   - `username` (e.g., `"john_doe"`)
   - `role` (e.g., `"admin"`, `"student"`, `"faculty"`)
   - `permissions` (a list of strings representing permissions, e.g., `["read", "write"]`)  

3. Include a class docstring describing the purpose of the class.  

#### Example Code:
```python
class User:
    """A class to represent a university user with attributes and permissions."""

    def __init__(self, username, role, permissions=None):
        self.username = username
        self.role = role
        self.permissions = permissions if permissions else []
```

---

### Task 2: Instantiate Objects  
1. Create instances of the `User` class:  
   - A student named `alice` with no initial permissions.  
   - An admin named `admin_user` with `["read", "write", "delete"]` permissions.  

#### Example Code:
```python
# Create user instances
alice = User("alice", "student")
admin_user = User("admin_user", "admin", ["read", "write", "delete"])

# Print user details
print(alice.__dict__)
print(admin_user.__dict__)
```

---

### Task 3: Add Methods to Manage Permissions  
1. Add methods to the `User` class:
   - `grant_permission(permission)` to add a new permission.
   - `revoke_permission(permission)` to remove a permission.  
2. Update the user’s `permissions` attribute accordingly.

#### Example Code:
```python
class User:
    """A class to represent a university user with attributes and permissions."""

    def __init__(self, username, role, permissions=None):
        self.username = username
        self.role = role
        self.permissions = permissions if permissions else []

    def grant_permission(self, permission):
        """Grant a new permission to the user."""
        if permission not in self.permissions:
            self.permissions.append(permission)

    def revoke_permission(self, permission):
        """Revoke a permission from the user."""
        if permission in self.permissions:
            self.permissions.remove(permission)
```

---

### Task 4: Test Permission Management  
1. Grant the `read` permission to `alice`.  
2. Revoke the `delete` permission from `admin_user`.  
3. Print the updated permissions for both users.  

#### Example Code:
```python
# Grant and revoke permissions
alice.grant_permission("read")
print(f"Alice's permissions: {alice.permissions}")

admin_user.revoke_permission("delete")
print(f"Admin's permissions: {admin_user.permissions}")
```

---

### Task 5: Add Role-Specific Behaviors  
1. Add a method `is_admin()` that returns `True` if the user’s role is `admin`.  
2. Add a method `has_permission(permission)` to check if the user has a specific permission.  

#### Example Code:
```python
class User:
    """A class to represent a university user with attributes and permissions."""

    def __init__(self, username, role, permissions=None):
        self.username = username
        self.role = role
        self.permissions = permissions if permissions else []

    def grant_permission(self, permission):
        """Grant a new permission to the user."""
        if permission not in self.permissions:
            self.permissions.append(permission)

    def revoke_permission(self, permission):
        """Revoke a permission from the user."""
        if permission in self.permissions:
            self.permissions.remove(permission)

    def is_admin(self):
        """Check if the user is an admin."""
        return self.role == "admin"

    def has_permission(self, permission):
        """Check if the user has a specific permission."""
        return permission in self.permissions
```

---

### Task 6: Test Role-Specific Behaviors  
1. Check if `alice` is an admin.  
2. Check if `admin_user` has the `write` permission.  

#### Example Code:
```python
print(f"Is Alice an admin? {alice.is_admin()}")
print(f"Does Admin have 'write' permission? {admin_user.has_permission('write')}")
```

---

### Bonus Task: Manage Multiple Users  
1. Create a list of users with varying roles and permissions.  
2. Write a function `list_admins(users)` that takes a list of `User` objects and prints the usernames of all admins.  

#### Example Code:
```python
def list_admins(users):
    """Print the usernames of all admin users."""
    admins = [user.username for user in users if user.is_admin()]
    print("Admins:", admins)

# Create a list of users
users = [
    User("alice", "student"),
    User("bob", "faculty", ["read"]),
    User("charlie", "admin", ["read", "write"]),
]

list_admins(users)
```


