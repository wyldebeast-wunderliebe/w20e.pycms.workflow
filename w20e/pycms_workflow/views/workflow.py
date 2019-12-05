from builtins import object
from w20e.pycms_workflow.workflow import Workflow
from w20e.pycms.actions import IActions


class TransView(object):

    """ Provide transitions """

    def __init__(self, context, request):

        self.context = context
        self.request = request
        self.wf = Workflow(self.context, self.request)

    def __call__(self):

        res = {'wf': self.wf}

        reg = self.request.registry

        actions = reg.getUtility(IActions)

        res['action'] = actions.get_action("content", "state")

        if self.request.params.get("to", None):

            self.wf.trans_to(self.request.params['to'])

        return res
