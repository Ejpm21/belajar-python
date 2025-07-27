# disini firstname defaul valuenya eka dan lastnamenya kosong/spasi
def say_hello(firstName="Eka", lastName=" "):
    print(f"Hallo {firstName} {lastName}")
    
#jika ingin memasukan 2 parameter sekaligus
say_hello("jipa", "Rolim")
# jika hanya ingin mengisi selain parameter pertama secara langsung dengan langsung mendeklarasikan parameternya
say_hello(lastName="Jiparolim")
    
# jika langsung mendeklarasikan parameter tidak masalah jika tiidak berurutan
say_hello(lastName="Jiparolim", firstName="Eka")