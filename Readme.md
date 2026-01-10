# Bad Apple in Fontawesome

The aim of this project is to recreate the famous bad apple music video using icons from the fontawesome library.
Icons for black and white pixels as well as the output resolution can be set via the config file included.

Ill be dabbeling with the pillow image library for python and trying to render a preview frontend using tkinter
Fontawesome icons will be integrated using the ttkbootstrap-icons-fa package.

Lets see where this journey takes me..

### First hurdle:
Installing ffmpeg to path in windows. Why am i still not using the wsl?
 - Solution: Create a folder called ffmpeg on your C drive and add the files for ffmpeg adding them to the user path. Extra points for copying the ffmpeg.exe file and naming it ffmpeg without the extension to plan for compatibility with better operating systems

### Update
Rendering a window with tk is not that bad. Although its no where near as pretty as the usual bootstrap front ends im used to. No idea how to update any styling on this yet either.

Functionally speaking opening a window and rendering an image seems to work just fine for now but i will need to be able to figure out argument passing soon enough. Still unsure if i want to go for a config file or if i will be using argparse.

Im currently just iterating over the files in the frame folder. It would be useful to learn how generators work so i just yield a new image object with each call. But ram usage now seems fine enough. Ill cross that bridge when I get there.

