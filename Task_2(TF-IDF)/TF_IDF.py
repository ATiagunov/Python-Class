import os
import collections
import math
import re

class TF_IDF:

    def __init__(self, dir_name):
        self._word_counters = {}
        self._tf_indexes = {}
        self._idf_indexes = {}
        self._dir_name = dir_name
        self._files_in_work_dir = [os.path.join(self._dir_name, f) for f in os.listdir(dir_name)]
        for f in self._files_in_work_dir:
            self._word_counters[f] = collections.Counter()

    def info(self):
        print("Work directory ", self._dir_name)
        print("Files for calc ", self._files_in_work_dir)

    def _calc_tf_index(self):
        for file_name in self._files_in_work_dir:
            file = open(file_name, "r")
            words_in_file = 0
            self._tf_indexes[file_name] = {}
            for line in file:
                words = re.findall(r'\w+', line)
                words_in_file += len(words)
                for word in words:
                    self._word_counters[file_name][word] += 1

            for word in self._word_counters[file_name]:
                self._tf_indexes[file_name][word] = self._word_counters[file_name][word] / words_in_file
            file.close()
        print(self._tf_indexes)

    def _calc_idf_index(self):
        for file_name in self._files_in_work_dir:
            file = open(file_name, "r")
            presence_in_files = 0
            self._idf_indexes[file_name] = {}
            for line in file:
                words = re.findall(r'\w+', line)
                for word in words:
                    for counter in self._word_counters.values():
                        if counter[word] != 0:
                            presence_in_files += 1
                    self._idf_indexes[file_name][word] = math.log(len(self._files_in_work_dir) / presence_in_files, 10)
                    presence_in_files = 0
            file.close()
        print(self._idf_indexes)

    def calc_tf_idf(self):
        self._calc_tf_index()
        self._calc_idf_index()
        for file in self._files_in_work_dir:
            for word in self._idf_indexes[file]:
                print("IN FILE ", file, "FOR WORD ", word, " TF_IDF INDEX IS",
                      self._idf_indexes[file][word] * self._tf_indexes[file][word])


x = TF_IDF('/home/alexander/PycharmProjects/python_practice/Texts')
x.info()
x.calc_tf_idf()
