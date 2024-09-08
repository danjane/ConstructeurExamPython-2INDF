import Autocreate2indfRentreeExam
import pdfrw

n_copies = 18

writer = pdfrw.PdfWriter()

for i in range(n_copies):
    print(f'Creating test {i} of {n_copies}...')
    pdf_file = Autocreate2indfRentreeExam.generate_exam()
    writer.addpages(pdfrw.PdfReader(pdf_file).pages)

writer.write('combined_file.pdf')

