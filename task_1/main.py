class User:
    email = "default@example.com"

    def __getitem__(self, item):
        return self.__dict__.get(item, self.__class__.__dict__.get(item))


user1 = User()
user1.name = 'John'
user1.age = 25

print(user1.name)  # John
print(user1.age)  # 25
print(user1.email)  # exception: AttributeError

print(user1['name'])  # John
print(user1['age'])  # 25
print(user1['email'])  # None
