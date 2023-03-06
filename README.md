# py-chrome-eq-script
Use plain text parametric EQ filters in Google Chrome or other Chromium-based browsers.

# Background
This script is primarily for chromebook users. As far as I know, there is no chrome extension that allows you to directly import plain text parametric EQ filters, such as those provided by the AutoEQ project. This script is able to convert such filters and output a preset file which can imported to the chrome extension "[Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik)". Until a chrome extension adds this functionality by default, this is probably the only way to import an EQ profile to a chromebook.

# Usage
- Obtain parametric EQ filters for your headphones/earbuds from AutoEQ [here](https://github.com/jaakkopasanen/AutoEq/tree/master/results) or elsewhere.

- Rename the file to ```input.txt``` and place it in the same directory as ```main.py```

- Run ```main.py```, the output file will be named ```eq-script-output.json```

- Add the [Ears: Bass Boost, EQ Any Audio!](https://chrome.google.com/webstore/detail/ears-bass-boost-eq-any-au/nfdfiepdkbnoanddpianalelglmfooik) to your browser

- Click on the extension icon and click "Import Presets" and then navigate to ```eq-script-output.json```

- If the preset isnt automatically applied, it is named "test" and you should see it right next to the bass boost preset which is there by default. Click on it to apply the preset.



