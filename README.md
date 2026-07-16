# 📚 EPUB Deluxe Builder Pro

> Professional EPUB 3 Generator for TXT, ZIP, DOCX and HTML.

Create beautiful, commercial-quality EPUB books optimized for:

- 🍎 Apple Books
- 📖 Kobo
- 📚 Google Play Books
- 🌙 Moon+ Reader
- 📱 ReadEra
- 🔥 FBReader
- 📘 PocketBook

---

## ✨ Features

### 📖 EPUB 3

- EPUB 3 compliant
- Navigation Document (nav.xhtml)
- toc.ncx
- Optimized package.opf
- Valid XHTML5

---

### 📄 Input

Supported formats:

- TXT
- ZIP (contains TXT)
- DOCX *(planned)*
- HTML *(planned)*
- Markdown *(planned)*

Automatic encoding detection:

- UTF-8
- UTF-8 BOM
- UTF-16
- GB18030
- GBK
- Big5
- CP1258

---

### 🧹 Smart Cleaner

Automatically removes:

- Advertisements
- Watermarks
- Duplicate blank lines
- Website URLs
- Reading platform signatures

Normalize:

- Spaces
- Paragraphs
- Unicode text

---

### 📚 Smart Chapter Detection

Automatically detects chapters like:

```
Chapter 1

Chapter 20

Chương 1

Chương 99

第1章

第八十章

Thứ 73 chương
```

Custom chapter patterns will be supported.

---

### 🎨 Deluxe Layout

Professional typography:

- Justified text
- First line indent
- Comfortable line spacing
- Beautiful chapter titles
- Responsive images
- Dark mode friendly

---

### 🖼 Cover

Supports:

- JPG
- PNG

Automatically:

- Resize
- Optimize
- Convert to JPEG
- Apple Books compatible

---

### 📑 Metadata

Automatically generates:

- Title
- Author
- Publisher
- Language
- UUID
- Modified date
- Identifier

---

### 📖 Table of Contents

Generate:

- nav.xhtml
- toc.ncx

Automatic navigation.

---

### ⚡ Batch Convert *(planned)*

Convert:

```
100 TXT

↓

100 EPUB
```

---

### 🖥 GUI *(planned)*

Modern desktop application.

- Drag & Drop
- Progress Bar
- Dark Mode
- Batch Processing

---

## 📂 Project Structure

```
EPUB-Deluxe-Builder/

├── main.py

├── requirements.txt

├── README.md

├── build.bat

│

├── core/

│   ├── builder.py

│   ├── cleaner.py

│   ├── chapter_parser.py

│   ├── cover.py

│   ├── css.py

│   ├── metadata.py

│   ├── toc.py

│   └── utils.py

│

├── gui/

│   ├── app.py

│   ├── dialogs.py

│   └── widgets.py

│

├── resources/

│   ├── icon.ico

│   ├── style.css

│   └── default_cover.jpg

│

└── output/
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/<your-account>/EPUB-Deluxe-Builder.git

cd EPUB-Deluxe-Builder
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## 📦 Build EXE

```bash
pyinstaller --onefile --windowed main.py
```

---

## 🎯 Roadmap

### Version 0.1

- [x] TXT Reader
- [x] EPUB Generator
- [x] Cover
- [x] TOC
- [x] Metadata

---

### Version 0.2

- [ ] ZIP Support
- [ ] Better Cleaner
- [ ] Better CSS
- [ ] Apple Books Optimization

---

### Version 0.3

- [ ] DOCX Import
- [ ] HTML Import
- [ ] Markdown Import

---

### Version 0.4

- [ ] Batch Convert
- [ ] GUI
- [ ] Settings

---

### Version 1.0

- [ ] Stable Release
- [ ] Windows Installer
- [ ] Auto Update

---

## 🛠 Technologies

- Python 3.11+
- EbookLib
- Pillow
- BeautifulSoup4
- lxml
- charset-normalizer

---

## 📜 License

MIT License

---

## ❤️ Acknowledgements

Built with:

- EbookLib
- Pillow
- Python Community

---

## 🤝 Contributions

Pull requests are welcome.

For major changes, please open an issue first to discuss your proposal.

---

## ⭐ Support

If this project helps you, please consider giving it a ⭐ on GitHub.
