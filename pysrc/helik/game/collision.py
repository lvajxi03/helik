#!/usr/bin/env python3

"""
Collision handler module
"""


class Collision:
    """
    Collision handler class
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

    def on_update(self, delta):
        """
        Update handler event
        """
        self.current += 1
        self.current %= self.max_frames

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to paint the collision
        """
        canvas.blit(self.images[self.current], self.rects[self.current])
