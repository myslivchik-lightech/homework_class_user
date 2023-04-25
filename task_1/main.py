class User:
    def __getitem__(self, item):
        return self.__dict__.get(item, None)


user1 = User()
user1.name = 'John'
user1.age = 25

print(user1.name)  # John
print(user1.age)  # 25
print(user1.email)  # exception: AttributeError

print(user1['name'])  # John
print(user1['age'])  # 25
print(user1['email'])  # None
