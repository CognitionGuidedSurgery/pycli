import unittest

__author__ = 'Alexander Weigl <Alexander.Weigl@student.kit.edu>'
__date__ = "2015-02-19"
__version__ = "0.1"

import pycli, os.path, sys

ROOT = os.path.dirname(os.path.abspath(__file__))

from xml.etree import  ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


class BaseTests(unittest.TestCase):
    def test_reading_xml_reg_aladin(self):
        executable = pycli.Executable.from_xml(os.path.join(ROOT, "reg_aladin.xml"))
        print repr(executable)

        print prettify(executable.as_xml())


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
