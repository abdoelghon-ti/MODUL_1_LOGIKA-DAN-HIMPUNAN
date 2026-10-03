muka_terdeteksi = True
kartu_terdeteksi = False
sidik_jari = False


# Model logika
pintu_terbuka = muka_terdeteksi or kartu_terdeteksi or sidik_jari

# Output
if pintu_terbuka:
    print("PINTU TERBUKA")
else:
    print("PINTU TERTUTUP")