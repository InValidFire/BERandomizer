# BERandomizer
Personal project aimed to randomize everything possible within Minecraft Bedrock Edition
## Current Features
- Automatic updates (can be disabled in a future version)
- Fully randomize all available recipes in BE 1.12, 1.13, and 1.14
    - Should support future recipes as they're added with little or no modification
- Allows for multiple datasets
    - Can store 1.12, 1.13, and 1.14 behavior data
    - Lets you choose which one to randomize
    - Supports randomizing custom data as well
        - Just drop it in it's own folder
        - data/DATASETNAME/(data contents)
            - ex. data/Vanilla-1.12/stuff
- Generates based on seed
    - Input same seed, get the same results.
    - Accepts strings or numbers, go wild.
        - Y'all know how this works. :p
## Planned Features
- Store both resource and behavior data
	- Needed to start randomizing blocks
- Settings
    - Toggle automatic updates
	- Choose file name
	- Choose directory format
- Add data values to documentation
- Automatically download data if nothing is found
- More error handling
    - Verify data has manifest.json
        - Possibly hard code manifest creation?
- Code optimization
    - Definitely needs work
- User-friendliness improvements
- More randomness
    - loot tables
    - entities?
    - blocks?
    - randomly generated custom blocks/items/entities?
        - this one will be fun!
## Usage
In order to use this, make sure y'all have Python installed, once that is done, download this repo, extract if necessary, and click on Run.bat to start the script.

Remember to place behavior pack data in data/pickaname/(extract here) otherwise you'll get errors.
Any questions on anything, contact me on Discord with Fire#4224