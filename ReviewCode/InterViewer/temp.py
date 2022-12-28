import faker

my_faker = faker.Faker()
words = [my_faker.word() for _ in range(10)]
nums = [my_faker.pyint(1, 100) for _ in range(10)]
