def cc():
    print "Modul List Append"
i=0
nama=[]
nim=[]
tugas=[]
uts=[]
uas=[]
total=[]
while True:
    a=raw_input('Nama : ')
    nama.append(a)
    b=raw_input('NIM  : ')
    nim.append(b)
    c=input('Nilai Tugas : ')
    tugas.append(c)
    d=input('Nilai UTS   : ')
    uts.append(d)
    e=input('Nilai UAS   : ')
    uas.append(e)

    rata=(c+d+e)/3
    total.append(rata)

    lagi=' '
    while lagi!='y' and lagi!='t':
        lagi=raw_input('\nTambah Data [y/t] : ')
    i+=1
    if lagi=='t':
        break

print'                      DATA MAHASISWA '
print'=========================================================='
print'|NO.|     Nama    |   NIM    | Tugas | UTS | UAS | AKHIR |'
print'=========================================================='
for n in range(i):
	print'|',n+1, '|\t',nama[n],' |',nim[n],' |',tugas[n],' | ',uts[n],' | ',uas[n],' |',total[n],'|'
