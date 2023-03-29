import faker
import json
import csv

fake = faker.Faker()

while True:
    try:
        user_input = int(input("Please enter a number between 1 and 100,000: "))
        if user_input < 1 or user_input > 100000:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 1000.")

with open("data.txt", "w") as f:
    for i in range(user_input):
        name = fake.name()
        address = fake.address().replace("\n", "")
        city = fake.city()
        state = fake.state()
        sex = fake.random_element(elements=("Male", "Female"))
        age = fake.random_int(min=18, max=100)
        phone_number = fake.phone_number()
        email = fake.email()
        ssn = fake.ssn()
        f.write(f"{name},{address},{sex},{age},{phone_number},{email},{ssn}\n")

output_format = input("Please enter the output format (.csv or .json): ")

if output_format == ".csv":
    with open("data.txt", "r") as f:
        data = [line.strip().split(",") for line in f]
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("Data written to data.csv.")
elif output_format == ".json":
    with open("data.txt", "r") as f:
        data = [line.strip().split(",") for line in f]
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("Data written to data.json.")
else:
    print("Invalid output format. Please enter .csv or .json.")