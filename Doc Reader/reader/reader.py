"""
https://textract.readthedocs.io/en/stable/#
Motivation : I have dome some research on the multiple libraries.
https://pypdf.readthedocs.io/en/stable/index.html#, https://github.com/deanmalmgren/textract


I found the above more useful as it supports multiple range of docs like word, pdf.

Requirement :
   - Read a file and extract text only.
   - check file extension

Issues: textract does not work well with pdf so using PdfReader to read pdf
"""
import magic
import textract
from dataclasses import dataclass
from pypdf import PdfReader
from enum import Enum

def get_file_ext(file_path=str):
    """
    Just read the file
    :return: true, false
    """
    return magic.from_file(file_path)


@dataclass
class Reader:
    file: str
    doc_pdf: str = "PDF"
    doc_word: str = "Microsoft Word"

    def get_file_format(self, file=str) -> str:
        """

        :param file:
        :return: string
        """
        file_foramt = get_file_ext(file)
        print(file_foramt, self.doc_pdf)
        if file_foramt.startswith(self.doc_pdf):
            return self.doc_pdf
        elif file_foramt.startswith(self.doc_word):
            return self.doc_word
        else:
            return "Error Document Type : {}".format(file_foramt)

    def extract_text_from_file(self):
        if not self.get_file_format(self.file).startswith("Error"):
            print("Processing Doc")
            if self.get_file_format(self.file).startswith(self.doc_word):
                text = textract.process(self.file)
                print(text)
                return text
            elif self.get_file_format(self.file).startswith(self.doc_pdf):
                reader = PdfReader(self.file)
                number_of_pages = len(reader.pages)
                print(number_of_pages)
                page = reader.pages[0]
                print(page, "-----")
                text = page.extract_text()

        else:
            print("Error - Cannot Process Document of Type : {}".format(self.get_file_format(self.file)))
            return "Error Document Type : {}".format(self.get_file_format(self.file))