import urllib.request

class Search:
    def __init__(self, books, libraries):
        self.links=[]
        self.libraries=libraries
        for b in books:
            self.links.append(str(b)[2:-3])

    def get_html(self, link):
        data=urllib.request.urlopen(link)
        bytes=data.read()
        html=bytes.decode("utf8")
        return html

    def check_availability(self):
        available=[]
        for link in self.links:
            html=self.get_html(link)
            if "Saatavilla" in html:
                if len(self.libraries)<=0:
                    available.append(link)
                    continue
                a=html.find("allavailitems")
                html=html[a:]
                b=html.find("</table>")
                html=html[:b]
                for lib in self.libraries:
                    if lib in html:
                        available.append(link)
                        break
        return available
