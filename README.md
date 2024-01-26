# pdf-transformer
Convert PDF to structured formats with deep-learning-assisted Layout Analysis and Text Recognition.


## Why convert to Markdown?

- Markdown is a great standard to convert from and to various formats
- Markdown supports rich texts, but still keeps simple enough to read, write and distribute
- Most info of PDF could be represented in Markdown
  - Except some complicated elements such as tables that can not be structured well, and some info of layouts and pages which would be dropped (to some extent, this is pros instead of cons)
- Trust me, I have struggled with processing PDF, TeX, HTML and some other markup languages (such as PostScript and SVG) for more than 7 years, and I have summarized three rules of choosing document formats:
  1. Richness should give way to readability;
  2. Flexibility should serve ease of distribution;
  3. Unstructured is inferior to structured.


## Two methodologies of PDF preprocessing solutions
### Method 1: Based on file structure
- Explanation:
  - PDF file is essentially bytes stream, which contains info of glyphs and positions
- How to do:
  - Extract contents as texts or dicts from PDF, then organize and group them
  - Really fast, but ugly. I prefer more general and elegant methods. See method 2.
- Recommended Packages:
    - PyMuPDF

### Method 2: Based on ViT and OCR
- Explanation:
  - PDF files have various kinds of elements (pictures & equations), and complicated layouts (multiple columns & mixed orders)
- How to do:
  - Layout analysis:
    - Datasets
      - PubLayNet
      - CDLA: Chinese texts, and more labels (equation and caption)
    - Text Object Detection
      - DBNet
      - CnSTD
      - DiT: Slow, and env setup is a headache, but really good
      - LayoutLM series: Better than DiT, but slower and more complicated
    - Post-processing
      - After detection, it would be necessary to take some more efforts on organizing and grouping the detected document elements
      - For example: figures containing texts or tables, long table containing texts or figures, texts containg equations
      - In above example cases, same document element might be detected as different text types, and developers must take care of these.
  - Text Recognition:
    - Pure Text
      - PaddleOCR
      - CnOCR 
      - I guess someone would mention tesseract, but if anytone has ever used and finetuned it for a long time and has seen various bad results, he would no longer consider using it.
    - Equation
      - LaTeX-OCR
    - Table
      - Deepdoctection
      - table-transformer
      - No solution as far as I have tested can work perfectly for all cases, as real-world tables are much more complicated than what people might have expected
  - Page-level Understanding with Vision-based Large-Language Models:
    - This is another very long story … Let me write it someday in the future.
- Related work
  - Nougat by Meta
    - Results for English papers are great.
    - But slow, buggy, and no Chinese support. And no activity for months.
  - Pix2Text by breezedeus
