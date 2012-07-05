w20e.pycms.workflow
===================

Workflow module for PyCMS. To use it in your PyCMS app, add the egg
dependency (usually in your buildout) and include the package ZCML
from your configure.zcml like so:

  <include package="w20e.pycms_workflow"/>

You may want to create more complex workflows than the simple one
provided. Check out the example workflow in ./workflow/simple.zcml.
Include your own file in ZCML, et voila!
