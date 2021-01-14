from bs4 import BeautifulSoup

# reading links from the html document

class DownloadLinks:

    def  links(self) :
        htmlobj = open('html.source/bcl_1674867910.htm')
        soup = BeautifulSoup(htmlobj)
        writeobj = open("links_doc.txt","w")

        i=0
        for link in soup.findAll('a'):
            if(i==0):
                writeobj.write(link.get('href'))
            else:
                writeobj.write("\n"+link.get('href'))
                i = i+1