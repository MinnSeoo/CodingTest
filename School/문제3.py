odd_list = []
even_list = []

while True:
    user_input = int(input())
    if user_input == 0:
        break

    elif user_input % 2 == 0:
        even_list.append(user_input)
        
    else:
        odd_list.append(user_input)

print(odd_list)
print(even_list)