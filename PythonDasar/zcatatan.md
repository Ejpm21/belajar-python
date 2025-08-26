# PYTHON

## HELLO WORLD
* hanya mencoba berbagai macam perintah python
*  fungsi `print()` digunakan untuk menampilkan output
* bisa dilihat di file [Hello World](helloworld.py)

## Komentar
* seperti biasa digunakan untuk penanda, atau bisa untuk dokumentasi agar tidak perlu mentelaah kode ulang
* bisa dengan `#` untuk satu baris
``` 
"""
untuk 
multi 
baris
"""
```
* bisa dilihat di file [komen](comment.py)

## \n
* dalam python setiap kita pencetak print() akan secara default ditambahkan end="\n"
* dengan itu agar tidak endline kita harus memberitahunya secara explisit menggunakan end=""
* contoh print("hari ini saya akan pergi kesekolah, end="")

## Number
* ada beberapa tipe tapi yang umum 
    - integer(int), bilangan bulat
    - float, untuk bilangan desimal
    - misal ingin mengetahui tipe data gunakan `print(type(x))`
    - x  sebagai variabel yang ingin diketahui tipenya
* bisa dilihat di file [number](number.py)

## Operasi matematika
* digunakan untuk operasi matematika dan bahkan bisa digunakan untuk menggabungkan beberapa string
* operator umum
    - `+` digunakan untuk menjumlahkan bilangan
    - `-` digunakan untuk mengurangi bilangan
    - `/` digunakan untuk membagi, dan langsung ada (koma) walapun dibelakangnya 0
    - `*` digunakan untuk mengkali bilangan
    - `%` modulus, atau sisa bagi jadi yang muncul itu cuma sisa dari pembagian, misal 10 / 3 maka sisanya 1, jadi yang ditampilkan 1
    - `//` pembagian bulat jadi misalnya 10 /3 hasilnya 3.3333 dibulatkan hasilnya langsung 3 saja
    - `**` operasi pangkat
* bisa dilihat di file [Operasi Matematika](operasiMatematika.py)

## Variable
* digunakan untuk menyimpan nilai
* jadi analoginya kita bisa menyimpan apapun di dalam sebuah kotak(variable)
* bisa dilihat di file `variable`
* nama variable tidak boleh diawali angka, tetapi bisa ditambah angka
* tidak perlu deklarasi tipe data
* bisa dilihat di file [Variable](variable.py)

## String / teks
* bisa disebut teks, bisa di tulis dengan kutip  maupun kutip 2
* shortcut string
    - misal kita punya variable teks = "belajar bareng"
    - `print(teks.upper())`, digunakan untuk mengubah isi dari variable teks menjadi huruf besar semua
    - `print(teks.lower())`, igunakan untuk mengubah isi dari variable teks menjadi huruf kecil
    - `print(teks[0:7])`, artinya mengambil huruf dari index 0 sampai sebelum 7 jadi yang diambil(belajar)
    - `print(len(teks))`, artinya menghitung panjang dari isi variable teks, (dimulai dari 1, dan spasi dihitung), jadi hasilnya 14
    - `print(teks.replace("bareng", "sendiri"))` jadi mengubah kata bareng jadi sendiri, dengan aturan bahwa harus sama huruf besar dan kecilnya, dan misal ada banyak kata "bareng" maka akan diganti semua
* bisa dilihat di file [String](teks.py)

## String Format
* digunakan untuk menyisipkan variable ke sebuah string/teks
* bisa dilihat di file [Format String](formatString.py)

## input
* digunakan untuk mengambil input dari pengguna
* dan secara default input bertipe `str()`
* bisa dilihat di file [Input](input.py)

## Input Number
* sama seperti tadi, tetapi karena default input itu string jadi harus merubahnya menjadi int/float
* bisa dilihat di file [input Number](inputNumber.py)

## Boolean
* hanya memiliki 2 nilai yaitu true or false
* bisa dilihat di file [Boolean](boolean.py)

## Operator Logika
* terdapat 3 yaitu
    - `and`, kedua variable harus bernilai true maka hasilnya true, jika salah 1 atau dua duanya false maka hasilnya false
    - `or` , cukup salah satu variable atau dua duanya true maka hasilnya true, akan bernilai false jika kedua variablenya bernilai false
    - `not`, kebalikannya jika `not true` maka hasilnya false, dan begitupun sebaliknya
* bisa dilihat di file [Operator Logika](operatorLogika.py)

## Operator Perbandingan
* Operator ini digunakan untuk membandingkan dua nilai dan hasilnya selalu boolean
* macam macam operator
    - `==`, sama dengan misal 5 == 5 maka hasilnya `true` 
    - `!=`, tidak sama dengan misal 6 != 5 hasilnya `true` jika 6!=6 hasilnya `false` 
    - `<`, lebih kecil misal 6<5 hasilnya `false`
    - `>`, lebih besar misal 6>5 hasilnya `true`
    - `<=` lebih kecil sama dengan misal 6 <= 6 hasilnya `true`
    - `>=` lebih besar sama dengan misal 6 >= 7 hasilnya `false`
* bisa dilihat di file [Operator Perbandingan](operatorPerbandingan.py)



## If statemen
* digunakan untuk kondisi yang akan terpenuhi
* misal kondisi terpenuhi harus ada tab atau spasi 4x (indentasi)
* bisa dilihat di file [IF](if.py)


## else statemen
* else digunakan jika kondisi if itu tidak terpenuhi
* bisa dilihat di file [Else](else.py)

## Elif statemen
* digunakan jika ada kondisi dimana banyak pilihan(tidak hanya salah atau benar)
* bisa dilihat di file [elif](elif.py)

## if in
* cara untuk mengecek apakah sebuah item ada di dalam sebuah kumpulan data (seperti list, string, atau tuple).
* Hasil dari pengecekan in ini adalah nilai boolean, yaitu True (jika itemnya ada) atau False (jika itemnya tidak ada).
* bisa dilihat di file [if_in](if_in.py)

## List
* sebuah variable yang digunakan untuk menyimpan banyak data
* list menggunakan index yang berarti dimulai dari 0
* fitur list
    - misal kita memiliki variable `buah=["apel","pisang","mangga"]`
    - untuk mengakses kita bisa gunanakan `buah[0]` untuk mengakses index ke 0 yaitu apel
    - menghitung panjang isi data menggunakan `len(buah)`
    - menambah data di list menggunakan `buah.append("jeruk")`, atau bisa juga `.insert(index, value)` jadi bisa ditentukan posisi menambahkan valuenya.
    - ganti data di list `buah[1]="melon"`, mengganti index 1 yaitu pisang menjadi melon
    - untuk mengetahui posisi index gunakan `buah.index("mangga")` maka akan memberitahu posisi manggan pada variable buah yaitu 2
    - menghapus data `buah.remove("apel")` atau `del buah[0]` jika ingin menggunakan index, ada juga `buah.pop(index)`, dan slicing assigment untuk menghapus banyak sekaligus `buah[1:3] = []` menghapus dari index 1 sampai sebelum 3 berarti (1 dan 2 terhapus)

* list itu unik data bisa campur mau itu string, int, boolean float pun bisa
* dan bisa menyimpan list didalam list(nested list) bisa dilihat di file list
* bisa dilihat di file [List](list.py)

## For loop
* bisa digunakan untuk mengakses array
* pada file `forLoop` ada penjelasan range dan enumerate
    - `range`, digunakan untuk membuat deretan angka misal range(3) maka 0,1,2
    range(n) selalu dimulai dari 0 dan berhenti di n - 1
    misa lagi range(mulai,sampai,selisih), range(1, 5, 2) maka (1,3)
    jadi seandainya range(5,0,-1) maka(5,4,3,2,1)
    - `enumerate`, akan mengubah list jadi pasangan (index, item) yang pasti harus gunakan 2 variable, 1 untuk mengakses list satu lagi untuk index
* bisa dilihat di file [Program Forloop](program_forLoop.py) dan [forloop](forLoop.py)

## while loop
* while loop digunakan untuk mengulang kode selama suatu kondisi bernilai True.
* Digunakan jika tidak tahu pasti kapan harus berhenti
* bisa dilihat di file [while loop](while_loop.py)

## enumerate
* built-in function yang dipakai saat looping supaya bisa dapat index dan value dari elemen list (atau iterable lainnya) secara bersamaan.
* misal ada data `buah = ["apel", "mangga", "jeruk"]`
```
for idx, b in enumerate(buah):
    print(idx, b)
```
* maka akan menghasilkan index dan sebuah value
* bisa dilihat di file [Enumerate](enumerate.py)
## continue
* biasanya berguna untuk mengskip program dalam looping, jadi program hanya melewatkan tanpa memberhentikan program
* Bisa digunakan di for dan while
* bisa dilihat di file [Continue](continue.py)

## break
* Digunakan untuk menghentikan loop secara paksa, meskipun kondisinya masih True.
* digunakan untuk menstop biasanya untuk perulangan atau kondisi
* Setelah break, program akan keluar dari loop dan lanjut ke baris setelah loop.
* bisa dilihat di file [Break](break.py)

## Tuple
* jika list menggunakan `[]` maka Tuple menggunakan `()` selain itu juga misal sebuah variable `angka = 1,2,3` maka akan dianggap tuple walaupun tidak menggunakan kurung
* berbeda dengan list, tuple ini datanya sudah g bisa di rubah, tambah, hapus juga tidak bisa
* tuple ini sangat berguna pada methode
* Cocok untuk data yang tidak ingin diubah.
* Lebih cepat dan aman dibanding list.
* Bisa diakses dengan index (data[0]) tapi tidak bisa append, remove, dll.
* bisa dilihat di file [Tuple](tuple.py)

## tipe data set
* mirip dengan list dan tuple, tetapi set menggunakan `{}`
* perbedaannya terletak pada saat di run, pada data yang sama dia tidak akan terdetect (unique)
* jadi data tidak boleh duplikat
* dan posisi data itu berubah ubah jadi kita tidak dapat mengakses data melalui index
* cara satu satunya hanya menggunakan for loop
* jika dalam list itu menggunakan `append` di set menggunakan `add` untuk menambah data
* untuk menghapus data sama dengan list menggunakan `remove`
* Untuk mengecek apakah elemen ada di set: `if "apel" in buah:`
* bisa dilihat di file [Set](set.py)

## method / function
* method digunakan untuk mengelompokkan kode agar bisa dipanggil berkali-kali. Bisa dengan atau tanpa parameter.
* digunakan agar tidak terjadi duplikasi code
* bisa dilihat di file [Method](method.py)

## method parameter
* Parameter digunakan untuk mengirim data ke dalam fungsi.
* `print("parameter")` ini sebenarnya adalah method isi didalam tanda kurung itulah parameter
* argumen adalah data yang dimasukan ke parameter
* bisa dilihat di file [Method parameter](methodParam.py)

## default value argument
* jika ada sebuah function yang memiliki parameter, jika memanggil function tanpa mengisinya dengan argumen maka akan error
* disini default value digunakan agar saat tidak mengisi parameter akan tetap bisa di eksekusi bisa dibilang jadi opsional jika terdapat default value
* cara membuat: `def helo(name="default value")`
* dengan catatan jika parameter 1 memeiliki default value maka parameter ke 2 juga harus ada default value
* tetapi bisa jika parameter ke 2 punya default value dan yang pertama tidak memiliki default value
* jadi intinya default value harus dibelakang, jika paling depan memiliki default value maka semua parameter dibelakangnya juga harus mempunyai default value (parameter wajib, berada didepan sedangkan yang opsional dibelakang)
* misal kita memiliki parameter `def hello(firstname="Eka",lastname=" ")` ini bisa karena bagian belakang memiliki default values kosong
* dan misal hanya hanya mengisi bagian lastname kita bisa langsung panggil parameternya `hello(lastname="Jiparolim")`
* bisa dilihat di file [Default Value](defaultValue.py)

## argumen  list
* ini digunakan untuk mengatasi masalah fungsi dengan jumlah argumen yang terbatas, misal terdapat fungsi yang dapat menjumlahkan, kita dapat membuat 2 parameter yang bisa menampung 2 argument, tetapi bagaimana jika argumen yang ingin dikirim itu fleksible? bisa 2,3,5 saat itu argument list digunakan sering disebut `*args`
* tambahkan `*` di depan parameter
* digunakan ketika kita ingin mengirim banyak argumen sekaligus ke dalam satu parameter.
* mengubah semua argumen yang dikirim menjadi tuple
* bisa digabung dengan parameter biasa, dengan catatan parameter biasa harus berada didepan baru diikuti *args
* bisa dilihat di file [Argument List](argumenList.py)

## Return Value
* digunakan di dalam fungsi (function/method) untuk mengembalikan suatu nilai ke luar fungsi agar bisa disimpan dan digunakan lagi di bagian lain dari program.
* Kegunaan
    - Nilai hasil fungsi bisa disimpan ke dalam variabel.
    - Fungsi menjadi lebih fleksibel dan bisa digunakan ulang.
* jika tanpa return fungsinya hanya untuk mencatatat teks, tanpa bisa digunakan ulang
* return hanya bisa mengeluarkan 1 nilai tetapi bisa memiliki banyak data misal tuple yang berisi 4 data dll
* `[]` digunakan jika ingin mereturn sebuah list
* `{}` digunakan jika ingin mereturn sebuah dictionaary
* `,` atau `()` jika ingin mereturn sebuah tuple
*  Pernyataan return akan langsung menghentikan eksekusi fungsi. Kode apa pun yang ditulis setelah return di dalam fungsi tidak akan pernah dijalankan.
* bisa dilihat di file [Return](returnValue.py)

## Dictionary
*  adalah tipe data yang menyimpan pasangan key (kunci) dan value (nilai).
misal punya biodata
```
biodata = {
    "nama": "Rudi",
    "umur": 20,
    "asal": "Bandung"
}
```
* fitur
    - Akses data	`biodata["nama"]` → "Rudi"
    - Menambah data	`biodata["hobi"] = "Membaca"`
    - Mengubah nilai	`biodata["umur"] = 21`
    - Menghapus key	`del biodata["asal"]`
    - Mengecek key	`"nama" in biodata` → True
    - Looping key dan value	`for key, value in biodata.items():`
    - Mengambil semua key	`biodata.keys()` atau langsung `biodata` 
    - Mengambil semua value	`biodata.values()`
    - Mengambil semua item	`biodata.items()`
* bisa dilihat di file [Dictionary](dictionary.py)

## Key Word Argument list
* `**kwargs` adalah cara untuk mengirim banyak parameter dengan nama (dalam bentuk pasangan key=value) ke dalam fungsi.
* kapan digunakan
    - Saat kamu tidak tahu berapa banyak argumen keyword yang akan dikirim.
    - Ketika ingin membuat fungsi yang fleksibel menerima parameter apapun.
* aturan
    - Posisi Paling Akhir: **kwargs harus menjadi parameter terakhir dalam definisi fungsi.
    - Setelah *args: Jika ada *args, maka **kwargs harus diletakkan setelahnya.
    - standar_args → default_args → *args → **kwargs
* mengakses nilai dengan aman
```
def sapa(**kwargs):
    nama = kwargs.get("nama", "Tamu")
    print(f"Halo, {nama}!")

sapa(nama="Rina")   # Output: Halo, Rina!
sapa()              # Output: Halo, Tamu!
```
* bisa dilihat di file [Keyword Argument](keywordArgument.py) atau [kwargs](kwargs.py) disini akan dijelaskan secara lengkap

## module
* cara untuk mengambil function/method, class dan lain lain dari file yang berbeda
* bisa mengambil semua methodnya maupun spesifik misal hanya 1 mehod
* contoh kita punya 2 file, file utama app.py dan modul.py
* didalam modul.py terdapat 2 method yaitu tambah(), dan kurang()

* misal kita ingin mengambil semua dari modul.py lakukan `import modul`
```
import modul

tampil = modul.tambah(10,2)
print(tampil)
```

* bisa juga mengambil  1 method `from modul import tambah`, jadi lebih mudah dalam menulis code tidak perlu penulisan nama file lagi dibelakangnya seperti yang sebelumnya
```
from modul import tambah

tampil = tambah(10,2)
print(tampil)
```
* jadi jika kita hanya mengimport sebagian data tidak perlu deklarasi nama file lagi didepan methodnya seperti `modul.tambah()` 
* bisa dilihat di folder [Module](/module/)

## Numeric types
* integer, bilangan bulat
* float, decimal bilangan koma
* complex, bilangan kompleks seperti a = 2 + 3j maka a itu bilangan komplex
* jarang sekali digunakan dalam pemrograman, hanya bidang bidang tertentu seperti riset atau yang lain
* seperti aljabar gitu intinya

## string method
* `https://docs.python.org/3/library/stdtypes.html#string-methods`
* String method adalah fungsi bawaan (built-in) yang bisa kamu gunakan langsung untuk memanipulasi atau memproses data string

* .lower()	    Ubah semua huruf ke huruf kecil	    "Hello".lower() → 'hello'
* .upper()	    Ubah semua huruf ke huruf besar	    "hello".upper() → 'HELLO'
* .capitalize()	Awal kalimat jadi kapital	        "halo dunia".capitalize() → 'Halo dunia'
* .title()	    Setiap kata kapital	                "halo dunia".title() → 'Halo Dunia'
* .strip()	    Hapus spasi (atau karakter tertentu) di depan dan belakang	" halo ".strip() → 'halo'
* .replace(old, new)	Ganti kata atau huruf	        "halo".replace("a", "e") → 'helo'
* .split()	    Pisahkan string jadi list berdasarkan spasi (default)	"a,b,c".split(",") → ['a', 'b', 'c']
* .join(list)	    Gabungkan list menjadi string	    " ".join(["saya", "belajar", "python"]) → 'saya belajar python'
* .find(sub)	    Cari posisi pertama substring	     "hello".find("l") → 2
* .startswith(prefix)	Apakah string dimulai dengan prefix?	"hello".startswith("he") → True
* .endswith(suffix)	Apakah string diakhiri dengan suffix?	"hello".endswith("o") → True
* .count(sub)	    Hitung berapa kali sub muncul	    "banana".count("a") → 3
* .isdigit()	    Apakah string hanya berisi angka?	"123".isdigit() → True
* .isalpha()	    Apakah hanya huruf (tanpa spasi/angka)? "hello".isalpha() → True

## match-case
