class Application:
    # Maybe some default
    _configuration = {"db_host": "localhost", "user": "a_user", "password": "a_password"}

    @property
    def configuration(self):
        return Application._configuration

    @configuration.setter
    def configuration(self, configuration):
        Application._configuration = configuration

