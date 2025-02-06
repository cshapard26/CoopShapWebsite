# Introduction
Like all physical systems, magnetic interactions are based on mathematics. Given information like distance, charge, and shape, we can calculate exactly how electromagnetic interactions should behave. However, in a much simpler environment like a videogame simulation, we can control these behaviors however we see fit. In the case of Magnet Game, I have to build the entire electromagnetic interaction system from scratch. But there's a twist. Unlike real-world systems, Magnet Game exists in discrete time and discrete space, which changes the expected behavior of magnets. I have to decide how to implement those interactions to make the environment seem intuitive to a player.

# Discrete Time
Discrete time means that the game is not continually updating the time. The magnets can only move and interact at certain times, and I have chosen to make that whenever the player presses a button. Take the example below of 2 magnets in an infinite loop below. Blue repels blue and attracts red (and vice versa). The green lights in the top left show when the user presses a button.

Insert Gif 1 Here

Even though there are times when two blue magnets sit next to each other, they do not repel until after the user's input. This is because time does not update until the instantaneous time the user presses a key. The computer then calculates where the magents should move (explained in a future post), and then teleports them to their position in the next time state.

# Discrete Space
Discrete space means that each object in the game can only exist in certain positions. It can be in space 1 or space 2, but not space 1.5. This is how all grid-based games work. In chess, you can't respond to e4 with d4.5. This is a very important topic for Magnet Game, because real-world systems are in continuous space and that changes greatly in discrete space (similar to how signals in DSP change when discretized). Check the gif below, which is the same as the example above, but without the animations.

Insert Gif 2 Here

This is how the computer sees the objects in the game, teleporting from one position to another, but not seeing anything that happens in between. Though visually in the first gif, the two magnets pass each other, they don't "connect" and start moving together as you might expect in a continuous time system. The two magnets don't even see each other.

This also changes how forces interact in the game. In the real world, magnetic forces extend infinitely, but diminish quickly. In Magnet Game, they extend only for a certain number of discrete spaces. Small magnets only send attractive forces to cells in the four cardinal directions surrounding them. Large magnets have a 2 cell wide diamond of influence.

In continuous space and time, you might expect something where the magnets rotate around a post, but stay together. Like this:

Insert Gif 3 Here

But in Magnet Game's discretized world, this is what actually happens:

Insert Gif 4 Here

# Why Animate
If the animations are decpetive about how the system really works, then why include them? Why not have the visuals fully represent what is actually happening in the game? One reason. This:

Insert Gif 5 Here

Is easier to understand than this:

Insert Gif 6 Here

# Map Code
As promised, here is some code you can use in your own project. It generates a map in your Godot Scene on runtime, adding all the sprites and backgrounds to the scene. This won't be plug-and-play in your project, as you will need to implement custom classes such as Matrix and Cell, but it should give you a good starting place to start implementing grid-style movement and runtime instantiation. 

```
var map_size : Vector2i
var cells : Matrix
var cell_background : PackedScene
var original_map_string : Matrix

func _create_map(grid_size : int) -> void:
    cells = Matrix.new(map_size.x, map_size.y)
        for row in range(map_size.x):
            for cell in range(map_size.y):
                cells.set_element(row, cell, Cell.new())
                var curr_cell = cells.get_element(row, cell)
                curr_cell.name = "Cell_" + str(row) + "_" + str(cell)
                curr_cell.location = Vector2i(row, cell)
                curr_cell.position = curr_cell.location * grid_size
                Cell_Node.add_child(curr_cell)
                
                # Sprite
                var bg_sprite = cell_background.instantiate()
                bg_sprite.z_index = -100
                bg_sprite.name = "Background_Reg"
                curr_cell.add_child(bg_sprite)
                
                # Fill cell
                var curr_data = original_map_string.get_element(row, cell)
                for i in range(len(curr_data)):
                    # Edge cases
                    if curr_data[i] == " ":
                        continue
                    
                    # Create GameObject (gobj)
                    var obj = char_to_gobj(curr_data[i]).new()
                    obj.host_cell = curr_cell
                    obj.id = GlobalFunctions.generate_random_id()
                    obj.name = str(obj.id)
                    obj.position = obj.host_cell.position
                    obj.z_index = obj.display_z

                    GOBJ_Node.add_child(obj)
```