import PyPDF2 
import warnings
import os


# execution merge pdfs according to path
def multi_merge(path):
    warnings.filterwarnings("ignore")
    pdfWriter = PyPDF2.PdfFileWriter()
    pdf_new = open("%s\_SIR1.pdf" % path, 'wb')
    merge_all(path, pdfWriter, pdf_new)
    pdf_new.close()


# execution merge single pdf
def merge_single(path):
    pdfWriter = PyPDF2.PdfFileWriter()
    pdf_new = open("%s\_SIR1.pdf" % path, 'wb')
    merge_pdf("D:\kamil\KAR4301B\pdf\KAR4301B_REW.01_210420_PS01.pdf", pdfWriter, pdf_new)
    merge_pdf("D:\kamil\KAR4301B\pdf\KAR4301B_REW.01_210420_T01.pdf", pdfWriter, pdf_new)
    merge_pdf("D:\kamil\KAR4301B\pdf\KAR4301B_REW.02_210420_T02_TAB.pdf", pdfWriter, pdf_new)
    pdf_new.close()


# to merge single pdfs
def merge_pdf(path, pdfWriter, pdf_new):
    pdf_open = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_open, strict=False)
    for pageNum in range(pdf_reader.numPages):
        pageObj = pdf_reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfWriter.write(pdf_new)
    pdf_open.close()


# create list of pdfs in path
def merge_all(path, pdfWriter, pdf_new):
    pdf_all = os.listdir(path)
    for elem in pdf_all:
        merge_pdf("%s\%s" % (path, elem), pdfWriter, pdf_new)


warnings.filterwarnings("ignore")

merge_single("D:\kamil\KAR4301B\pdf")

multi_merge("D:\kamil\KAR4301B\pdf")
