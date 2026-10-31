# Si Jago Merah

Simulasi pemadaman kebakaran hutan pada grid 10x10.

Tugas Besar 01 mata kuliah WI1102 Berpikir Komputasional
Kelompok 01 (K-34) · Semester 1 2026/2027
Sekolah Teknik Elektro dan Informatika (STEI-K), Institut Teknologi Bandung

![Logo Si Jago Merah](assets/logo.png)

## Anggota Kelompok

| Nama | NIM |
|------|-----|
| Aksa Rachman | 19626104 |
| Mahesa Rahasia Hati Kahfilano | 19626020 |
| Davin Gusti Nurandi | 19626014 |
| Fathyakan Thorique Zidane | 19626038 |

Dosen pembimbing: Muhammad Shiddiq Sayyid Hashuro, S.T., M.Eng., Ph.D.

## Tentang Program

Si Jago Merah adalah program simulasi kebakaran hutan berbasis terminal. Hutan
dimodelkan sebagai grid 10x10, di mana setiap sel berisi satu pohon. Api menyebar
dari pohon ke pohon mengikuti arah dan kecepatan angin, sedangkan satu truk pemadam
bergerak menuju pohon terbakar terdekat untuk memadamkannya.

Simulasi berjalan per tick dan menampilkan kondisi grid setiap tick, mulai dari
kondisi awal sampai tidak ada lagi pohon yang terbakar. Di akhir simulasi, program
menampilkan rekap jumlah pohon yang selamat, padam, basah, dan hangus.

Program ini dibuat untuk melihat bagaimana api menyebar dan bagaimana strategi
pemadaman bekerja pada beberapa skenario, tanpa harus menghadapi risiko di lapangan.

## Isi Repository

```text
.
├── README.md
├── assets/
│   └── logo.png
├── source-code/
│   └── Python_Tubes.py
├── flowchart/                  # berkas flowchart menyusul
├── ppt/
│   └── Si Jago Merah - Presentasi.pdf
└── laporan-akhir/
    └── Laporan Akhir - Si Jago Merah.pdf
```

## Cara Menjalankan

Program hanya memakai modul bawaan Python (`random` dan `time`), jadi tidak perlu
install apa pun. Jalankan dengan:

```bash
python source-code/Python_Tubes.py
```

Lalu masukkan jumlah titik api, posisi awal truk, koordinat titik api, arah angin
(N/E/S/W), dan kecepatan angin (rendah/sedang/tinggi).

Contoh skenario yang dipakai di laporan:

| Input | Nilai |
|-------|-------|
| Jumlah titik api | 4 |
| Posisi awal truk | baris 0, kolom 3 |
| Titik api | (0,4), (1,5), (3,9), (7,2) |
| Arah angin | S |
| Kecepatan angin | sedang |

> Kalau emoji tidak muncul di terminal, jalankan dengan
> `$env:PYTHONIOENCODING="utf-8"; python source-code/Python_Tubes.py` (PowerShell)
> atau `PYTHONIOENCODING=utf-8 python source-code/Python_Tubes.py` (Linux/macOS).

## Aturan Simulasi

- Grid berukuran 10x10. Setiap pohon punya kondisi: sehat, terbakar, sedang
  dipadamkan, basah, padam, atau hangus.
- Api menyebar setiap 5 tick, ke arah searah angin dan dua arah tegak lurus angin.
- Burn timer pohon terbakar bertambah 1 setiap tick. Kalau melewati batas, pohon
  berubah menjadi hangus.
- Truk bergerak 1 petak per tick menuju pohon terbakar terdekat (Manhattan Distance).
  Kalau jaraknya sama, dipilih pohon dengan skor bahaya paling tinggi.
- Saat sampai di target, truk memadamkan area 3x3 selama 3 tick.
- Simulasi selesai kalau sudah tidak ada pohon yang terbakar atau sedang dipadamkan.

Parameter penyebaran api:

| Kecepatan angin | Searah angin | Tegak lurus | Batas hangus |
|-----------------|:------------:|:-----------:|:------------:|
| Rendah | 30% | 3% | 15 tick |
| Sedang | 60% | 6% | 12 tick |
| Tinggi | 70% | 7% | 10 tick |

## Batasan

Simulasi ini masih sederhana: grid 10x10 masih hardcoded, angin statis, semua pohon
dianggap sama, tidak ada terrain, hanya ada satu truk, dan air truk tidak terbatas.
Pengembangan yang mungkin dilakukan antara lain grid dinamis, peta dari file,
pathfinding, multi-truk, angin dinamis, dan variasi jenis pohon.

## Dokumen

- Laporan akhir: [Laporan Akhir - Si Jago Merah.pdf](laporan-akhir/Laporan%20Akhir%20-%20Si%20Jago%20Merah.pdf)
- Slide presentasi: [Si Jago Merah - Presentasi.pdf](ppt/Si%20Jago%20Merah%20-%20Presentasi.pdf)
- Kode program: [Python_Tubes.py](source-code/Python_Tubes.py)
- Flowchart: [folder flowchart](flowchart/) (berkas menyusul)
