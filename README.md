<h1>Snake Game with Pygame</h1>
<p>This code implements a snake game using Pygame. The game has a 750 x 750 window and each tile has a size of 50 x 50. The snake starts with a length of 1 and its starting position is randomly generated. The game allows the snake to move up, down, left, and right, and the snake can grow by eating the food (represented as a red square). The game ends when the snake collides with the border or with itself.</p>
<h2>Requirements</h2>
<ul>
  <li>Pygame</li>
</ul>
<h2>Usage</h2>
<p>Run the code to start the game. The game can be controlled by the arrow keys on the keyboard.</p>
<h2>Key Components</h2>
<ul>
  <li><code>snake</code>: represents the snake, implemented as a Pygame Rect.</li>
  <li><code>length</code>: the length of the snake.</li>
  <li><code>segments</code>: a list of rects representing the segments of the snake.</li>
  <li><code>snake_dir</code>: the direction of the snake's movement.</li>
  <li><code>food</code>: the food that the snake can eat to grow.</li>
  <li><code>screen</code>: the screen of the game, implemented as a Pygame display.</li>
  <li><code>clock</code>: a Pygame Clock object used to control the frame rate of the game.</li>
  <li><code>dirs</code>: a dictionary that keeps track of the valid keys for controlling the snake.</li>
</ul>
