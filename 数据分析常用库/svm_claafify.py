import time
import pandas as pd
def loadData(sar='train'):
	dataSrc = r'%s.data' % src
	labelSrc = r'%s.label' % src
	label = pd.read_table(labelSrc, sep=' ', names=['label'])
	mapSrc = r'%s.map' % src
	return TF,doc2term,term2doc,cate2docs,label
if __name__=='__main__':
	start=time.time()
	loadData()
