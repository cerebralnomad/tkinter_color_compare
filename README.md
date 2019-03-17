# tkinter_color_compare
Compare up to four colors available to tkinter on Ubuntu

This is a companion app to https://github.com/cerebralnomad/tkinter_color_demo
Where it previews a single color at a time, wit hthis one you can select four colors
to see how they look together.

This program works on Ubuntu flavors. It may or may not work the same on other distros
or operating systems.  
The color list is taken from /etc/X11/rgb.txt on Ubuntu systems.

##Installation

Download both .py files to their own directory or clone the repo. Make color_compare.py executable and run it

##Usage

When first opened, this screen is displayed:

![Screenshot](/screenshots/color_compare1.png?raw=true "Screenshot")

Use the four drop down boxes to choose the color for each of the four panels.  
Click the 'Change Colors' button to apply the changes.

![Screenshot](/screenshots/color_demo2.png?raw=true "Screenshot")

Select new colors to compare or click 'Exit' to quit the program.

The color names you decide on are used in the "background = <color>" parameters in tkinter.

