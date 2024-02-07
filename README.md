# py-chrome-eq-script
Use parametric EQ profiles in Google Chrome or other Chromium-based browsers.

# Background
This script is primarily for Chromebook users. As far as I know, no Chrome extension allows you to directly import parametric equalizer profiles in the Equalizer APO format, such as those provided by the AutoEQ project. This script can convert such profiles and output a preset file which can imported to the Chrome extension "[Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik)". Until a chrome extension adds this functionality by default, this is probably the only way to import a custom EQ profile to a Chromebook.

EDIT: By using the new "[AutoEQ web app](https://autoeq.app/)", it is now possible to download an AutoEQ profile that is directly compatible with the Ears extension. However, this is not a solution for those with custom parametric EQ profiles.

# Limitations
- This script does not import preamp because it is not supported by the Ears extension. However, there is a volume slider that can serve the same purpose if you experience clipping.

- Input EQ is limited to one high-shelf (HSC) filter, one low-shelf (LSC) filter, and nine peaking (PK) filters. If you are unable to run the script because of this, use the Equalizer tool at "[squig.link](https://squig.link/)" to remove, add, and modify filters for your EQ.

# Usage
- Obtain a parametric EQ profile for your headphones/earbuds.

- Usage: ```python3 py-chrome-eq-script.py <file path of input file>```

-  the output file will be named ```output.json```

- Add the [Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik) extension to your browser

- Click on the extension icon. Then, click "Import Presets" and navigate to ```output.json```

- If the preset isn't automatically applied, you should be able to see it next to the bass boost preset which is there by default. It's called "py-chrome-eq-script" and you can click on it to apply the preset.
