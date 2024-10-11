from application import Application
from module import (show_configuration, mutate_configuration)


if __name__ == "__main__":
    app = Application()
    print(f"Initial configuration (from main): {app.configuration}")
    app.configuration = {"db_host": "another_host", "user": "another_user", "password": "another_password"}
    print(f"Updated configuration (from main): {app.configuration}")

    show_configuration()
    mutate_configuration()
    show_configuration()

    print(f"Initial configuration (from main): {app.configuration}")
