ada_bpjs = False
ada_sktm = False
ada_asuransi_swasta = False

# Model logika
keringanan = ada_bpjs or ada_sktm or ada_asuransi_swasta

# Output
if keringanan:
    print("DAPAT KERINGANAN")
else:
    print("BAYAR PENUH")