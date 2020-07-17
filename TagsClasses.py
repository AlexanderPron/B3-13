class HTML():
    def __init__(self, html):
        self.html = html
    def __enter__(self):
        self.html = "<html>\n"
        return self
    def __exit__(self, type, value, traceback):
        pass
    def __str__(self):
        self.html += "</html>"
        return self.html
class TopLevelTag(HTML):
    def __init(self, html, tag):
        self.tag = tag
    def __enter__(self):
        self.html = HTML.__enter__ + "<{}>\n".format(self.tag)
        return self
    def __iadd__(self):
        self.html += "</{}}>".format(self.tag)
        return self.html
class Tag():
    pass

