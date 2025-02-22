prompt = "welcome to your travel log, please enter the city you traveled to"
prompt += "\nEnter 'quit' to exit."

city = input(prompt)
City_list = []
while True:
    if city == 'quit':
        break
    if city != 'quit':
        City_list.append(city)
        print(City_list)
    city = input(prompt)
