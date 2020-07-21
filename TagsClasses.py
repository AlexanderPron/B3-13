class Tag:
    '''Класс, описывающий отображение тэгов, которые могут быть одиночными или парными, могут иметь css классы (klass), могут иметь атрибуты (**kwargs). 
    indentLevel - принимает уровень вложенности тэга - родителя (нужно для оформления вывода с отступами)'''
    def __init__(self, tag, indentLevel, is_single=False, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.is_single = is_single
        self.children = []
        self.indentLevel = indentLevel
        if klass is not None:
            self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "")
            self.attributes[attr] = value

    def __enter__(self, *args, **kwargs):
        self.indentLevel += 1       # При входе в контекст увеличиваем уровень вложенности на 1
        return self

    def __exit__(self, *args, **kwargs):
        pass
    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if len(self.children) > 0:
            opening = "\n"+"\t"*self.indentLevel+"<{tag} {attrs}>".format(tag=self.tag, attrs=attrs)
            if self.text:
                internal = "%s" % self.text
            else:
                internal = ""
            for child in self.children:
                internal += str(child)
            ending = "\n"+"\t"*self.indentLevel+"</%s>" % self.tag
            return opening + internal + ending
        else:
            if self.is_single:
                return "\n"+"\t"*self.indentLevel+"<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)
            else:
                return "\n"+"\t"*self.indentLevel+"<{tag} {attrs}>{text}".format(tag=self.tag, attrs=attrs, text=self.text)+"</{tag}>".format(tag=self.tag)


class HTML:
    '''Класс, описывающий вывод внешних тегов html документа <html> </html>, а также в нём задается способ вывода результата генерации html-документа:
    если output = None, то вывод в консоль
    если output = "путь/имя_файла", то вывод будет осуществлен в файл, содержимое файла будет перезаписано'''
    def __init__(self, output=None):
        self.output = output
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.output is not None:
            with open(self.output, "w") as fp:
                fp.write(str(self))
        else:
            print(self)

    def __str__(self):
        html = "<html>\n"
        for child in self.children:
            html += str(child)
        html += "</html>"
        return html


class TopLevelTag:
    ''' Класс, описывающий отображение тегов верхнего уровня, такие как <head>, <body> и т.д. Они всегда парные, не сродержат текста внутри себя и для упрощения не содержат атрибутов. 
    По умолчанию принимает indentLevel = 1 что соответствует первому уровню вложенности, т.к. такие теги находятся лишь внутри <html>. indentLevel введено лишь для вывода сгенерированного html документа с корректными отступами'''
    def __init__(self, tag, indentLevel = 1, **kwargs):
        self.tag = tag
        self.children = []
        self.indentLevel = indentLevel

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def __str__(self):
        html = "\t"*self.indentLevel +"<%s>" % self.tag
        for child in self.children:
            html += str(child)
        html += "\n"+"\t"*self.indentLevel + "</%s>\n" % self.tag
        return html




