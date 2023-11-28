import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'data/Person1K/Annotations'
txtsavepath = 'data/Person1K/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

with open('data\Person1K\ImageSets/trainval.txt', 'w') as ftrainval:
    ftest = open('data\Person1K\ImageSets/test.txt', 'w')
    ftrain = open('data\Person1K\ImageSets/train.txt', 'w')
    fval = open('data\Person1K\ImageSets/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftest.write(name)
            else:
                fval.write(name)
        else:
            ftrain.write(name)

ftrain.close()
fval.close()
ftest.close()