class User:
    def __init__(self, age, gender, income):
        self.age = age
        self.gender = gender
        self.income = income

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income
        }
        
