# Si Jago Merah: Simulasi Pemadaman Kebakaran Hutan

Simulasi berbasis terminal untuk memodelkan penyebaran api pada kebakaran hutan dan strategi pemadaman menggunakan truk pemadam. Proyek ini dibuat untuk memenuhi Tugas Besar 01 mata kuliah **WI1102 Berpikir Komputasional**, Semester 1 2026/2027, STEI-K Institut Teknologi Bandung.

**Anggota Kelompok 01 (K-34):**
1. Aksa Rachman (19626104)
2. Mahesa Rahasia Hati Kahfilano (19626020)
3. Davin Gusti Nurandi (19626014)
4. Fathyakan Thorique Zidane (19626038)

*Dosen Pembimbing: Muhammad Shiddiq Sayyid Hashuro, S.T., M.Eng., Ph.D.*

---

## Tentang Program

Kebakaran hutan (karhutla) merupakan bencana yang sering terjadi di Indonesia dan sangat sulit diprediksi serta dipadamkan secara langsung. Untuk mempelajari bagaimana api menyebar dan bagaimana strategi pemadaman yang efektif tanpa harus menghadapi risiko di lapangan, kami membuat **Si Jago Merah**.

Program ini memodelkan hutan sebagai grid 10x10. Api menyebar secara dinamis mengikuti arah dan kecepatan angin, sementara satu unit truk pemadam bergerak otomatis untuk memadamkan pohon terbakar terdekat. Simulasi berjalan per *tick* (waktu diskrit) dan menampilkan visualisasi grid secara *real-time* di terminal.

## Penerapan Berpikir Komputasional

Proyek ini dirancang menggunakan 4 pilar berpikir komputasional:
- **Dekomposisi:** Memecah masalah besar menjadi bagian input, proses simulasi (pergerakan api & truk), dan output (visualisasi & rekap).
- **Pengenalan Pola:** Mengidentifikasi pola penyebaran api berdasarkan arah angin dan pola pergerakan truk.
- **Abstraksi:** Menyederhanakan hutan nyata menjadi grid 10x10, waktu kontinu menjadi *tick*, dan kondisi cuaca menjadi parameter statis.
- **Algoritma:** Menyusun langkah-langkah sekuensial (Sequence), percabangan (Selection), perulangan (Repetition), penggunaan array 2D, dan pembagian sub-program.

---

## Aturan Simulasi

- **Grid 10x10:** Setiap sel mewakili satu pohon dengan 6 kondisi: `sehat`, `terbakar`, `sedang dipadamkan`, `basah`, `padam`, dan `hangus`.
- **Penyebaran Api:** Terjadi setiap 5 *tick*. Api menyebar ke arah searah angin dan dua arah tegak lurus (angin N, S, E, atau W).
- **Burn Timer:** Pohon yang terbakar akan menjadi `hangus` jika melewati batas waktu, tergantung kecepatan angin.
- **Truk Pemadam:** Bergerak 1 petak per *tick* menuju api terdekat (Manhattan Distance). Jika ada jarak yang sama, dipilih pohon dengan skor bahaya tertinggi.
- **Pemadaman:** Saat tiba di target, truk menyiram area 3x3. Pohon terbakar menjadi `sedang dipadamkan`, pohon sehat menjadi `basah`. Setelah 3 *tick*, area tersebut menjadi `padam`.
- **Game Over:** Simulasi berhenti jika tidak ada lagi pohon berstatus `terbakar` atau `sedang dipadamkan`.

**Parameter Angin:**

| Kecepatan | Peluang Searah | Peluang Samping | Batas Hangus |
| :--- | :---: | :---: | :---: |
| Rendah | 30% | 3% | 15 tick |
| Sedang | 60% | 6% | 12 tick |
| Tinggi | 70% | 7% | 10 tick |

---

## Penjelasan Subprogram

Berikut adalah penjelasan dari fungsi-fungsi yang digunakan dalam program sesuai dengan laporan akhir:

- **`cetak_grid`**
  Fungsi ini bertanggung jawab menampilkan seluruh kondisi simulasi ke layar. Fungsi ini bukan hanya grid 10x10 dengan emoji yang ditampilkan, tetapi juga informasi pendukung: jumlah pohon untuk setiap kondisi (selamat, terbakar, hangus, padam, basah), posisi dan status truk, target truk saat ini beserta ETA (perkiraan berapa tick lagi truk sampai di target), dan juga sisa tick sampai api menyebar lagi. Tujuan fungsi ini untuk memudahkan pengguna dalam menganalisis apa yang terjadi di tick tersebut tanpa harus mengingat angka-angka sebelumnya.

- **`cetak_rekap`**
  Fungsi ini menampilkan rekap akhir setelah simulasi selesai. Rekap terdiri atas total tick yang dibutuhkan, jumlah pohon di setiap kondisi akhir (selamat, padam, basah, hangus), dan persentase masing-masing.

- **`mencari_jarak`**
  Fungsi ini digunakan untuk menghitung jarak Manhattan antara dua titik pada grid. Jarak Manhattan diukur berdasarkan jumlah jarak horizontal ditambah jarak vertikal. Fungsi ini digunakan di beberapa situasi, terutama untuk menentukan pohon mana yang paling dekat dengan truk dan untuk menghitung ETA di `cetak_grid`.

- **`dalam_grid`**
  Fungsi ini bertugas sebagai pengaman yang memeriksa posisi (baris, kolom) dalam batas grid 10x10. Fungsi ini bertugas untuk memeriksa apakah koordinat yang dimasukin valid dan memang benar-benar berada di dalam grid. Fungsi ini wajib dipanggil sebelum mengakses grid dengan indeks apapun karena akses di luar batas akan menyebabkan error dan dari sintaks Python itu sendiri, di mana akan mengartikan indeks negatif sebagai akses dari belakang, yang bisa membuat bug sulit dilacak.

- **`probabilitas_penyebaran`**
  Fungsi ini menentukan apakah penyebaran api berhasil terjadi atau tidak. Fungsi akan mengambil satu angka acak dari 0 sampai 100, lalu membandingkan dengan persentase yang diinginkan. Jika angka acaknya lebih kecil atau sama dengan persentase, penyebaran dianggap berhasil. Dengan cara ini, penentuan penyebaran dengan persentase 30% akan benar-benar menghasilkan sekitar 30 keberhasilan dari 100 percobaan.

- **`menghitung_skor`**
  Fungsi ini menghitung tingkat bahaya sebuah pohon yang sedang terbakar. Fungsi ini dibangun dengan dasar logika bahwa pohon yang dikelilingi banyak pohon sehat dan banyak pohon yang terbakar lebih berbahaya karena api memiliki lebih banyak pilihan untuk menyebar. Setiap tetangga sehat memberikan +1 poin, dan jika tetangga tersebut berada searah dengan angin, poinnya akan ditambah kembali +1 karena api lebih mudah menyebar ke arah tersebut. Selain itu, setiap tetangga yang terbakar akan memberikan +5 poin. Skor ini digunakan sebagai penentu akhir saat terdapat beberapa pohon terbakar yang jaraknya sama dari truk. Fungsi akan memetakan truk agar memilih pohon terbakar yang paling berpotensi menyebar luas.

- **`mengubah_kondisi_pohon`**
  Fungsi ini mengubah kondisi sebuah pohon pada posisi tertentu menjadi kondisi baru. Semua perubahan kondisi pohon di program ini akan selalu melewati fungsi ini agar konsisten dan mudah dilacak.

- **`menambahkan_burn_timer`**
  Fungsi ini akan menambah burn timer sebuah pohon sebesar 1. Fungsi ini akan dipanggil setiap tick untuk setiap pohon yang berstatus terbakar atau sedang dipadamkan.

- **`mencari_target_pohon`**
  Fungsi ini menentukan pohon berikutnya yang akan menjadi target untuk truk. Fungsi bekerja dengan menelusuri seluruh grid, dan setiap pohon yang sedang terbakar, dilakukan perhitungan jarak dari truk dan skor bahayanya. Prioritas utama adalah jarak terdekat, sehingga truk tidak akan menyeberang jauh jika terdapat api di dekatnya. Namun jika terdapat beberapa pohon dengan jarak yang sama persis, skor bahaya akan digunakan sebagai penentu dengan memilih yang paling berbahaya. Fungsi ini mengembalikan posisi target, atau (-1,-1) jika sudah tidak terdapat pohon yang terbakar.

- **`tandai_area_pemadaman`**
  Fungsi ini akan dipanggil ketika truk tiba di target untuk menandai seluruh area 3x3 di sekitar posisi truk. Pohon-pohon yang sedang terbakar di area tersebut akan diubah menjadi sedang dipadamkan, dan pohon-pohon sehat di sekitarnya diubah menjadi basah agar tidak ikut terbakar saat api menyebar. Konsep ini mirip dengan cara kerja pemadam kebakaran di dunia nyata yang membuat semacam sekat basah di sekitar api.

- **`gerak_truk`**
  Fungsi ini menggerakan truk sejauh satu petak menuju target. Prioritasnya adalah sumbu horizontal dulu (arah kiri atau kanan), lalu truk bergerak di sumbu vertikal (arah atas atau bawah). Konsekuensinya, jika target berada diagonal dari truk, truk akan bergerak horizontal terlebih dahulu hingga sejajar, lalu kemudian bergerak secara vertikal. Fungsi ini mengembalikan posisi truk yang baru setelah truk bergerak.

- **`menyelesaikan_pemadaman`**
  Fungsi ini dipanggil setelah truk memadamkan area selama 3 tick untuk mengubah semua pohon yang tadinya berstatus sedang dipadamkan menjadi padam. Dengan begitu, pohon-pohon tersebut sudah benar-benar aman dan tidak akan terbakar lagi.

- **`update_truk`**
  Fungsi ini bertugas sebagai pengendali utama truk. Fungsi ini dipanggil sekali per tick dari main loop. Perilakunya tergantung dari status truk saat itu. Jika statusnya sedang mendatangi pohon, maka terdapat beberapa kemungkinan: target bisa saja sudah hangus terlebih dahulu sebelum truk sampai, sehingga program akan melakukan pemindaian terlebih dulu pada kondisi target. Jika kondisi tidak valid, maka truk akan mencari target baru. Jika ternyata sudah tidak terdapat pohon yang terbakar, truk diam di tempat. Jika target masih valid dan truk belum sampai, truk bergerak satu petak. Setelah bergerak, fungsi akan melakukan pemindaian pada posisi truk; Jika truk sudah sampai target, maka truk langsung mulai memadamkan area. Jika statusnya sedang memadamkan, truk menambah hitungan lama memadamkan, dan setelah hitungan mencapai 3, area terpadamkan dan truk siap mencari target baru.

---

## Struktur Repositori

```text
.
├── README.md
├── source-code/
│   └── Python_Tubes.py
├── flowchart/
│   └── link.md
├── ppt/
│   └── Si Jago Merah - Presentasi.pdf
└── laporan-akhir/
    └── Laporan Akhir - Si Jago Merah.pdf