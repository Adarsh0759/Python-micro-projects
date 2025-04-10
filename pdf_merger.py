import PyPDF2
#filess need to be merged and path 
pdffiles=["Adarsh  Anand 995583.pdf","Adarsh's Resume.pdf","SSPL_CoverLetter.pdf"]

merger=PyPDF2.PdfMerger()
for filename in pdffiles:
    pdfFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')