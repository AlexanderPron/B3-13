from sample_tag import Tag 
with Tag("body", toplevel=True) as body:
     with Tag("div") as div:
         with Tag("p") as paragraph:
             paragraph.text = "Какой-то текст"
             div.children.append(paragraph)

         body.children.append(div)