from __future__ import absolute_import

from .model import *

from argparse import ArgumentParser

def build_argument_parser(executable):
    """

    :param executable:
    :return:
    """

    a = ArgumentParser()
    a.add_argument("--xml")

    return a