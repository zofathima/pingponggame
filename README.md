Your Pong Game To-Do List
This project will help you master a few key concepts, like creating multiple classes and making objects interact with each other.

Step 1: The Paddles (Paddle Class)
[ ] Create a new class called Paddle that inherits from turtle.Turtle. Remember to write (Turtle) after the class name to get all its powers.

[ ] In the Paddle class, define an __init__ method that takes x_pos and y_pos as inputs.

[ ] Call super().__init__() to properly set up the new object.

[ ] Use methods on self to set its shape to "square" and its color to "white".

[ ] Make the paddle object bigger by using self.shapesize(stretch_wid=1, stretch_len=5).

[ ] Use self.penup() to stop the paddle from drawing.

[ ] Use self.goto(x_pos, y_pos) to move the paddle to its starting spot.

[ ] Create a up method for the paddle. This method should move the paddle's y-coordinate up by 20.

[ ] Create a down method to move the paddle's y-coordinate down by 20.

Step 2: The Ball (Ball Class)
[ ] Create a new class called Ball that also inherits from turtle.Turtle.

[ ] Define its __init__ method.

[ ] Call super().__init__().

[ ] Use methods on self to set its shape to "circle" and its color to "white".

[ ] Use self.penup().

[ ] Create attributes on self to control the ball's movement: x_move = 10, y_move = 10, and a move_speed = 0.1.

[ ] Create a move method that uses the ball's x_move and y_move attributes to update its position.

[ ] Create a bounce_y method that reverses the ball's y_move direction (e.g., self.y_move *= -1). Also, make the ball faster by reducing move_speed slightly (e.g., self.move_speed *= 0.9).

[ ] Create a bounce_x method that reverses the ball's x_move direction and makes it faster.

[ ] Create a reset_pos method that moves the ball back to the center of the screen (0, 0). This method should also reset the move_speed and call bounce_x() to change direction.

Step 3: The Scoreboard (Scoreboard Class)
[ ] Create a new class called Scoreboard that inherits from turtle.Turtle.

[ ] Define its __init__ method.

[ ] Call super().__init__().

[ ] Use methods on self to set its color to "white", lift the pen up (penup()), and hide the turtle shape (hideturtle()).

[ ] Use self.goto(0, 260) to move the scoreboard to the top of the screen.

[ ] Create attributes for the scores: l_score = 0 and r_score = 0.

[ ] Write the initial score to the screen using self.write().

[ ] Create a l_point method that adds one to the l_score, clears the old score, and rewrites the new score.

[ ] Create a r_point method that does the same for the r_score.

Step 4: Putting It All Together (The Main Game Logic)
[ ] Import Screen from turtle, and all the classes you just created (Paddle, Ball, Scoreboard). You'll also need to import the time and random modules.

[ ] Set up the screen with a title, a black background, and a size of 800x600.

[ ] Use screen.tracer(0) to turn off screen updates. This will make the game animation smoother.

[ ] Create two Paddle objects: one for the right side and one for the left.

[ ] Create a Ball object.

[ ] Create a Scoreboard object.

[ ] Use screen.listen() and screen.onkey() to connect the keyboard keys ("Up", "Down", "w", "s") to the paddle movement methods you created.

[ ] Create a while loop that runs as long as the game is on.

[ ] Inside the loop:

[ ] Add time.sleep(ball.move_speed) to control the game's speed.

[ ] Call screen.update() to show the latest positions of the objects.

[ ] Call ball.move() to make the ball move.

[ ] Add an if statement to check if the ball hits the top or bottom wall and call ball.bounce_y().

[ ] Add an if statement to check if the ball hits either paddle and call ball.bounce_x().

[ ] Add if statements to check if the ball goes past a paddle and call the appropriate scoring method (scoreboard.l_point() or scoreboard.r_point()) and ball.reset_pos().

[ ] At the end, use screen.exitonclick() to keep the screen open after the game is over.