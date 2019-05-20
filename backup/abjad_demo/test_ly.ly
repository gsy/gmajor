\version "2.18.2"

\header {
    tagline = ##f
  }

\include "event-listener.ly"


\score {
  \new Staff
  {
    {
      \set autoBeaming = ##f
      \time 4/4
      \clef "treble_8"
      r4
      r2
      es'8
    }
  }
}

% {
%   c' e' g' e'
% }
