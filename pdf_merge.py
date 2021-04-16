import PyPDF2 
 
def merge_pdf(path):
    pdf_open = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_open, strict=False)
    for pageNum in range(pdf_reader.numPages):
        pageObj = pdf_reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfWriter.write(pdf_new)
    pdf_open.close()
    

pdfWriter = PyPDF2.PdfFileWriter()
pdf_new = open(r"D:\kamil\BYD1118A\pdf\_SIR2.pdf", 'wb')
merge_pdf(r"D:\kamil\BYD1118A\pdf\BYD1118A_REW.01_210416_T02_TAB.pdf")
merge_pdf(r"D:\kamil\BYD1118A\pdf\BYD1118A_REW.01_210416_T03_TAB.pdf")
pdf_new.close()