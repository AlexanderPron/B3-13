
    # Генерируем страничку такого вида:
    # <html>
    # 	<head>
    # 		<meta charset="utf-8"/>
    # 		<title >test a4.5</title>
    # 	</head>
    # 	<body>
    # 		<div class="div-0 div-1">
    # 			<div class="div-2">
    # 				<div class="div-3"></div>
    # 			</div>
    # 		</div>
    # 		<form action="https:/google.com/search" method="GET">
    # 			<label for="google-find">Find via Google: </label>
    # 			<input class="simple-input" type="search" name="q" id="google-find" placeholder="Find!"/>
    # 			<button class="simple-button bs-button" type="submit">Send</button>
    # 		</form>
    # 	</body>
    # </html>
    #================ Как пользоваться генератором HTML ===========================
    # В начале создается основной тэг <html> при помощи менеджера контекста with, в котором определяем метод вывода результата: если output = None, то вывод происходит в консоль, иначе - в файл по пути и названию, содержащемся в переменной filePath 
    # Затем создаем тэг верхнего уровня c отступом в 1 табуляцию (уровень вложенности = 1 - по умолчанию)
    # Для оргнизации вложенности тегов, необходимо оргнизовать вложенность менеджеров контекста with 
    # Затем создаем обычный тэг (см. описание класса Tag), передаем в качестве параметров название тега, уровень вложенности родителя, кортеж css классов, атрибуты тэга
    # Если в качестве аттрибута передается зарезервированное в python слово (for, type  т.п.), то перед таким аттрибутом необходимо поставить нижнее подчеркивание _ (в конструкторе класса это подчеркивание удалим)
    # Реализация практически полностью взята из разбора ДЗ, с небольшими дополнениями
from TagsClasses import *

def main(output=None):
    with HTML(output=output) as doc:
        with TopLevelTag("head") as head:
            with Tag("meta", head.indentLevel, is_single=True, charset="utf-8") as meta:
                head += meta
            with Tag("title", head.indentLevel) as title:
                title.text = "test a4.5"
                head += title
            doc += head
        with TopLevelTag("body") as body:
            with Tag("div", body.indentLevel, klass=("div-0","div-1",)) as div1:
                with Tag("div", div1.indentLevel, klass=("div-2",)) as div2:
                    with Tag("div", div2.indentLevel, klass=("div-3",)) as div3:
                        div2 += div3
                    div1 += div2
                body += div1

            with Tag("form", body.indentLevel, action="https:/google.com/search", method="GET") as form:
                with Tag("label", form.indentLevel, _for = "google-find") as label: # В конструкторе Tag уберём нижнее подчеркивание _ (иначе нельзя передать параметр с зарезервированным словом for)
                    label.text = "Find via Google: "
                    form += label
                with Tag("input", form.indentLevel, is_single=True, klass = ("simple-input",), _type="search", name="q", id="google-find", placeholder="Find!") as input:
                    form += input
                with Tag("button", form.indentLevel, klass = ("simple-button", "bs-button",), _type="submit") as button:
                    button.text = "Send"
                    form += button
                body += form
            doc += body


if __name__ == "__main__":
    # filePath = None  # None - если хотим вывод в консоль
    filePath = "index.html"
    main(filePath)