class User:
    email = "default@example.com"

    def __getitem__(self, item):
        return getattr(self, item, None)


'''getattr(object, name, default)
    позволяет получить значение атрибута объекта по его имени'''


user1 = User()
user1.name = 'John'
user1.age = 25

print(user1.name)  # John
print(user1.age)  # 25
print(user1.email)  # exception: AttributeError

print(user1['name'])  # John
print(user1['age'])  # 25
print(user1['email'])  # None
