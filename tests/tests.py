'''
@author: nino
'''
import unittest
import yaml
from nose.tools import assert_raises #@UnresolvedImport
import os
import sys

from csdl.parser import parser, CSDLParser

parse = parser.parseString

def yaml_dump(s):
    d = {"test_": dict(input=s, output=parse(s).asList())}
    sys.stderr.write("""%s

""" % yaml.dump(d))

class Test(unittest.TestCase):
    def test_comparison_statements(self):
        for s, op in [("""twitter.text contains "google" """, "contains"),
                      ("""interaction.sample < 5.25""", "<"),
                      ("""interaction.sample in [5.25, 12]""", "in")]:
            v = parse(s)
            assert len(v[0]) == 3
            assert v[0][1] == op

    def test_exists(self):
        for s in ["""interaction.geo exists"""]:
            v = parse(s)
            assert v[0][1] == "exists"
            
    def test_input_output(self):
        d = yaml.load(open(os.path.join(os.path.dirname(__file__), "tests.yaml")))
        for test_name, test in d.iteritems():
            print "testing", test_name
            input = test['input']
            output = test['expected']
            parsed = parse(input)
            def on_fail():
                test["result"] = parsed.asList()
                return "Result...\n" + yaml.dump({test_name: test})
            assert parsed.asList() == output, on_fail()
    
    def test_custom_parser(self):
        class MyParser(CSDLParser):
            def validateIdentifier(self, token):
                if token[0].startswith("interaction"):
                    raise Exception("fail")
        
        parser = MyParser()
        parser.parseString('twitter.text contains "Cincinnati Reds"')
        assert_raises(Exception, parser.parseString, "interaction.geo exists")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
