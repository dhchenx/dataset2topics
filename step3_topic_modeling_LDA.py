from gensim import corpora, models
import gensim
import jieba
import jieba.posseg as pseg
from quickcsv.file import *
import os

# 按国家拆分数据集
def divide_by_country(csv_file):
    dict_country_doc={}
    list_all_item = read_csv(csv_file)
    for item in list_all_item:
        file_id = item['fileId']
        # 国家
        country = item['area']
        # 全文txt的路径
        text_path = f"datasets/raw_text/text_{file_id}.txt"
        if not os.path.exists(text_path):
            continue
        # 读取全文用作后续处理
        text = open(text_path, 'r', encoding='utf-8').read()
        #print(text_path)
        #print("TEXT: ", text)  # 全文
        if country not in dict_country_doc:
            dict_country_doc[country]=[text]
        else:
            dict_country_doc[country].append(text)
        # print()
    return dict_country_doc

# LDA的方法
def LDA(
        list_doc,
        NUM_TOPICS = 5, # 主题数
        NUM_WORDS = 50, # 每个主题显示的最多关键词数
        NUM_PASS = 5, # 每个有效关键词至少包含n个词
):
    # 用于分词的额外完整词语
    jieba.load_userdict('datasets/keywords/countries.csv')
    jieba.load_userdict('datasets/keywords/leaders_unique_names.csv')
    jieba.load_userdict('datasets/keywords/carbon2.csv')

    stopwords = [w.strip() for w in open('datasets/stopwords/hit_stopwords.txt', 'r', encoding='utf-8').readlines()
                 if w.strip() != ""]

    doc_set = []
    for doc in list_doc:
        # list_words=jieba.cut(doc,cut_all=False)
        list_words = pseg.cut(doc)
        list_w = []
        for w, f in list_words:
            if f in ['n', 'nr', 'ns', 'nt', 'nz', 'vn', 'nd', 'nh', 'nl', 'i']: # 筛选重要的词语
                if w not in stopwords and len(w) != 1:
                    list_w.append(w)
        # print(list_w)
        doc_set.append(list_w)

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for tokens in doc_set:
        # clean and tokenize document string

        # stem tokens
        # stemmed_tokens = [p_stemmer.stem(i) for i in tokens]

        # add tokens to list
        texts.append(tokens)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=NUM_PASS)

    # print keywords
    topics = ldamodel.print_topics(num_words=NUM_WORDS, num_topics=NUM_TOPICS)

    for topic in topics:
        print(topic)


if __name__=="__main__":
    dict_country_doc=divide_by_country(csv_file='datasets/list_g20_news.csv')
    for country in dict_country_doc:
        list_doc=dict_country_doc[country]
        print(country+'“双碳”报道的主题（'+str(len(list_doc))+'篇文档）：')
        LDA(list_doc,NUM_TOPICS=6,NUM_WORDS=20,NUM_PASS=10)
        print()