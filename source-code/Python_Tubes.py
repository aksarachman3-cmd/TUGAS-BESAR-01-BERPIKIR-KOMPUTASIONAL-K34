'''
Author              : Kelompok 01
Tanggal Pengerjaan  : 19-21 Oktober 2026

PROGRAM SIMULASI PEMADAMAN KEBAKARAN HUTAN

Deskripsi:
Simulasi ini memodelkan kebakaran hutan pada grid 10x10, di mana api menyebar dari
pohon ke pohon mengikuti arah dan kecepatan angin, sementara satu unit truk pemadam
berusaha memadamkan api dengan mendatangi pohon terbakar terdekat. Setiap pohon punya
kondisi (sehat, terbakar, sedang dipadamkan, basah, padam, hangus) dan burn timer yang
membuat pohon yang terlalu lama terbakar akan hangus dengan sendirinya. Simulasi
berjalan per tick dan menampilkan grid di setiap tick-nya supaya proses penyebaran
api maupun pergerakan truk bisa diamati langkah demi langkah.

Cara Kerja Simulasi Secara Umum:
Simulasi diawali dengan pengguna memasukkan jumlah titik api, posisi awal truk,
koordinat setiap titik api, arah angin, dan kecepatan angin. Setelah semua parameter
siap, program masuk ke main loop yang berjalan per tick. Di setiap tick, program
melakukan lima tahap berurutan: memperbarui burn timer setiap pohon yang sedang
terbakar (sekaligus mengubah pohon yang sudah terlalu lama terbakar menjadi hangus),
menyebarkan api ke pohon tetangga bila tick saat ini kelipatan 5, menerapkan hasil
penyebaran tersebut ke grid, memindahkan truk pemadam (bergerak menuju target atau
memadamkan area bila sudah sampai), lalu memeriksa apakah masih ada api yang tersisa.
Bila sudah tidak ada pohon yang berstatus terbakar maupun sedang dipadamkan, program
menampilkan rekap akhir dan berhenti.

ATURAN SIMULASI
1.  Grid berukuran 10x10. Setiap sel dapat berisi satu pohon dengan salah satu dari
    enam kondisi: sehat, terbakar, sedang dipadamkan, basah, padam, atau hangus.
2.  Api menyebar setiap 5 tick, tepatnya saat tick % 5 == 0. Pada tick tersebut, api
    menyebar ke tiga arah sekaligus: searah angin (peluang paling besar), dan dua arah
    tegak lurus terhadap angin.
3.  Peluang penyebaran dan batas hangus bergantung pada kecepatan angin yang dipilih:
    kecepatan rendah berarti api menyebar pelan dan pohon lebih cepat hangus; kecepatan
    tinggi berarti api menyebar agresif dan pohon bertahan lebih lama. Nilai pastinya:
    - Rendah : searah 30%, samping 3%, batas hangus 10 tick
    - Sedang : searah 60%, samping 6%, batas hangus 12 tick
    - Tinggi : searah 70%, samping 7%, batas hangus 15 tick
4.  Arah angin mengikuti konvensi mata angin: N berarti api menyebar ke atas (baris
    berkurang), S ke bawah (baris bertambah), E ke kanan (kolom bertambah), W ke kiri
    (kolom berkurang).
5.  Setiap pohon yang berstatus terbakar atau sedang dipadamkan mengalami penambahan
    burn timer sebesar 1 per tick. Begitu burn timer mencapai batas hangus, pohon
    berubah menjadi hangus dan tidak bisa dipadamkan lagi.
6.  Penyebaran api dilakukan dalam dua fase terpisah supaya tidak terjadi rantai
    penyebaran dalam satu tick. Pertama program mencatat dulu pohon-pohon mana yang
    akan terbakar ke dalam array sementara bernama akan_terbakar, baru setelah
    semua pengecekan selesai, hasilnya diterapkan sekaligus ke grid.
7.  Truk pemadam bergerak 1 petak per tick menuju pohon terbakar terdekat (diukur
    dengan jarak Manhattan). Bila ada beberapa pohon dengan jarak yang sama, dipilih
    yang skor bahayanya paling tinggi.
8.  Sesampainya di target, truk menandai seluruh area 3x3 di sekitarnya: pohon yang
    sedang terbakar diubah menjadi sedang dipadamkan, sedangkan pohon sehat di
    sekitarnya diubah menjadi basah supaya tidak ikut terbakar.
9.  Setelah 3 tick memadamkan, semua pohon yang berstatus sedang dipadamkan di area
    tersebut berubah menjadi padam.
10. Simulasi berakhir ketika sudah tidak ada lagi pohon berstatus terbakar maupun
    sedang dipadamkan.

KAMUS
emoji_pohon                     = dictionary yang memetakan setiap kondisi pohon ke emoji
                                  (sehat, terbakar, sedang dipadamkan, basah, padam, hangus)
emoji_truk                      = emoji untuk merepresentasikan truk pemadam
kondisi                         = array 2D berisi kondisi setiap pohon pada grid
burn_timer                      = array 2D berisi lama (dalam tick) setiap pohon telah terbakar
akan_terbakar                   = array 2D boolean sementara untuk menandai pohon yang akan
                                  terbakar pada tick tersebut
jumlah_titik_api                = jumlah titik api awal yang dimasukkan oleh pengguna
koordinat_baris_truk            = baris posisi awal truk pemadam
koordinat_kolom_truk            = kolom posisi awal truk pemadam
titik_api_awal                  = list berisi koordinat setiap titik api awal
arah_angin                      = arah angin yang dipilih pengguna (N, S, E, atau W)
kecepatan_angin                 = kecepatan angin yang dipilih pengguna (rendah, sedang, tinggi)
persen_searah                   = persentase peluang penyebaran api searah angin
persen_samping                  = persentase peluang penyebaran api tegak lurus angin
batas_hangus                    = jumlah tick yang dibutuhkan pohon terbakar untuk menjadi hangus
pohon_lain_searah               = delta posisi menuju sel searah angin
pohon_lain_samping1             = delta posisi menuju sel tegak lurus angin (arah pertama)
pohon_lain_samping2             = delta posisi menuju sel tegak lurus angin (arah kedua)
truk_baris                      = baris posisi truk pemadam saat ini
truk_kolom                      = kolom posisi truk pemadam saat ini
status_truk                     = status truk pemadam ("mendatangi pohon" atau "memadamkan")
lama_memadam                    = lama (dalam tick) truk telah memadamkan target saat ini
target_baris                    = baris target pohon yang sedang dituju atau dipadamkan
target_kolom                    = kolom target pohon yang sedang dituju atau dipadamkan
tick                            = penghitung waktu simulasi
baris, kolom                    = variabel iterasi untuk mengakses indeks grid
i, j                            = variabel iterasi untuk menelusuri grid
check_double_input              = fungsi untuk memeriksa apakah koordinat titik api yang
                                  akan dimasukkan sudah ada di titik_api_awal (mencegah
                                  duplikasi koordinat titik api)
validasi_input                  = konsep validasi nilai yang dimasukkan pengguna. Setiap
                                  input dibungkus while loop agar pengguna tidak bisa
                                  memasukkan nilai di luar batas. Aturan:
                                  - jumlah_titik_api harus >= 1
                                  - koordinat_baris_truk dan koordinat_kolom_truk
                                    harus 0-9
                                  - koordinat baris dan kolom titik api harus 0-9
                                  - kombinasi (baris, kolom) titik api tidak boleh
                                    duplikat (dicek lewat check_double_input)
                                  Selama input belum valid, program meminta ulang
                                  sampai nilainya benar.

PENJELASAN SUB PROGRAM

Dalam pembuatannya, program ini memanfaatkan sejumlah sub program agar kode tidak menumpuk pada satu bagian saja. 
Sub program yang digunakan terdiri dari fungsi untuk tampilan, fungsi perhitungan, fungsi pengubah data pohon, 
serta fungsi pengendali truk pemadam.

1) Fungsi Tampilan

i. cetak_grid
Fungsi ini bertanggung jawab menampilkan seluruh kondisi simulasi ke layar. 
Fungsi ini bukan hanya grid 10x10 dengan emoji yang ditampilkan, 
tetapi juga informasi pendukung: jumlah pohon untuk setiap kondisi (selamat, terbakar, hangus, padam, basah), 
posisi dan status truk, target truk saat ini beserta ETA (perkiraan berapa tick lagi truk sampai di target), 
dan juga sisa tick sampai api menyebar lagi. Tujuan fungsi ini untuk memudahkan pengguna dalam menganalisis 
apa yang terjadi di tick tersebut tanpa harus mengingat angka-angka sebelumnya.

ii. cetak_rekap
Fungsi ini menampilkan rekap akhir setelah simulasi selesai. 
Rekap terdiri atas total tick yang dibutuhkan, jumlah pohon di setiap kondisi akhir (selamat, padam, basah, hangus), 
dan persentase masing-masing.

2) Fungsi Perhitungan

i) mencari_jarak
Fungsi ini digunakan untuk menghitung jarak Manhattan antara dua titik pada grid. 
Jarak Manhattan diukur berdasarkan jumlah jarak horizontal ditambah jarak vertikal. 
Fungsi ini digunakan di beberapa situasi, terutama 
untuk menentukan pohon mana yang paling dekat dengan truk dan untuk menghitung ETA di cetak_grid.

ii) dalam_grid
Fungsi ini bertugas sebagai pengaman yang memeriksa posisi (baris, kolom) dalam batas grid 10x10. 
Fungsi ini bertugas untuk memeriksa apakah koordinat yang dimasukkan valid dan memang benar-benar berada di dalam grid. 
Fungsi ini wajib dipanggil sebelum mengakses grid dengan indeks apapun karena akses di luar batas 
akan menyebabkan error dan dari sintaks Python itu sendiri, di mana akan mengartikan indeks negatif sebagai akses dari belakang, 
yang bisa membuat bug sulit dilacak.

iii) probabilitas_penyebaran
Fungsi ini menentukan apakah penyebaran api berhasil terjadi atau tidak. 
Fungsi akan mengambil satu angka acak dari 0 sampai 100, lalu membandingkan dengan persentase yang diinginkan. 
Jika angka acaknya lebih kecil atau sama dengan persentase, penyebaran dianggap berhasil. 
Dengan cara ini, penentuan penyebaran dengan persentase 30% akan benar-benar menghasilkan sekitar 30 keberhasilan dari 100 percobaan.

iv) menghitung_skor
Fungsi ini menghitung tingkat bahaya sebuah pohon yang sedang terbakar. 
Fungsi ini dibangun dengan dasar logika bahwa pohon yang dikelilingi banyak pohon sehat dan banyak pohon yang terbakar lebih berbahaya 
karena api memiliki lebih banyak pilihan untuk menyebar. Setiap tetangga sehat memberikan +1 poin, dan 
jika tetangga tersebut berada searah dengan angin, poinnya akan ditambah kembali +1 
karena api lebih mudah menyebar ke arah tersebut. 
Selain itu, setiap tetangga yang terbakar akan memberikan +5 poin. 
Skor ini digunakan sebagai penentu akhir saat terdapat beberapa pohon terbakar yang jaraknya sama dari truk. 
Fungsi akan memetakan truk agar memilih pohon terbakar yang paling berpotensi menyebar luas.

3) Fungsi Pengubah Data Pohon

i) mengubah_kondisi_pohon
Fungsi ini mengubah kondisi sebuah pohon pada posisi tertentu menjadi kondisi baru. 
Semua perubahan kondisi pohon di program ini akan selalu melewati fungsi ini agar konsisten dan mudah dilacak.

ii) menambahkan_burn_timer
Fungsi ini akan menambah burn timer sebuah pohon sebesar 1. 
Fungsi ini akan dipanggil setiap tick untuk setiap pohon yang berstatus terbakar atau sedang dipadamkan.

4) Fungsi Pengendali Truk Pemadam

i) mencari_target_pohon
Fungsi ini menentukan pohon berikutnya yang akan menjadi target untuk truk. 
Fungsi bekerja dengan menelusuri seluruh grid, dan setiap pohon yang sedang terbakar, 
dilakukan perhitungan jarak dari truk dan skor bahayanya. Prioritas utama adalah jarak terdekat, 
sehingga truk tidak akan menyeberang jauh jika terdapat api di dekatnya. 
Namun jika terdapat beberapa pohon dengan jarak yang sama persis, 
skor bahaya akan digunakan sebagai penentu dengan memilih yang paling berbahaya. 
Fungsi ini mengembalikan posisi target, atau (-1,-1) jika sudah tidak terdapat pohon yang terbakar.

ii) tandai_area_pemadaman
Fungsi ini akan dipanggil ketika truk tiba di target untuk menandai seluruh area 3x3 di sekitar posisi truk. 
Pohon-pohon yang sedang terbakar di area tersebut akan diubah menjadi sedang dipadamkan, 
dan pohon-pohon sehat di sekitarnya diubah menjadi basah agar tidak ikut terbakar saat api menyebar. 
Konsep ini mirip dengan cara kerja pemadam kebakaran di dunia nyata yang membuat semacam sekat basah di sekitar api.

iii) gerak_truk
Fungsi ini menggerakkan truk sejauh satu petak menuju target. Prioritasnya adalah sumbu horizontal dulu (arah kiri atau kanan), 
lalu truk bergerak di sumbu vertikal (arah atas atau bawah). 
Konsekuensinya, jika target berada diagonal dari truk, truk akan bergerak horizontal terlebih dahulu hingga sejajar, 
lalu kemudian bergerak secara vertikal. Fungsi ini mengembalikan posisi truk yang baru setelah truk bergerak.

iv) menyelesaikan_pemadaman
Fungsi ini dipanggil setelah truk memadamkan area selama 3 tick untuk mengubah semua pohon yang tadinya berstatus sedang dipadamkan menjadi padam. 
Dengan begitu, pohon-pohon tersebut sudah benar-benar aman dan tidak akan terbakar lagi.

v) update_truk
Fungsi ini bertugas sebagai pengendali utama truk. 
Fungsi ini dipanggil sekali per tick dari main loop. 
Perilakunya tergantung dari status truk saat itu. 
Jika statusnya sedang mendatangi pohon, maka terdapat beberapa kemungkinan: 
target bisa saja sudah hangus terlebih dahulu sebelum truk sampai, sehingga program akan melakukan pemindaian terlebih dulu pada kondisi target. 
Jika kondisi tidak valid, maka truk akan mencari target baru. 
Jika ternyata sudah tidak terdapat pohon yang terbakar, truk diam di tempat.
Jika target masih valid dan truk belum sampai, truk bergerak satu petak. 
Setelah bergerak, fungsi akan melakukan pemindaian pada posisi truk; 
Jika truk sudah sampai target, maka truk langsung mulai memadamkan area. 
Jika statusnya sedang memadamkan, truk menambah hitungan lama memadamkan, 
dan setelah hitungan mencapai 3, area terpadamkan dan truk siap mencari target baru.

5) Fungsi Validasi Input (Tambahan)

check_double_input
Fungsi ini adalah validator input yang mencegah pengguna memasukkan koordinat titik api yang sama dua kali. 
Kalau koordinat duplikat dibiarkan masuk, pohon yang sama akan di-set "terbakar" berulang kali sehingga burn timer, skor bahaya, dan statistik rekap akhir bisa kacau. 
Cara kerjanya: fungsi menerima tiga parameter, yaitu titik_api_awal (list koordinat yang sudah tersimpan), serta baris dan kolom koordinat baru yang akan dicek. 
Program menelusuri seluruh isi list dengan indeks i, lalu membandingkan setiap elemen dengan [baris, kolom]. 
Kalau ada satu saja elemen yang nilainya sama persis, fungsi langsung mengembalikan True. 
Kalau penelusuran selesai tanpa menemukan kecocokan, fungsi mengembalikan False. 
Nilai kembalian ini dipakai oleh loop input: kalau True, program menampilkan pesan "Maaf, koordinat sudah pernah dimasukkan" 
lalu mengulang permintaan baris dan kolom untuk titik api yang sama; kalau False, koordinat baru langsung di-append ke titik_api_awal 
dan lanjut ke titik api berikutnya.

Validasi Input
Seluruh pembacaan input pengguna dibungkus while loop agar program tidak pernah memakai nilai yang tidak valid. 
Polanya: minta input, cek syarat, kalau lolos break, kalau tidak tampilkan pesan "Maaf, ..." lalu ulangi. 
Validasi yang dilakukan di antaranya: jumlah_titik_api minimal 1; koordinat baris dan kolom truk harus 0 sampai 9; 
koordinat baris dan kolom titik api harus 0 sampai 9; dan kombinasi (baris, kolom) titik api belum pernah dimasukkan, 
dicek lewat check_double_input. Khusus untuk titik api, validasi baris dan kolom dibungkus satu while loop tambahan yang juga menampung pengecekan duplikat, 
sehingga kalau pengguna memasukkan koordinat duplikat, program hanya mengulang pembacaan titik api yang sedang diisi, bukan mengulang dari titik api pertama.


'''

import random
import time

# Emoji tiap kondisi pohon
emoji_pohon = {"sehat": "🌳",
               "terbakar" : "🔥",
               "sedang dipadamkan" : "🧯",
               "basah" : "💧",
               "padam" : "✅",
               "hangus" : "⬛"}

# Emoji truk pemadam
emoji_truk = "🚒"

# Grid utama: kondisi pohon, burn timer, dan penanda sementara saat penyebaran api
kondisi = [["sehat"]* 10 for i in range(10)]
burn_timer = [[0]* 10 for i in range(10)]
akan_terbakar = [[False] * 10 for i in range(10)]


# Menampilkan grid, statistik, posisi truk, target, ETA, dan sisa tick penyebaran
def cetak_grid(tick, truk_baris, truk_kolom, status_truk, target_baris, target_kolom, arah_angin, kecepatan_angin):
    if target_baris != -1:
        eta = mencari_jarak(truk_baris, truk_kolom, target_baris, target_kolom)
    else:
        eta = "-"
    sisa_tick_nyebar = 5 - (tick % 5)
    if sisa_tick_nyebar == 5:
        sisa_tick_nyebar = 0

    print(f"\n{'═' * 50}")
    print(f"  TICK {tick}  |  Angin: {arah_angin.lower()}, {kecepatan_angin}")
    print(f"{'═' * 50}")
    print()

    print("  ", end="")
    for j in range(10):
        print(f"{j} ", end="")
    print()

    for i in range(10):
        print(f"{i} ", end="")
        for j in range(10):
            if i == truk_baris and j == truk_kolom:
                print(emoji_truk + " ", end="")
            elif(kondisi[i][j]=="sehat"):
                print(emoji_pohon["sehat"] + " ", end="")
            elif(kondisi[i][j]=="terbakar"):
                print(emoji_pohon["terbakar"] + " ", end="")
            elif(kondisi[i][j]=="sedang dipadamkan"):
                print(emoji_pohon["sedang dipadamkan"] + " ", end="")
            elif(kondisi[i][j]=="basah"):
                print(emoji_pohon["basah"] + " ", end="")
            elif(kondisi[i][j]=="padam"):
                print(emoji_pohon["padam"] + " ", end="")
            else:
                print(emoji_pohon["hangus"] + " ", end="")
        print()

    print()

    sehat  = 0
    bakar  = 0
    hangus = 0
    padam  = 0
    basah  = 0
    for i in range(10):
        for j in range(10):
            if kondisi[i][j] == "sehat":
                sehat += 1
            elif kondisi[i][j] == "terbakar":
                bakar += 1
            elif kondisi[i][j] == "hangus":
                hangus += 1
            elif kondisi[i][j] == "padam":
                padam += 1
            elif kondisi[i][j] == "basah":
                basah += 1

    print(f"Pohon selamat  : {sehat}")
    print(f"Pohon terbakar : {bakar}")
    print(f"Pohon hangus   : {hangus}")
    print(f"Pohon padam    : {padam}")
    print(f"Pohon basah    : {basah}")
    print()

    if status_truk == "mendatangi pohon":
        print(f"Unit  : moving → baris={target_baris}, kolom={target_kolom} | eta: {eta} tick")
    else:
        print(f"Unit  : working @ baris={truk_baris}, kolom={truk_kolom} | memadamkan area...")

    print(f"Api nyebar dalam: {sisa_tick_nyebar} tick lagi")


# Jarak Manhattan antara dua titik
def mencari_jarak(baris1, kolom1, baris2, kolom2):
    return abs(baris1 - baris2) + abs(kolom1 - kolom2)


# Cek posisi masih di dalam grid
def dalam_grid(baris, kolom):
    return (0<=baris<10 and 0<=kolom<10)


# Menentukan apakah penyebaran api berhasil
def probabilitas_penyebaran(persen):
    return (random.randint(1,100)<=persen)


# Skor bahaya pohon terbakar berdasarkan tetangga sehat dan arah angin
def menghitung_skor(baris, kolom, delta_posisi_pohon_searah):
    skor = 0

    # Tetangga kiri
    if(dalam_grid(baris,kolom-1) and kondisi[baris][kolom-1]=="sehat"):
        skor +=1
        if(delta_posisi_pohon_searah[0]==0 and delta_posisi_pohon_searah[1]==-1):
            skor+=1
    elif(dalam_grid(baris,kolom-1) and kondisi[baris][kolom-1]=="terbakar"):
        skor+=5

    # Tetangga kanan
    if(dalam_grid(baris,kolom+1) and kondisi[baris][kolom+1]=="sehat"):
        skor +=1
        if(delta_posisi_pohon_searah[0]==0 and delta_posisi_pohon_searah[1]==1):
            skor+=1
    elif(dalam_grid(baris,kolom+1) and kondisi[baris][kolom+1]=="terbakar"):
        skor+=5

    # Tetangga bawah
    if(dalam_grid(baris+1,kolom) and kondisi[baris+1][kolom]=="sehat"):
        skor +=1
        if(delta_posisi_pohon_searah[0]==1 and delta_posisi_pohon_searah[1]==0):
            skor+=1
    elif(dalam_grid(baris+1,kolom) and kondisi[baris+1][kolom]=="terbakar"):
        skor+=5
            
    # Tetangga atas
    if(dalam_grid(baris-1,kolom) and kondisi[baris-1][kolom]=="sehat"):
        skor +=1
        if(delta_posisi_pohon_searah[0]==-1 and delta_posisi_pohon_searah[1]==0):
            skor+=1
    elif(dalam_grid(baris-1,kolom) and kondisi[baris-1][kolom]=="terbakar"):
            skor+=5

    return skor


# Ubah kondisi pohon
def mengubah_kondisi_pohon(baris,kolom,kondisi_baru):
    kondisi[baris][kolom] = kondisi_baru


# Tambah burn timer pohon
def menambahkan_burn_timer(baris,kolom):
    burn_timer[baris][kolom]+=1


# Cari target pohon terbakar terdekat, tie-break pakai skor bahaya
def mencari_target_pohon(truk_baris, truk_kolom, delta_posisi_pohon_searah):
    pohon_terdekat_baris = -1
    pohon_terdekat_kolom = -1
    jarak_terdekat = 9999
    skor_terbaik = -1
    for baris in range(10):
        for kolom in range(10):
            if(kondisi[baris][kolom]!="terbakar"):
                continue
            skor = menghitung_skor(baris,kolom,delta_posisi_pohon_searah)
            jarak = mencari_jarak(truk_baris, truk_kolom, baris, kolom)

            # Kandidat jarak lebih dekat
            if (jarak < jarak_terdekat):
                pohon_terdekat_baris = baris
                pohon_terdekat_kolom = kolom
                jarak_terdekat = jarak
                skor_terbaik = skor
            # Jarak sama, pilih skor bahaya lebih tinggi
            elif (jarak == jarak_terdekat and skor > skor_terbaik):
                pohon_terdekat_baris = baris
                pohon_terdekat_kolom = kolom
                skor_terbaik = skor

    return pohon_terdekat_baris, pohon_terdekat_kolom


# Tandai area 3x3: yang terbakar jadi sedang dipadamkan, yang sehat jadi basah
def tandai_area_pemadaman(baris,kolom):
    for i in range(-1,2):
        for j in range(-1,2):
            if not dalam_grid(baris+i, kolom+j):
                continue
            if(kondisi[baris+i][kolom+j]=="terbakar"):
                mengubah_kondisi_pohon(baris+i,kolom+j,"sedang dipadamkan")
            elif(kondisi[baris+i][kolom+j]=="sehat"):
                mengubah_kondisi_pohon(baris+i,kolom+j,"basah")


# Gerakkan truk satu petak menuju target
def gerak_truk(truk_baris,truk_kolom,target_baris,target_kolom):
    if(target_baris<truk_baris):
        truk_baris-=1
    elif(target_baris>truk_baris):
        truk_baris+=1
    else:
        if(target_kolom>truk_kolom):
            truk_kolom+=1
        if(target_kolom<truk_kolom):
            truk_kolom-=1
    return truk_baris, truk_kolom


# Ubah pohon yang sedang dipadamkan menjadi padam setelah 3 tick
def menyelesaikan_pemadaman(baris,kolom):
    for i in range(-1,2):
        for j in range(-1,2):
            if not dalam_grid(baris+i, kolom+j):
                continue
            if(kondisi[baris+i][kolom+j]=="sedang dipadamkan"):
                mengubah_kondisi_pohon(baris+i,kolom+j,"padam")


# Pengendali utama truk per tick
def update_truk(delta_posisi_pohon_searah):
    global truk_baris, truk_kolom, status_truk, lama_memadam, target_baris, target_kolom

    if(status_truk=="mendatangi pohon"):
        # Validasi target; kalau sudah tidak terbakar, cari target baru
        if (target_baris==-1 or kondisi[target_baris][target_kolom] != "terbakar"):
            target_baris,target_kolom = mencari_target_pohon(truk_baris,truk_kolom, delta_posisi_pohon_searah)

        # Tidak ada api lagi
        if target_baris == -1:
            return

        # Sudah di target, mulai memadamkan
        if(truk_baris==target_baris and truk_kolom==target_kolom):
            status_truk = "memadamkan"
            lama_memadam = 0
            tandai_area_pemadaman(truk_baris,truk_kolom)
            return

        # Bergerak satu petak
        truk_baris, truk_kolom = gerak_truk(truk_baris, truk_kolom, target_baris, target_kolom)

        # Cek lagi setelah bergerak
        if(truk_baris==target_baris and truk_kolom==target_kolom):
            status_truk = "memadamkan"
            lama_memadam = 0
            tandai_area_pemadaman(truk_baris,truk_kolom)
            return

    else:
            # Proses memadamkan selama 3 tick
            lama_memadam += 1
            if lama_memadam >= 3:
                menyelesaikan_pemadaman(truk_baris, truk_kolom)
                status_truk  = "mendatangi pohon"
                lama_memadam = 0
                target_baris = -1
                target_kolom = -1

#Mengecek Input Titik Api yang Double
def check_double_input(titik_api_awal,baris,kolom):
    for i in range(len(titik_api_awal)):
        if(titik_api_awal[i] == [baris,kolom]):
            return True
    return False
    
# Rekap akhir simulasi
def cetak_rekap(tick):
    sehat  = 0
    padam  = 0
    basah  = 0
    hangus = 0

    for i in range(10):
        for j in range(10):
            if kondisi[i][j] == "sehat":
                sehat += 1
            elif kondisi[i][j] == "padam":
                padam += 1
            elif kondisi[i][j] == "basah":
                basah += 1
            elif kondisi[i][j] == "hangus":
                hangus += 1

    dipadamkan = padam + basah


    print(f"\n╔══════════════════════════════════╗")
    print(f"║         SIMULASI SELESAI          ║")
    print(f"╠══════════════════════════════════╣")
    print(f"║ Total tick        : {tick:<3}          ║")
    print(f"║ Pohon awal        : 100          ║")
    print(f"║                                  ║")
    print(f"║ Pohon selamat     : {sehat:<3}  ({sehat}%)   ║")
    print(f"║ Pohon padam       : {padam:<3}  ({padam}%)   ║")
    print(f"║ Pohon basah       : {basah:<3}  ({basah}%)   ║")
    print(f"║ Pohon hangus      : {hangus:<3}  ({hangus}%)   ║")
    print(f"╚══════════════════════════════════╝")


# Input pengguna
print("\n === SISTEM SIMULASI PEMADAMAN KEBAKARAN HUTAN ===")
print()

while True:
  jumlah_titik_api = int(input("Masukkan jumlah titik api          : "))
  if(jumlah_titik_api>0):
    print()
    break
  else:
    print("Maaf, jumlah titik api minimal ada 1")

while True:
  koordinat_baris_truk = int(input("Masukkan posisi awal truk (baris)  : "))
  if(0<=koordinat_baris_truk<=9):
    break
  else:
    print("Maaf, koordinat baris truk harus di antara 0 dan 9")

while True:
  koordinat_kolom_truk = int(input("Masukkan posisi awal truk (kolom)  : "))
  if(0<=koordinat_kolom_truk<=9):
    break
  else:
    print("Maaf, koordinat kolom truk harus di antara 0 dan 9")

print()

titik_api_awal = []
for k in range(jumlah_titik_api):
    while True:
        while True:
            baris = int(input(f"Masukkan titik api {k+1} (baris)       : "))
            if(0<=baris<=9):
                break
            else:
                print("Maaf, koordinat baris titik api harus di antara 0 dan 9")
        while True:
            kolom = int(input(f"Masukkan titik api {k+1} (kolom)       : "))
            if(0<=kolom<=9):
                break
            else:
                print("Maaf, koordinat kolom titik api harus di antara 0 dan 9")
        if(check_double_input(titik_api_awal,baris,kolom)):
            print("Maaf, koordinat sudah pernah dimasukkan")
        else:
            break
    titik_api_awal.append([baris,kolom])

print()
arah_angin      = input("Masukkan arah angin (N/E/S/W)      : ").upper()
kecepatan_angin = input("Masukkan kecepatan angin (rendah/sedang/tinggi): ").lower()

print()
print("=== SIMULASI DIMULAI ===")
print()
time.sleep(1)


# Parameter penyebaran berdasarkan kecepatan angin
if kecepatan_angin == "rendah":
    persen_searah  = 30
    persen_samping = 3
    batas_hangus   = 15
elif kecepatan_angin == "sedang":
    persen_searah  = 60
    persen_samping = 6
    batas_hangus   = 12
else:
    persen_searah  = 70
    persen_samping = 7
    batas_hangus   = 10


# Delta arah penyebaran api berdasarkan arah angin
if arah_angin == "N":
    pohon_lain_searah   = (-1, 0)
    pohon_lain_samping1 = (0, 1)
    pohon_lain_samping2 = (0, -1)
elif arah_angin == "S":
    pohon_lain_searah   = (1, 0)
    pohon_lain_samping1 = (0, 1)
    pohon_lain_samping2 = (0, -1)
elif arah_angin == "E":
    pohon_lain_searah   = (0, 1)
    pohon_lain_samping1 = (1, 0)
    pohon_lain_samping2 = (-1, 0)
else:
    pohon_lain_searah   = (0, -1)
    pohon_lain_samping1 = (1, 0)
    pohon_lain_samping2 = (-1, 0)


# Pasang titik api awal dan posisi truk
for baris, kolom in titik_api_awal:
    mengubah_kondisi_pohon(baris, kolom, "terbakar")

truk_baris       = koordinat_baris_truk
truk_kolom       = koordinat_kolom_truk
status_truk      = "mendatangi pohon"
lama_memadam     = 0
target_baris     = -1
target_kolom     = -1

target_baris, target_kolom = mencari_target_pohon(truk_baris, truk_kolom, pohon_lain_searah)


# Kondisi awal tick 0
cetak_grid(0, truk_baris, truk_kolom, status_truk, target_baris, target_kolom, arah_angin, kecepatan_angin)
time.sleep(1)


# Main loop simulasi
tick = 0
while True:
    tick += 1

    # Tahap 1: update burn timer dan ubah pohon yang sudah terlalu lama terbakar
    for i in range(10):
        for j in range(10):
            if kondisi[i][j] == "terbakar" or kondisi[i][j] == "sedang dipadamkan":
                burn_timer[i][j] += 1
                if burn_timer[i][j] >= batas_hangus:
                    kondisi[i][j] = "hangus"

    # Tahap 2 dan 3: penyebaran api setiap 5 tick
    if tick % 5 == 0:
        for i in range(10):
            for j in range(10):
                akan_terbakar[i][j] = False

        for i in range(10):
            for j in range(10):
                if kondisi[i][j] != "terbakar":
                    continue

                # Arah searah angin
                pohon_searah_baris = i + pohon_lain_searah[0]
                pohon_searah_kolom = j + pohon_lain_searah[1]
                if dalam_grid(pohon_searah_baris, pohon_searah_kolom) and kondisi[pohon_searah_baris][pohon_searah_kolom] == "sehat":
                    if probabilitas_penyebaran(persen_searah):
                        akan_terbakar[pohon_searah_baris][pohon_searah_kolom] = True

                # Arah samping pertama
                pohon_samping1_baris = i + pohon_lain_samping1[0]
                pohon_samping1_kolom = j + pohon_lain_samping1[1]
                if dalam_grid(pohon_samping1_baris, pohon_samping1_kolom) and kondisi[pohon_samping1_baris][pohon_samping1_kolom] == "sehat":
                    if probabilitas_penyebaran(persen_samping):
                        akan_terbakar[pohon_samping1_baris][pohon_samping1_kolom] = True

                # Arah samping kedua
                pohon_samping2_baris = i + pohon_lain_samping2[0]
                pohon_samping2_kolom = j + pohon_lain_samping2[1]
                if dalam_grid(pohon_samping2_baris, pohon_samping2_kolom) and kondisi[pohon_samping2_baris][pohon_samping2_kolom] == "sehat":
                    if probabilitas_penyebaran(persen_samping):
                        akan_terbakar[pohon_samping2_baris][pohon_samping2_kolom] = True

        # Terapkan hasil penyebaran
        for i in range(10):
            for j in range(10):
                if akan_terbakar[i][j]:
                    mengubah_kondisi_pohon(i, j, "terbakar")
                    burn_timer[i][j] = 0

    # Tahap 4: truk pemadam
    update_truk(pohon_lain_searah)

    # Tampilkan kondisi tick ini
    cetak_grid(tick, truk_baris, truk_kolom, status_truk, target_baris, target_kolom, arah_angin, kecepatan_angin)

    # Tahap 5: cek apakah simulasi selesai
    ada_api = False
    for i in range(10):
        for j in range(10):
            if kondisi[i][j] == "terbakar" or kondisi[i][j] == "sedang dipadamkan":
                ada_api = True

    if not ada_api:
        print(f"\n🔥 Simulasi selesai di tick {tick}.")
        cetak_rekap(tick)
        break

    time.sleep(1)