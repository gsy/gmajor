# -*- coding: utf-8 -*-

import abjad
from abjad import Note, Measure, Rest, TimeSignature, Duration, Chord, show
from fractions import Fraction
import xml.etree.ElementTree as parser

tree = parser.parse('./castle.xml')
root = tree.getroot()


def parse_duration(duration_type, dot_count):
    if duration_type == 'eighth':
        duration = Fraction(1, 8)
    elif duration_type == 'quarter':
        duration = Fraction(1, 4)
    elif duration_type == 'half':
        duration = Fraction(1, 2)
    elif duration_type == 'whole':
        duration = Fraction(1, 1)

    if dot_count:
        duration = duration * (Fraction(1, 1) + Fraction(1, 2) * dot_count)

    return (duration.numerator, duration.denominator)


def parse_pitch(step, octave, alter=""):
    def parse_alter(alter):
        if alter == "1":
            return "#"
        else:
            return ""

    return "{}{}{}".format(step, parse_alter(alter), octave)


def make_pitch(step, octave, alter=""):
    alter_str = "#" if alter == "1" else ""
    return "{}{}{}".format(step, alter_str, octave)


def make_duration():
    pass


def make_note():
    pass


def construct_pitch(pitch_node, _duration_type, _dot_count):
    _step = pitch_node.find("step").text
    _octave = pitch_node.find("octave").text
    _alter = pitch_node.find("alter")

    if _alter is not None:
        _parsed_pitch = parse_pitch(_step, _octave, _alter.text)
    else:
        _parsed_pitch = parse_pitch(_step, _octave)

    _parsed_duration = parse_duration(_duration_type, _dot_count)
    return Note.from_pitch_and_duration(_parsed_pitch, _parsed_duration)


measures = []
chord_number = 0
count = 0

for _measure in root.iter(tag='measure'):
    number = int(_measure.attrib["number"])
    print("measuer number", number)

    notes = []
    chord = []
    pre_note = None
    has_tuplet, actual_notes, normal_notes, tuplet_elements = False, 1, 1, []

    for note in _measure.iter(tag='note'):
        _note = note[0]
        _pitch = note.find("pitch")
        _duration = note.find("duration")
        _duration_type = note.find("type").text
        dots = note.findall("dot")
        _dot_count = len(dots) if dots is not None else 0

        if _note.tag == "chord":
            _pitch = note.find("pitch")
            current = construct_pitch(_pitch, _duration_type, _dot_count)
            chord = [pre_note, current]
            _parsed_duration = parse_duration(_duration_type, _dot_count)
            if has_tuplet:
                tuplet_elements.pop()
                tuplet_elements.append(Chord(chord, Duration(_parsed_duration)))
            else:
                notes.pop()
                notes.append(Chord(chord, Duration(_parsed_duration)))

        elif _note.tag == "pitch":
            _modification = note.find("time-modification")

            if _modification is not None:
                if has_tuplet is False:
                    has_tuplet = True
                    actual_notes = int(_modification.find("actual-notes").text)
                    normal_notes = int(_modification.find("normal-notes").text)
            else:
                if has_tuplet:
                    notes.append(abjad.Tuplet((normal_notes, actual_notes), tuplet_elements))
                has_tuplet = False

            note = construct_pitch(_pitch, _duration_type, _dot_count)
            if has_tuplet:
                tuplet_elements.append(note)
            else:
                notes.append(note)

            pre_note = note

        elif _note.tag == "rest":
            _parsed_duration = parse_duration(_duration_type, _dot_count)
            notes.append(Rest(abjad.Duration(_parsed_duration)))
        else:
            print(_note.tag)

    measure = Measure(TimeSignature((4, 4)), notes)
    measures.append(measure)

clef = abjad.Clef('treble_8')
abjad.attach(clef, measures[0][0])
staff = abjad.Staff(measures)
show(staff)

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
