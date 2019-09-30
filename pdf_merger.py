import os
import PyPDF2

userpdflocation = input('Folder path to PDFs that need merging: ')
os.chdir(userpdflocation)
userfilename = input('What should I call the file?')

pdf2merge = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdf2merge:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open(userfilename + '.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
