belanja_besar = True
punya_member = True
kupon_diskon = True

# Model logika
diskon = belanja_besar or punya_member or kupon_diskon

# Output
if diskon:
    print("DAPAT DISKON")
else:
    print("HARGA NORMAL")