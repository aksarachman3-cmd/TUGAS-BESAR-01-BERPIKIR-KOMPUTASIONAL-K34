# Flowchart — Si Jago Merah

Folder ini disediakan untuk menyimpan diagram alir (flowchart) program simulasi
**Si Jago Merah**, baik diagram alir utama maupun diagram alir setiap subprogram.

[← Kembali ke README utama](../README.md)

---

## Status Folder

> Folder ini masih kosong. Berkas flowchart akan ditambahkan oleh tim. README ini
> berfungsi sebagai penjelasan isi folder sekaligus daftar flowchart yang direncanakan.

## Tautan Flowchart

Tautan sumber flowchart:

> _Belum tersedia — silakan tambahkan tautan di sini._

<!-- TODO: tempel tautan flowchart (mis. Google Drive/Figma/diagram) di atas. -->

## Daftar Flowchart

Berdasarkan laporan akhir, flowchart yang digunakan dalam tugas besar ini meliputi:

| No | Nama Flowchart | Keterangan |
|:--:|----------------|------------|
| 1 | Diagram Alir Keseluruhan Program | Alur utama simulasi dari input hingga rekap |
| 2 | Diagram Alir Kondisi Pohon Hangus | Perubahan kondisi pohon hingga hangus |
| 3 | Diagram Alir Kondisi Pohon Dipadamkan | Perubahan kondisi pohon hingga padam |
| 4 | `cetak_grid` | Menampilkan grid dan informasi pendukung |
| 5 | `cetak_rekap` | Menampilkan rekap akhir simulasi |
| 6 | `mencari_jarak` | Menghitung jarak Manhattan |
| 7 | `dalam_grid` | Memeriksa batas grid |
| 8 | `probabilitas_penyebaran` | Menentukan keberhasilan penyebaran api |
| 9 | `menghitung_skor` | Menghitung skor bahaya pohon |
| 10 | `mengubah_kondisi_pohon` | Mengubah kondisi pohon |
| 11 | `menambahkan_burn_timer` | Menambah burn timer |
| 12 | `mencari_target_pohon` | Menentukan target truk |
| 13 | `tandai_area_pemadaman` | Menandai area 3×3 |
| 14 | `gerak_truk` | Menggerakkan truk menuju target |
| 15 | `menyelesaikan_pemadaman` | Mengubah pohon menjadi padam |
| 16 | `update_truk` | Pengendali utama truk per tick |

## Konvensi Penamaan Berkas

Agar mudah ditelusuri, disarankan menggunakan format:

```text
flowchart-utama.(png|svg|pdf)
flowchart-<nama-fungsi>.(png|svg|pdf)
```

Contoh:

```text
flowchart-utama.png
flowchart-cetak-grid.png
flowchart-mencari-target-pohon.png
flowchart-update-truk.png
```

## Keterkaitan dengan Berkas Lain

- Diagram asli juga tercantum pada **BAB 2** laporan akhir:
  [`laporan-akhir/`](../laporan-akhir/README.md)
- Penjelasan kode tiap fungsi: [`source-code/README.md`](../source-code/README.md)
- Ringkasan alur program pada presentasi: [`ppt/README.md`](../ppt/README.md)
