def ee():
    print "Modul Dictionary"
    
dict1={'Nama1':'Jane Doe', 'Nama2':'John Smith', 'Nama3':'Bob Stone', 'telp1':'+27 555 5379', 'telp2':'+27 555 6254', 'telp3': '+27 555 5689'}

print ' Name         Telephone Number'
print dict1['Nama1'],'   ',dict1['telp1'],'\n', dict1['Nama2'],' ',dict1['telp2'],'\n', dict1['Nama3'],'  ', dict1['telp3']

dict1['telp1']='+27 555 1024'
print '\nUbah nomor telp Jane Doe'
print ' Name        Telephone Number'
print dict1['Nama1'],'   ',dict1['telp1'],'\n', dict1['Nama2'],' ',dict1['telp2'],'\n', dict1['Nama3'],'  ', dict1['telp3']

dict1['Nama4']='Anna Cooper'
dict1['telp4']='+27 55 3237'
print '\n Menambah Data Baru'
print ' Name        Telephone Number'
print dict1['Nama1'],'   ',dict1['telp1'],'\n', dict1['Nama2'],' ',dict1['telp2'],'\n', dict1['Nama3'],'  ', dict1['telp3'],'\n', dict1['Nama4'],'', dict1['telp4']

print '\nCetak Nomor Telp Bob Stone = ',dict1.keys()

print '\nCetak Semua Key = ',dict1.keys()

print '\nCetak Semua Value= ',dict1.values()
