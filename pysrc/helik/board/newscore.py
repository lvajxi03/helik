#!/usr/bin/env python3

"""
NewScore board module
"""
import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, ALL_CHARS
from helik.platform import TimerType
from helik.platform import ButtonType
from helik.datatypes import BoardType
from .standard import Board


all_chrows = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz.-_012', '3456789⌫']

HEADING_SHADOW_DX = 5
LETTER_BLOCK_DX = 40
LETTER_BLOCK_DY = 55
LETTER_BLOCK_W = 34
LETTER_BLOCK_H = 55

LINE_WIDTH = 320
LINE_DY = 330
LINE_DX = (ARENA_WIDTH - LINE_WIDTH) // 2

SPACE_Y_OFFSET = 605
DONE_Y_OFFSET = 660
SHADOW_DX = 20
BLOCK_DX = 15
STATUS_DX = 200
CONGRATS_DY = 25
CONGRATS_S_DY = 20
CONGRATS_2_DY = 170
NICK_DY = 261
ENTER_NICKNAME_DX = 10
ENTER_NICKNAME_DY = 260
CURSOR_DY = 261

SURR_W = 60
SURR_H = 75
BIG_BUTTON_W = 340
BUTTON_DX = 10
BUTTON_S_DX = 15

BORDER_RADIUS = 8
BORDER_WIDTH = 5


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
        self.rectangles = {}
        self.counter = 0
        self.recalculate_rectangles()

    def update_nick(self, last):
        """
        Update nick with given character
        :param last: character to add
        """
        if len(self.nick) < 8:
            self.nick += last

    def trim_nick(self):
        """
        Remove last character from nick
        """
        self.nick = self.nick[:-1]

    def activate(self, **kwargs):
        """
        Activate event handler
        :param kwargs: additional parameters, like help or previous board
        """
        self.arena.audio.enable_background_music("background-music")
        self.nick = self.arena.config["lastnick"]
        pygame.time.set_timer(TimerType.SECOND, 500)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.SECOND, 0)

    def recalculate_rectangles(self):
        """
        Recalculate internal rectangles that depend on locales
        (for instance, around the text labels)
        """
        self.rectangles = {}
        for i in range(5):
            for j in range(8):
                r = pygame.Rect(LINE_DX + j * LETTER_BLOCK_DX,
                                LINE_DY + i * LETTER_BLOCK_DY,
                                LETTER_BLOCK_W, LETTER_BLOCK_H)
                self.rectangles[all_chrows[i][j]] = r

        re = self.resman["newscore"]["space"].r
        re.y = SPACE_Y_OFFSET
        re.x = (ARENA_WIDTH - re.w) // 2
        self.rectangles[' '] = re

        re = self.resman["newscore"]["done"].r
        re.y = DONE_Y_OFFSET
        re.x = (ARENA_WIDTH - re.w) // 2
        self.rectangles[';'] = re

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
        self.paint_default_bg()

        la = self.resman["newscore-status"]
        la.paint_at(self.buffer, ARENA_WIDTH - la.w - STATUS_DX,
                    ARENA_HEIGHT - LETTER_BLOCK_H)

        la = self.resman["newscore"]["congrats-shadow"]
        la.x = (ARENA_WIDTH - la.w) // 2 + HEADING_SHADOW_DX
        la.y = CONGRATS_DY
        la.paint(self.buffer)

        la = self.resman["newscore"]["congrats"]
        la.x = (ARENA_WIDTH - la.w) // 2
        la.y = CONGRATS_S_DY
        la.paint(self.buffer)

        la = self.resman["newscore"]["congrats-2"]
        la.x = (ARENA_WIDTH - la.w) // 2
        la.y = CONGRATS_2_DY
        la.paint(self.buffer)

        counter = 0
        for counter, letter in enumerate(self.nick):
            self.buffer.blit(
                self.resman.letters[letter],
                (ARENA_WIDTH // 2 + counter * LETTER_BLOCK_W, NICK_DY))

        if self.counter == 0:
            if len(self.nick) == 0:
                self.buffer.blit(self.resman.images['cursor'],
                                 (ARENA_WIDTH // 2 + counter * LETTER_BLOCK_W,
                                  CURSOR_DY))
            else:
                self.buffer.blit(self.resman.images['cursor'],
                                 (ARENA_WIDTH // 2 + (counter + 1) * LETTER_BLOCK_W,
                                  CURSOR_DY))

        la = self.resman["newscore"]["enter-nickname"]
        la.x = ARENA_WIDTH // 2 - la.w - ENTER_NICKNAME_DX
        la.y = ENTER_NICKNAME_DY
        la.paint(self.buffer)

        for i in range(5):
            for j in range(8):
                self.buffer.blit(
                    self.resman.letters[all_chrows[i][j]],
                    (LINE_DX + j * LETTER_BLOCK_DX,
                     LINE_DY + i * LETTER_BLOCK_DY))

        la = self.resman["newscore"]["space"]
        re = self.rectangles[' ']
        la.paint_at(self.buffer, re.x, re.y)

        la = self.resman["newscore"]["done"]
        re = self.rectangles[';']
        la.paint_at(self.buffer, re.x, re.y)

        if self.y < 5:
            r = pygame.Rect(LINE_DX + self.x * LETTER_BLOCK_DX - BUTTON_S_DX,
                            LINE_DY + self.y * LETTER_BLOCK_H - BLOCK_DX, SURR_W, SURR_H)
            pygame.draw.rect(self.buffer, self.resman.colors["shadow-default"],
                             r,
                             width=BORDER_WIDTH, border_radius=BORDER_RADIUS)
            r = pygame.Rect(LINE_DX + self.x * LETTER_BLOCK_DX - BLOCK_DX,
                            LINE_DY + self.y * LETTER_BLOCK_H - BUTTON_DX, SURR_W, SURR_H)
            pygame.draw.rect(self.buffer, self.resman.colors["yellow-default"],
                             r, width=BORDER_WIDTH, border_radius=BORDER_RADIUS)
        elif self.y == 5:
            r = pygame.Rect(LINE_DX - BUTTON_S_DX, LINE_DY + self.y * LETTER_BLOCK_H - SHADOW_DX,
                            BIG_BUTTON_W, SURR_H)
            pygame.draw.rect(self.buffer, self.resman.colors["shadow-default"],
                             r, width=BORDER_WIDTH, border_radius=BORDER_RADIUS)
            r = pygame.Rect(LINE_DX - BUTTON_DX, LINE_DY + self.y * LETTER_BLOCK_H - BLOCK_DX,
                            BIG_BUTTON_W, SURR_H)
            pygame.draw.rect(self.buffer, self.resman.colors["yellow-default"],
                             r, width=BORDER_WIDTH, border_radius=BORDER_RADIUS)
        elif self.y == 6:
            r = pygame.Rect(LINE_DX - BUTTON_S_DX, LINE_DY + self.y * LETTER_BLOCK_H - SHADOW_DX,
                            BIG_BUTTON_W, SURR_H)
            pygame.draw.rect(self.buffer, self.resman.colors["shadow-default"],
                             r, width=BORDER_WIDTH, border_radius=BORDER_RADIUS)
            r = pygame.Rect(LINE_DX - BUTTON_DX,
                            LINE_DY + self.y * LETTER_BLOCK_H - BLOCK_DX,
                            BIG_BUTTON_W, SURR_H)
            pygame.draw.rect(self.buffer, self.resman.colors["yellow-default"],
                             r, width=BORDER_WIDTH, border_radius=BORDER_RADIUS)

    def store_nick(self):
        """
        Store nick in configuration
        """
        self.nick = self.nick.strip()
        if self.nick == '':
            self.nick = 'no name'
        self.arena.config.append_hiscore(self.nick,
                                         self.arena.boards[BoardType.GAME].data['points'])
        self.arena.config["lastnick"] = self.nick

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        name = pygame.key.name(key)
        if name in ALL_CHARS or name == pygame.K_SPACE:
            self.update_nick(name)

        match key:
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_DOWN:
                if self.y < 6:
                    self.y += 1
            case pygame.K_UP:
                if self.y > 0:
                    self.y -= 1
            case pygame.K_LEFT:
                if self.x > 0:
                    self.x -= 1
            case pygame.K_RIGHT:
                if self.x < 7 and self.y < 5:
                    self.x += 1
            case pygame.K_DELETE:
                self.trim_nick()
            case pygame.K_BACKSPACE:
                self.trim_nick()
            case pygame.K_RETURN:
                if self.y == 5:
                    self.update_nick(' ')
                elif self.y == 6:
                    self.nick = self.nick.strip()
                    if self.nick == '':
                        self.nick = 'no name'
                    self.arena.config.append_hiscore(
                        self.nick,
                        self.arena.boards[BoardType.GAME].data['points'])
                    self.arena.config["lastnick"] = self.nick
                    self.arena.change_board(BoardType.HISCORES)
                elif self.y < 5:
                    letter = all_chrows[self.y][self.x]
                    if letter == '⌫':
                        self.trim_nick()
                    else:
                        self.update_nick(letter)
        self.recalculate_rectangles()

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        match button:
            case 1:
                ch_lang = False
                rects = self.resman.rectangles["lang-rectangles"]
                for lang in rects:
                    if rects[lang].collidepoint(pos):
                        ch_lang = True
                        self.arena.set_lang(lang)
                        self.audio.play_sfx("arrow")
                        self.recalculate_rectangles()
                if not ch_lang:
                    for pair in self.rectangles.items():
                        letter, rect = pair
                        if rect.collidepoint(pos):
                            if letter == ';':
                                self.store_nick()
                                self.on_keyup(pygame.K_ESCAPE)
                            elif letter == '⌫':
                                self.trim_nick()
                            else:
                                self.update_nick(letter)
            case 4:
                self.on_keyup(pygame.K_UP)
            case 5:
                self.on_keyup(pygame.K_DOWN)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        match button:
            case ButtonType.B:
                self.arena.toggle_lang()
            case ButtonType.A:
                self.on_keyup(pygame.K_ESCAPE)
