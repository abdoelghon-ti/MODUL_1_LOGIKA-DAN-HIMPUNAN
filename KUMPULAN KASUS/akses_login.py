user_valid = True
pass_valid = True
email_valid = True

# Model logika
bisa_login = user_valid and pass_valid and email_valid

# Output
if bisa_login:
    print("LOGIN BERHASIL")
else:
    print("LOGIN GAGAL")