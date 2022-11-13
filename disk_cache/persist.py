import pickle
import os
from collections import OrderedDict

cache_file_Name="cache"

def save_in_memory(cache_dict):
        outfile = open(cache_file_Name,'wb')
        pickle.dump(cache_dict,outfile)
        outfile.close()

def initialise_cache_from_memory():
    cache_dict=OrderedDict() 
    if os.path.exists(cache_file_Name):
        infile = open(cache_file_Name,'rb')
        cache_dict = pickle.load(infile)
        infile.close()
    return cache_dict