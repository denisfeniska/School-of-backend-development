class User():
    def __init__(self, name) -> None:
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.name, User.info)


class Person(User):
    def __init__(self, name, date) -> None:
        super().__init__(name)
        self.date = date

    def info(self):
        return f'Дата рождения: {self.date}'
    
    def subscribe(self, user):
        pass

class Comminity(User):
    def __init__(self, name, description) -> None:
        super().__init__(name)
        self.description = description

    def info(self):
        return f'Описание: {self.description}'
