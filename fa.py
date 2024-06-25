# generate fake data for my model User
# from models import User
from fa import Faker
fake=Faker()
user=User()
for i in range(100):
    user.govt_id=fake.random_int(min=1000,max=9999)
    user.name=fake.name()
    user.age=fake.random_int(min=18,max=100)
    user.Gender=fake.random_element(elements=('M','F'))
    user.address=fake.address()
    number=fake.random_int(min=1,max=10)
    user.total_cases=number
    case=""
    for i in range(number):
        case=case+fake.random_element(elements=('theft','bribe','rape','murder'))
        case=case+","
    case[:-1]
    user.cases_names=case
    user.save()
data = fake.date_time_between(start_date='2010-01-01', end_date='now')
print(data)