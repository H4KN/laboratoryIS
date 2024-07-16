# user.py
class User:
    def __init__(self, id, name, role, password=""):
        self.id = id
        self.name = name
        self.role = role
        self.password = password

    def setPassword(self, password):
        if self.validatePassword(password):
            self.password = password
        else:
            raise ValueError("Invalid password")

    def getPassword(self):
        return self.password

    def setRole(self, role):
        if self.validateRole(role):
            self.role = role
        else:
            raise ValueError("Invalid role")

    def getRole(self):
        return self.role

    def validatePassword(self, password):
        return len(password) >= 8  # Example: minimum length of 8

    def validateRole(self, role):
        allowed_roles = ["admin", "user", "guest"]
        return role in allowed_roles

    def authenticate(self, password):
        return self.password == password

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "password": self.password
        }

    @staticmethod
    def fromDict(data):
        return User(data["id"], data["name"], data["role"], data["password"])

    def __str__(self):
        return f"{self.name} ({self.id}) {self.role}"