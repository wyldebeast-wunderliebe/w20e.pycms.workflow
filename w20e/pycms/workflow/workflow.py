from zope.interface import Interface, implementedBy
from repoze.workflow import get_workflow


def add_wf(event):

    if event['renderer_name'] == 'w20e.pycms:templates/action_workflow.pt':

        event['wf'] = Workflow(event['context'], event['request'])


class Workflow(object):

    def __init__(self, context, request):

        self.context = context
        self.request = request

        iface = implementedBy(self.context.__class__).flattened().next()
        self.wf = get_workflow(iface, 'security')

    @property
    def state(self):
        return self.wf and self.wf.state_of(self.context) or "-"

    @property
    def transitions(self):
        return self.wf and self.wf.get_transitions(self.context,
                                                   self.request) or []

    def trans_to(self, to_state):

        """ Transition to state """
        
        self.wf.transition_to_state(self.context, self.request, to_state)
