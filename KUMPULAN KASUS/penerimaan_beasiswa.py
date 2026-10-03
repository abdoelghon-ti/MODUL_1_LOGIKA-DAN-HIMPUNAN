ipk_tinggi = False
organisasi = False
lolos_wawancara = False

# Model logika
beasiswa = ipk_tinggi and organisasi and lolos_wawancara

# Output
if beasiswa:
    print("DAPAT BEASISWA")
else:
    print("TIDAK DAPAT BEASISWA")