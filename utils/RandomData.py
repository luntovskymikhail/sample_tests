from random import randint, choice

from mimesis import Person, Address, Finance
from mimesis.enums import Gender
from mimesis.builtins import RussiaSpecProvider as Spec


class RandomData:
    @staticmethod
    def ctrl_summ(nums, type):
        """Вычисление контр. суммы для ИНН"""
        ctrl_type = {
            "n2_12": [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            "n1_12": [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            "n1_10": [2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        n = 0
        l = ctrl_type[type]
        for i in range(0, len(l)):
            n += nums[i] * l[i]
        return n % 11 % 10

    @staticmethod
    def inn(l):
        """Генерация ИНН"""
        nums = [
            randint(9, 9) if x == 0 else randint(6, 6) if x == 1 else randint(0, 9)
            for x in range(0, 9 if l == 10 else 10)
        ]

        if l == 10:
            n1 = RandomData.ctrl_summ(nums, "n1_10")
            nums.append(n1)

        elif l == 12:
            n2 = RandomData.ctrl_summ(nums, "n2_12")
            nums.append(n2)
            n1 = RandomData.ctrl_summ(nums, "n1_12")
            nums.append(n1)
        return "".join([str(x) for x in nums])

    @staticmethod
    def email() -> str:
        """Возвращает адрес электронной почты"""
        domains = ["atest.ru", "atest.com"]
        person = Person("en")
        return person.email(domains=domains)

    @staticmethod
    def fio():
        """Возвращает ФИО"""
        gender = choice([Gender.MALE, Gender.FEMALE])
        last_name = Person(locale="ru").surname(gender=gender)
        first_name = Person(locale="ru").name(gender=gender)
        father_name = Spec().patronymic(gender=gender)
        return f"{last_name} {first_name} {father_name}"

    @staticmethod
    def phone_number():
        """Возвращает номер телефона"""
        return Person("en").telephone("+7-(9##)-###-####")

    @staticmethod
    def address():
        """Возвращает адрес"""
        address = Address(locale="ru").address()
        city = Address(locale="ru").city()
        return f'{city.replace("ё", "е")} {address.replace("ё", "е")}'

    @staticmethod
    def company():
        """Возвращает название компании"""
        company_quotes = Finance(locale="ru").company()
        company = "".join(
            char
            for char in company_quotes
            if char in "1234567890 AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
            "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
        )
        company_type = "ООО"
        return company_type + " " + company.replace("  ", " ")

    @staticmethod
    def kpp():
        """Возвращает КПП"""
        return str(randint(100_000_000, 999_999_999))

    @staticmethod
    def passport_series():
        """Возвращает серию паспорта"""
        return Spec().passport_series().replace(" ", "")

    @staticmethod
    def passport_number():
        """Возвращает номер паспорта"""
        return str(Spec().passport_number())

    @staticmethod
    def passport_place():
        """Возвращает место выдачи паспорта"""
        address = Address(locale="ru").address()
        return f'МВД {address.replace("ё", "е")}'

    @staticmethod
    def postcode():
        """Возвращает почтовый индекс"""
        return Address(locale="ru").postal_code()
