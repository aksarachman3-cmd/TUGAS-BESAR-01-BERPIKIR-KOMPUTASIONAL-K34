# Source Code — Si Jago Merah

Folder ini berisi kode program simulasi **Si Jago Merah** beserta penjelasan singkat
mengenai struktur dan cara menjalankannya.

[← Kembali ke README utama](../README.md)

---

## Isi Folder

| Berkas | Keterangan |
|--------|------------|
| `Python_Tubes.py` | Program utama simulasi pemadaman kebakaran hutan |

## Deskripsi Program

`Python_Tubes.py` memodelkan kebakaran hutan pada grid **10×10**. Setiap sel berisi
satu pohon dengan salah satu dari enam kondisi:

| Kondisi | Emoji | Arti |
|---------|:-----:|------|
| `sehat` | 🌳 | Pohon belum terbakar dan dapat terbakar |
| `terbakar` | 🔥 | Pohon sedang terbakar dan menyebarkan api |
| `sedang dipadamkan` | 🧯 | Pohon sedang ditangani truk |
| `basah` | 💧 | Pohon disekat air agar tidak ikut terbakar |
| `padam` | ✅ | Pohon berhasil dipadamkan dan aman |
| `hangus` | ⬛ | Pohon terbakar terlalu lama dan tidak bisa diselamatkan |
| Truk | 🚒 | Posisi truk pemadam saat ini |

Api menyebar mengikuti arah dan kecepatan angin, sedangkan satu truk pemadam bergerak
menuju pohon terbakar terdekat menggunakan **Manhattan Distance**. Jika beberapa pohon
berjarak sama, truk memilih pohon dengan **skor bahaya** tertinggi.

## Cara Menjalankan

Tidak ada dependensi eksternal. Program hanya memakai modul bawaan `random` dan `time`.

```bash
python source-code/Python_Tubes.py
```

Atau dari dalam folder ini:

```bash
cd source-code
python Python_Tubes.py
```

> Gunakan terminal yang mendukung UTF-8 agar emoji tampil dengan benar.
> PowerShell: `$env:PYTHONIOENCODING="utf-8"; python Python_Tubes.py`

### Contoh Input

Skenario demo pada laporan:

| Input | Nilai |
|-------|-------|
| Jumlah titik api | `4` |
| Posisi awal truk — baris | `0` |
| Posisi awal truk — kolom | `3` |
| Titik api 1 — baris, kolom | `0`, `4` |
| Titik api 2 — baris, kolom | `1`, `5` |
| Titik api 3 — baris, kolom | `3`, `9` |
| Titik api 4 — baris, kolom | `7`, `2` |
| Arah angin | `S` |
| Kecepatan angin | `sedang` |

## Alur Eksekusi

1. **Input pengguna** — jumlah titik api, posisi awal truk, koordinat titik api,
   arah angin, dan kecepatan angin. Semua input divalidasi dengan `while` loop.
2. **Inisialisasi** — titik api dipasang pada grid, truk ditempatkan, lalu target
   pertama dicari.
3. **Tampilkan kondisi awal (tick 0)**.
4. **Main loop per tick**:
   1. Update burn timer dan ubah pohon yang melewati batas menjadi `hangus`.
   2. Jika `tick % 5 == 0`, hitung penyebaran api ke arah searah angin dan dua arah
      tegak lurus.
   3. Terapkan hasil penyebaran dari array `akan_terbakar` secara serentak.
   4. Panggil `update_truk` untuk menggerakkan atau memadamkan.
   5. Cetak grid tick tersebut.
   6. Jika tidak ada lagi pohon `terbakar` / `sedang dipadamkan`, tampilkan rekap
      dan berhenti.
5. **Rekap akhir** — total tick, jumlah pohon per kondisi, dan persentasenya.

## Struktur Fungsi

| Fungsi | Peran |
|--------|-------|
| `cetak_grid(...)` | Menampilkan grid 10×10, statistik pohon, status truk, target, ETA, dan sisa tick penyebaran |
| `cetak_rekap(tick)` | Menampilkan rekap akhir simulasi beserta persentase tiap kondisi |
| `mencari_jarak(b1, k1, b2, k2)` | Menghitung jarak Manhattan antara dua titik |
| `dalam_grid(baris, kolom)` | Memeriksa apakah posisi masih berada di dalam grid |
| `probabilitas_penyebaran(persen)` | Mengundi angka 1–100 dan membandingkannya dengan persentase |
| `menghitung_skor(baris, kolom, delta_searah)` | Menghitung skor bahaya pohon terbakar berdasarkan tetangga dan arah angin |
| `mengubah_kondisi_pohon(baris, kolom, kondisi_baru)` | Mengubah kondisi satu pohon secara terpusat |
| `menambahkan_burn_timer(baris, kolom)` | Menambah burn timer satu pohon |
| `mencari_target_pohon(truk_baris, truk_kolom, delta_searah)` | Mencari pohon terbakar terdekat; tie-break dengan skor bahaya |
| `tandai_area_pemadaman(baris, kolom)` | Menandai area 3×3: `terbakar` → `sedang dipadamkan`, `sehat` → `basah` |
| `gerak_truk(truk_b, truk_k, target_b, target_k)` | Menggerakkan truk satu petak menuju target |
| `menyelesaikan_pemadaman(baris, kolom)` | Mengubah `sedang dipadamkan` → `padam` setelah 3 tick |
| `update_truk(delta_searah)` | Pengendali utama truk per tick |
| `check_double_input(titik_api_awal, baris, kolom)` | Mencegah koordinat titik api duplikat |

## Variabel Utama

| Variabel | Keterangan |
|----------|------------|
| `kondisi` | Array 2D berisi kondisi setiap pohon |
| `burn_timer` | Array 2D berisi lama (tick) setiap pohon terbakar |
| `akan_terbakar` | Array 2D boolean sementara untuk penyebaran dua fase |
| `titik_api_awal` | List koordinat titik api awal |
| `arah_angin` | Arah angin: `N`, `S`, `E`, `W` |
| `kecepatan_angin` | Kecepatan angin: `rendah`, `sedang`, `tinggi` |
| `persen_searah` | Peluang penyebaran searah angin |
| `persen_samping` | Peluang penyebaran tegak lurus angin |
| `batas_hangus` | Jumlah tick sebelum pohon menjadi hangus |
| `truk_baris`, `truk_kolom` | Posisi truk saat ini |
| `status_truk` | `mendatangi pohon` atau `memadamkan` |
| `lama_memadam` | Lama truk memadamkan target saat ini |
| `target_baris`, `target_kolom` | Posisi target truk |
| `tick` | Penghitung waktu simulasi |

## Parameter Simulasi

| Kecepatan | Peluang searah | Peluang tegak lurus | Batas hangus |
|-----------|:--------------:|:-------------------:|:------------:|
| `rendah` | 30% | 3% | 15 tick |
| `sedang` | 60% | 6% | 12 tick |
| `tinggi` | 70% | 7% | 10 tick |

Nilai-nilai ini ditentukan melalui uji coba agar tempo penyebaran api seimbang dengan
kecepatan truk (1 petak per tick) dan masih menyisakan peluang penyelamatan.

## Catatan Implementasi

- **Penyebaran dua fase** — hasil penyebaran dikumpulkan dulu di `akan_terbakar`,
  baru diterapkan sekaligus. Ini mencegah pohon yang baru terbakar ikut menyebarkan
  api pada tick yang sama.
- **Validasi input** — jumlah titik api minimal 1, koordinat 0–9, dan koordinat titik
  api tidak boleh duplikat.
- **Skor bahaya** — `+1` per tetangga sehat, `+1` tambahan bila tetangga tersebut
  searah angin, dan `+5` per tetangga yang terbakar.
- **Pergerakan truk** — truk menyelesaikan sumbu baris terlebih dahulu; setelah baris
  sejajar dengan target, truk bergerak pada sumbu kolom.
- **Area pemadaman** — berlaku pada area 3×3 di sekitar truk, termasuk sel diagonal.
- Emoji hanya dipakai untuk tampilan; logika simulasi tidak bergantung pada emoji.

## Dokumentasi Terkait

- [README utama](../README.md)
- [Flowchart](../flowchart/README.md)
- [Laporan akhir](../laporan-akhir/README.md)
- [Presentasi](../ppt/README.md)
