"""
-------------------------------------------------------------------------------
Name: ICS2O-CPT 2021.py
Purpose: To demostrate knowledge on certain aspects of coding. 

Author: Schwarzenberg.Maximilian

Created: 23/03/2021
------------------------------------------------------------------------------
"""
 
import pygame

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
DRED = (139,0,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
DGREEN = (49,99,0)
DDGREEN = (0,128,0)
BLUE = 	(0,0,255)
LBLUE =	(154,203,255)
PURPLE = (128,0,128)
 
pygame.init()

button_colour1 = GREEN
button_colour2 = RED
text_colour1 = BLACK
text_colour2 = BLACK

font = pygame.font.SysFont('Courier ', 30, True, False)
font1 = pygame.font.SysFont('Courier ', 75, True, False)
font2 = pygame.font.SysFont('Courier ', 60, True, True)

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

player_avatar = 1
plyr_changed = False

"""
 Scene number that controls the scene
0 = Title screen
1 = Gameplay
2 = Pause screen
3 = Game over screen
"""
scene = 0

 # The score that the player changes
score = 0
point_given = False
level = 1
next_level = 0

 # Loading images
cermit = pygame.image.load("cermit1.png").convert_alpha()
bingus = pygame.image.load("bingus.png").convert_alpha()
bee = pygame.image.load("bee.png").convert_alpha()
virus_image = pygame.image.load("virus.png").convert_alpha()
day_texture = pygame.image.load("day_sky.png").convert()
day_texture2 = pygame.image.load("day_sky2.png").convert()
after_texture = pygame.image.load("afternoon_sky.png").convert()
after_texture2 = pygame.image.load("afternoon_sky2.png").convert()
night_texture = pygame.image.load("night_sky.png").convert()
night_texture2 = pygame.image.load("night_sky2.png").convert()
grass_texture1 = pygame.image.load("grass-texture.png").convert()
grass_texture2 = pygame.image.load("grass-texture2.png").convert()
grass_texture3 = pygame.image.load("grass-texture3.png").convert()
arrow = pygame.image.load("long-arrow-left.png").convert_alpha()
iamspeed = pygame.image.load("iamspeed.png").convert_alpha()
 
pygame.display.set_caption("ICS2O-CPT 2021")
 
 #Loop until the user clicks the close button.
done = False
 
 # Used to manage how fast the screen updates
clock = pygame.time.Clock()

 # Positions of the parts
plyr_x = 100
plyr_y = 461
plyr_width = 56
plyr_height = 64

virus_x = 960
virus_box_close = 960
virus_box_far = virus_box_close + 50
grass_x = 0
sky_x = 0
grass_x2 = 1600
sky_x2 = 1600
speed_x = 3200

 # Speed of the parts
speed_virus = 7
speed_grass = 7
speed_sky = 0.7

hack = False
h_given = False
level_7 = False

 # Mouse and button click detection
button_pressed = False
mouse_click = False

 # Initializing the jumping variables 
isJump = False
jumpcount = 9

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop   
        elif plyr_y > 461:
          plyr_y += 6
        elif event.type == pygame.KEYDOWN:
            print("k_down")
        elif event.type == pygame.KEYUP:
            print("k_up")
            plyr_changed = False
        keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse button down")
            mouse_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse button up")
            mouse_click = False
        if keys[pygame.K_q] and h_given == False:
            hack = not(hack)
            h_given = True
            print(" hack: " + str(hack))

     # mouse variables
    mouse_position = pygame.mouse.get_pos()
    mouse_x = mouse_position[0]
    mouse_y = mouse_position[1]
    #print(mouse_position)

     # buttons in the scenes
    if scene == 0:
      if mouse_x > 50 and mouse_y > 350 and mouse_x < 375 and mouse_y < 425:
        button_colour1 = DDGREEN
        text_colour1 = WHITE
        if mouse_click == True:
          print("stareted game")
          scene = 1
      if mouse_x < 50 or mouse_y < 350 or mouse_x > 375 or mouse_y > 425:
        button_colour1 = GREEN
        text_colour1 = BLACK
      if mouse_x > 425 and mouse_y > 350 and mouse_x < 750 and mouse_y < 425:
        button_colour2 = DRED
        text_colour2 = WHITE
        if mouse_click == True:
          print("quit game")
          done = True
      if mouse_x < 425 or mouse_y < 350 or mouse_x > 750 or mouse_y > 425:
        button_colour2 = RED
        text_colour2 = BLACK
    
    if scene == 1:
      if mouse_x < 52 and mouse_y < 52 and mouse_click == True:
          print("paused game")
          scene = 2
    
    if scene == 2:
      if mouse_x > 50 and mouse_y > 350 and mouse_x < 375 and mouse_y < 425:
        button_colour1 = DDGREEN
        text_colour1 = WHITE
        if mouse_click == True:
          print("unpaused game")
          scene = 1
      if mouse_x < 50 or mouse_y < 350 or mouse_x > 375 or mouse_y > 425:
        button_colour1 = GREEN
        text_colour1 = BLACK
      if mouse_x > 425 and mouse_y > 350 and mouse_x < 750 and mouse_y < 425:
        button_colour2 = DRED
        text_colour2 = WHITE
        if mouse_click == True:
          print("quit to title")
          scene = 0
      if mouse_x < 425 or mouse_y < 350 or mouse_x > 750 or mouse_y > 425:
        button_colour2 = RED
        text_colour2 = BLACK
    
    if scene == 3:
      if mouse_x > 50 and mouse_y > 350 and mouse_x < 375 and mouse_y < 425:
        button_colour1 = DDGREEN
        text_colour1 = WHITE
        if mouse_click == True:
          print("stareted game")
          virus_x = 960
          grass_x = 0
          sky_x = 0
          grass_x2 = 1600
          sky_x2 = 1600
          speed_x = 3200
          speed_virus = 7
          virus_box_close = 960
          virus_box_far = virus_box_close + 50
          speed_grass = 7
          speed_sky = 0.7
          score = 0
          point_given = False
          level = 1
          hack = False
          h_given = False
          scene = 1
      if mouse_x < 50 or mouse_y < 350 or mouse_x > 375 or mouse_y > 425:
        button_colour1 = GREEN
        text_colour1 = BLACK
      if mouse_x > 425 and mouse_y > 350 and mouse_x < 750 and mouse_y < 425:
        button_colour2 = DRED
        text_colour2 = WHITE
        if mouse_click == True:
          print("quit game")
          done = True
      if mouse_x < 425 or mouse_y < 350 or mouse_x > 750 or mouse_y > 425:
        button_colour2 = RED
        text_colour2 = BLACK

    # --- Game logic should go here
    
     # The jumping function. This makes use of a quadratic formula to make the arc properly. 
    if isJump == False:
      if keys[pygame.K_SPACE]: #to jump
        isJump = True
    if isJump == True:
      if jumpcount >= -9:
        negative = 1
        if jumpcount < 0:
          negative = -1
        plyr_y -= (jumpcount ** 2 ) / 2 * negative
        jumpcount -= 0.75
      else:
        isJump = False
        jumpcount = 9

    if score >= 10:
        speed_virus = 10
        speed_grass = 10
        speed_sky = 1.0
        level = 2
        
    if score >= 30:
        speed_virus = 15
        speed_grass = 15
        speed_sky = 1.5
        level = 3
        
    if score >= 50:
        speed_virus = 20
        speed_grass = 20
        speed_sky = 2.0
        level = 4
        
    if score >= 70:
        speed_virus = 25
        speed_grass = 25
        speed_sky = 2.5
        level = 5
        
    if score >= 90:
        speed_virus = 30
        speed_grass = 30
        speed_sky = 3.0
        level = 6

     # The last level 7
    if score >= 200 and scene == 1:
        speed_virus = 50
        speed_grass = 50
        speed_sky = 5.0
        level = 7
        level_7 = True
        next_level = "[X]"
        screen.fill(LBLUE)
        level_7 = font.render("U beat the game! Thank you for playing.", True, BLACK)
        screen.blit(level_7, [25, 200])
        credits_title = font2.render("CREDITS:", True, BLACK)
        screen.blit(credits_title, [225, 250])
        credits_1 = font.render("nikokouk", True, BLACK)
        screen.blit(credits_1, [255, 310])
        credits_2 = font.render("TheFaded", True, BLACK)
        screen.blit(credits_2, [255, 360])
        credits_3 = font.render("Cat Goes Brrr", True, BLACK)
        screen.blit(credits_3, [255, 410])
        credits_4 = font.render("TypeL3mon", True, BLACK)
        screen.blit(credits_4, [255, 460])
        credits_5 = font.render("Dan_Does_Music", True, BLACK)
        screen.blit(credits_5, [255, 510])
        credits_6 = font.render("and YOU for playing.", True, BLACK)
        screen.blit(credits_6, [255, 560])
        level_display = font.render("Level: " + str(level) + "", True, BLUE)
        screen.blit(level_display, [2, 64])
        if scene == 1:
            speed_x = speed_x - 50
        screen.blit(iamspeed, [speed_x, 410])
        if isJump == True:
            score = score + 2
            print("   score: " + str(score))
            point_given = True

    if score >= 10500:
        scene = 4
        if isJump == True:
            score = score + 2
            print("   score: " + str(score))
            point_given = True
            
    if score >= 11500:
        pygame.time.wait(3600)
        done = True
        
     # The function that makes the running seem infinite by looping
    if scene == 1:
      virus_x = virus_x - speed_virus
      if virus_x <= -160 and level_7 == False:
        virus_x = 1040
      virus_box_close = virus_x - speed_virus
      if virus_box_close <= -160 and level_7 == False:
        virus_box_close = 1040
      virus_box_far = virus_x + 50 - speed_virus
      if virus_box_far <= -80 and level_7 == False:
        virus_box_far = 1120
      sky_x = sky_x - speed_sky
      if sky_x <= -1600 and level_7 == False:
        sky_x = 1600
      sky_x2 = sky_x2 - speed_sky
      if sky_x2 <= -1600 and level_7 == False:
        sky_x2 = 1600
      grass_x = grass_x - speed_grass
      if grass_x <= -1600 and level_7 == False:
        grass_x = 1600
      grass_x2 = grass_x2 - speed_grass
      if grass_x2 <= -1600 and level_7 == False:
        grass_x2 = 1600
      addtoscore = font.render("+1", True, PURPLE)
    

     # The scoring function
    if virus_x > 100 and virus_x < 156 and point_given == False:
        if plyr_y < 461:
            score = score + 1
            print("   ")
            print("   score: " + str(score))
            print("   ")
            point_given = True
    if plyr_x + 50 > virus_box_close and plyr_x + 22 < virus_box_far and plyr_y > 370 and virus_x > 0 and hack == False:
        scene = 3
        point_given = True
    if virus_x < 100:
        point_given = False
        h_given = False
    
    if level == 1:
        next_level = 10 - score
    if level == 2:
        next_level = 30 - score
    if level == 3:
        next_level = 50 - score
    if level == 4:
        next_level = 70 - score
    if level == 5:
        next_level = 90 - score
    if level == 6:
        next_level = 200 - score
    
    # --- Drawing code should go here
    
     # The function to change characters (Press E to change in the title screen)
    if keys[pygame.K_e] and scene == 0 and plyr_changed == False:
        player_avatar = player_avatar + 1
        if player_avatar == 1 or player_avatar == 4 and plyr_changed == False:
            print("Player selected: Cermit")
        if player_avatar == 2 and plyr_changed == False:
            print("Player selected: Bingus")
        if player_avatar == 3 and plyr_changed == False:
            print("Player selected: Bee")
        plyr_changed = True
        if player_avatar > 3:
            player_avatar = 1
    
    
    
     # Drawing the visuals on the screen
    if scene == 0:
      screen.fill(LBLUE)
      pygame.draw.rect(screen, DGREEN, [50, 100, 700, 200])
      if player_avatar == 1:
        screen.blit(cermit, [122, 125])
      if player_avatar == 2:
        screen.blit(bingus, [122, 125])
      if player_avatar == 3:
        screen.blit(bee, [122, 125])
      title = font2.render("CERMIT VIRUS JUMPER", True, BLACK)
      screen.blit(title, [51, 160])
      subtitle = font.render("ICS2O1b CPT", True, BLACK)
      screen.blit(subtitle, [310, 250])
      pygame.draw.rect(screen, button_colour1, [50, 350, 325, 75])
      play = font1.render("PLAY", True, text_colour1)
      screen.blit(play, [115, 350])
      pygame.draw.rect(screen, button_colour2, [425, 350, 325, 75])
      quit = font1.render("QUIT", True, text_colour2)
      screen.blit(quit, [490, 350])
      howtoplay0 = font.render("How to play:", True, BLACK)
      screen.blit(howtoplay0, [50, 450])
      howtoplay1 = font.render("You are a player that jumps over viruses.", True, BLACK)
      screen.blit(howtoplay1, [50, 485])
      howtoplay2 = font.render("Press space to jump.", True, BLACK)
      screen.blit(howtoplay2, [50, 510])
    if scene == 1:
      if level == 1 or level == 2:
          screen.blit(day_texture, [sky_x, 0])
          screen.blit(day_texture2, [sky_x2, 0])
          screen.blit(grass_texture1, [grass_x, 525])
          screen.blit(grass_texture1, [grass_x2, 525])
      if level == 3 or level == 4:
          screen.blit(after_texture, [sky_x, 0])
          screen.blit(after_texture2, [sky_x2, 0])
          screen.blit(grass_texture2, [grass_x, 525])
          screen.blit(grass_texture2, [grass_x2, 525])
      if level == 5 or level == 6:
          screen.blit(night_texture, [sky_x, 0])
          screen.blit(night_texture2, [sky_x2, 0])
          screen.blit(grass_texture3, [grass_x, 525])
          screen.blit(grass_texture3, [grass_x2, 525])
      if player_avatar == 1:
        screen.blit(cermit, [plyr_x, plyr_y])
      if player_avatar == 2:
        screen.blit(bingus, [plyr_x, plyr_y])
      if player_avatar == 3:
        screen.blit(bee, [plyr_x, plyr_y])
      screen.blit(virus_image, [virus_x, 450])
      pygame.draw.rect(screen, RED, [0, 0, 52, 52])
      screen.blit(arrow, [1, 1])
      """
      pygame.draw.line(screen, BLACK, [plyr_x + 50, 280], [plyr_x + 50, 525], 1)
      pygame.draw.line(screen, BLACK, [plyr_x + 22, 280], [plyr_x + 22, 525], 1)
      pygame.draw.line(screen, BLACK, [virus_box_close, 370], [virus_box_close, 525], 1)
      pygame.draw.line(screen, BLACK, [virus_box_far, 370], [virus_box_far, 525], 1)
      pygame.draw.line(screen, BLACK, [virus_box_close, 370], [virus_box_far, 370], 1)
      pygame.draw.line(screen, BLACK, [virus_box_close, 450], [virus_box_far, 450], 1)
      #"""
      pygame.draw.rect(screen, WHITE, [60, 9, 204, 33])
      score_display = font.render("Score: " + str(score), True, BLACK)
      screen.blit(score_display, [60, 9])
      level_display = font.render("Level: " + str(level) + " ("+ str(next_level) + " point(s) left to level " + str(level + 1) + ".)", True, BLUE)
      screen.blit(level_display, [2, 64])
      if point_given == True:
        screen.blit(addtoscore, [274, 9])
      if virus_x < 0:
        screen.blit(addtoscore, [274, -25])
     
    if scene == 2:
      screen.fill(LBLUE)
      pygame.draw.rect(screen, DGREEN, [50, 100, 700, 200])
      title = font2.render("CERMIT VIRUS JUMPER", True, BLACK)
      screen.blit(title, [51, 160])
      subtitle = font.render("PAUSED", True, BLACK)
      screen.blit(subtitle, [335, 250])
      pygame.draw.rect(screen, button_colour1, [50, 350, 325, 75])
      play = font1.render("PLAY", True, text_colour1)
      screen.blit(play, [115, 350])
      pygame.draw.rect(screen, button_colour2, [425, 350, 325, 75])
      quit = font1.render("QUIT", True, text_colour2)
      screen.blit(quit, [490, 350])
    if scene == 3:
      screen.fill(LBLUE)
      pygame.draw.rect(screen, DGREEN, [50, 100, 700, 200])
      title = font2.render("CERMIT VIRUS JUMPER", True, BLACK)
      screen.blit(title, [51, 160])
      subtitle = font.render("GAME OVER", True, RED)
      screen.blit(subtitle, [335, 250])
      pygame.draw.rect(screen, button_colour1, [50, 350, 325, 75])
      play = font1.render("AGAIN", True, text_colour1)
      screen.blit(play, [100, 350])
      pygame.draw.rect(screen, button_colour2, [425, 350, 325, 75])
      quit = font1.render("QUIT", True, text_colour2)
      screen.blit(quit, [490, 350])
      virus_x = 960
    
    if scene == 4:
      screen.fill(BLACK)
      pygame.draw.rect(screen, DGREEN, [50, 100, 700, 200])
      why = font2.render("why are you still here?", True, WHITE)
      screen.blit(why, [1, 160])
      nothing = font.render("there is nothing left,", True, WHITE)
      screen.blit(nothing, [230, 360])
      leave = font.render("leave already.", True, WHITE)
      screen.blit(leave, [280, 510])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()