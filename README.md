# EPUB-Deluxe-Builder

Professional EPUB 3 Publishing Engine

Version: 1.0.0

## Giới thiệu

EPUB-Deluxe-Builder là công cụ xây dựng EPUB 3 tự động, hỗ trợ từ tạo sách đơn giản đến quy trình xuất bản chuyên nghiệp.

Tính năng:

* EPUB 3 Generator
* Metadata OPF
* Automatic Manifest
* Navigation TOC
* Cover Generator
* Font Embedding
* Typography Engine
* Image Optimization
* Reading Themes
* Kindle Compatibility Check
* Audiobook Media Overlay
* Search Index
* Release Packaging

---

# Installation

## Yêu cầu

* Python >= 3.10

Cài đặt:

```bash
pip install .
```

Kiểm tra:

```bash
epub-deluxe version
```

---

# Quick Start

Tạo project:

```text
MyBook/

├── book.json
└── content/

    └── chapters/

        ├── 001.xhtml
        └── 002.xhtml
```

Build EPUB:

```bash
epub-deluxe build MyBook
```

Xuất file:

```text
book.epub
```

---

# Configuration

File:

```text
book.json
```

Ví dụ:

```json
{
"title":"Pháp Sư Phía Trên",

"author":"Author",

"language":"vi",

"publisher":"EPUB Deluxe",

"description":"Fantasy novel",

"keywords":[
"magic",
"fantasy"
],

"series":"Novel Series"
}
```

---

# Themes

Hỗ trợ:

## Classic

```bash
--theme classic
```

Phong cách sách giấy.

## Modern

```bash
--theme modern
```

Giao diện tối giản.

## Dark

```bash
--theme dark
```

Đọc ban đêm.

## Sepia

```bash
--theme sepia
```

Giảm mỏi mắt.

## Manga

```bash
--theme manga
```

Tối ưu truyện tranh.

---

# CLI Usage

Build:

```bash
epub-deluxe build MyBook
```

Chọn output:

```bash
epub-deluxe build MyBook \
-o Novel.epub
```

Chọn theme:

```bash
epub-deluxe build MyBook \
--theme dark
```

---

# Architecture

```text
EPUB-Deluxe-Builder

├── core

│   ├── builder.py
│   ├── metadata.py
│   ├── manifest.py
│   ├── toc.py
│   ├── validator.py
│   └── pipeline.py


├── features

│   ├── chapter.py
│   ├── cover.py
│   ├── typography.py
│   ├── image_opt.py
│   ├── kindle.py
│   └── theme.py


├── pro

│   ├── epubcheck.py
│   ├── metadata_ai.py
│   ├── toc_advanced.py
│   ├── search_index.py
│   ├── audiobook.py
│   └── packaging.py


├── tests

├── epub_deluxe

└── build.py
```

---

# Developer Guide

Chạy test:

```bash
pytest tests/
```

Build thủ công:

```python
from core.pipeline import DeluxePipeline


pipeline = DeluxePipeline(
    "MyBook",
    "output.epub"
)


pipeline.run(
    theme="classic"
)
```

---

# EPUB Pipeline

```text
Source Book

↓

Chapter Processing

↓

Cover Generation

↓

Image Optimization

↓

Typography

↓

Theme

↓

Metadata

↓

Manifest

↓

TOC

↓

Validation

↓

EPUB Release
```

---

# Release

## Version 1.0.0

Included:

* EPUB 3 engine
* Deluxe formatting
* Kindle support
* Audiobook support
* Publishing tools

---

# License

MIT License

---

# Contributing

1. Fork repository

2. Create feature branch

3. Add tests

4. Submit Pull Request

---

EPUB-Deluxe-Builder
Build better EPUB books.
