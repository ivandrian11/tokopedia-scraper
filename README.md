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

```json
[
  {
    "product_name": "Samsung Galaxy M54 5G 8/256GB",
    "product_price": "Rp6.499.000",
    "product_discount": null,
    "original_price": null,
    "product_image": "https://images.tokopedia.net/img/cache/200-square/VqbcmM/2024/1/28/a6caaa3c-c4dc-43fe-9bf1-d9d6ed81cec6.jpg",
    "merchant_name": "Hapeworld - Samsung Authorized",
    "merchant_loc": "Banjarmasin",
    "rating": null,
    "product_sold": null,
    "product_detail_link": "https://www.tokopedia.com/hapeworldasp/samsung-galaxy-m54-5g-8-256gb-dark-blue-34d18?extParam=ivf%3Dfalse&src=topads&management_type=1&ob=23&r_replacement=new&is_search=1&keywords=samsung&dv=desktop&pub_id=0&pub_unit=0&page=2&src=search&pub_domain=0"
  },
  {
    "product_name": "Samsung Galaxy A05S 6/128 GB Garansi Resmi 1 Tahun",
    "product_price": "Rp2.085.000",
    "product_discount": "9%",
    "original_price": "Rp2.299.000",
    "product_image": "https://images.tokopedia.net/img/cache/200-square/VqbcmM/2023/11/27/a2034f62-d07d-4dd0-8a95-48c9f2135d3e.jpg",
    "merchant_name": "NEW ERA PONSEL",
    "merchant_loc": "Jakarta Timur",
    "rating": "4.9",
    "product_sold": "250+ terjual",
    "product_detail_link": "https://www.tokopedia.com/neweraponsel/samsung-galaxy-a05s-6-128-gb-garansi-resmi-1-tahun-green-promo-6-128gb-10459?extParam=cmp=1&ivf=false&src=search"
  }
]
```
