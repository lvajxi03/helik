#!/usr/bin/env python3

"""
NewScore board module
"""
import pygame
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, ALL_CHARS, STATUS_HEIGHT
from helik.htypes import BoardType, TimerType


all_chrows = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz.-_012', '3456789⌫']


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
        self.margin_x = 0
        self.margin_y = 0
        self.recalculate_rectangles()
        self.counter = 0

    def activate(self):
        """
        Activate event handler
        """
        self.nick = self.arena.config["lastnick"]
        pygame.time.set_timer(TimerType.SECOND, 500)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.SECOND, 0)

    def recalculate_rectangles(self):
        # l, r = self.resman.labels[self.arena.config['lang']]["control"]["keyboard"]
        # self.margin_x = (ARENA_WIDTH - r.w) // 2
        # self.margin_y = ARENA_HEIGHT // 4 - 150
        # self.r1 = pygame.Rect(self.margin_x - 15 + self.x * 52, self.margin_y - 15 + self.y * 52, 55, 65)
        # self.r2 = pygame.Rect(self.margin_x - 20 + self.x * 52, self.margin_y - 10 + self.y * 52, 55, 65)
        # self.r3 = pygame.Rect(self.margin_x - 20, self.margin_y - 12 + 5 * 52, 8*52 + 20, 65)
        # self.r3a = pygame.Rect(self.margin_x - 15, self.margin_y - 7 + 5 * 52, 8 * 52 + 20, 65)
        #
        # self.r4 = pygame.Rect(self.margin_x - 20, self.margin_y - 12 + 6 * 52, 8 * 52 + 20, 65)
        # self.r4a = pygame.Rect(self.margin_x - 15, self.margin_y - 7 + 6 * 52, 8 * 52 + 20, 65)
        pass

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.SECOND:
            self.counter += 1
            self.counter %= 2

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.resman.images["flag-pl"], self.resman.rectangles["lang-rectangles"]["pl"])
        self.buffer.blit(self.resman.images["flag-en"], self.resman.rectangles["lang-rectangles"]["en"])

        la, re = self.resman.locale[self.arena.config["lang"]]["common"]["newscore-status"]
        self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

        la, re = self.resman.locale[self.arena.config["lang"]]["newscore"]["congrats-shadow"]
        re.x = (ARENA_WIDTH - re.w) // 2 + 5
        re.y = 25
        self.buffer.blit(la, re)

        la, re = self.resman.locale[self.arena.config["lang"]]["newscore"]["congrats"]
        re.x = (ARENA_WIDTH - re.w) // 2

        re.y = 20
        self.buffer.blit(la, re)

        la, re = self.resman.locale[self.arena.config["lang"]]["newscore"]["congrats-2"]
        re.x = (ARENA_WIDTH - re.w) // 2
        re.y = 170
        self.buffer.blit(la, re)

        i = 0
        for l in self.nick:
            self.buffer.blit(self.resman.letters[l], (ARENA_WIDTH // 2 + i * 34, 261))
            i += 1

        if self.counter == 0:
            self.buffer.blit(self.resman.images['cursor'],
                             (ARENA_WIDTH // 2 + i * 34,
                              266))

        l, r = self.resman.locale[self.arena.config["lang"]]["newscore"]["enter-nickname"]
        r.x = ARENA_WIDTH // 2 - r.w - 10
        r.y = 260
        self.buffer.blit(l, r)

        dx = (ARENA_WIDTH - 320) // 2
        for i in range(5):
            for j in range(8):
                self.buffer.blit(self.resman.letters[all_chrows[i][j]], (dx + j * 40, 330 + i * 55))

        la, re = self.resman.locale[self.arena.config["lang"]]["newscore"]["space"]
        re.y = 610
        re.x = (ARENA_WIDTH - re.w) // 2
        self.buffer.blit(la, re)

        la, re = self.resman.locale[self.arena.config["lang"]]["newscore"]["done"]
        re.y = 680
        re.x = (ARENA_WIDTH - re.w) // 2
        self.buffer.blit(la, re)

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
        if name in ALL_CHARS:
            if len(self.nick) < 8:
                self.nick += name
        elif key == pygame.K_ESCAPE:
            if self.nick == '':
                self.nick = 'no name'
            self.arena.config.append_hiscore(self.nick, self.arena.boards[BoardType.GAME].data['points'])
            self.arena.config["lastnick"] = self.nick
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
        elif key == pygame.K_DELETE:
            self.nick = self.nick[:-1]
        elif key == pygame.K_BACKSPACE:
            self.nick = self.nick[:-1]
        elif key == pygame.K_RETURN:
            if self.y == 5:
                self.nick += ' '
            elif self.y == 6:
                if self.nick == '':
                    self.nick = 'no name'
                self.arena.config.append_hiscore(self.nick, self.arena.boards[BoardType.GAME].data['points'])
                self.arena.config["lastnick"] = self.nick
                self.arena.change_board(BoardType.MENU)
            elif self.y < 5:
                letter = all_chrows[self.y][self.x]
                if letter == ';':
                    # remove last char
                    self.nick = self.nick[:-1]
                else:
                    if len(self.nick) < 8:
                        self.nick += letter
        self.recalculate_rectangles()

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        if button == 1:
            rects = self.resman.rectangles["lang-rectangles"]
            for lang in rects:
                if rects[lang].collidepoint(pos):
                    self.arena.config['lang'] = lang
                    self.audio.play_sound("arrow")
        elif button == 4:
            self.on_keyup(pygame.K_UP)
        elif button == 5:
            self.on_keyup(pygame.K_DOWN)
        elif button == 2 or button == 3:
            self.arena.change_board(BoardType.MENU)
