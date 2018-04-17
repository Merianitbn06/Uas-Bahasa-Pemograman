def ff():
        print "Modul Kalkulator Function"
TAMBAH, KURANG, BAGI, KALI = range(4)

def hitung (a, b, operator=TAMBAH, format_output=float):
	hasil=0
	if operator == TAMBAH :
		hasil = a + b
	elif operator == KURANG :
		hasil = a - b
	elif operator == BAGI :
		hasil = a / b
	elif operator == KALI :
		hasil = a * b
	else :
		ValueError('OPERATOR YANG DIIJINKAN TAMBAH, KURANG, KALI, BAGI')
		
	if format_output == float :
		hasil = float(hasil)
	elif format_output == int :
		hasil = round(hasil)
	else :
		ValueError('format_output harus int atau float')
	return hasil
