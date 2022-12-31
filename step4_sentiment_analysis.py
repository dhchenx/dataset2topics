import stanza
# pip install stanza
# https://stanfordnlp.github.io/stanza/sentiment.html
# The existing models each support negative, neutral, and positive, represented by 0, 1, 2 respectively.

def get_meaning(value):
    if value==0:
        return "消极"
    if value==1:
        return "中立"
    if value==2:
        return "积极"

nlp = stanza.Pipeline(lang='zh', processors='tokenize,sentiment')
doc = nlp('巴西总统博索纳罗表示，巴西国家石油公司的天然气价格上涨是不可接受的。习近平强调，实现“双碳”目标是一场广泛而深刻的变革，不是轻轻松松就能实现的。')

for i, sentence in enumerate(doc.sentences):
    print(sentence.text, " -> ", get_meaning(sentence.sentiment))

