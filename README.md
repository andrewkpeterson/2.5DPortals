# 2.5DPortals

![Demo](https://github.com/andrewkpeterson/2.5DPortals/blob/master/demo.gif)

In the GIF above, the narrow corrider connecting the red and green sides of the room is shorter on the 
inside than it is on the outside.

This program splits up a scene into convex sectors and then renders walls starting with the sector furthest from the camera to the sector the camera is current in.

The program renders the scene from the perspective of more than one camera. For instance,
when the main camera looks down the narrow corridor, the program renders from the perspective of a camera placed in a 
different part of the scene, where there is a shorter corridor.
