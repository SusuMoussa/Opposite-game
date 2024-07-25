Data = {
    "White":"Black",
    "Good":"Bad",
    "Red":"Blue",
}

user_choice = input ("Write Somethin pleaz ")

user_choice = user_choice.replace(user_choice, Data[user_choice])

print(user_choice)