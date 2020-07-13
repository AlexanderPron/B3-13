class HTML:
    def __init__(self, output_method = "console"):
        self.output_method = output_method
        if self.output_method == "console":
            print("<html>//n</html>")

class TopLevelTag(HTML):
    pass
    def __init__(self, topTag):
        self.topTag = topTag


class Tag(TopLevelTag):
    pass
    def __init__(self, tag, is_single=False):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.is_single = is_single
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.toplevel:
            print("<%s>" % self.tag)
            for child in self.children:
                print(child)

            print("</%s>" % self.tag)

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if self.children:
            opening = "<{tag} {attrs}>".format(tag=self.tag, attrs=attrs)
            internal = "%s" % self.text
            for child in self.children:
                internal += str(child)
            ending = "</%s>" % self.tag
            return opening + internal + ending
        else:
            if self.is_single:
                return "<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)

            else:
                return "<{tag} {attrs}>{text}</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )




