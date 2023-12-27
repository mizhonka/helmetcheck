import urllib.request

class Search:
    def __init__(self, targets, libraries):
        self.targets=targets
        self.available=dict.fromkeys([target.title for target in targets])
        self.libraries=libraries

    def get_html(self, link):
        data=urllib.request.urlopen(link)
        bytes=data.read()
        html=bytes.decode("utf8")
        return html

    def check_availability(self):
        for target in self.targets:
            link=target.link
            piece=target.title
            html=self.get_html(link)
            if "Saatavilla" in html:
                a=html.find("allavailitems")
                html=html[a:]
                b=html.find("</table>")
                html=html[:b]
                for lib in self.libraries:
                    if lib in html:
                        if not self.available[piece]:
                            self.available[piece]=[]
                        self.available[piece].append(link)
                        break
        return self.available
