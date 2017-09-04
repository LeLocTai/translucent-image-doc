**************************
Frequently Asked Questions
**************************

Can I blur other UI?
--------------------

**TL;DR:** Kind of. See the demo.

If I run the blur algorithm once for each UI on the screen, it will get too expensive too fast.
Infact, if you use a Mac or Window 10 computer, you will notice the blur effect is disabled for windows that aren't in focus.

For this reason, the blurring is done once per camera - it is what the TranslucentImageSource component do. The result of this is we get much higher performance, but every TranslucentImage share that same source will have the exact same background - which mean they will not "see" others below them.

If you really need to blur UIs, this can be done by setting up another camera and canvas. The new canvas will contain the UI that you want to blur. You can then set the new camera to only see that canvas with clear flag of "Depth only" or "Don't clear", and the other camera to not see it. Add a TranslucentImageSource to the new camera, and use it as the source for the top level UI. The UIs that are in the new canvas should use the old camera as source. **In short: see the demo.**


Have another question?
----------------------

:ref:`Contact me <support>`.