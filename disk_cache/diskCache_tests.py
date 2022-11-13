import unittest
import math
from  diskCache import DiskCache


class DiskCacheTestCase(unittest.TestCase):
    def setUp(self):
        self.cache = DiskCache(2)

    def test_1_get_negative(self):
        result=self.cache.get("abc")
        self.assertEqual(-1,result)

    def test_2_put_key(self):
        result=self.cache.put("abc","123")
        self.assertTrue(result,True)



if __name__ == '__main__':
    unittest.main()