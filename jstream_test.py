#!/usr/bin/env python3 
import jstream
import io
import unittest
import json

big_thing = """
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
"""

large_json = json.dumps({"big-thing": big_thing})

class JStreamTests(unittest.TestCase):
    def test_small_sequence(self):
        data = '''
        [1,2
        ,3]       [4 ,5, 6]
        {"a":
        "b"}
        '''
        expect = [[1,2,3], [4,5,6],{'a':'b'}]
        data_stream = io.StringIO(data)
        got = [x for x in jstream.json_objects(data_stream)]
        self.assertTrue(expect == got, 
                msg="\n  expected: {}\n  got: {}\n".format(expect,got))

    def test_large_sequence(self):
        data = "[1,2,3]" + large_json
        expect = [[1,2,3], {'big-thing': big_thing}]
        data_stream = io.StringIO(data)
        got = [x for x in jstream.json_objects(data_stream)]
        self.assertTrue(expect == got, 
                msg="\n  expected: {}\n  got: {}\n".format(expect,got))

    def test_incomplete_sequence(self):
        data = "[1,2,3" + large_json
        expect = []
        data_stream = io.StringIO(data)
        got = [x for x in jstream.json_objects(data_stream)]
        self.assertTrue(expect == got, 
                msg="\n  expected: {}\n  got: {}\n".format(expect,got))

    def test_empty_sequence(self):
        data_stream = io.StringIO('')
        expect = []
        got = [x for x in jstream.json_objects(data_stream)]
        self.assertTrue(expect == got,
                msg="\n  expected: {}\n  got: {}\n".format(expect,got))

if __name__ == '__main__':
    unittest.main()
