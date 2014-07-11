w20e.pycms_workflow
===================

Workflow module for PyCMS. To use it in your PyCMS app, add the egg
dependency (usually in your buildout) and include the package ZCML
from your configure.zcml like so:

  <include package="w20e.pycms_workflow"/>

To include a workflow, for example the very simple public/private
worfklow provided in this package, add to your zcml:

  <include file="w20e.pycms_workflow:workflow/simple.zcml" />

You may want to create more complex workflows than the simple one
provided. Check out the example workflow in ./workflow/simple.zcml and
start reading the repoze.workflow documentation. That's precisely what
is under the hood...  Include your own file in ZCML, et voila!
