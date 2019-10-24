#https://github.com/joke2k/faker
# Add 'faker' to your anaconda environment
# or 'pipenv install faker'
# 
from faker import Faker
fake = Faker()

for x in range(100):
    print(fake.name())
for x in range(100):
    print(fake.job())
# 'Lucy Cechtelar'