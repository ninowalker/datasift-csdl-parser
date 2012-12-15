datasift-csdl-parser
====================

Python parser for Datasift's CSDL grammar. See http://dev.datasift.com/csdl

Usage
-----

    from csdl.parser import parser
    parsed = parser.parseString('twitter.text contains "Cincinnati Reds"')
    assert parsed.asList() == [['twitter.text', 'contains', '"Cincinnati Reds"']]

Running and adding tests
------------------------

    python setup.py nosetests
    
The file `tests/tests.yaml` contains an extensive list of tests. Please add to it if you feel the need.

License
-------

Copyright (C) 2012 Nino Walker

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
