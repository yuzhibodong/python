# Copyright (C) 2012, 2013, 2014, 2015 Julian Marchant <onpon4@riseup.net>
# 
# This file is part of the Pygame SGE.
# 
# The Pygame SGE is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# The Pygame SGE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with the Pygame SGE.  If not, see <http://www.gnu.org/licenses/>.

"""
This module provides functions related to joystick input.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pygame
import six

import sge
from sge import r


__all__ = ["refresh", "get_axis", "get_hat_x", "get_hat_y",
           "get_button_pressed", "get_joysticks", "get_name", "get_id",
           "get_axes", "get_hats", "get_trackballs", "get_buttons"]


def refresh():
    """
    Refresh the SGE's knowledge of joysticks.

    Call this method to allow the SGE to use joysticks that were plugged
    in while the game was running.
    """
    r.game_joysticks = []
    r.game_js_names = {}
    r.game_js_ids = {}
    pygame.joystick.quit()
    pygame.joystick.init()

    if pygame.joystick.get_init():
        for i in six.moves.range(pygame.joystick.get_count()):
            joy = pygame.joystick.Joystick(i)
            joy.init()
            n = joy.get_name()
            r.game_joysticks.append(joy)
            r.game_js_names[i] = n
            if n not in r.game_js_ids:
                r.game_js_ids[n] = i


def get_axis(joystick, axis):
    """
    Return the position of a joystick axis as a float from ``-1`` to
    ``1``, where ``0`` is centered, ``-1`` is all the way to the left or
    up, and ``1`` is all the way to the right or down.  Return ``0`` if
    the requested joystick or axis does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    - ``axis`` -- The number of the axis to check, where ``0`` is the
      first axis of the joystick.
    """
    joystick = get_id(joystick)

    if (joystick is not None and joystick < len(r.game_joysticks) and
            axis < r.game_joysticks[joystick].get_numaxes()):
        return max(-1.0, min(r.game_joysticks[joystick].get_axis(axis), 1.0))
    else:
        return 0


def get_hat_x(joystick, hat):
    """
    Return the horizontal position of a joystick hat (d-pad).  Can be
    ``-1`` (left), ``0`` (centered), or ``1`` (right).  Return ``0`` if
    the requested joystick or hat does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    - ``hat`` -- The number of the hat to check, where ``0`` is the
      first hat of the joystick.
    """
    return r._get_hat(get_id(joystick), hat)[0]


def get_hat_y(joystick, hat):
    """
    Return the vertical position of a joystick hat (d-pad).  Can be
    ``-1`` (up), ``0`` (centered), or ``1`` (down).  Return ``0`` if the
    requested joystick or hat does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    - ``hat`` -- The number of the hat to check, where ``0`` is the
      first hat of the joystick.
    """
    return -r._get_hat(get_id(joystick), hat)[1]


def get_pressed(joystick, button):
    """
    Return whether or not a joystick button is pressed, or
    :const:`False` if the requested joystick or button does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    - ``button`` -- The number of the button to check, where ``0`` is
      the first button of the joystick.
    """
    joystick = get_id(joystick)

    if (joystick is not None and joystick < len(r.game_joysticks) and
            button < r.game_joysticks[joystick].get_numbuttons()):
        return r.game_joysticks[joystick].get_button(button)
    else:
        return False


def get_joysticks():
    """Return the number of joysticks available."""
    return len(r.game_joysticks)


def get_name(joystick):
    """
    Return the name of a joystick, or :const:`None` if the requested
    joystick does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    """
    if isinstance(joystick, six.integer_types):
        return r.game_js_names.setdefault(joystick)
    elif joystick in r.game_js_names.values():
        return joystick
    else:
        return None


def get_id(joystick):
    """
    Return the number of a joystick, where ``0`` is the first joystick,
    or :const:`None` if the requested joystick does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    """
    if not isinstance(joystick, six.integer_types):
        return r.game_js_ids.setdefault(joystick)
    elif joystick in r.game_js_names:
        return joystick
    else:
        return None


def get_axes(joystick):
    """
    Return the number of axes available on a joystick, or ``0`` if the
    requested joystick does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    """
    joystick = get_id(joystick)

    if joystick is not None and joystick < len(r.game_joysticks):
        return r.game_joysticks[joystick].get_numaxes()
    else:
        return 0


def get_hats(joystick):
    """
    Return the number of hats (d-pads) available on a joystick, or ``0``
    if the requested joystick does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    """
    joystick = get_id(joystick)

    if joystick is not None and joystick < len(r.game_joysticks):
        return r.game_joysticks[joystick].get_numhats()
    else:
        return 0


def get_trackballs(joystick):
    """
    Return the number of trackballs available on a joystick, or ``0`` if
    the requested joystick does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    """
    joystick = get_id(joystick)

    if joystick is not None and joystick < len(r.game_joysticks):
        return r.game_joysticks[joystick].get_numballs()
    else:
        return 0


def get_buttons(joystick):
    """
    Return the number of buttons available on a joystick, or ``0`` if
    the requested joystick does not exist.

    Arguments:

    - ``joystick`` -- The number of the joystick to check, where ``0``
      is the first joystick, or the name of the joystick to check.
    """
    joystick = get_id(joystick)

    if joystick is not None and joystick < len(r.game_joysticks):
        return r.game_joysticks[joystick].get_numbuttons()
    else:
        return 0
