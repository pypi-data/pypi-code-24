from builtins import str
from builtins import object
import pygraphviz as pgv


class Visualizer(object):

    def __init__(self):
        self._added = set()


    def _add_state_and_children(self, graph, state, added_state_ids):
        if state.identifier in added_state_ids:
            return
        if state.success:
            graph.add_node(
                    state.identifier,
                    color='green',
                    label=str(state.identifier) + ' [' +
                    ','.join(state.matched_keywords) + ']')
        else:
            graph.add_node(state.identifier)
        added_state_ids.add(state.identifier)
        for symbol, child in state.transitions.items():
            self._add_state_and_children(graph, child, added_state_ids)
            graph.add_edge(state.identifier, child.identifier, label=symbol)
    
    
    def draw(self, filename, kwtree):
        graph = pgv.AGraph(directed=True)
        added_state_ids = set()
        self._add_state_and_children(graph, kwtree._zero_state, added_state_ids)
        graph.draw(filename, prog='dot')
