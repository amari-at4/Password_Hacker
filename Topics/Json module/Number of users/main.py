# write your code here
with open("users.json", "r") as json_file:
    users_json = json.load(json_file)

print(len(users_json['users']))
