saklar_bawah = True
saklar_atas = False

# Model logika (XOR menggunakan simbol ^)
lampu_menyala = saklar_bawah ^ saklar_atas

# Output
if lampu_menyala:
    print("LAMPU MENYALA")
else:
    print("LAMPU MATI")