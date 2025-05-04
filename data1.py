fname = input('File yang ingin dibuka: ')
try:
    fread = open(fname)
except:
    print('File yang diminta tidak ada.')