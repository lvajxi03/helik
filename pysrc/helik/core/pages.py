#!/usr/bin/env python3

"""
Pages module
"""

import webbrowser
import pygame


class Button:
    """
    Button
    A surface with an action, executed with web browser
    """
    def __init__(self, surface, location, action, palette):
        """
        Button constructor
        :param surface: button label/image
        :param location: button location (x and y tuple)
        :param action: button action to execute (str)
        :param palette: color palette
        """
        self.surface = surface
        self.location = location
        self.frame_color = palette["yellow-default"]
        x, y = self.location
        self.action = action
        self.r = pygame.Rect(x, y, self.surface.get_width(), self.surface.get_height())
        self.r2 = pygame.Rect(self.r.x - 10, self.r.y - 10, self.r.w + 20, self.r.h + 20)

    def contains(self, x, y):
        """
        Check if button's rectangle contains given point
        :param x: x coordinate of a point
        :param y: y coordinate of a point
        :return: True if button's rectangle contains given point, False otherwise
        """
        return self.r.collidepoint(x, y)

    def paint(self, canvas):
        """
        Paint button
        :param canvas: target canvas
        """
        x, y = pygame.mouse.get_pos()
        if self.contains(x, y):
            pygame.draw.rect(canvas, self.frame_color,
                             self.r2, width=5, border_radius=20)
        canvas.blit(self.surface, self.location)

    def execute(self):
        """
        Execute an action
        """
        if self.action:
            webbrowser.open(self.action)


class Page:
    """
    Page - mix of static images and labels
    """
    def __init__(self, data, resman, lang):
        """
        Page constructor
        :param data: initial JSON data
        :param resman: resouce manager handler
        """
        self.data = {}
        self.data = {"images": [], "labels": [], "buttons": []}
        for elem in data["images"]:
            if "action" in elem:
                b = Button(resman.images[elem["image"]],
                           elem["location"],
                           elem["action"], resman.colors)
                self.data["buttons"].append(b)
            else:
                elem["image"] = resman.images[elem["image"]]
                self.data['images'].append(elem)
        for elem in data["labels"]:
            if "action" in elem:
                b = Button(resman.images[elem["image"]],
                           elem["location"],
                           elem["action"], resman.colors)
                self.data["buttons"].append(b)
            else:
                elem["label"] = resman.locale[lang]["pages"][elem["label"]]
                self.data["labels"].append(elem)

    def on_click(self):
        """
        Handle left mouse button click
        :return: True if button was clicked, False otherwise
        """
        x, y = pygame.mouse.get_pos()
        for button in self.data["buttons"]:
            if button.contains(x, y):
                button.execute()
                return True

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: buffer to paint page to
        """
        for img in self.data['images']:
            image = img["image"]
            x, y = img["location"]
            canvas.blit(image, (x, y))

        for img in self.data['labels']:
            label, _ = img["label"]
            x, y = img["location"]
            canvas.blit(label, (x, y))

        for b in self.data["buttons"]:
            b.paint(canvas)


class Pager:
    """
    Pager - set of Pages
    """
    def __init__(self, data, resman):
        """
        Pager constructor
        :param data:
        :param resman:-+
        """
        self.pages = {}
        self.lang = "pl"  # Ok,there has to be something default
        self.current = 0
        for lang in data:
            self.pages[lang] = []
            for elem in data[lang]:
                page = Page(elem, resman, lang)
                self.pages[lang].append(page)

    def activate(self):
        """
        Activate event handler
        """
        self.current = 0

    def change_lang(self, newlang):
        """
        Change current language
        """
        self.lang = newlang
        if self.current > len(self.pages[self.lang]) - 1:
            self.current = len(self.pages[self.lang]) - 1

    def prev(self):
        """
        Switch to previous page
        """
        if self.has_prev():
            self.current -= 1

    def next(self):
        """
        Switch to next page
        """
        if self.has_next():
            self.current += 1

    def has_next(self) -> bool:
        """
        Check if next page exists
        """
        if len(self.pages[self.lang]) > 0 and self.current < len(
                self.pages[self.lang]) - 1:
            return True
        return False

    def has_prev(self) -> bool:
        """
        Check if prev page exists
        """
        if len(self.pages[self.lang]) > 0 and self.current > 0:
            return True
        return False

    def on_paint(self, buffer):
        """
        Paint event handler
        :param buffer: a buffer to paint
        """
        if len(self.pages[self.lang]) > 0:
            self.pages[self.lang][self.current].on_paint(buffer)

    def on_click(self):
        """
        Handle left mouse button click
        :return: True if a button was clicked, False otherwise
        """
        if len(self.pages[self.lang]) > 0:
            return self.pages[self.lang][self.current].on_click()
        return False
