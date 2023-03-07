# zeldaGame
Throwback Zelda clone with Pygame. Move with arrow keys, pick items by walking over them, drop equipped weapon with spacebar.

> $ pip3 install -r requirements.txt

> $ python3 main.py

File main.py:

The main map gives the player access to the dungeon, where a maze or puzzle would lead to Gannon. 

The player hits obstacles like water, tree, temple, through the rect.colliderect() method. Only one of the 3 trees works though, probably because of the trees' spawning method (lines 174-188).

The player picks up items by walking over them. The sword and shield have no use at this point. The key lets the player open a chest that contains a wand, which throws orbs. The orbs' damage to ennemies is inconclusive at this point.

The player takes damage (a lot of it) upon contact with the ennemies. An attempt was made to add a clock so the damage isn't continuous. It doesn't work for now. This section is commented out, around lines 240-256.


In the heroes.py page, Link's transformation and the Midna character have been set aside.

In the items.py page, the gold and the bow have no use. The others have a rect attribute that allows them to be picked up.

The landscape is separated in two grid, one for the overworld and another for the dungeon, each is 20 x 10 tiles. Changing a tile will change the grid appearance. every texture id stored in grid.py lines 79-100.

All the sprites (almost everything that is not part of the grid) is in the sprites files. Link for example, has his own file. Every last bit of his animation is divided in pngs, we also have animation for the staff attacking, the shield blocking and the sword attacking.
