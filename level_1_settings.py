import pygame
import sys

level_map = [
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                                                                           ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                                                              ',
    'DDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                                                    ',
    'DDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD             DDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                                          ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                        DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                      ',
    'DDDDDDDDXDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                              DDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                                               ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDD                                                                              XXXXXXXXXXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDD                                                                                        XXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXX   XDDDDDDXXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                                XXXXXXXXXXXXXXXX                                             XXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
    'DDDDDDDDDDDDDDDXXXDDDXXDDDDDXXXXXX      XXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                            XXXX                                                XXXXXXXDDDDDDDDDDDDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'DDDDDDDXXXXXXXX   XXX  XXXXX                                                                                                                                        XX                            XXXX                                                     XXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXX    ',
    'DDDDDXX                 XX                                                                                                                                                                       XXXX                                                          XXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ',
    'DDDDX                    X                                                                                                                                                 XX                    XXXX                                                          XXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXX ',
    'DDDDX                                                                                                                                                                               XX           XXXX                              XXX                             XXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXX     ',
    'DDDDX                                                                                                 2                       X                                                                  XXXXX                             XDX                           XXXXXXXXDDDDDDDDDDDXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXX ',
    'DDDDX                                                                                                                       XXXXXX                                                               XXXXX                   XXX       XDX                          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      ',
    'DDDDX                                                                                                                       XXXXXXXXXX                          2                                XXXXXX                   D        XDX   XX                                                                  XXXXXXXXXXXXXXXXXXXXXXXDDDXXXXXXXXXXXXXXXXXX                            ',
    'DDDDX                X                                     XXXXXXXXXXXXX                                     XXXXXXX        XXXXXXXXXXX                                                      XXXXXXXXXXXXX    XX                   XDX   XXXXX                                                              EXXXXXXXXXXXXXXXXXXXXXXXDDXXXXXXXXXXXXXXXXXXXX                                       ',
    'DDDXX               XDX                    XXXXX      XXXXXXXXXXXXXXXXXXXXXXX                                               XXXXX                                                            XXXXXXXXXXX                           XDX    XXXDXX                                                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                ',
    'DDDDX  P           XDDDX                   XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                   XXXXXXXX            XXX                 XXXXXX                    XXXXXXXXXXXXXXXX                 XX  XDX      XDX                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ',
    'DDDDXXXXXXXXXXXXXXXDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'DDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 30
w = 1000
h = 600