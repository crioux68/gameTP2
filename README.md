# zeldaGame
Throwback Zelda clone with Pygame. Move with arrow keys, pick items by walking over them, drop equipped weapon with spacebar.

> $ pip3 install -r requirements.txt

> $ python3 main.py



File main.py:

The main map gives the player access to the dungeon, where a maze or puzzle would lead to Gannon. 

The player hits obstacles like water, tree, temple, through the rect.colliderect() method. Only one of the 3 trees works though, probably because of the trees' spawning method (lines 237-248).

The player picks up items by walking over them. The sword and shield have no use at this point. The key lets the player open a chest that contains a wand, which throws orbs. The orbs damage ennemies inconsistently at this point.

The player takes damage (a lot of it) upon contact with the ennemies. An attempt was made to add a clock so the damage isn't continuous. It doesn't work for now. This section is commented out, around lines 310-326.


In the heroes.py page, Link's transformation and the Midna character have been set aside.

In the items.py page, the gold and the bow have no use. The others have a rect attribute that allows them to be picked up.

The landscape is separated in two grids, one for the overworld and another for the dungeon. Each is 20 x 10 tiles. Changing a tile will change the grid appearance. Every texture id is stored in grid.py, lines 110-134.

All the sprites (almost everything that is not part of the grid) are in the sprites files. Link, for example, has his own file. Every last bit of his animation is divided in pngs. There's also animation for the staff attacking, the shield blocking and the sword attacking.

Every sound effects are in the "Sounds" file and are used in the code to make the game more fun. The current sound effects/songs are :
-picking up an item
-dropping a weapon
-opening a chest
-using the wand
-player taking damage
-Menu song (plays in the menu)
-Overworld Song (plays in the overworld)
-Temple song (plays in the temple)

When the game starts, there is a menu with START and QUIT buttons : 
-If you press on the START button the game starts
-If you press on the QUIT button the game closes

When the game ends, there is a menu with the RESTART and QUIT buttons:
-If you press on the RESTART button the game comes back to the starting menu where you have the options to START and QUIT the game.
-If you press on the QUIT button the game closes

To travel around the windows of the game, you have to change the self.state in the function to change (see the state_manager() function, lines 800-809).

To add levels to the game, you only need to add another function like puzzle_room() on main Game (lines 553 and beyond).
In this function needed to be fixe is to put the function in another page so main game can be a smaller code that we could import our function.

Ganon stays in the temple.
Once Link spawns inside the temple, walking around is the only thing he can do at the moment. No collider were added in the temple. He can't get out.

A background image is missing at the end of the game (in the Game Over screen). 

when you come into contact with an item, you have to enter the answer to the riddle and then press the enter key to be able to get out of there. refer to the enigma function on line 958 and its integration on line 550

When you press the escape button, you open the menu with the buttons. You can refer to the pause menu function on line 819 and its integration on line 456

!!!-KNOWN BUGS

Visually, the original code's variable and function names were in capital letters, and most of the new ones are not. It can get confusing.


The pause menu isn't implemented in the temple


When you click on the RESTART button the game reloads with Link having the items he already had when the game ended (doesn't reset the complete game).

when the puzzle is wrong, sometimes the player does not move back directly. It still poses a second enigma before.


(W.B) Ganon stays in the temple in the begining, but after a while, he can get out of the temple. Since the movements of Ganon are random, he doesn't follow any rule of colliding like Link does. This could be prevented by adding a collider to Ganon to make him stay on the Dungeon map instead of sometimes walking away. (More details in the Branch mouvements-boss-dungeon)

(W.B) There was a bug with the entrance of the Dungeon that allowed the player to enter from the top of the Dungeon. This issue has been resolved and the problem was due to some misalignment of the collider for said Dungeon.    
