# Konsep
## Big O Notation (Kompleksitas Waktu)
* Singkatnya Big O Notation mengukur seberapa efisien sebuah algoritma
* Fokusnya bukan pada kecepatan dalam hitungan detik(karena itu tergantung device) tetapi bagaimana kinerja sebuah algoritma melambat seiring bertambahnya jumlah data yang diolah /diinput
* Tujuan
    - Membandingan Algoritma: untuk memilih "Algoritma A lebih baik dari Algoritma B" untuk data dalam jumlah besar.
    - Memprediksi Skalabilitas: Membantu dalam Prediksi bagaimana Kode berjalan jika datanya tumbuh dari 100 menuju 1.000.000, apakah akan tetap cepat atau melambat.
    - Menulis Kode yang lebih baik: Melatih intuisi untuk mengenali bagian kode mana yang tidak efisien ( misalnya, nessted loop yang tidak perlu), dan menncari solusi yang lebih baik.
### Cara Kerja
Big O mengabaikan hal-hal kecil dan fokus pada tren pertumbuhan dalam skenario terburuk (worst-case scenario).
* 0(1) - Waktu Konstan (Luar Biasa Cepat)
    -  berarti sebuah operasi membutuhkan waktu yang sama untuk selesai, tidak peduli seberapa besar jumlah data inputnya intinya wau itu ada 10 ataupun 1000 cara yang dilakukan sama saja jadi tidak akan mempengaruhi performa walaupun datanya bertambah.
    - contoh dalam Kode Python, akses element List/Tuple dengan index ataupin akses Dictionary menggunakan key, tidak peduli berapa banyak datanya kita hanya perlu menuju ke index/key yang sudah ditentukan tanpa mengeceknya 1 per 1
* O(Logn) - Waktu Logaritmik
    - berarti waktu eksekusi sebuah algoritma hanya bertambah satu langkah setiap kali jumlah data (n) menjadi dua kali lipat. Ini membuatnya sangat cepat dan skalabel untuk dataset yang luar biasa besar.
    - misal ada 100 data, maka pendekatan linear akan memeriksa 1 per 1 sedangkan pendekatan logaritmik akan membandingkan, apakah lebih tinggi dari 50 atau lebih rendah?, misal lebih rendah, maka akan di cari lagi lebih tinggi dari 25 atau lebih rendah?, akan seperti itu sampai angkanya ketemu
    - itu akan membuat misal data 1000 yaitu naik 10x lipat tetapi usahanya hanya bertambah sedikit itulah O(logn)
    - contohnya seperti binary search
* O(n) - Waktu Linear
    - berarti waktu eksekusi sebuah algoritma tumbuh secara langsung dan sebanding dengan jumlah data masukan, Jika jumlah data menjadi 2x lipat, waktu eksekusinya juga akan menjadi sekitar 2x lipat. Jika data 100x lipat, waktunya juga 100x lipat. Ini adalah salah satu kompleksitas yang paling umum dan intuitif.
    - analogi sederhananya Anda harus mengambil setiap barang satu per satu untuk menghitungnya. Jika ada 10 barang, Anda butuh 10 hitungan. Jika ada 100 barang, Anda butuh 100 hitungan. Waktu yang Anda butuhkan berbanding lurus dengan jumlah barang. Itulah O(n).
    - misal `for angka in data` maka loop ini akan berjalan sebanyak isi dari data tersebut, misal di tambah 100 ya loopnya juga akan ditambah 100 kali
* O(n**2) - waktu kuadratik
    - berarti waktu eksekusi sebuah algoritma tumbuh secara eksponensial (kuadrat) seiring dengan jumlah data masukan (n)
    - contohnya nested loop
    ```
    for i in data_list: 
        for j in data_list:
    ```
* inti dari Big O Notation ini adalah cara kita berpikir apa yang terbaik, dan apa yang harus dibayar, misal ingin data yang terurut maka gunakan list, tetapi jika mengakses list lewat valuenya maka harus menggunakan O(n) yang sedikit lebih lambat, misal ingin ambil datanya tidak peduli urutannya, maka gunakan set O(1) tetapi harga yang harus dibayar itu data pasti tidak terurut

## Rekursif
* rekursi adalah sebuah konsep di mana sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan sebuah masalah, Fungsi tersebut akan terus memanggil dirinya sendiri dengan versi masalah yang lebih kecil, sampai ia mencapai sebuah kondisi berhenti yang sederhana.
* Komponen wajib dalam rekursif
    - Base Case: Ini adalah kondisi berhenti. Ini adalah versi masalah yang paling sederhana yang bisa langsung dijawab tanpa perlu memanggil fungsi lagi. Tanpa base case, fungsi akan terus memanggil dirinya sendiri selamanya
    - Recursif Step: Ini adalah bagian di mana fungsi memanggil dirinya sendiri, tetapi dengan input yang lebih sederhana atau lebih dekat ke base case.
* meskipun lebih clean codingannya tetapi, Bisa jadi lebih lambat dan boros memori karena setiap pemanggilan fungsi disimpan dalam tumpukan memori (call stack), jika base case salah akan terjadi infinite loop, dan lebih susah di debug dibanding loop biasa
* Contoh bisa dilihat di file [Rekursif](rekursif.py)


# Algoritma

## Sorting (Pengurutan)
Di level dasar ada Bubble sort dan selection sort, keduanya adalah fundamental membangun logika pemrograman
### Bubble Sort
* Bubble adalah algoritma paling sederhana untuk pengurutan, logikanya bandingkan elemen pertama dengan kedua jika elemen pertama lebih besar maka tukar posisinya geser ke elemen ke 2 dan 3 bandingkan jika 2 lebih besar geser lagi, sampai elemen paling besar berada di akhir, lalu ulangi prosesnya tetapi abaikan elemen terakhirnya karena sudah paling besar, sampai list terurut
* efisiensi lambat O(n**2) untuk data besar
* Contoh bisa dilihat di file [BubbleSort](bubbleSort.py) atau [sorting](sorting.py)

### Selection sort
* Selection Sort logikanya, misal ada data [9,3,5,7] di awal akan melakukan loop sebanyak len(data) - 1 lalu min akan di isi dengan index i yaitu 0 maka 9 akan menjadi element perbandingan awal, lalu akan di lakukan looping dimulai dari index i + 1 yaitu index 1 yaitu 3, apakah 3 < 9 karna true maka min akan diisi oleh 3 dan akan melakukan perbandingan ke index 2 dan 3 karena index 1 sudah menjadi yang terkecil, setelah di cek maka index i yaitu 0 akan di tuker dengan min yaitu index 1 maka hasilnya [3,9,5,7] dan dilanjut loopnya i = 1 maka min akan diisi oleh index 1 yaitu 9 dan akan dibandingkan dengan i+1 yaitu index 2 dengan value 5 akan di bandingkan apakah 5 lebih kecil dari 9 karena true maka min akan diisi oleh index 2 yaitu 5 akan dibandingkan ke index 3, karena 5 lebih kecil dari 7 maka min tetap index 2 lalu index i yaitu 1 akan di tukar dengan min yaitu index 2 maka hasilnya [3,5,9,7] dan seterusnya, intinya index i akan di tukar oleh index dari variable min
* contoh bisa dilihat di file [Selection Sort](selectionSort.py) atau [Sorting](sorting.py)

## Seraching
Didasar algoritma ini ada linear search dan juga binary search
### Linear Search
* Linear Search adalah algoritma pencarian yang paling dasar, di mana kita mencari sebuah item dalam sebuah koleksi dengan cara memeriksa setiap item satu per satu, dari awal sampai akhir.
* bisa digunakan saat data tidak terurut, dan juga baiknya digunakan pada data yang terbilang sedikit
* Efisiensi performa yaitu O(n)
* logikanya mencari data dan mencocokannya ke target dengan cara satu per satu di cek
* biasanya jika data tidak di temukan baiknya menggunakan return -1 karena 0 bisa mewakili index
* contoh bisa dilihat di [Linear Search](linearSearch.py)

### Binary search
* Binary Search adalah sebuah algoritma pencarian yang sangat efisien untuk menemukan sebuah nilai (target) di dalam sebuah kumpulan data yang sudah terurut. Algoritma ini bekerja dengan metode "bagi dan taklukkan" (divide and conquer), di mana ia secara berulang kali membagi area pencarian menjadi dua bagian dan mengabaikan bagian yang tidak relevan.
* Tujuan utama Binary Search adalah untuk menemukan posisi sebuah item dalam daftar secara jauh lebih cepat daripada Linear Search, terutama pada kumpulan data yang sangat besar.
* Efisiensi O(logn) bisa dibilang cepat
* kekurangannya data harus dalam keadaan terurut
* inti dari logikanya adalah mencocokan nilai tengah dengan target, jika target lebih besar dari nilai tengah berarti sisi kiri tidak relevan maka data kiri dan tengah akan di ubah (visualisasinya seperti dihapus) karena sudah pasti tidak ada disitu datanya, dia akan melakukan itu terus sampai nilai tengah == target atau bahkan loop sudah bernilai false jika posisi index  kiri sudah lebih besar dari kanan dan mereturn -1
* contoh bisa dilihat di [Binary Search](binarySearch.py)

