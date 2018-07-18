class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for c in self.children:
            ret += c.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'


