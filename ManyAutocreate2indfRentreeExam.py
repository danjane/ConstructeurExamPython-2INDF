import Autocreate2indfRentreeExam
import pdfrw

n_copies = 2

writer = pdfrw.PdfWriter()

for _ in range(n_copies):
    pdf_file = Autocreate2indfRentreeExam.generate_exam()
    writer.addpages(pdfrw.PdfReader(pdf_file).pages)

writer.write('combined_file.pdf')

