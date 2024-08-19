from reader.reader import Reader
import string

file1: str = "Raju-Resume-2024.pdf"
file2: str = "Raju-Resume-2024.docx"

print("Reading file {}".format(file1))
r1 = Reader(file1)
print(r1.extract_text_from_file())
print("Reading file {}".format(file2))
r1 = Reader(file2)
print(r1.extract_text_from_file())