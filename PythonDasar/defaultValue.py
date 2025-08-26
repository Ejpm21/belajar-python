# disini firstname default valuenya eka dan lastnamenya kosong/spasi
def say_hello(firstName="Eka", lastName=" "):
    print(f"Hallo {firstName} {lastName}")
    
#jika ingin memasukan 2 parameter sekaligus
say_hello("jipa", "Rolim")
# jika hanya ingin mengisi selain parameter pertama secara langsung dengan langsung mendeklarasikan parameternya
say_hello(lastName="Jiparolim")
    
# jika langsung mendeklarasikan parameter tidak masalah jika tiidak berurutan
say_hello(lastName="Jiparolim", firstName="Eka")

# parameter wajib berada di depan sedangkan yang opsional berada dibelakang
def hallo(nama, email, negara="indonesia", status="aktif"):
    print(f"nama: {nama}, email: {email}, negara: {negara}, status: {status}")
    

# ini akan error karena syarat default value jika parameter depan memiliki default value maka parameter dibelakang
# nya juga wajib memiliki default value
# def say_hello2(nama1="jpm",nama2):
#     print(f"hallo {nama1} {nama2}")