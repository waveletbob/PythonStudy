#coding:utf-8
from math import log
import pandas as pd
import treePlotter as tp
def createTree(dataSet,labels):
	classList = list(dataSet.iloc[:, -1])
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataset.iloc[0])==1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel: {}}
	del(labels[bestFeat])
	featValues = list(dataSet.iloc[:, bestFeat])
	uniqueVals = set(featValues)
	for value in uniqueVals:
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat, value), labels[:])
	return myTree
def majorityCnt(classList):
	classCount={}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(), key=lambda x: x[1],reverse=True)	
	return sortedClassCount[0][0]
def chooseBestFeatureToSplit(dataSet):
	numFeatures=len(dataset.iloc[0])-1
	baseEntropy=calcShannonEnt(dataset)
	bestInfoGain=0.0
	bestFeature=-1
	for i in range(numFeatures):
		featList=dataset.iloc[:,i]
		uniqueVals=set(featList)
		newEntropy=0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if infoGain > bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature
def splitDataSet(dataSet, axis, value):
	retDataSet = dataSet.loc[dataSet.iloc[:, axis] == value]
	del retDataSet[retDataSet.columns[axis]]
	return retDataSet
def createTree(dataSet,labels):
	classList = list(dataSet.iloc[:, -1])
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet.iloc[0]) == 1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel: {}}
	del(labels[bestFeat])
	featValues = list(dataSet.iloc[:, bestFeat])
	uniqueVals = set(featValues)
	for value in uniqueVals:
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat, value), labels[:])
	return myTree
def getBestSplit():
	dataset=pd.read_csv("./weatherData.csv",encoding='gbk')
	# print(len(dataset))
	labels=list(dataset.columns[:-1])
	sortedData=dataset.sort_values(by=dataset.columns[1])
	print(sortedData)
	infGain=0
	bestSplit=-1
	HD=calcShannonEnt(dataset)
	# print(HD)经验熵
	print(sortedData.values[:-2, :])
	for pos, item in enumerate(sortedData.values[:-2, :]):
		print(pos,item)
		prob = (pos + 1) / len(sortedData)
		newEnt = prob * calcShannonEnt(sortedData.iloc[:pos+1, :]) + (1 -prob) * calcShannonEnt(sortedData.iloc[pos+1:, :])
		newEnt = HD - newEnt
		if newEnt>infGain:
			infGain=newEnt
			bestSplit=item[1]
	temperatureSplit = bestSplit
	print('温度最佳分割点为:%d' % temperatureSplit)
	sortedData = dataset.sort_values(by=dataset.columns[2])
	infGain=0
	bestSplit=-1
	for pos,item in enumerate(sortedData.values[:-2,:]):
		prob=(pos+1)/len(sortedData)
		newEnt=prob*calcShannonEnt(sortedData.iloc[:pos+1,:])+(1-prob)*calcShannonEnt(sortedData.iloc[pos+1:,:])
		newEnt=HD-newEnt
		if newEnt>infGain:
			infGain=newEnt
			bestSplit=item[2]
	humiditySplit=bestSplit
	print('湿度最佳分割点为:%d' % humiditySplit)
	highPos = dataset.iloc[:, 1] > temperatureSplit
	lowPos = dataset.iloc[:, 1] <= temperatureSplit
	dataset.ix[highPos, 1] = '高'
	dataset.ix[lowPos, 1] = '正常'
	highPos = dataset.iloc[:, 2] > humiditySplit
	lowPos = dataset.iloc[:, 2] <= humiditySplit
	dataset.ix[highPos, 2] = '高'
	dataset.ix[lowPos, 2] = '正常'
	return dataset,labels


def calcShannonEnt(dataset):
	numEntries=len(dataset)
	# print(numEntries)计算的是实例总数
	labelEntries=dataset.iloc[:,-1]
	# print(labelEntries)得出的是结果数
	labelCounts=labelEntries.value_counts()
	shannonEnt=0#初始经验熵
	for count in labelCounts:
		prob=count/numEntries
		shannonEnt-=prob*log(prob,2)
	return shannonEnt

if __name__ == '__main__':
	dataset,labels=getBestSplit()
	tree=createTree(dataset,labels[:])

	instance = ['晴', '寒冷', '正常', '有']
	decide = decision(tree, instance)
	print(',␣'.join(instance), '->', decide)
	instance=['晴', '寒冷', '高', '无']
	decide = decision(tree, instance)
	print(',␣'.join(instance), '->', decide)

	tP.createPlot(tree)
def decision(tree,instance):
	outcome=tree
	while type(outcome)==dict:
		key=list(outcome.keys())[0]
		pos=labels.index(key)
		keyVal=instance[pos]
		outcome=outcome[key][keyVal]
	return outcome