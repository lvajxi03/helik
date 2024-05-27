#!/usr/bin/env python3

"""
NewScore board module
"""
import pygame
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType


all_chars = 'qwertyuiopasdfghjklzxcvbnm,_ -0123456789'
all_chrows = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz.-_012', '3456789;']


class BoardNewScore(Board):
    """
    NewScore board class
    """
    def __init__(self, parent):
        """
        Create NewScore object
        :param parent: parent object handle
        """
        super().__init__(parent)
        self.nick = ""
        self.x = 0
        self.y = 0
        self.old_x = 0
        self.r1 = pygame.Rect(self.x - 30, self.y - 30, 50, 90)
        self.r2 = pygame.Rect(self.x - 25, self.y - 25, 50, 90)
        self.r3 = pygame.Rect(0, 0, 0, 0)
        self.r3a = pygame.Rect(0, 0, 0, 0)
        self.r4 = pygame.Rect(0, 0, 0, 0)
        self.r4a = pygame.Rect(0, 0, 0, 0)
        self.recalculate_rectangles()

    def activate(self):
        """
        Activate event handler
        """
        self.nick = ""

    def recalculate_rectangles(self):
        l, r = self.resman.labels[self.arena.config['lang']]["control"]["keyboard"]
        margin_x = (ARENA_WIDTH - r.w) // 2
        margin_y = ARENA_HEIGHT // 4
        self.r1 = pygame.Rect(margin_x - 15 + self.x * 52, margin_y - 15 + self.y * 52, 55, 65)
        self.r2 = pygame.Rect(margin_x - 20 + self.x * 52, margin_y - 10 + self.y * 52, 55, 65)
        self.r3 = pygame.Rect(margin_x - 20, margin_y - 12 + 5 * 52, 8*52 + 20, 65)
        self.r3a = pygame.Rect(margin_x - 15, margin_y - 7 + 5 * 52, 8 * 52 + 20, 65)

        self.r4 = pygame.Rect(margin_x - 20, margin_y - 12 + 6 * 52, 8 * 52 + 20, 65)
        self.r4a = pygame.Rect(margin_x - 15, margin_y - 7 + 6 * 52, 8 * 52 + 20, 65)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        l, r = self.resman.labels[self.arena.config['lang']]["control"]["keyboard"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = ARENA_HEIGHT // 4

        self.buffer.blit(l, r)

        if self.y < 5:
            pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                             self.r2, width=5, border_radius=20)
            pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                             self.r1, width=5, border_radius=20)
        elif self.y == 5:
            pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                             self.r3a, width=5, border_radius=20)
            pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                             self.r3, width=5, border_radius=20)
        elif self.y == 6:
            pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                             self.r4a, width=5, border_radius=20)
            pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                             self.r4, width=5, border_radius=20)

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        name = pygame.key.name(key)
        if name in all_chars:
            if len(self.nick) < 8:
                self.nick += name
        elif key == pygame.K_ESCAPE:
            self.arena.change_board(BoardType.MENU)
        elif key == pygame.K_DOWN:
            if self.y < 6:
                self.y += 1
                if self.y < 5:
                    self.old_x = self.x
                elif self.y == 5 or self.y == 6:
                    self.x = 0
        elif key == pygame.K_UP:
            if self.y > 0:
                self.y -= 1
                if self.y < 5:
                    self.x = self.old_x
        elif key == pygame.K_LEFT:
            if self.x > 0:
                self.x -= 1
        elif key == pygame.K_RIGHT:
            if self.x < 7 and self.y < 5:
                self.x += 1
        elif key == pygame.K_RETURN:
            if self.y == 5:
                self.nick += ' '
            elif self.y == 6:
                if self.nick == '':
                    self.nick = 'no name'
                self.arena.config.append_hiscore(self.nick, self.arena.boards[BoardType.GAME].data['points'])
                self.arena.change_board(BoardType.MENU)
            elif self.y < 5:
                letter = all_chrows[self.y][self.x]
                if letter == ';':
                    # remove last char
                    self.nick = self.nick[:-1]
                else:
                    self.nick += letter
        self.recalculate_rectangles()
