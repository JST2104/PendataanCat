from os import system
from time import sleep

def print_menu():
	system("cls")
	print("""
	[1]. Lihat Semua Cat
	[2]. Tambah Stok Cat
	[3]. Cari Cat
	[4]. Hapus Data Cat
	[5]. Perbarui Merek Cat
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(cat=None, ukuran=True, warna=True, harga=True, all_data=False):
	if cat != None and all_data == False:
		print(f"UKURAN : {cat}")
		print(f"WARNA : {tokocat[cat]['warna']}")
		print(f"HARGA : {tokocat[cat]['harga']}")
	elif harga == False and all_data == False:
		print(f"UKURAN : {cat}")
		print(f"WARNA : {tokocat[cat]['warna']}")
	elif all_data == True:
		for every_paint in tokocat:
			ukuran = every_paint
			warna = tokocat[every_paint]["warna"]
			harga = tokocat[every_paint]["harga"]
			print(f"UKURAN : {ukuran} - WARNA : {warna} - HARGA : {harga}")

def view_tokocat():
	print_header("DAFTAR CAT TERSIMPAN")
	if not_empty(tokocat):
		print_data(all_data=True)
	else:
		print("MAAF CAT BELUM TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def add_paint():
	print_header("MENAMBAHKAN CAT")
	merek = input("MEREK CAT : ")
	ukuran = input("UKURAN \t: ")
	warna = input("WARNA \t: ")
	harga = input("HARGA \t: ")
	respon = input(f"Apakah yakin ingin menyimpan cat : {merek} ? (Y/N) ")
	if verify_ans(respon):
		tokocat[merek] = {
			"ukuran" :ukuran,
			"warna" : warna,
			"harga" : harga
		}
		print("Data Cat Tersimpan.")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching(cat):
	if cat in tokocat:
		return True
	else:
		return False

def find_paint():
	print_header("MENCARI CAT")
	merek = input("Nama Merek yang Dicari : ")
	exists = searching(merek)
	if exists:
		print("Data Ditemukan")
		print_data(cat=merek)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_paint():
	print_header("MENGHAPUS SEPATU")
	ukuran = input("Cat yang akan dihapus : ")
	exists = searching(ukuran)
	if exists:
		print_data(cat=ukuran)
		respon = input(f"Yakin ingin menghapus {ukuran} ? (Y/N) ")
		if verify_ans(respon):
			del tokocat[ukuran]
			print("Data Cat Telah Dihapus")
		else:
			print("Data Cat Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")
	
def update_paint_ukuran(paint):
	print(f"Ukuran Lama : {paint}")
	new_size = input("Masukan Ukuran baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tokocat[new_size] = tokocat[paint]
		del tokocat[paint]
		print("Data Telah di simpan")
		print_data(new_size)
	else:
		print("Data Batal diubah")

def update_paint_warna(paint):
	print(f"Warna Lama : {tokocat[paint]['warna']}")
	new_color = input("Masukan Warna Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result : 
		tokocat[paint]['warna'] = new_color
		print("Data Telah di simpan")
		print_data(paint)
	else:
		print("Data Telah diubah")

def update_paint_harga(paint):
	print(f"Harga Lama : {tokocat[paint]['harga']}")
	new_price = input("Masukan Harga Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result : 
		tokocat[paint]['Harga'] = new_price
		print("Data Telah di simpan")
		print_data(paint)
	else:
		print("Data Telah diubah")

def update_paint():
	print_header("MENGUPDATE DATA CAT")
	merek = input("Merek Cat yang akan di-update : ")
	exists = searching(merek)
	if exists:
		print_data(merek)
		print("EDIT FIELD [1] UKURAN - [2] WARNA - [3] HARGA")
		respon = input("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_shoes_ukuran(ukuran)
		elif respon == "2":
			update_shoes_warna(warna)
		elif respon == "3":
			update_shoes_harga(harga)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")


def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_tokocat()
	elif char == "2":
		add_paint()
	elif char == "3":
		find_paint()
	elif char == "4":
		delete_paint()
	elif char == "5":
		update_paint()

tokocat = {
	"No Drop" : {
		"Ukuran": "5 KG",
		"Warna" : "Cyan",
		"Harga" : "Rp 50.000,00"
	},
	"Nippon Paint" : {
		"Ukuran" : "5 KG",
		"Warna" : "Orange",
		"Harga" : "Rp 55.000,00"
	}
}

stop = False

while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)