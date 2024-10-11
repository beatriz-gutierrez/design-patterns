"""
    This example demonstrates a basic MVC structure for a user management
    system.
    The Model handles data storage and retrieval, the View handles data
    presentation, and the Controller coordinates between them, handling
    user input and updating the View accordingly.

    This example demonstrates a basic MVC structure for a user management system. 
    The Model handles data storage and retrieval, the View handles data presentation, 
    and the Controller coordinates between them, handling user input and updating the 
    View accordingl

    https://www.perplexity.ai/search/explain-the-model-view-control-T61lbUXIQ7OdBDNHinHcrQ
"""


# Model
class UserModel:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, email: str):
        self.users[username] = email

    def get_user(self, username: str) -> str:
        return self.users.get(username)


# View
class UserView:
    def show_user(self, username: str, email: str):
        print(f"Username: {username}, Email: {email}")

    def error_message(self, message: str):
        print(f"Error: {message}")


# Controller
class UserController:
    def __init__(self, model: UserModel, view: UserView):
        self.model = model
        self.view = view

    def add_user(self, username: str, email: str):
        if username and email:
            self.model.add_user(username, email)
            self.view.show_user(username, email)
        else:
            self.view.error_message("Username and email are required.")

    def show_user(self, username: str):
        email = self.model.get_user(username)
        if email:
            self.view.show_user(username, email)
        else:
            self.view.error_message("User not found.")
