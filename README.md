# Tokopedia Scraper

Proyek ini dibuat menggunakan bahasa pemrograman Python 3.10.13 dengan package **Scrapy** dan **scrapy-playwright**.

## Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Run](#run)

## Getting Started

### Prerequisites

1. Pastikan telah menginstal [Python](https://www.python.org/downloads/).
2. Pastikan telah menginstal [pip](https://pip.pypa.io/en/stable/cli/pip_install/). Umumnya pip terinstal berbarengan dengan Python.
3. Pastikan telah menginstal package [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) dan [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright).

### Installation

1. Clone repository ini.

```bash
git clone https://github.com/ivandrian11/tokopedia-scraper.git
```

2. Ubah lokasi directory menuju directory hasil cloning.

```bash
cd tokopedia-scraper
```

## Run

1. Pastikan saat ini sedang berada di lokasi root dan terdapat berkas `Makefile` pada directory yang sama.
   > **FYI:** Gunakan command `tree` untuk mengecek hirarki saat ini.
   >
   > ```bash
   > $ tree
   > ```

```bash
.
├── Makefile
├── output
│   ├── review-500.json
│   └── search-500.json
├── README.md
├── scrapy.cfg
└── tokped
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        ├── __init__.py
        ├── review_spider.py
        └── search_spider.py
```

2. Sesuaikan argumen yang akan digunakan pada berkas **Makefile** untuk bagian **_run-search_**. Saat ini hanya ada 2 argumen, yaitu `keyword` dan `max_items`.

```
run-search:
	scrapy crawl tokped-search -a keyword=<isi_disini> -a max_items=<isi_disini> -o output/search.json
```

3. Jalankan command berikut untuk memulai proses scraping.

```bash
$ make run-search
```

4. Setelah proses selesai, hasil scraping sudah bisa dilihat pada folder **output**.
