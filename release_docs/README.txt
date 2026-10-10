PENTIS 0.9
===============

A falling-block puzzle game with pentominoes: every piece is made of
five blocks instead of four. There are more shapes, more awkward gaps
and more ways to clear several rows at once.

Thank you for playing!


GETTING STARTED
---------------
macOS:    Unzip, drag Pentis into Applications and open it.
          The first time, macOS will block it - read
          "How to open Pentis on Mac.txt" (takes one minute, only once).

Windows:  Unzip and run Pentis.exe.
          If Windows shows "Windows protected your PC", click
          "More info" and then "Run anyway".

On first start, go to OPTIONS > Username and enter your name so your
highscores are saved under it.


CONTROLS (default)
------------------
  Left / Right arrow     Move the piece
  Down arrow             Move the piece down one row
  Z                      Rotate counter-clockwise
  X                      Rotate clockwise
  C                      Rotate 180 degrees
  Space                  Smash - drop the piece to the bottom instantly

  P or Esc               Pause
  M                      Music on / off
  H                      Help screen (full rules and scoring)

All piece controls can be changed in OPTIONS > Controls.


HOW TO PLAY
-----------
Fill complete horizontal rows to clear them. The game ends when the
pieces stack up to the top.

Modes (OPTIONS > Mode)
  Practice      No speed-up. Scores are not saved.
  Competitive   The game gets faster over time. Scores are saved.

Difficulty (OPTIONS > Difficulty) - how many different pentomino shapes
can appear. Each difficulty has its own scoreboard.
  Novice    9 shapes
  Standard  11 shapes
  Advanced  12 shapes
  Pro       13 shapes

Scoring
  Piece placed        3 points
  1 row cleared     100 points
  2 rows cleared    400 points
  3 rows cleared    900 points
  4 rows cleared  1,600 points
  5 rows cleared  2,500 points
  (rows cleared x rows cleared x 100 - clearing several rows at once
  pays off!)

DAS - Delayed Auto Shift (OPTIONS > DAS)
  Initial Delay   How long you hold Left/Right before the piece starts
                  sliding on its own.
  Repeat Rate     How fast it slides while you keep holding the key.

Languages: English, Deutsch, Romana (OPTIONS > Language).


YOUR SAVED DATA
---------------
Settings and highscores are stored here:
  macOS:    ~/Library/Application Support/Pentis
  Windows:  %LOCALAPPDATA%\Pentis
            (paste this into the File Explorer address bar)

Deleting that folder resets Pentis to a fresh install.


FEEDBACK AND BUG REPORTS
------------------------
Any kind of feedback is welcome - what you liked, what felt wrong,
what you would like to see next.

  E-mail:   pentis.feedback@gmail.com
  Website:  https://grapefruit256.itch.io/pentis

If Pentis ever closes unexpectedly, a file called crash.log is written
to the saved-data folder above. Please attach it to your bug report,
together with your operating system version. It helps us a lot.


CREDITS
-------
Project owner:  Grapefruit 256
Built with Python and Pygame.

Pentis (c) 2026. All rights reserved.
