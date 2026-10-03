# Tabel Uji Logika Boolean

### 1. akses_login.py (Logika AND)
| user_valid | pass_valid | email_valid | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- |
| True | True | True | LOGIN BERHASIL | PASS |
| True | True | False | LOGIN GAGAL | PASS |
| True | False | True | LOGIN GAGAL | PASS |
| False | False | False | LOGIN GAGAL | PASS |

### 2. diskon_belanja.py (Logika OR)
| belanja_besar | punya_member | kupon_diskon | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- |
| True | True | True | DAPAT DISKON | PASS |
| True | False | False | DAPAT DISKON | PASS |
| False | True | False | DAPAT DISKON | PASS |
| False | False | False | HARGA NORMAL | PASS |

### 3. keringanan_tagihan_rs.py (Logika OR)
| ada_bpjs | ada_sktm | ada_asuransi_swasta | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | 
| False | False | False | BAYAR PENUH | PASS |
| True | False | False | DAPAT KERINGANAN | PASS |
| False | True | False | DAPAT KERINGANAN | PASS |
| True | True | True | DAPAT KERINGANAN | PASS |

### 4. penarikan_uang.py (Logika AND)
| saldo_cukup | di_bawah_limit | pin_kode_atm | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | 
| True | True | False | PENARIKAN DITOLAK | PASS |
| True | True | True | PENARIKAN BERHASIL | PASS |
| True | False | True | PENARIKAN DITOLAK | PASS |
| False | False | False | PENARIKAN DITOLAK | PASS |

### 5. penerimaan_beasiswa.py (Logika AND)
| ipk_tinggi | organisasi | lolos_wawancara | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | 
| False | False | False | TIDAK DAPAT BEASISWA | PASS |
| True | True | True | DAPAT BEASISWA | PASS |
| True | True | False | TIDAK DAPAT BEASISWA | PASS |
| False | True | True | TIDAK DAPAT BEASISWA | PASS |

### 6. pilihan_hadiah.py (Logika XOR)
| ambil_motor | ambil_uang | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- | 
| True | True | KLAIM INVALID: Harus memilih tepat salah satu | PASS |
| True | False | KLAIM SAH: Hadiah berhasil diproses | PASS |
| False | True | KLAIM SAH: Hadiah berhasil diproses | PASS |
| False | False | KLAIM INVALID: Harus memilih tepat salah satu | PASS |

### 7. pintu_otomatis.py (Logika OR)
| muka_terdeteksi | kartu_terdeteksi | sidik_jari | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- |
| True | False | False | PINTU TERBUKA | PASS |
| False | True | False | PINTU TERBUKA | PASS |
| False | False | True | PINTU TERBUKA | PASS |
| False | False | False | PINTU TERTUTUP | PASS |

### 8. saklar_lampu.py (Logika XOR)
| saklar_bawah | saklar_atas | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- |
| True | False | LAMPU MENYALA | PASS |
| True | True | LAMPU MATI | PASS |
| False | True | LAMPU MENYALA | PASS |
| False | False | LAMPU MATI | PASS |
