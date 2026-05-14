---
name: project-highscores
description: Highscores/scoreboard system is fully implemented - do not claim it's a stub
metadata:
  type: feedback
---

The scoreboard IS fully implemented in `inoutput.py:highscoreBox()`. It:
- Reads from the encrypted local file via `readHighscoresJS()`
- Has hardcoded baseline entries (fictitious players) per mode as a starting leaderboard
- Merges saved scores with hardcoded ones (saved score wins if higher)
- Renders a sortable, scrollable, per-mode leaderboard with Rank/Player/Score columns
- Left/right navigation between modes (Novice, Standard, Advanced, Pro)

**Why:** I incorrectly claimed the scoreboard was a stub because I only saw `print("online highscores will be available asap")` in startMenu.py without checking that `io.highscoreBox()` was already being called. The print is just a leftover debug line.

**How to apply:** Always read `highscoreBox` in inoutput.py before making claims about scoreboard completeness.
