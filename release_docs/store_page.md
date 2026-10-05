# Pentis 0.9 beta: download page text

This is the text for the public download page (itch.io or similar).
Copy everything below the line. Things to fill in or check before publishing are marked **[TODO]**.

---

## Pentis

**Falling blocks, one block more.**

Pentis is a falling-block puzzle game played with *pentominoes*: every piece is made of five blocks instead of four. That means more shapes, trickier gaps and bigger combos. Clearing five rows at once is possible, and it pays 2,500 points.

### Features

- **Up to 13 different pentomino shapes.** Choose from four difficulty levels, from Novice (9 shapes) to Pro (13 shapes).
- **Two modes.** *Practice* to learn the pieces at your own pace, *Competitive* where the game keeps speeding up and your score counts.
- **Local scoreboards** for every difficulty level.
- **Fully remappable controls** and adjustable DAS (Delayed Auto Shift) for players who like to fine-tune.
- **Three rotation keys:** counter-clockwise, clockwise and 180°.
- **Music and sound effects**, each switchable on/off.
- **Three languages:** English, Deutsch, Română.

### Controls

| Key | Action |
|---|---|
| ← → | Move |
| ↓ | Move down one row |
| Z / X / C | Rotate counter-clockwise / clockwise / 180° |
| Space | Smash: drop the piece instantly |
| P or Esc | Pause |
| M | Music on/off |
| H | Help |

### Downloads

- **macOS** (Apple Silicon and Intel), macOS 11 or later **[TODO: confirm after the universal2 build]**
- **Windows** 10 / 11 **[TODO: confirm after the Windows build]**

### ⚠️ Mac users, please read

Pentis is not registered with Apple yet, so macOS blocks it the first time you open it. To allow it (only once):

1. Double-click Pentis and close the warning.
2. Open **System Settings → Privacy & Security**, scroll down and click **Open Anyway** next to "Pentis was blocked…".
3. Confirm with your password.

If macOS says the app is *"damaged"*, open Terminal, type `xattr -dr com.apple.quarantine ` (with a trailing space), drag Pentis into the Terminal window and press Return.

Step-by-step instructions are included in the download (*How to open Pentis on Mac.txt*).

### Windows users

If you see "Windows protected your PC", click **More info → Run anyway**.

### This is a beta

Pentis 0.9 is our first public release. Something may break, and we'd love to hear about it, along with anything you liked or didn't like. **[TODO: say where: comments below / email / Discord]**

If the game closes unexpectedly, it writes a `crash.log` file. Attaching it to your report helps us fix the problem quickly:

- macOS: `~/Library/Application Support/Pentis`
- Windows: `%LOCALAPPDATA%\Pentis`

### Credits

Project owner: Martin · Developer: Samaia · Made with Python and Pygame

© 2026 Samaia Gahramanov. All rights reserved.
