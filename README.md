# rox-parser-main

Parser untuk mengubah file `TextAsset/*.bytes` menjadi `JSON/*.json`.

## Pembaruan Terbaru (2026-02-18)

1. Perbaikan alur migrasi data sumber
- `migrate.py` sekarang memetakan file dari `../TextAsset` ke `rox-parser-main/TextAsset` dengan daftar target yang eksplisit.
- Ditambahkan penanganan nama file berbeda: `th_langsnew.bytes` dari sumber akan disalin sebagai `th_langs.bytes`.
- Target parser diperluas, termasuk `data_ItemV2_ItemV2.bytes`.

2. Peningkatan parser generator Lua
- `generate_lua.py` diperbarui untuk menangani dua pola sumber:
  - file yang langsung diawali `return ...`
  - file dengan deklarasi tabel lokal
- Penentuan template lebih fleksibel melalui `TEMPLATE_FILE_NAME` (`json_serializer_template.lua` atau versi basic).
- Ditambahkan fallback `__default_values` jika tidak ada di sumber.
- Eksekusi Lua memakai binary lokal `tools/lua/bin/lua.exe` jika tersedia, dan fallback ke `lua` di PATH jika tidak ada.

3. Optimasi serializer JSON
- `json_serializer_template.lua` memakai pendekatan streaming (`write_json`) agar tidak membangun string JSON besar di memori.
- Escaping karakter JSON dilakukan saat proses tulis file.

4. Sinkronisasi aset parser
- File `TextAsset/*.bytes` di repo parser sudah disinkronkan ke data terbaru.
- Hasil parse `JSON/*.json` diregenerasi mengikuti data terbaru.
- Struktur file lama yang sudah tidak relevan dibersihkan mengikuti sumber terbaru.

5. Penambahan runtime Lua lokal
- `tools/lua/bin/lua.exe` ditambahkan agar proses parse bisa jalan tanpa instalasi Lua global.

## Cara Menjalankan

Jalankan dari root workspace (`d:\Project`):

```powershell
.\.venv\Scripts\Activate.ps1
python rox-parser-main\migrate.py
python rox-parser-main\generate_lua.py
```

Output JSON akan berada di:

- `rox-parser-main/JSON`
