class Person:
    def __init__(self, name, patronymic, surname, telephone_dict) -> None:
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.telephone_dict = telephone_dict
        self.s = ''

    def get_phone(self):
        if 'private' in self.telephone_dict:
            return self.telephone_dict['private']
        else:
            return None

    def get_name(self):
        self.s += self.surname + ' '
        self.s += self.name + ' '
        self.s += self.patronymic + ' '
        return self.s

    def get_work_phone(self):
        if 'work' in self.telephone_dict:
            self.telephone_dict['work']
        else:
            return None

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.patronymic}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company():
    def __init__(self, compony_name, compony_type, telephone_dict, *people) -> None:
        self.compony_name = compony_name
        self.compony_type = compony_type
        self.telephone_dict = telephone_dict
        self.people = people

    def get_phone(self):
        if 'contact' in self.telephone_dict:
            return self.telephone_dict['contact']
        else:
            for person in self.people:
                if person.get_work_phone():
                    return person.get_work_phone()
            else:
                return None

    def get_name(self):
        return self.compony_name

    def get_sms_text(self):
        return f"Для компании {self.compony_name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.compony_type}"


def send_sms(*objects):
    for obj in objects:
        if obj.get_phone():
            print(
                f'Отправлено СМС на номер {obj.get_phone()} с текстом: {obj.get_sms_text()}')
        else:
            print(
                f'Не удалось отправить сообщение абоненту: {obj.get_name()}')


person1 = Person("Степан", "Петрович",
                 "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович",
                 "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович",
                 "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович",
                 "Торвальдсон", {})
company1 = Company("Яблочный комбинат",
                   "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО",
                   {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма",
                   "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4,
         company1, company2, company3)
