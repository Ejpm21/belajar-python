# PYTHON

## HELLO WORLD
* hanya mencoba berbagai macam perintah python
*  fungsi `print()` digunakan untuk menampilkan output

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

## Number
* ada beberapa tipe tapi yang umum 
    - integer(int), bilangan bulat
    - float, untuk bilangan desimal
    - misal ingin mengetahui tipe data gunakan `print(type(x))
    - x  sebagai variabel yang ingin diketahui tipenya
* bisa dilihat di file `number`
 
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

## Variable
* digunakan untuk menyimpan nilai
* jadi analoginya kita bisa menyimpan apapun di dalam sebuah kotak(variable)
* bisa dilihat di file `variable`
* nama variable tidak boleh diawali angka, tetapi bisa ditambah angka
* tidak perlu deklarasi tipe data

## String / teks
* bisa disebut teks, bisa di tulis dengan kutip  maupun kutip 2
* shortcut string
    - misal kita punya variable teks = "belajar bareng"
    - `print(teks.upper())`, digunakan untuk mengubah isi dari variable teks menjadi huruf besar semua
    - `print(teks.lower())`, igunakan untuk mengubah isi dari variable teks menjadi huruf kecil
    - `print(teks[0:7])`, artinya mengambil huruf dari index 0 sampai sebelum 7 jadi yang diambil(belajar)
    - `print(len(teks))`, artinya menghitung panjang dari isi variable teks, (dimulai dari 1, dan spasi dihitung), jadi hasilnya 14
    - `print(teks.replace("bareng", "sendiri"))` jadi mengubah kata bareng jadi sendiri, dengan aturan bahwa harus sama huruf besar dan kecilnya, dan misal ada banyak kata "bareng" maka akan diganti semua

## String Format
* digunakan untuk menyisipkan variable ke sebuah string/teks
* bisa dilihat di file `formatString`

## input
* digunakan untuk mengambil input dari pengguna
* dan secara default input bertipe `str()`
* bisa dilihat di file `input`

## Input Number
* sama seperti tadi, tetapi karena default input itu string jadi harus merubahnya menjadi int/float
* bisa dilihat di file `inputNumber`

## Boolean
* hanya memiliki 2 nilai yaitu true or false

## Operator Logika
* terdapat 3 yaitu
    - `and`, kedua variable harus bernilai true maka hasilnya true, jika salah 1 atau dua duanya false maka hasilnya false
    - `or` , cukup salah satu variable atau dua duanya true maka hasilnya true, akan bernilai false jika kedua variablenya bernilai false
    - `not`, kebalikannya jika `not true` maka hasilnya false, dan begitupun sebaliknya

## Operator Perbandingan
* Operator ini digunakan untuk membandingkan dua nilai dan hasilnya selalu boolean
* macam macam operator
    - `==`, sama dengan misal 5 == 5 maka hasilnya `true` 
    - `!=`, tidak sama dengan misal 6 != 5 hasilnya `true` jika 6!=6 hasilnya `false` 
    - `<`, lebih kecil misal 6<5 hasilnya `false`
    - `>`, lebih besar misal 6>5 hasilnya `true`
    - `<=` lebih kecil sama dengan misal 6 <= 6 hasilnya `true`
    - `>=` lebih besar sama dengan misal 6 >= 7 hasilnya `false`


## If statemen
* digunakan untuk kondisi yang akan terpenuhi
* misal kondisi terpenuhi harus ada tab atau spasi 4x (indentasi)

## else statemen
* else digunakan jika kondisi if itu tidak terpenuhi

## Elif statemen
* digunakan jika ada kondisi dimana banyak pilihan(tidak hanya salah atau benar)

## List
* sebuah variable yang digunakan untuk menyimpan banyak data
* list menggunakan index yang berarti dimulai dari 0
* fitur list
    - misal kita memiliki variable `buah=["apel","pisang","mangga"]`
    - untuk mengakses kita bisa gunanakan `buah[0]` untuk mengakses index ke 0 yaitu apel
    - menghitung panjang isi data menggunakan `len(buah)`
    - menambah data di list menggunakan `buah.append("jeruk")`
    - ganti data di list `buah[1]="melon"`, mengganti index 1 yaitu pisang menjadi melon
    - menghapus data `buah.remove("apel")` atau `del buah[0]`

* list itu unik data bisa campur mau itu string, int, boolean float pun bisa
* dan bisa menyimpan list didalam list(nested list) bisa dilihat di file list

## For loop
* bisa digunakan untuk mengakses array
* pada file `forLoop` ada penjelasan range dan enumerate
    - `range`, digunakan untuk membuat deretan angka misal range(3) maka 0,1,2
    range(n) selalu dimulai dari 0 dan berhenti di n - 1
    misa lagi range(mulai,sampai,selisih), range(1, 5, 2) maka (1,3)
    - `enumerate`, akan mengubah list jadi pasangan (index, item) yang pasti harus gunakan 2 variable, 1 untuk mengakses list satu lagi untuk index

* bisa dilihat di file `program_forLoop` dan `forLoop`

## while loop
* while loop digunakan untuk mengulang kode selama suatu kondisi bernilai True.\
* Digunakan jika tidak tahu pasti kapan harus berhenti

## continue
* biasanya berguna untuk mengskip program dalam looping, jadi program hanya melewatkan tanpa memberhentikan program
* Bisa digunakan di for dan while

## break
* Digunakan untuk menghentikan loop secara paksa, meskipun kondisinya masih True.
* digunakan untuk menstop biasanya untuk perulangan atau kondisi
* Setelah break, program akan keluar dari loop dan lanjut ke baris setelah loop.

## Tuple
* jika list menggunakan `[]` maka Tuple menggunakan `()`
* berbeda dengan list, tuple ini datanya sudah g bisa di rubah, tambah, hapus juga tidak bisa
* tuple ini sangat berguna pada methode
* Cocok untuk data yang tidak ingin diubah.
* Lebih cepat dan aman dibanding list.
* Bisa diakses dengan index (data[0]) tapi tidak bisa append, remove, dll.

## tipe data set
* mirip dengan list dan tuple, tetapi set menggunakan `{}`
* perbedaannya terletak pada saat di run, pada data yang sama dia tidak akan terdetect (unique)
* jadi data tidak boleh duplikat
* dan posisi data itu berubah ubah jadi kita tidak dapat mengakses data melalui index
* cara satu satunya hanya menggunakan for loop
* jika dalam list itu menggunakan `append` di set menggunakan `add` untuk menambah data
* untuk menghapus data sama dengan list menggunakan `remove`
* Untuk mengecek apakah elemen ada di set: `if "apel" in buah:`

## method / function
* method digunakan untuk mengelompokkan kode agar bisa dipanggil berkali-kali. Bisa dengan atau tanpa parameter.
* digunakan agar tidak terjadi duplikasi code

## method parameter
* Parameter digunakan untuk mengirim data ke dalam fungsi.
* `print("parameter")` ini sebenarnya adalah method isi didalam tanda kurung itulah parameter
* argumen adalah data yang dimasukan ke parameter

## default value argument
* jadi kalau ada parameter saat memanggil parameter dan g ada isinya itu pasti error
* disini default value digunakan agar saat tidak mengisi parameter akan tetap bisa di eksekusi
* `def helo(name="default value")`
* dengan catatan jika parameter memeiliki devault value maka parameter ke 2 juga harus ada default value
* tetapi bisa jika parameter ke 2 punya default value dan yang pertama tidak memiliki default value
* misal kita memiliki parameter `def hello(firstname="Eka",lastname=" ")`
* dan kita ingin hanya mengisi bagian lastname kita bisa langsung panggil parameternya
* `hello(lastname="Jiparolim")`

## argumen  list
* tambahkan `*` di depan parameter
* digunakan ketika kita ingin mengirim banyak argumen sekaligus ke dalam satu parameter.
* mengubah semua argumen yang dikirim menjadi tuple
* bisa digabung dengan parameter biasa, dengan catatan parameter biasa harus duluan

## Return Value
* digunakan di dalam fungsi (function/method) untuk mengembalikan suatu nilai ke luar fungsi agar bisa disimpan dan digunakan lagi di bagian lain dari program.
* Kegunaan
    - Nilai hasil fungsi bisa disimpan ke dalam variabel.
    - Fungsi menjadi lebih fleksibel dan bisa digunakan ulang.
* jika tanpa return fungsinya hanya untuk mencatatat teks, tanpa bisa digunakan ulang
* retur juga bisa lebih adri 1 data, bisa menggunakan tuple, list boolean dll

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
    - Mengambil semua key	`biodata.keys()`
    - Mengambil semua value	`biodata.values()`
    - Mengambil semua item	`biodata.items()`

## Key Word Argument list
* **kwargs adalah cara untuk mengirim banyak parameter dengan nama (dalam bentuk pasangan key=value) ke dalam fungsi.
* kapan digunakan
    - Saat kamu tidak tahu berapa banyak argumen keyword yang akan dikirim.
    - Ketika ingin membuat fungsi yang fleksibel menerima parameter apapun.
* mengakses nilai dengan aman
```
def sapa(**kwargs):
    nama = kwargs.get("nama", "Tamu")
    print(f"Halo, {nama}!")

sapa(nama="Rina")   # Output: Halo, Rina!
sapa()              # Output: Halo, Tamu!
```

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
* jadi jika kita hanya mengimport sebagian data tidak perlu deklarasi anma file lagi didepan methodnya seperti `modul.tambah()` 

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
