# py-chrome-eq-script
Use parametric EQ profiles in Google Chrome or other Chromium-based browsers.

# Background
This script is primarily intended to be used by Chromebook users. AFAIK, there are no chromium extensions which contain the functionality of importing and using parametric EQ profiles (APO Format), such as those provided by the AutoEQ project. This script can convert parametric EQ profiles and output a preset file, which can imported to the Chrome extension "[Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik)". Until a chromium extension adds this functionality by default, this is the most convenient solution for those who would like to import a custom parametric EQ profile to a Chromebook.

EDIT: By using the new "[AutoEQ web app](https://autoeq.app/)", it is now possible to download an AutoEQ profile that is directly compatible with the Ears extension. However, this is not a solution for those with custom parametric EQ profiles.

# Limitations
- This script does not import preamp because it is not supported by the Ears extension. However, there is a volume slider that can serve the same purpose if you experience clipping.

- Input EQ is limited to one high-shelf (HSC) filter, one low-shelf (LSC) filter, and nine peaking (PK) filters. If you are unable to run the script because of this, use the Equalizer tool at "[squig.link](https://squig.link/)" to remove, add, and modify filters for your EQ. The HSC filter must be the first filter, and the LSC filter must be the last one. Or, you can replace either of them with PK filters.

# Usage
- Obtain or create a parametric EQ profile for your audio device.

- Usage: ```python3 py-chrome-eq-script.py <file path of input file>```

-  the output file will be named ```output.json```

- Add the [Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik) extension to your browser

- Click on the extension icon. Then, click "Import Presets" and navigate to ```output.json```

- If the preset isn't automatically applied, you can click on the newly created preset called "py-chrome-eq-script" and you may click on it to apply the preset.
