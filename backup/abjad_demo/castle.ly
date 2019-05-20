\version "2.18.2"
\include "event-listener.ly"

\header {
    encodingsoftware = "Guitar Pro 6"
    encodingdate = "2019-01-23"
    copyright = "久石让"
    title = "castle in the sky"
    }

\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPZeroVoiceOne =  \relative e' {
    \transposition c' \clef "tab" \stopStaff \override Staff.StaffSymbol
    #'line-count = #6 \startStaff \key c \major
    \numericTimeSignature\time 4/4 \tempo "" 4=80 r4 r2 e8 \1 [ fis8 \1
    ] | % 1
    \clef "tab" <g e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ fis'8 \1 ] g4 \1 b4
    \1 | % 2
    \clef "tab" <fis d,>8 ~ \1 [ \4 [ <b, fis'>8 \3 ] ~ \1 ] <d fis>8 \2
    [ \1 [ fis8 ~ \1 ] fis4 \1 b,4 \2 | % 3
    \clef "tab" <e c,>8 \1 [ \5 [ e,8 \4 ] g8 \3 [ d'8 \2 ] e4 \1 g4 \1
    | % 4
    \clef "tab" <b,, d'>8 \5 [ \2 [ d8 \4 ] g8 \3 [ d'8 ~ \2 ] d4 \2 b8
    \2 [ b8 \2 ] | % 5
    \clef "tab" <c a,>8 \2 [ \5 [ e,8 \4 ] a8 \3 [ b8 \2 ] c4 \2 g'4 \1
    | % 6
    \clef "tab" <b, g,>8 \2 [ \6 [ e,8 \4 ] g8 \3 [ b8 ~ \2 ] b8 \2 [ b8
    \2 ] b8 \2 [ b8 \2 ] | % 7
    \clef "tab" <fis' fis,,>8 \1 [ \6 [ fis,8 \4 ] ais8 \3 [ cis8 \2 ]
    cis4 \2 fis4 \1 | % 8
    \clef "tab" <fis b,,>8 \1 [ \5 [ fis,8 \4 ] dis'8 \2 [ fis8 \1 ] fis4
    \1 e8 \1 [ fis8 \1 ] | % 9
    \clef "tab" <g e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ fis'8 \1 ] g4 \1 b4
    \1 | \barNumberCheck #10
    \clef "tab" <d,, fis'>8 \4 [ \1 [ b'8 \3 ] d8 \2 [ fis8 ~ \1 ] fis4
    \1 b,8 \2 [ b8 \2 ] | % 11
    \clef "tab" <e c,>8 \1 [ \5 [ e,8 \4 ] g8 \3 [ d'8 \2 ] e4 \1 g4 \1
    | % 12
    \clef "tab" <b,, d'>8 \5 [ \2 [ d8 \4 ] g8 \3 [ d'8 ~ \2 ] d4 \2 r8
    b8 \2 | % 13
    \clef "tab" <a, c'>4 \5 \2 g''8 \1 [ fis8 ~ \1 ] fis4 \1 g4 \1 | % 14
    \clef "tab" \times 2/3 {
        <a e,,>4 \1 \6 a4 \1 b4 \1 }
    g4 \1 r4 | % 15
    \clef "tab" <g a,,>8 \2 [ \5 [ fis8 \2 ] e8 \2 [ e8 \2 ] <fis b,,>4
    \1 \5 dis4 \2 | % 16
    \clef "tab" <e e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ e8 ~ \1 ] e4 \1 g8
    \1 [ a8 \1 ] | % 17
    \clef "tab" <b g,>4. \1 \3 a8 \1 b4 \1 d4 \1 | % 18
    \clef "tab" <a fis,>4. \1 \4 fis,8 ~ \4 fis4 \4 d'8 \2 [ d8 \2 ] | % 19
    \clef "tab" <g e,>4. \1 \4 fis8 \1 g4 \1 b4 \1 | \barNumberCheck #20
    \clef "tab" <b d,,>4. \1 \4 d,,4. ~ \4 d4 \4 | % 21
    \clef "tab" <e' c,>8 \1 [ \5 [ fis8 \1 ] g4 \1 fis8 \1 [ g8 \1 ] a4
    \1 | % 22
    \clef "tab" <g b,,>4. \1 \5 d8 \2 d4 \2 c,8 \5 [ b8 \5 ] | % 23
    \clef "tab" <c'' a,,>4 \1 \5 b4 \1 a4 \1 g4 \2 | % 24
    \clef "tab" <b b,,>8 ~ \1 [ \6 [ <a, b'>8 \4 ] ~ \1 ] <e' b'>8 \3 [
    ~ \1 [ <fis b>8 ~ \2 ] ~ \1 ] <fis b>8 \2 [ ~ \1 [ <a, b'>8 \4 ] ~
    \1 ] <e' b'>8 \3 [ ~ \1 [ <fis b>8 \2 ] ~ \1 ] | % 25
    \clef "tab" <b,, b''>8 \6 [ \1 [ a'8 \4 ] dis8 \3 [ fis8 \2 ] b4 \1
    b,4 \2 | % 26
    \clef "tab" <e e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ e8 \1 ] d8 \2 [ e,8
    \4 ] g8 \3 [ d'8 \2 ] | % 27
    \clef "tab" <b c,>8 \2 [ \5 [ a8 \3 ] g8 \3 [ c,8 ~ \5 ] c4 \5 r8 g'8
    \3 | % 28
    \clef "tab" <a d,>4 \3 \4 g8 \3 [ a8 ~ \3 ] a8 \3 d4. \2 | % 29
    \clef "tab" <b g,>4. \2 \6 g,8 \6 fis4 \6 b'4 \2 | \barNumberCheck
    #30
    \clef "tab" <e e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ e8 \1 ] d8 \2 [ e,8
    \4 ] g8 \3 [ d'8 \2 ] | % 31
    \clef "tab" <b c,>8 \2 [ \5 [ a8 \3 ] g8 \3 [ c,8 ~ \5 ] c4 \5 r8 g'8
    \3 | % 32
    \clef "tab" <a d,>4 \3 \4 g8 \3 [ a8 ~ \3 ] a4 \3 fis4 \4 | % 33
    \clef "tab" <e e,>8 \4 [ \6 [ b8 \5 ] e8 \4 [ g8 ~ \3 ] g4 \3 e8 \4
    [ fis8 \4 ] | % 34
    \clef "tab" g8 \4 [ b8 \2 ] e8 \1 [ fis,8 \4 ] g4 \4 b4 \2 | % 35
    \clef "tab" fis8 \4 [ b8 \3 ] d8 \2 [ fis8 ~ \1 ] fis4 \1 b,,8 \5 [
    b8 \5 ] | % 36
    \clef "tab" e8 \4 [ g8 \3 ] c8 \2 [ d,8 \4 ] e4 \4 g4 \4 | % 37
    \clef "tab" d8 \4 [ g8 \3 ] b8 \2 [ g'8 ~ \1 ] g4 \1 b,,8 \5 [ b8 \5
    ] | % 38
    \clef "tab" c8 \5 [ a'8 \3 ] c8 \2 [ b,8 \5 ] c4 \5 g'4 \4 | % 39
    \clef "tab" b,8 \5 [ g'8 \3 ] b8 \2 [ e8 ~ \1 ] e8 \1 [ g,8 \4 ] g8
    \4 [ g8 \4 ] | \barNumberCheck #40
    \clef "tab" fis8 \4 [ ais8 \3 ] cis8 \2 [ cis,8 \5 ] cis4 \5 fis4 \4
    | % 41
    \clef "tab" fis8 \4 [ a8 \3 ] dis8 \2 [ fis8 \1 ] fis4 \1 e8 \1 [
    fis8 \1 ] | % 42
    \clef "tab" <g e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ fis'8 \1 ] g4 \1 b4
    \1 | % 43
    \clef "tab" <fis d,>8 \1 [ \4 [ b,8 \3 ] d8 \2 [ fis8 ~ \1 ] fis4 \1
    b,4 \2 | % 44
    \clef "tab" <e c,>8 \1 [ \5 [ e,8 \4 ] g8 \3 [ d'8 \2 ] e4 \1 g4 \1
    | % 45
    \clef "tab" <d b,>8 \2 [ \5 [ d,8 \4 ] g8 \3 [ d'8 ~ \2 ] d4 \2 r8 b8
    \2 | % 46
    \clef "tab" <c a,>4 \2 \5 g'8 \1 [ fis8 ~ \1 ] fis4 \1 g4 \1 | % 47
    \clef "tab" <a e,,>4 \1 \6 b8 \1 [ g8 ~ \1 ] g4 \1 r4 | % 48
    \clef "tab" <g a,,>8 \2 [ \5 [ fis8 \2 ] e8 \2 [ e8 \2 ] <fis b,,>4
    \1 \5 dis4 \2 | % 49
    \clef "tab" <e e,,>8 \1 [ \6 [ g,8 \3 ] b8 \2 [ e8 ~ \1 ] e4 \1 e8
    \1 [ fis8 \1 ] | \barNumberCheck #50
    \clef "tab" <g a,,>8 \1 [ \5 [ fis8 \1 ] e8 \1 [ e8 \1 ] fis4 \1 dis4
    \2 | % 51
    \clef "tab" <e b g e b e,>1 \1 \2 \3 \4 \5 \6 }


% The score definition
\score {
    <<
        \new TabStaff \with { stringTunings = #`( ,(ly:make-pitch 0 2 0)
            ,(ly:make-pitch -1 6 0) ,(ly:make-pitch -1 4 0)
            ,(ly:make-pitch -1 1 0) ,(ly:make-pitch -2 5 0)
            ,(ly:make-pitch -2 2 0) ) } <<
            \set TabStaff.instrumentName = "Steel Guitar"
            \set TabStaff.shortInstrumentName = "S-Gt"
            \context TabStaff <<
                \context TabVoice = "PartPZeroVoiceOne" { \PartPZeroVoiceOne }
                >>
            >>

        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {}
    }
