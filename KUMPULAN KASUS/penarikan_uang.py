saldo_cukup = True
di_bawah_limit = True
pin_kode_atm = False


# Model logika
bisa_tarik = saldo_cukup and di_bawah_limit and pin_kode_atm

# Output
if bisa_tarik:
    print("PENARIKAN BERHASIL")
else:
    print("PENARIKAN DITOLAK")