texts = [['human', 'interface', 'computer'],
 ['survey', 'user', 'computer', 'system', 'response', 'time'],
 ['eps', 'user', 'interface', 'system'],
 ['system', 'human', 'system', 'eps'],
 ['user', 'response', 'time'],
 ['trees'],
 ['graph', 'trees'],
 ['graph', 'minors', 'trees'],
 ['graph', 'minors', 'survey']]
from gensim import corpora
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
print corpus[0] # [(0, 1), (1, 1), (2, 1)]


from gensim import models
tfidf = models.TfidfModel(corpus)
doc_bow = [(0, 1), (1, 1)]
print tfidf[doc_bow] # [(0, 0.70710678), (1, 0.70710678)]
tfidf.save("./model.tfidf")
tfidf = models.TfidfModel.load("./model.tfidf")

# 构造LSI模型并将待检索的query和文本转化为LSI主题向量
# 转换之前的corpus和query均是BOW向量
lsi_model = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
documents = lsi_model[corpus]
query_vec = lsi_model[query]


index = similarities.MatrixSimilarity(documents)
index.save('/tmp/deerwester.index')
#待检索的目标文档过多,sMatrixSimilarity往往会带来内存不够用，可以改用similarities.Similarity类。
index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
sims = index[query_vec] # return: an iterator of tuple (idx, sim)