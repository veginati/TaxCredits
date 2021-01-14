from bs4 import BeautifulSoup
# reading links from the html document



class DownloadLinks(object):

    def links(self):
        htmlobj = open('./py/html.source/data_after_2017.htm',"r")
        soup = BeautifulSoup(htmlobj,features='html.parser')
        writeobj = open("./py/links_source/links_doc.txt", "a")

        i = 0
        for link in soup.findAll('a'):
            if (i == 0):
                writeobj.write(link.get('href'))
            else:
                writeobj.write("\n" + link.get('href'))
            i = i + 1
        writeobj.flush()

    def test(self):
        print('data')
