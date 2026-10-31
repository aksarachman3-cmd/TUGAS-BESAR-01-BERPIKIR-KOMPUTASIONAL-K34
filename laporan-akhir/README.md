# Laporan Akhir — Si Jago Merah

Folder ini berisi laporan akhir tugas besar **Si Jago Merah: Simulasi Sistem
Pemadaman Kebakaran Hutan**.

[← Kembali ke README utama](../README.md)

---

## Isi Folder

| Berkas | Keterangan |
|--------|------------|
| `Laporan Akhir - Si Jago Merah.pdf` | Laporan akhir lengkap (42 halaman) |

## Identitas Laporan

| Item | Keterangan |
|------|------------|
| Mata kuliah | WI1102 Berpikir Komputasional |
| Tugas | Tugas Besar 01 |
| Semester | 1 2026/2027 |
| Kelompok | 01 · K-34 |
| Program studi | Tahap Persiapan Bersama, STEI-K, Institut Teknologi Bandung |
| Dosen pembimbing | Muhammad Shiddiq Sayyid Hashuro, S.T., M.Eng., Ph.D. |

**Anggota kelompok:**

| Nama | NIM |
|------|-----|
| Aksa Rachman | 19626104 |
| Mahesa Rahasia Hati Kahfilano | 19626020 |
| Davin Gusti Nurandi | 19626014 |
| Fathyakan Thorique Zidane | 19626038 |

## Struktur Laporan

| Bagian | Isi |
|--------|-----|
| Surat pernyataan | Pernyataan penggunaan AI dan tingkat penggunaannya |
| Kata pengantar | Ucapan syukur dan terima kasih |
| Daftar isi, daftar gambar | Navigasi laporan |
| **BAB 1 — Pendahuluan** | Latar belakang, rumusan masalah, tujuan, solusi, dan batasan |
| **BAB 2 — Kerangka Berpikir** | Dekomposisi, pengenalan pola, abstraksi–generalisasi, algoritma, dan dasar penentuan parameter |
| Cuplikan penjalanan program | Contoh skenario dan tangkapan layar simulasi |
| **BAB 3 — Penutup** | Arah pengembangan dan kesimpulan |
| Daftar pustaka | Sumber data dan referensi |
| Lampiran | Pembagian tugas dalam kelompok |

## Ringkasan Isi

### BAB 1 — Pendahuluan

Membahas tingginya kasus kebakaran hutan dan lahan di Indonesia, dampaknya terhadap
kesehatan masyarakat dan lingkungan, serta sulitnya memprediksi penyebaran api.
Dari kondisi tersebut, kelompok merancang **Si Jago Merah** sebagai simulasi berbasis
grid 10×10 yang berfokus pada arah dan kecepatan angin serta satu unit truk pemadam.

**Batasan:** grid 10×10, angin statis, vegetasi diseragamkan, lingkungan berupa grid
pohon tanpa terrain, truk hanya bergerak horizontal/vertikal, dan air tak terbatas.

### BAB 2 — Kerangka Berpikir

Menerapkan empat pilar berpikir komputasional:

- **Dekomposisi** — input, eksekusi simulasi, dan visualisasi/rekap.
- **Pengenalan pola** — pola penyebaran api, perubahan kondisi pohon, burn timer,
  dan pergerakan truk.
- **Abstraksi–generalisasi** — penyederhanaan hutan, angin, pohon, waktu, api, dan truk.
- **Algoritma** — main program per tick dan subprogram untuk tampilan, perhitungan,
  perubahan kondisi pohon, serta pengendalian truk.

Bab ini juga memuat flowchart utama dan flowchart subprogram, aturan simulasi, serta
dasar penentuan nilai parameter (grid, jeda penyebaran, peluang penyebaran, batas
hangus, lama pemadaman, area pemadaman, dan bobot skor bahaya).

### BAB 3 — Penutup

Memaparkan 14 arah pengembangan, antara lain grid dinamis, config eksternal, peta dari
file, pathfinding A*/BFS, multi-truk, unit udara, firebreak, angin dinamis, penyebaran
8 arah, basah mengering, *reignite*, variasi jenis pohon, kapasitas air, serta
*record & replay*. Bab ini ditutup dengan kesimpulan mengenai perancangan dan
implementasi Si Jago Merah.

## Cara Membuka

```text
laporan-akhir/Laporan Akhir - Si Jago Merah.pdf
```

## Keterkaitan dengan Berkas Lain

- Kode program: [`source-code/`](../source-code/README.md)
- Flowchart: [`flowchart/`](../flowchart/README.md)
- Slide presentasi: [`ppt/`](../ppt/README.md)
