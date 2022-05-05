from Person import Person


class Student(Person):
    def __init__(self, name: str, age: int, email: str):
        super().__init__(name, age)
        self.email = email

    def get_info(self):
        return f"This is {self.summery()}. His email is : {self.email}"

    def summery(self, name: str = None):
        return f"{self.getName() if name is None else name}"


s1 = Student("Sajib", 20, "rezwanhossainsajib@gmail.com")
s1.setName("Developer Rezwan")
print(s1.get_info())
