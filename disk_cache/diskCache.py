from persist import *


class DiskCache:
    def __init__(self,size) -> None:
        self.size=size
        self.dict=initialise_cache_from_memory()    

    def get(self, key) :
        if key in self.dict:
            value = self.dict[key]
           
            del self.dict[key]
         
            self.dict[key] = value
           
            return value
        return -1

    def put(self, key, value) :                
        if key in self.dict:            
            del self.dict[key]
            self.dict[key] = value
            
        elif len(self.dict) < self.size:       
            self.dict[key] = value     
        else:
            self.dict.popitem(last=False)  
            self.dict[key] = value
        save_in_memory(self.dict)
        return True