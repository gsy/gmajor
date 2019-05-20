import abjad


staff = abjad.Staff("c'4 d'4 e'4 d'4 f'4")
manager = abjad.persist(staff)
print(manager)
for x in abjad.persist(staff).as_midi():
    x
    print(x)
