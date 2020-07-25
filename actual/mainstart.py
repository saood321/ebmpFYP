from distanceCalculation import *
from cameraOpen import *
from landmarks import *
from tkinter.messagebox import *

mood=camera()
if not mood:
    showerror("EBMP","No mood has been detected")
else:
        import MusicPlayer
        MusicPlayer.call(mood,"normal")












