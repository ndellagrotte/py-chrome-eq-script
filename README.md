# py-chrome-eq-script
Use AutoEQ/custom EQ filters in Google Chrome or other Chromium-based browsers.

# Background
This script is primarily for chromebook users. As far as I know, there is no chrome extension that allows you to directly import parametric equalizer filters in the Equalizer APO format, such as those provided by the AutoEQ project. This script is able to convert such filters and output a preset file which can imported to the chrome extension "[Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik)". Until a chrome extension adds this functionality by default, this is probably the only way to import a custom EQ profile to a chromebook.

# Limitations
- There is no preamp option, but there is a volume slider which you should use if you experience clipping.

- You should only use this script on EQs that have 9 filters or less

- Filter type is unsupported, the default is PK (Peaking filter)

# Usage
- Obtain parametric EQ filters for your headphones/earbuds from AutoEQ [here](https://github.com/jaakkopasanen/AutoEq/tree/master/results) or elsewhere.

- Useage: ```python3 py-chrome-eq-script.py <file path of input file>```

-  the output file will be named ```output.json```

- Add the [Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik) extension to your browser

- Click on the extension icon and click "Import Presets" and then navigate to ```output.json```

- If the preset isn't automatically applied, you should be able to see it next to the bass boost preset which is there by default. It's called "py-chrome-eq-script" and you can click on it to apply the preset.




