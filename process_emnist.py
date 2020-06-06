import os
import scipy.misc
import numpy as np
import imageio

def get_images(imgf, n):
    f = open(imgf, "rb")
    f.read(16)
    images = []

    for i in range(n):
        image = []
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)
    return images

def get_labels(labelf, n):
    l = open(labelf, "rb")
    l.read(8)
    labels = []
    for i in range(n):
        labels.append(ord(l.read(1)))
    return labels

def output_csv(images, labels, outf):
    o = open(outf, "w")
    for i in range(len(images)):
        o.write(",".join(str(x) for x in [labels[i]] + images[i]) + "\n")
    o.close()

def output_png(images, labels, prefix):
    for i in range(len(images)):
        cls_dir = os.path.join(prefix,str(labels[i]))
        if not(os.path.isdir(cls_dir)):
            os.makedirs(cls_dir)
        out = os.path.join(cls_dir, "%06d-num%d.png"%(i,labels[i]))
        imageio.imwrite(out, np.array(images[i]).reshape(28,28))

def csv_and_png(imgf, labelf, prefix, n):
    images = get_images(imgf, n)
    labels = get_labels(labelf, n)
    output_csv(images, labels, "emnist_%s.csv"%prefix)
    output_png(images, labels, prefix)

data_dir = './data/gzip/'
test_images = os.path.join(data_dir,"emnist-letters-test-images-idx3-ubyte")
test_labels = os.path.join(data_dir, "emnist-letters-test-labels-idx1-ubyte")
train_images = os.path.join(data_dir,"emnist-letters-train-images-idx3-ubyte")
train_labels = os.path.join(data_dir,"emnist-letters-train-labels-idx1-ubyte")


csv_and_png(train_images,train_labels, "train", 60000)
csv_and_png(test_images,test_images,  "test",  10000)