# -*- coding: utf-8 -*-

import abjad
from abjad import Note, Measure, Rest, TimeSignature, Duration, Chord, show
from fractions import Fraction
import xml.etree.ElementTree as parser


class Tree(object):
    def __init__(self, root):
        self.root = root
        # 这个就是游标了
        self.current = root

    def add_child(self, node):
        self.current.add_node(node)
        self.current = node

    def add_parent(self, node, merge=False):
        if not merge or self.current.parent.tag != node.tag:
            self.current.parent.add_node(node)
            self.current.parent.remove_node(self.current)
            node.add_node(self.current)
            self.current.set_parent(node)
            self.current = node


class TreeNode(object):
    def __init__(self, tag):
        self._tag = tag
        self._is_leaf = True
        self._children = []
        self._parent = None

    def add_node(self, node):
        self._children.append(node)
        node.set_parent(self)
        self._is_leaf = False

    def remove_node(self, node):
        self._children.remove(node)
        if len(self._children) == 0:
            self._is_leaf = True

    def set_parent(self, parent):
        self._parent = parent

    def attach_maker(self, maker):
        self.maker = maker

    @property
    def tag(self):
        return self._tag

    @property
    def is_leaf(self):
        return self._is_leaf

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children


class ContextStack(object):
    def __init__(self):
        self.stack = []

    def new_context(self, context):
        self.stack.append(context)

    def current_context(self):
        return self.stack[-1]

    def remove_context(self):
        return self.stack.pop()


context_stack = ContextStack()


def make_duration(duration_type, dot_count):
    duration = {
        'eighth': Fraction(1, 8),
        'quarter': Fraction(1, 4),
        'half': Fraction(1, 2),
        'whole': Fraction(1, 1)
    }[duration_type]

    if dot_count:
        duration = duration * (Fraction(1, 1) + Fraction(1, 2) * dot_count)

    return (duration.numerator, duration.denominator)


def make_pitch(step, octave, alter=""):
    alter_str = "#" if alter == "1" else ""
    return "{}{}{}".format(step, alter_str, octave)


def make_note(note_node):
    context = context_stack.current_context()
    context.append()


def build_tree_from_xml(xml_file):
    document = parser.parse(xml_file)
    document_root = document.getroot()
    tree = Tree(TreeNode("score"))

    for _measure in document_root.iter(tag='measure'):
        number = int(_measure.attrib["number"])
        print("measuer number", number)

        # 一开头的 context 是在一个 measure 上
        tree.add_child(TreeNode("measure"))

        for note in _measure.iter(tag='note'):
            _note = note[0]
            time_modification = note.find("time-modification")
            # _pitch = note.find("pitch")
            # _duration = note.find("duration")
            # _duration_type = note.find("type").text
            # dots = note.findall("dot")
            # _dot_count = len(dots) if dots is not None else 0

            if _note.tag == "pitch":
                print("add pitch node")
                if time_modification is not None:
                    tree.add_parent(TreeNode("tuplet"), merge=True)
                tree.add_child(TreeNode("pitch"))

            elif _note.tag == "chord":
                print("add chord node")
                tree.add_parent(TreeNode("chord"), merge=True)
                tree.add_child(TreeNode("pitch"))

            elif _note.tag == "rest":
                print("add rest node")
                tree.add_child(TreeNode("rest"))

    return tree


def print_tree(root):
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        print(node.tag)
        for child in node.children:
            stack.append(child)


def build_score_from_tree(tree):
    stack = [tree.root]
    while len(stack) > 0:
        node = stack.pop()
        if node.tag == 'measure':
            pass


if __name__ == '__main__':
    tree = build_tree_from_xml('./castle.xml')
    print_tree(tree.root)
    score = build_score_from_tree(tree)
    show(score)


# clef = abjad.Clef('treble_8')
# abjad.attach(clef, measures[0][0])
# staff = abjad.Staff(measures)
# show(staff)





# duration = abjad.Duration(1, 4)
# rests = [abjad.Rest(abjad.Duration(1, 4)), abjad.Rest(abjad.Duration(2, 4))]


# notes = [
#     abjad.Note(16, abjad.Duration(1, 8)),
#     abjad.Note("e4", abjad.Duration(1, 8)),
#     abjad.Note(18, abjad.Duration(1, 8)),
#     # 这两个是一个 chord
#     abjad.Chord([19, -8], abjad.Duration(1, 8)),
#     abjad.Note(7, abjad.Duration(1, 8)),
#     abjad.Note(6, abjad.Duration(1, 8)),
#     abjad.Note(18, abjad.Duration(1, 8)),
#     abjad.Note(19, abjad.Duration(1, 4)),
#     abjad.Note(23, abjad.Duration(1, 4)),
# ]
# staff = abjad.Staff(rests + notes)

# abjad.show(staff)
# output = abjad.persist(staff).as_ly()
# out_file = output[0]
# command = "lilypond -dpreview -dbackend=svg {}".format(out_file)
# print(command)

# 理论知识：什么是 fifth of circle
