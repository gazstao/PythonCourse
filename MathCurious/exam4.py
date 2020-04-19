users = [
    {
        'name': 'Rolf',
        'age': 34
    },
    {
        'name': 'Anna',
        'age': 28
    }
]

def print_users_list(user_list):
    for i, user in enumerate(user_list):
        print_user_details(i, user)

def print_user_details(number, user):
    print("{} | name: {}, age: {}.".format(number, user['name'], user['age']))

print_user_list(users)