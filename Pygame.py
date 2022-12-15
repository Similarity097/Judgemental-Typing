'''import time
def time_thread(self):
	while self.running:
		time.sleep(0.1)
		self.counter += 0.1
		cps = len(self.inpuy_entry())/self.counter
		self.speed_label.config(text=f"speed: \n{cps:.2f} CPS\n{cpm:,2f} CPM)'''
	

"""
 Show how to put a timer on the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
  

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 60
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
   
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])
 
    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, BLACK)
 
    screen.blit(text, [250, 280])
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
 
    # Limit frames per second
    clock.tick(frame_rate)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()