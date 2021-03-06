#!/usr/bin/env python
#coding:utf8
import numpy
class Dataset():
    def __init__(self,data,labels):
        self._data = data
        self._labels = labels
        self._numbers = self._data.shape[0]
        self._index_in_epoch = 0
        self._epochs = 0
    def numbers(self):
        return self._numbers
    def epochs(self):
        return self._epochs
    def data(self):
        return self._data
    def labels(self):
        return self._labels
    def all(self):
        return self._data,self._labels
    def next_batch(self,batch_size):
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._numbers:
            #finished epoch
            self._epochs += 1
            #shuffle data
            perm = numpy.arange(self._numbers)
            numpy.random.shuffle(perm)
            self._data = self._data[perm]
            self._labels = self._labels[perm]
            #start next epoch
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._numbers
        end = self._index_in_epoch
        return self._data[start:end],self._labels[start:end]
