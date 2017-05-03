"""
 https://github.com/lathama/python-testing-example
"""
#from __future__ import print_function
#import future_builtins
import os, sys, time, unittest

import_dir = "./libraries/"
for d in os.listdir(import_dir):
 if os.path.isdir(import_dir + d):
  sys.path.insert(1, import_dir + d)

__version__ = '1.0.0'
TESTING = True

from testingdemo.howto import AnExample

if TESTING:
  COVERAGE = False
  try:
    import coverage
    COVERAGE = True
    codecoverage = coverage.Coverage()
    codecoverage.exclude("import", which="exclude")
    codecoverage.start()
  except:
    COVERAGE = False
    print("\n Coverage not importable, skipping code coverage testing")
  unittesting_log = open('unittesting.log', 'w')
  unittesting_log.write("Testing - " + str(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())) + "\n")
  suite = unittest.TestLoader().discover('unittests')
  unittest.TextTestRunner(stream=unittesting_log,descriptions=True,verbosity=3).run(suite)
  unittesting_log.close()

somethinguseful = AnExample()
somethinguseful.make_something()
somethinguseful.report_something()

if COVERAGE:
  codecoverage.stop()
  codecoverage.save()
  codecoverage.html_report(directory="coverage")