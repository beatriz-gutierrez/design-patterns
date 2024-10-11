from mvc_user_managment_system import UserModel, UserView, UserController

if __name__ == "__main__":
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)

    controller.add_user("Alice", "alice@gmail.com")
    controller.add_user("Max", "max@services.com")

    controller.show_user("Alice")
    controller.show_user("Bob")
    controller.show_user("Max")
