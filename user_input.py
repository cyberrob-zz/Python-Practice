def weather(temperature):
    if float(temperature) > 7:
        return "It's warm"
    else:
        return "It's cold"


user_input = input("Enter temperature:")
print(f"type of input: {type(user_input)}")
print(weather(float(user_input)))
