# PTT as TOGGLE:

This is a simple script that enables you to use "push to talk" as a toggle instead of having to keep the PTT key pressed down in games such as League of Legends.

## How to use ?

You can either:
- Download the latest release and run the .exe file
- Or you can :
  1. Install python (the easiest way to do this is through the microsoft store)
  2. Run `python -m pip install keyboard` in a command line
  3. Run the script by double clicking on the python file or running `python your/path/to/ptt_as_toggle.py`

By default the push to talk key used is 'C' and you can press ',' to stop the script at any moment. You can change these by editing the "config.json" file to match your preferred keybinds. 

Be aware that this script works by emulating a key being held down whenever you toggle your push to talk on so make sure you toggle it off before typing otherwise it will keep writing "ccccccc"


*This project isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc*