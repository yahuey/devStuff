import csv
comprimised_user = []
with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = row
        comprimised_user.append(password_row["Username"])

print(comprimised_user)
# I need to make this open a file. It needs an alias for now. 
with open("comprimised_users.txt", "w") as target:
    pass
