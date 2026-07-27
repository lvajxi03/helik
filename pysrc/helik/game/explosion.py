#!/usr/bin/env python3

"""
Explosion handler module
"""


class Explosion:
    """
    Explosion handler class
    """
    def __init__(self, images: list, x, y):
        self.images = images
        self.x = x
        self.y = y
        self.current = 0
        self.rects = []
        for image in self.images:
            r = image.get_rect()
            r.center = (x, y)
            self.rects.append(r)
        self.max_frames = len(self.images)
        self.valid = True

    def on_update(self, _):
        """
        Update handler event
        """
        self.current += 1
        if self.current >= self.max_frames:
            self.valid = False

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to paint the explosion
        """
        canvas.blit(self.images[self.current], self.rects[self.current])
