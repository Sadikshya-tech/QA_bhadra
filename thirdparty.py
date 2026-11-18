
# pip install modules_name

# pip show faker


from faker import Faker

fake=Faker()
print(fake.name())
print(fake.name_female())
print(fake.email())

