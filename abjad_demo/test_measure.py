# -*- coding: utf-8 -*-

import abjad
from abjad import Note, Measure, TimeSignature, show


notes = [
    abjad.Chord([Note.from_pitch_and_duration('G4', (1, 8)),
                 Note.from_pitch_and_duration('E2', (1, 8))],
                abjad.Duration(1, 8)),
    Note.from_pitch_and_duration('G3', (1, 8)),
    Note.from_pitch_and_duration('B3', (1, 8)),
    Note.from_pitch_and_duration('F#4', (1, 8)),
    Note.from_pitch_and_duration('G4', (1, 4)),
    Note.from_pitch_and_duration('B4', (1, 4)),
]

clef = abjad.Clef('treble_8')
measure = Measure(TimeSignature((4, 4)), notes)
abjad.attach(clef, measure[0])
show(measure)
