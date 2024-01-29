from pathlib import Path
from pdf2image import convert_from_path


class PDFPageExtractor:
    def __init__(self):
        pass

    def extract(self, pdf_path, page_num, output_path, dpi=300):
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            first_page=page_num,
            last_page=page_num,
        )
        print(f"Save page {page_num} to: {output_path}")
        images[0].save(output_path, "PNG")


if __name__ == "__main__":
    # pdf_path = (
    #     Path(__file__).parents[1]
    #     / "samples"
    #     / "pdfs"
    #     / "1706.03762 - Attention Is All You Need.pdf"
    # )
    # page_num = 5
    # output_path = (
    #     Path(__file__).parents[1]
    #     / "samples"
    #     / "equations"
    #     / f"attention_page_{page_num}.png"
    # )
    pdf_path = Path(__file__).parents[1] / "samples" / "pdfs" / "1810.04805 - BERT.pdf"
    page_num = 6
    output_path = (
        Path(__file__).parents[1] / "samples" / "columns" / f"bert_page_{page_num}.png"
    )
    extractor = PDFPageExtractor()
    extractor.extract(pdf_path=pdf_path, page_num=page_num, output_path=output_path)

    # python -m documents.page_extractor
