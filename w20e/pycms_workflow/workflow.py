from zope.interface import Interface, implementedBy
from repoze.workflow import get_workflow


def add_wf(event):

    if event['renderer_name'].endswith("action_workflow.pt"):

        try:
            event['wf'] = Workflow(event['context'], event['request'])
        except:
            event['wf'] = None


class Workflow(object):

    def __init__(self, context, request):

        self.context = context
        self.request = request

        iface = implementedBy(self.context.__class__).flattened().next()
        self.wf = get_workflow(iface, 'security')

        assert(self.wf is not None)

    @property
    def state(self):
        return self.wf.state_of(self.context)

    @property
    def transitions(self):
        return self.wf.get_transitions(self.context, self.request)

    def trans_to(self, to_state):

        """ Transition to state """
        
        self.wf.transition_to_state(self.context, self.request, to_state)
