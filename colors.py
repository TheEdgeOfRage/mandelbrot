#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

import curses


def init_21_colors():
	curses.init_color(1, 0, 0, 0)
	curses.init_color(2, 1000, 0, 0)
	curses.init_color(3, 1000, 333, 0)
	curses.init_color(4, 1000, 666, 0)
	curses.init_color(5, 1000, 1000, 0)
	curses.init_color(6, 666, 1000, 0)
	curses.init_color(7, 333, 1000, 0)
	curses.init_color(8, 0, 1000, 0)
	curses.init_color(9, 0, 1000, 333)
	curses.init_color(10, 0, 1000, 666)
	curses.init_color(11, 0, 1000, 1000)
	curses.init_color(12, 0, 666, 1000)
	curses.init_color(13, 0, 333, 1000)
	curses.init_color(14, 0, 0, 1000)
	curses.init_color(15, 333, 0, 1000)
	curses.init_color(16, 666, 0, 1000)
	curses.init_color(17, 1000, 0, 1000)
	curses.init_color(18, 1000, 0, 666)
	curses.init_color(19, 1000, 0, 333)
	curses.init_color(20, 1000, 0, 0)
	curses.init_color(21, 800, 800, 800)
	curses.init_color(22, 50, 50, 50)
	curses.init_pair(1, 0, 1)
	curses.init_pair(2, 0, 2)
	curses.init_pair(3, 0, 3)
	curses.init_pair(4, 0, 4)
	curses.init_pair(5, 0, 5)
	curses.init_pair(6, 0, 6)
	curses.init_pair(7, 0, 7)
	curses.init_pair(8, 0, 8)
	curses.init_pair(9, 0, 9)
	curses.init_pair(10, 0, 10)
	curses.init_pair(11, 0, 11)
	curses.init_pair(12, 0, 12)
	curses.init_pair(13, 0, 13)
	curses.init_pair(14, 0, 14)
	curses.init_pair(15, 0, 15)
	curses.init_pair(16, 0, 16)
	curses.init_pair(17, 0, 17)
	curses.init_pair(18, 0, 18)
	curses.init_pair(19, 0, 19)
	curses.init_pair(20, 0, 20)
	curses.init_pair(21, 21, 22)
	return 21


def init_21_monochrome():
	curses.init_color(1, 0, 0, 0)
	curses.init_color(2, 50, 50, 50)
	curses.init_color(3, 100, 100, 100)
	curses.init_color(4, 150, 150, 150)
	curses.init_color(5, 200, 200, 200)
	curses.init_color(6, 250, 250, 250)
	curses.init_color(7, 300, 300, 300)
	curses.init_color(8, 350, 350, 350)
	curses.init_color(9, 400, 400, 400)
	curses.init_color(10, 450, 450, 450)
	curses.init_color(11, 500, 500, 500)
	curses.init_color(12, 550, 550, 550)
	curses.init_color(13, 600, 600, 600)
	curses.init_color(14, 650, 650, 650)
	curses.init_color(15, 700, 700, 700)
	curses.init_color(16, 750, 750, 750)
	curses.init_color(17, 800, 800, 800)
	curses.init_color(18, 850, 850, 850)
	curses.init_color(19, 900, 900, 900)
	curses.init_color(20, 950, 950, 950)
	curses.init_pair(1, 0, 1)
	curses.init_pair(2, 0, 2)
	curses.init_pair(3, 0, 3)
	curses.init_pair(4, 0, 4)
	curses.init_pair(5, 0, 5)
	curses.init_pair(6, 0, 6)
	curses.init_pair(7, 0, 7)
	curses.init_pair(8, 0, 8)
	curses.init_pair(9, 0, 9)
	curses.init_pair(10, 0, 10)
	curses.init_pair(11, 0, 11)
	curses.init_pair(12, 0, 12)
	curses.init_pair(13, 0, 13)
	curses.init_pair(14, 0, 14)
	curses.init_pair(15, 0, 15)
	curses.init_pair(16, 0, 16)
	curses.init_pair(17, 0, 17)
	curses.init_pair(18, 0, 18)
	curses.init_pair(19, 0, 19)
	curses.init_pair(20, 0, 20)
	curses.init_pair(21, 17, 2)
	return 21


def init_101_colors():
	curses.init_color(1, 0, 0, 0)
	curses.init_color(2, 800, 159, 159)
	curses.init_color(3, 800, 199, 159)
	curses.init_color(4, 800, 238, 159)
	curses.init_color(5, 800, 277, 159)
	curses.init_color(6, 800, 316, 159)
	curses.init_color(7, 800, 355, 159)
	curses.init_color(8, 800, 395, 159)
	curses.init_color(9, 800, 434, 159)
	curses.init_color(10, 800, 473, 159)
	curses.init_color(11, 800, 512, 159)
	curses.init_color(12, 800, 551, 159)
	curses.init_color(13, 800, 591, 159)
	curses.init_color(14, 800, 630, 159)
	curses.init_color(15, 800, 669, 159)
	curses.init_color(16, 800, 708, 159)
	curses.init_color(17, 800, 747, 159)
	curses.init_color(18, 800, 786, 159)
	curses.init_color(19, 773, 800, 159)
	curses.init_color(20, 734, 800, 159)
	curses.init_color(21, 695, 800, 159)
	curses.init_color(22, 656, 800, 159)
	curses.init_color(23, 617, 800, 159)
	curses.init_color(24, 577, 800, 159)
	curses.init_color(25, 538, 800, 159)
	curses.init_color(26, 499, 800, 159)
	curses.init_color(27, 460, 800, 159)
	curses.init_color(28, 421, 800, 159)
	curses.init_color(29, 382, 800, 159)
	curses.init_color(30, 342, 800, 159)
	curses.init_color(31, 303, 800, 159)
	curses.init_color(32, 264, 800, 159)
	curses.init_color(33, 225, 800, 159)
	curses.init_color(34, 186, 800, 159)
	curses.init_color(35, 159, 800, 173)
	curses.init_color(36, 159, 800, 212)
	curses.init_color(37, 159, 800, 251)
	curses.init_color(38, 159, 800, 290)
	curses.init_color(39, 159, 800, 329)
	curses.init_color(40, 159, 800, 368)
	curses.init_color(41, 159, 800, 408)
	curses.init_color(42, 159, 800, 447)
	curses.init_color(43, 159, 800, 486)
	curses.init_color(44, 159, 800, 525)
	curses.init_color(45, 159, 800, 564)
	curses.init_color(46, 159, 800, 604)
	curses.init_color(47, 159, 800, 643)
	curses.init_color(48, 159, 800, 682)
	curses.init_color(49, 159, 800, 721)
	curses.init_color(50, 159, 800, 760)
	curses.init_color(51, 159, 800, 799)
	curses.init_color(52, 159, 760, 800)
	curses.init_color(53, 159, 721, 800)
	curses.init_color(54, 159, 682, 800)
	curses.init_color(55, 159, 643, 800)
	curses.init_color(56, 159, 604, 800)
	curses.init_color(57, 159, 564, 800)
	curses.init_color(58, 159, 525, 800)
	curses.init_color(59, 159, 486, 800)
	curses.init_color(60, 159, 447, 800)
	curses.init_color(61, 159, 408, 800)
	curses.init_color(62, 159, 368, 800)
	curses.init_color(63, 159, 329, 800)
	curses.init_color(64, 159, 290, 800)
	curses.init_color(65, 159, 251, 800)
	curses.init_color(66, 159, 212, 800)
	curses.init_color(67, 159, 173, 800)
	curses.init_color(68, 186, 159, 800)
	curses.init_color(69, 225, 159, 800)
	curses.init_color(70, 264, 159, 800)
	curses.init_color(71, 303, 159, 800)
	curses.init_color(72, 342, 159, 800)
	curses.init_color(73, 382, 159, 800)
	curses.init_color(74, 421, 159, 800)
	curses.init_color(75, 460, 159, 800)
	curses.init_color(76, 499, 159, 800)
	curses.init_color(77, 538, 159, 800)
	curses.init_color(78, 577, 159, 800)
	curses.init_color(79, 617, 159, 800)
	curses.init_color(80, 656, 159, 800)
	curses.init_color(81, 695, 159, 800)
	curses.init_color(82, 734, 159, 800)
	curses.init_color(83, 773, 159, 800)
	curses.init_color(84, 800, 159, 786)
	curses.init_color(85, 800, 159, 747)
	curses.init_color(86, 800, 159, 708)
	curses.init_color(87, 800, 159, 669)
	curses.init_color(88, 800, 159, 630)
	curses.init_color(89, 800, 159, 591)
	curses.init_color(90, 800, 159, 551)
	curses.init_color(91, 800, 159, 512)
	curses.init_color(92, 800, 159, 473)
	curses.init_color(93, 800, 159, 434)
	curses.init_color(94, 800, 159, 395)
	curses.init_color(95, 800, 159, 355)
	curses.init_color(96, 800, 159, 316)
	curses.init_color(97, 800, 159, 277)
	curses.init_color(98, 800, 159, 238)
	curses.init_color(99, 800, 159, 199)
	curses.init_color(100, 800, 159, 159)
	curses.init_color(101, 800, 800, 800)
	curses.init_color(102, 50, 50, 50)
	curses.init_pair(1, 0, 1)
	curses.init_pair(2, 0, 2)
	curses.init_pair(3, 0, 3)
	curses.init_pair(4, 0, 4)
	curses.init_pair(5, 0, 5)
	curses.init_pair(6, 0, 6)
	curses.init_pair(7, 0, 7)
	curses.init_pair(8, 0, 8)
	curses.init_pair(9, 0, 9)
	curses.init_pair(10, 0, 10)
	curses.init_pair(11, 0, 11)
	curses.init_pair(12, 0, 12)
	curses.init_pair(13, 0, 13)
	curses.init_pair(14, 0, 14)
	curses.init_pair(15, 0, 15)
	curses.init_pair(16, 0, 16)
	curses.init_pair(17, 0, 17)
	curses.init_pair(18, 0, 18)
	curses.init_pair(19, 0, 19)
	curses.init_pair(20, 0, 20)
	curses.init_pair(21, 0, 21)
	curses.init_pair(22, 0, 22)
	curses.init_pair(23, 0, 23)
	curses.init_pair(24, 0, 24)
	curses.init_pair(25, 0, 25)
	curses.init_pair(26, 0, 26)
	curses.init_pair(27, 0, 27)
	curses.init_pair(28, 0, 28)
	curses.init_pair(29, 0, 29)
	curses.init_pair(30, 0, 30)
	curses.init_pair(31, 0, 31)
	curses.init_pair(32, 0, 32)
	curses.init_pair(33, 0, 33)
	curses.init_pair(34, 0, 34)
	curses.init_pair(35, 0, 35)
	curses.init_pair(36, 0, 36)
	curses.init_pair(37, 0, 37)
	curses.init_pair(38, 0, 38)
	curses.init_pair(39, 0, 39)
	curses.init_pair(40, 0, 40)
	curses.init_pair(41, 0, 41)
	curses.init_pair(42, 0, 42)
	curses.init_pair(43, 0, 43)
	curses.init_pair(44, 0, 44)
	curses.init_pair(45, 0, 45)
	curses.init_pair(46, 0, 46)
	curses.init_pair(47, 0, 47)
	curses.init_pair(48, 0, 48)
	curses.init_pair(49, 0, 49)
	curses.init_pair(50, 0, 50)
	curses.init_pair(51, 0, 51)
	curses.init_pair(52, 0, 52)
	curses.init_pair(53, 0, 53)
	curses.init_pair(54, 0, 54)
	curses.init_pair(55, 0, 55)
	curses.init_pair(56, 0, 56)
	curses.init_pair(57, 0, 57)
	curses.init_pair(58, 0, 58)
	curses.init_pair(59, 0, 59)
	curses.init_pair(60, 0, 60)
	curses.init_pair(61, 0, 61)
	curses.init_pair(62, 0, 62)
	curses.init_pair(63, 0, 63)
	curses.init_pair(64, 0, 64)
	curses.init_pair(65, 0, 65)
	curses.init_pair(66, 0, 66)
	curses.init_pair(67, 0, 67)
	curses.init_pair(68, 0, 68)
	curses.init_pair(69, 0, 69)
	curses.init_pair(70, 0, 70)
	curses.init_pair(71, 0, 71)
	curses.init_pair(72, 0, 72)
	curses.init_pair(73, 0, 73)
	curses.init_pair(74, 0, 74)
	curses.init_pair(75, 0, 75)
	curses.init_pair(76, 0, 76)
	curses.init_pair(77, 0, 77)
	curses.init_pair(78, 0, 78)
	curses.init_pair(79, 0, 79)
	curses.init_pair(80, 0, 80)
	curses.init_pair(81, 0, 81)
	curses.init_pair(82, 0, 82)
	curses.init_pair(83, 0, 83)
	curses.init_pair(84, 0, 84)
	curses.init_pair(85, 0, 85)
	curses.init_pair(86, 0, 86)
	curses.init_pair(87, 0, 87)
	curses.init_pair(88, 0, 88)
	curses.init_pair(89, 0, 89)
	curses.init_pair(90, 0, 90)
	curses.init_pair(91, 0, 91)
	curses.init_pair(92, 0, 92)
	curses.init_pair(93, 0, 93)
	curses.init_pair(94, 0, 94)
	curses.init_pair(95, 0, 95)
	curses.init_pair(96, 0, 96)
	curses.init_pair(97, 0, 97)
	curses.init_pair(98, 0, 98)
	curses.init_pair(99, 0, 99)
	curses.init_pair(100, 0, 100)
	curses.init_pair(101, 101, 102)
	return 101


def init_101_monochrome():
	curses.init_color(1, 0, 0, 0)
	curses.init_color(2, 10, 10, 10)
	curses.init_color(3, 20, 20, 20)
	curses.init_color(4, 30, 30, 30)
	curses.init_color(5, 40, 40, 40)
	curses.init_color(6, 50, 50, 50)
	curses.init_color(7, 60, 60, 60)
	curses.init_color(8, 70, 70, 70)
	curses.init_color(9, 80, 80, 80)
	curses.init_color(10, 90, 90, 90)
	curses.init_color(11, 100, 100, 100)
	curses.init_color(12, 110, 110, 110)
	curses.init_color(13, 120, 120, 120)
	curses.init_color(14, 130, 130, 130)
	curses.init_color(15, 140, 140, 140)
	curses.init_color(16, 150, 150, 150)
	curses.init_color(17, 160, 160, 160)
	curses.init_color(18, 170, 170, 170)
	curses.init_color(19, 180, 180, 180)
	curses.init_color(20, 190, 190, 190)
	curses.init_color(21, 200, 200, 200)
	curses.init_color(22, 210, 210, 210)
	curses.init_color(23, 220, 220, 220)
	curses.init_color(24, 230, 230, 230)
	curses.init_color(25, 240, 240, 240)
	curses.init_color(26, 250, 250, 250)
	curses.init_color(27, 260, 260, 260)
	curses.init_color(28, 270, 270, 270)
	curses.init_color(29, 280, 280, 280)
	curses.init_color(30, 290, 290, 290)
	curses.init_color(31, 300, 300, 300)
	curses.init_color(32, 310, 310, 310)
	curses.init_color(33, 320, 320, 320)
	curses.init_color(34, 330, 330, 330)
	curses.init_color(35, 340, 340, 340)
	curses.init_color(36, 350, 350, 350)
	curses.init_color(37, 360, 360, 360)
	curses.init_color(38, 370, 370, 370)
	curses.init_color(39, 380, 380, 380)
	curses.init_color(40, 390, 390, 390)
	curses.init_color(41, 400, 400, 400)
	curses.init_color(42, 410, 410, 410)
	curses.init_color(43, 420, 420, 420)
	curses.init_color(44, 430, 430, 430)
	curses.init_color(45, 440, 440, 440)
	curses.init_color(46, 450, 450, 450)
	curses.init_color(47, 460, 460, 460)
	curses.init_color(48, 470, 470, 470)
	curses.init_color(49, 480, 480, 480)
	curses.init_color(50, 490, 490, 490)
	curses.init_color(51, 500, 500, 500)
	curses.init_color(52, 510, 510, 510)
	curses.init_color(53, 520, 520, 520)
	curses.init_color(54, 530, 530, 530)
	curses.init_color(55, 540, 540, 540)
	curses.init_color(56, 550, 550, 550)
	curses.init_color(57, 560, 560, 560)
	curses.init_color(58, 570, 570, 570)
	curses.init_color(59, 580, 580, 580)
	curses.init_color(60, 590, 590, 590)
	curses.init_color(61, 600, 600, 600)
	curses.init_color(62, 610, 610, 610)
	curses.init_color(63, 620, 620, 620)
	curses.init_color(64, 630, 630, 630)
	curses.init_color(65, 640, 640, 640)
	curses.init_color(66, 650, 650, 650)
	curses.init_color(67, 660, 660, 660)
	curses.init_color(68, 670, 670, 670)
	curses.init_color(69, 680, 680, 680)
	curses.init_color(70, 690, 690, 690)
	curses.init_color(71, 700, 700, 700)
	curses.init_color(72, 710, 710, 710)
	curses.init_color(73, 720, 720, 720)
	curses.init_color(74, 730, 730, 730)
	curses.init_color(75, 740, 740, 740)
	curses.init_color(76, 750, 750, 750)
	curses.init_color(77, 760, 760, 760)
	curses.init_color(78, 770, 770, 770)
	curses.init_color(79, 780, 780, 780)
	curses.init_color(80, 790, 790, 790)
	curses.init_color(81, 800, 800, 800)
	curses.init_color(82, 810, 810, 810)
	curses.init_color(83, 820, 820, 820)
	curses.init_color(84, 830, 830, 830)
	curses.init_color(85, 840, 840, 840)
	curses.init_color(86, 850, 850, 850)
	curses.init_color(87, 860, 860, 860)
	curses.init_color(88, 870, 870, 870)
	curses.init_color(89, 880, 880, 880)
	curses.init_color(90, 890, 890, 890)
	curses.init_color(91, 900, 900, 900)
	curses.init_color(92, 910, 910, 910)
	curses.init_color(93, 920, 920, 920)
	curses.init_color(94, 930, 930, 930)
	curses.init_color(95, 940, 940, 940)
	curses.init_color(96, 950, 950, 950)
	curses.init_color(97, 960, 960, 960)
	curses.init_color(98, 970, 970, 970)
	curses.init_color(99, 980, 980, 980)
	curses.init_color(100, 990, 990, 990)
	curses.init_pair(1, 0, 1)
	curses.init_pair(2, 0, 2)
	curses.init_pair(3, 0, 3)
	curses.init_pair(4, 0, 4)
	curses.init_pair(5, 0, 5)
	curses.init_pair(6, 0, 6)
	curses.init_pair(7, 0, 7)
	curses.init_pair(8, 0, 8)
	curses.init_pair(9, 0, 9)
	curses.init_pair(10, 0, 10)
	curses.init_pair(11, 0, 11)
	curses.init_pair(12, 0, 12)
	curses.init_pair(13, 0, 13)
	curses.init_pair(14, 0, 14)
	curses.init_pair(15, 0, 15)
	curses.init_pair(16, 0, 16)
	curses.init_pair(17, 0, 17)
	curses.init_pair(18, 0, 18)
	curses.init_pair(19, 0, 19)
	curses.init_pair(20, 0, 20)
	curses.init_pair(21, 0, 21)
	curses.init_pair(22, 0, 22)
	curses.init_pair(23, 0, 23)
	curses.init_pair(24, 0, 24)
	curses.init_pair(25, 0, 25)
	curses.init_pair(26, 0, 26)
	curses.init_pair(27, 0, 27)
	curses.init_pair(28, 0, 28)
	curses.init_pair(29, 0, 29)
	curses.init_pair(30, 0, 30)
	curses.init_pair(31, 0, 31)
	curses.init_pair(32, 0, 32)
	curses.init_pair(33, 0, 33)
	curses.init_pair(34, 0, 34)
	curses.init_pair(35, 0, 35)
	curses.init_pair(36, 0, 36)
	curses.init_pair(37, 0, 37)
	curses.init_pair(38, 0, 38)
	curses.init_pair(39, 0, 39)
	curses.init_pair(40, 0, 40)
	curses.init_pair(41, 0, 41)
	curses.init_pair(42, 0, 42)
	curses.init_pair(43, 0, 43)
	curses.init_pair(44, 0, 44)
	curses.init_pair(45, 0, 45)
	curses.init_pair(46, 0, 46)
	curses.init_pair(47, 0, 47)
	curses.init_pair(48, 0, 48)
	curses.init_pair(49, 0, 49)
	curses.init_pair(50, 0, 50)
	curses.init_pair(51, 0, 51)
	curses.init_pair(52, 0, 52)
	curses.init_pair(53, 0, 53)
	curses.init_pair(54, 0, 54)
	curses.init_pair(55, 0, 55)
	curses.init_pair(56, 0, 56)
	curses.init_pair(57, 0, 57)
	curses.init_pair(58, 0, 58)
	curses.init_pair(59, 0, 59)
	curses.init_pair(60, 0, 60)
	curses.init_pair(61, 0, 61)
	curses.init_pair(62, 0, 62)
	curses.init_pair(63, 0, 63)
	curses.init_pair(64, 0, 64)
	curses.init_pair(65, 0, 65)
	curses.init_pair(66, 0, 66)
	curses.init_pair(67, 0, 67)
	curses.init_pair(68, 0, 68)
	curses.init_pair(69, 0, 69)
	curses.init_pair(70, 0, 70)
	curses.init_pair(71, 0, 71)
	curses.init_pair(72, 0, 72)
	curses.init_pair(73, 0, 73)
	curses.init_pair(74, 0, 74)
	curses.init_pair(75, 0, 75)
	curses.init_pair(76, 0, 76)
	curses.init_pair(77, 0, 77)
	curses.init_pair(78, 0, 78)
	curses.init_pair(79, 0, 79)
	curses.init_pair(80, 0, 80)
	curses.init_pair(81, 0, 81)
	curses.init_pair(82, 0, 82)
	curses.init_pair(83, 0, 83)
	curses.init_pair(84, 0, 84)
	curses.init_pair(85, 0, 85)
	curses.init_pair(86, 0, 86)
	curses.init_pair(87, 0, 87)
	curses.init_pair(88, 0, 88)
	curses.init_pair(89, 0, 89)
	curses.init_pair(90, 0, 90)
	curses.init_pair(91, 0, 91)
	curses.init_pair(92, 0, 92)
	curses.init_pair(93, 0, 93)
	curses.init_pair(94, 0, 94)
	curses.init_pair(95, 0, 95)
	curses.init_pair(96, 0, 96)
	curses.init_pair(97, 0, 97)
	curses.init_pair(98, 0, 98)
	curses.init_pair(99, 0, 99)
	curses.init_pair(100, 0, 100)
	curses.init_pair(101, 81, 2)
	return 101
