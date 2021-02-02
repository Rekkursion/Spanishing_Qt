from dataclasses import dataclass, field
from enum import Enum


# the node-type of a component
class NodeType(Enum):
    VOWEL = 0
    CONSONANT = 1
    OTHER = 2


# the node-class for the linked-list
@dataclass
class Node:
    component: str
    node_type: NodeType
    next_p: any = field(default=None, compare=False)
    prev_p: any = field(default=None, compare=False)


class SyllableLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    # push a component back into the list
    def push_back(self, component: str, node_type: NodeType):
        # the new node
        node = Node(component=component, node_type=node_type)
        # if the list is empty currently
        if self.__head is None:
            self.__head = node
            self.__tail = node
        # if the list is not empty
        else:
            self.__tail.next_p = node
            node.prev_p = self.__tail
            self.__tail = node

    # combine a certain node w/ the previous one
    def combine_with_previous_node(self, q: Node):
        p = q.prev_p
        if q is not None and p is not None:
            # combine the components
            q.component = p.component + q.component
            # combine the node-type
            if q.node_type == NodeType.VOWEL or p.node_type == NodeType.VOWEL:
                q.node_type = NodeType.VOWEL
            # delete the previous node
            q.prev_p = p.prev_p
            if p.prev_p is not None:
                p.prev_p.next_p = q
            # if the deleted node is the head-node, re-point it at the q-node
            if self.__head == p:
                self.__head = q

    # combine a certain node w/ the next one
    def combine_with_next_node(self, p: Node):
        q = p.next_p
        if p is not None and q is not None:
            # combine the components
            p.component += q.component
            # combine the node-type
            if p.node_type == NodeType.VOWEL or q.node_type == NodeType.VOWEL:
                p.node_type = NodeType.VOWEL
            # delete the next node
            p.next_p = q.next_p
            if q.next_p is not None:
                q.next_p.prev_p = p
            # if the deleted node is the tail-node, re-point it at the p-node
            if self.__tail == q:
                self.__tail = p

    # convert the linked-list as a copied python-list and return it
    def as_list_copied(self):
        ret = []
        p = self.__head
        while p is not None:
            ret.append(p)
            p = p.next_p
        return ret

    # for testing
    def __repr__(self):
        ret = ''
        p = self.__head
        while p is not None:
            ret += f'[{p.component},{p.node_type.name}] -> '
            p = p.next_p
        return ret
