import abjad
from abjad import Note, show

# notes = [
#     Note("c'4"),
#     Note(0, abjad.Duration(1, 4)),
#     Note("d'4"),
#     Note(2, abjad.Duration(1, 4)),
#     Note("e'4"),
#     Note(4, abjad.Duration(1, 4)),
#     Note("f'4"),
#     Note(5, abjad.Duration(1, 4)),
#     Note("g'4"),
#     Note(7, abjad.Duration(1, 4)),
#     Note("a'4"),
#     Note(9, abjad.Duration(1, 4)),
#     Note("b'4"),
#     Note(11, abjad.Duration(1, 4)),

#     abjad.Note.from_pitch_and_duration('C#5', (3, 16))
# ]

# notes = [
#     # Note.from_pitch_and_duration('E4', (1, 8)),
#     # Note.from_pitch_and_duration('F#4', (1, 8)),
#     abjad.Chord([Note.from_pitch_and_duration('G4', (1, 8)), Note.from_pitch_and_duration('E2', (1, 8))],
#                 abjad.Duration(1, 8)),
#     Note.from_pitch_and_duration('G3', (1, 8)),
#     Note.from_pitch_and_duration('B3', (1, 8)),
#     Note.from_pitch_and_duration('F#4', (1, 8)),
#     Note.from_pitch_and_duration('G4', (1, 4)),
#     Note.from_pitch_and_duration('B4', (1, 4)),
# ]

notes = [
    abjad.Tuplet((2, 3),
                 [abjad.Chord([Note.from_pitch_and_duration('A4', (1, 4)),
                               Note.from_pitch_and_duration('E2', (1, 4))],
                              abjad.Duration(1, 4)),
                  Note.from_pitch_and_duration('A4', (1, 4)),
                  Note.from_pitch_and_duration('B4', (1, 4))]),
    Note.from_pitch_and_duration('G4', (1, 4)),
]

# clef = abjad.Clef('treble_8')
staff = abjad.Staff(notes)
# abjad.attach(clef, staff)
show(staff)
