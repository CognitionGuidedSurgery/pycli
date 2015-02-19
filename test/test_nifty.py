import unittest

__author__ = 'Alexander Weigl <Alexander.Weigl@student.kit.edu>'
__date__ = "2015-02-19"
__version__ = "0.1"

import pycli, os.path

ROOT = os.path.dirname(os.path.abspath(__file__))


class BaseTests(unittest.TestCase):
    def test_reading_xml_reg_aladin(self):
        executable = pycli.Executable.from_xml(os.path.join(ROOT, "reg_aladin.xml"))
        print repr(executable)


    def test_reading_xml_reg_f3d(self):
        executable = pycli.Executable.from_xml(os.path.join(ROOT, "reg_f3d.xml"))
        print executable


    def test_reading_xml_reg_jacobian(self):
        executable = pycli.Executable.from_xml(os.path.join(ROOT, "reg_jacobian.xml"))
        print executable


    def test_reading_xml_reg_tools(self):
        executable = pycli.Executable.from_xml(os.path.join(ROOT, "reg_tools.xml"))
        print executable


    def test_exec_xml_stub(self):
        return True


from pycli import *
