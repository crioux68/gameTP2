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
-Main menu song (plays in the overworld and the dungeon)

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


!!!-KNOWN BUGS

-Visually, the original code's variable and function names were in capital letters, and most of the new ones are not. It can get confusing.
-When you click on the RESTART button the game reloads with Link having the items he already had when the game ended (doesn't reset the complete game).
-Picking up an item that as previously been dropped can be inconsistent. 
-When Link spawns in the temple, the "f" key makes the firing sound intermittently, but you don't see the staff required for this sound effect, nor any orbs being fired.
-You can enter the dungeon through the top of the temple because of some non-optimal diagonal collisioning .
