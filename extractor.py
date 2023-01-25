import pytesseract
from PIL import Image

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Extractor:
    def __init__(self):
        pass
    def pdf_extractor(self,image):
        documents = pytesseract.image_to_string(image)
        return documents
    def img_extractor(self,document):
        documents = pytesseract.image_to_string(document)
        return documents

#img_path = 'data/train/dl/dl1.jpg'
# pdf_path = 'data/train/'
# im = Image.open(img_path)
# c = Extractor()
# documents = c.img_extractor(im)
# print(documents)