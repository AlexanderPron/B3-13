from TagsClasses import *

def main():
    html=""
    with HTML(html) as doc:
        with TopLevelTag("head") as head:
            html += head
        print(doc)

if __name__ == "__main__":
    main()