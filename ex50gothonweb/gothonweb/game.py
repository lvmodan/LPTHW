#!/usr/bin/env python
# coding=utf-8
from map import Room

central_corridor = Room('Central Corridor', ''' 
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.
You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the
Armory and about to pull a weapon to blast you.''')

generic_death = Room('death', 'You died, next life to survive')

central_corridor.add_paths({'shoot': generic_death,
                            'dodge': generic_death,
                            'tell a joke': generic_death})

START = central_corridor
