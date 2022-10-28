import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

with open(r'E:\李震祥\PYGIT\PYref\ReviewCode\module\data\constitution.txt', 'r') as f:
    txt_content = f.read()
    tet_list = re.finditer('[a-zA-Z]+', txt_content)
    txt_li = [word.group().lower() for word in tet_list]
    text = ' '.join(txt_li)

wordcloud = WordCloud().generate(text)
plt.figure(figsize=[12, 10])
plt.imshow(wordcloud)
plt.show()
