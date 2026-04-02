


langText = {
  "de": {
    "StartMenu": {
      "01": "Starten",
      "02": "Optionen"
    },
    "OptionsMenu": {
      "01": "Audio",
      "02": "Steuerung"
    },
    "Game": {
      "01": "Spiel gestartet"
    },
        
    "bigOnes bO_01": {
      "01": "Jokes und mehrere strings wie bei "
    }
  },
  "en": {
    "StartMenu": {
      "01": "Start",
      "02": "Options"
    },
    "OptionsMenu": {
      "01": "Audio",
      "02": "Controls"
    },
    "Game": {
      "01": "Game started"
    }
  },
 # // ...
}

print(langText["en"]["Game"]["01"])

selected_language = "en"
section = "Game"
key = "01"

if selected_language in langText and section in langText[selected_language] and key in langText[selected_language][section]:
    game_started_text = langText[selected_language][section][key]
    print(game_started_text)
else:
    print("Übersetzung nicht gefunden.")


