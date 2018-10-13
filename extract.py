import PyPDF2

f = open('textFile.txt','w')
pdfFileObject = open('sampleNameList.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
for i in range(count):
    for j in range(count):
        page = pdfReader.getPage(i)
        page1 = page.extractText()
        print(page1)


f.write(page1)
f.close()