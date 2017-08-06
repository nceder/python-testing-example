"""
 https://github.com/lathama/python-testing-example
"""

import datetime
import os
import sys
import unittest

from testingdemo.howto import *

__version__ = '1.0.1'


if '-t' in sys.argv:
    TESTING = True
else:
    TESTING = False

if not __debug__ or TESTING:
    print("### Running Tests, Coverage, and Style Checks ###")
    import_dir = "./libraries/"
    for d in os.listdir(import_dir):
        if os.path.isdir(import_dir + d):
            sys.path.insert(1, import_dir + d)

    try:
        import coverage
        COVERAGE = True
    except ImportError:
        COVERAGE = False
    try:
        import pycodestyle
        STYLECHECK = True
    except ImportError:
        STYLECHECK = False

    if COVERAGE:
        codecoverage = coverage.Coverage(omit='*unittests/*')
        # Unittests skew results
        codecoverage.start()
    else:
        print("Code Coverage Disabled")

    unittesting_log = open('unittesting.log', 'w')
    timestamp = str(datetime.datetime.now().isoformat(' ')) + "\n"
    unittesting_log.write("Testing Example - " + timestamp)
    suite = unittest.TestLoader().discover('./testingdemo/unittests')
    unittest.TextTestRunner(stream=unittesting_log, descriptions=True,
                            verbosity=3).run(suite)
    unittesting_log.close()

    unittesting_log = open('unittesting.log')
    print(unittesting_log.read())
    unittesting_log.close()

    if COVERAGE:
        codecoverage.stop()
        codecoverage.save()
        codecoverage.html_report(directory="coverage")
        print("Code coverage report done. See the index.html in: ")
        print("\t" + '/coverage')

    if STYLECHECK:
        print('Style Check Start')
        checker = pycodestyle.StyleGuide(exclude=['libraries'], quiet=False)
        result = checker.check_files('.')
        print('Style Check End')
    else:
        print("Code Style Checking is disabled")
    print("### Finished Tests, Coverage, and Style Checks ###")

