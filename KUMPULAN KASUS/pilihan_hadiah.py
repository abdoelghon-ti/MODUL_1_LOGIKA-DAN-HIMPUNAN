ambil_motor = True
ambil_uang = True

# Model logika (Hanya sah jika memilih tepat salah satu)
klaim_sah = ambil_motor ^ ambil_uang

# Output
if klaim_sah:
    print("KLAIM SAH: Hadiah berhasil diproses")
else:
    print("KLAIM INVALID: Harus memilih tepat salah satu")