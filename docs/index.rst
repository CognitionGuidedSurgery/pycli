.. pycli documentation master file, created by
   sphinx-quickstart on Thu Feb 19 21:11:38 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to clictk's documentation!
==================================


clictk provides support for Common Toolkit's Command Line Interface XML descriptions.
It provides a Python model, can read and write XML description, argparse functionalities and calls CLIs.


Getting Started
---------------


Install via pip::

    $ pip install pyclictk


Work Cases
----------

Working with CLIs
~~~~~~~~~~~~~~~~~

.. code-block::

   m = clictk.Executable.from_exec("reg_aladin")
   m = clictk.Executable.from_xml("reg_aladin.xml")

   print repr(m)


Python as Executable
~~~~~~~~~~~~~~~~~~~~

.. code-block::

   e = Executable(
    ...
    )


Interface
---------

.. automodule:: clictk
   :members:
   :undoc-members:


.. automodule:: clictk.model
   :members:
   :undoc-members:
