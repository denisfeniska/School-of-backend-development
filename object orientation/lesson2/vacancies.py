class Profile():
    def __init__(self, job_name) -> None:
        self.job_name = job_name

    def info(self):
        return ''

    def describe(self):
        print(self.job_name, Profile.info)

class Vacancy(Profile):
    def __init__(self, job_name, salary) -> None:
        super().__init__(job_name)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'

class Resume(Profile):
    def __init__(self, job_name, work_experience) -> None:
        super().__init__(job_name)
        self.work_experience = work_experience

    def info(self):
        return f'work experience: {self.work_experience}'



    