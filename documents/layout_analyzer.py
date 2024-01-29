from pathlib import Path
from cnstd import CnStd
from cnstd import LayoutAnalyzer as CnStdLayoutAnalyzer

from cnocr import CnOcr
from PIL import Image


class PDFLayoutAnalyzer:
    def __init__(self):
        pass

    def analyze(self, image_path):
        img = Image.open(image_path)
        analyzer = CnStdLayoutAnalyzer("mfd")
        res = analyzer.analyze(img)
        print(res)


if __name__ == "__main__":
    image_path = (
        Path(__file__).parents[1] / "samples" / "equations" / "attention_page_5.png"
    )
    analyzer = PDFLayoutAnalyzer()
    analyzer.analyze(image_path)

    # python -m documents.layout_analyzer

    # identify -format "%wx%h\n" samples/equations/attention_page_5.png
    # cnstd analyze -m mfd --resized-shape 1024 --conf-thresh 0.2 -i samples/equations/attention_page_5.png -o samples/equations/attention_page_5_mfd.png
    # cnstd analyze -m layout --resized-shape 1024 --conf-thresh 0.2 -i samples/equations/attention_page_5.png -o samples/equations/attention_page_5_layout.png

    # cnstd predict --resized-shape 1024,1296 --context cuda:0 -i samples/equations/attention_page_5.png # Not recommended

    # cnstd analyze -m layout --resized-shape 1024 --conf-thresh 0.2 -i samples/columns/bert_page_6.png -o samples/columns/bert_page_6_layout.png
    # cnstd analyze -m mfd --resized-shape 1024 --conf-thresh 0.2 -i samples/columns/bert_page_6.png -o samples/columns/bert_page_6_mfd.png
