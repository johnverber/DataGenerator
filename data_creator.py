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

output_format = input("Please enter the output format (.csv or .json or .xml): ")

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
elif output_format == ".xml":
    with open("data.txt", "r") as f:
        data = [line.strip().split(",") for line in f]
    with open("data.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write("<data>\n")
        for row in data:
            f.write("  <person>\n")
            f.write(f"    <name>{row[0]}</name>\n")
            f.write(f"    <address>{row[1]}</address>\n")
            f.write(f"    <sex>{row[2]}</sex>\n")
            f.write(f"    <age>{row[3]}</age>\n")
            f.write(f"    <phone_number>{row[4]}</phone_number>\n")
            f.write(f"    <email>{row[5]}</email>\n")
            f.write(f"    <ssn>{row[6]}</ssn>\n")
            f.write("  </person>\n")
        f.write("</data>\n")

else:
    print("Invalid output format. Please enter .csv or .json.")