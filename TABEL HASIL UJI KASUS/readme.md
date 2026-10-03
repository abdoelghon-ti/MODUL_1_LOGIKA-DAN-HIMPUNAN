# Tabel Uji Logika Boolean

### 1. akses_login.py (Logika AND)
| user_valid | pass_valid | email_valid | bisa_login | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | :--- |
| True | True | True | True | LOGIN BERHASIL | Data pada skrip |
| True | True | False | False | LOGIN GAGAL | |
| True | False | True | False | LOGIN GAGAL | |
| False | False | False | False | LOGIN GAGAL | |

### 2. diskon_belanja.py (Logika OR)
| belanja_besar | punya_member | kupon_diskon | diskon | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | :--- |
| True | True | True | True | DAPAT DISKON | Data pada skrip |
| True | False | False | True | DAPAT DISKON | |
| False | True | False | True | DAPAT DISKON | |
| False | False | False | False | HARGA NORMAL | |

### 3. keringanan_tagihan_rs.py (Logika OR)
| ada_bpjs | ada_sktm | ada_asuransi_swasta | keringanan | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | :--- |
| False | False | False | False | BAYAR PENUH | Data pada skrip |
| True | False | False | True | DAPAT KERINGANAN | |
| False | True | False | True | DAPAT KERINGANAN | |
| True | True | True | True | DAPAT KERINGANAN | |

### 4. penarikan_uang.py (Logika AND)
| saldo_cukup | di_bawah_limit | pin_kode_atm | bisa_tarik | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | :--- |
| True | True | False | False | PENARIKAN DITOLAK | Data pada skrip |
| True | True | True | True | PENARIKAN BERHASIL | |
| True | False | True | False | PENARIKAN DITOLAK | |
| False | False | False | False | PENARIKAN DITOLAK | |

### 5. penerimaan_beasiswa.py (Logika AND)
| ipk_tinggi | organisasi | lolos_wawancara | beasiswa | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | :--- |
| False | False | False | False | TIDAK DAPAT BEASISWA | Data pada skrip |
| True | True | True | True | DAPAT BEASISWA | |
| True | True | False | False | TIDAK DAPAT BEASISWA | |
| False | True | True | False | TIDAK DAPAT BEASISWA | |

### 6. pilihan_hadiah.py (Logika XOR)
| ambil_motor | ambil_uang | klaim_sah | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- | :--- |
| True | True | False | KLAIM INVALID: Harus memilih tepat salah satu | Data pada skrip |
| True | False | True | KLAIM SAH: Hadiah berhasil diproses | |
| False | True | True | KLAIM SAH: Hadiah berhasil diproses | |
| False | False | False | KLAIM INVALID: Harus memilih tepat salah satu | |

### 7. pintu_otomatis.py (Logika OR)
| muka_terdeteksi | kartu_terdeteksi | sidik_jari | pintu_terbuka | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- | :--- |
| True | False | False | True | PINTU TERBUKA | Data pada skrip |
| False | True | False | True | PINTU TERBUKA | |
| False | False | True | True | PINTU TERBUKA | |
| False | False | False | False | PINTU TERTUTUP | |

### 8. saklar_lampu.py (Logika XOR)
| saklar_bawah | saklar_atas | lampu_menyala | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- | :--- |
| True | False | True | LAMPU MENYALA | Data pada skrip |
| True | True | False | LAMPU MATI | |
| False | True | True | LAMPU MENYALA | |
| False | False | False | LAMPU MATI | |
