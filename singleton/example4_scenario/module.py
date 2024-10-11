from application import Application


def show_configuration():
    app = Application()
    print(f"Current configuration (from module): {app.configuration}")


def mutate_configuration():
    app = Application()
    app.configuration = {"db_host": "a_third_host", "user": "a_third_user", "password": "a_third_password"}
    print(f"Updated configuration (from module): {app.configuration}")
