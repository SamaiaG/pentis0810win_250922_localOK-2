import pygame as pg

pg.init()



# Set up the display
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))

# Define the initial delay and repeat rate
initial_delay_1 = 2000  # milliseconds
repeat_rate_1 = 100  # milliseconds
repeat_rate_2 = 200  # milliseconds

repeat_rate_down = 12  # milliseconds
repeat_rate_hdown = 30

# Initialize the key states
key_state_1 = False
key_state_2 = False
key_state_3 = False
key_state_4 = False
key_time_1 = 0
key_time_2 = 0
key_time_3 = 0
key_time_4 = 0

# The game loop
while True:


    # Get the state of the keys
    keys = pg.key.get_pressed()
    #print("keys:",keys)

    # Handle key 1
    if keys[pg.K_m]:
        # Check if the key is being held down
        if key_state_1:
            # Check if enough time has passed to repeat the action
            if pg.time.get_ticks() - key_time_1 > repeat_rate_1:
                # Repeat the action
                print("Key 1 repeated", key_time_1, repeat_rate_1)
                # key function here !!!??
                key_time_1 = pg.time.get_ticks()
        else:  # 1st Step
            # Start the key press
            key_state_1 = True
            key_time_1 = pg.time.get_ticks() + initial_delay_1  # Add initial delay
            
            print("Key 1 pressed", key_time_1, repeat_rate_1)

    else:
        # End the key press
        if key_state_1:
            print("Key 1 released", key_time_1, repeat_rate_1)
            key_state_1 = False

    # Handle key 2
    if keys[pg.K_RETURN]:
        # Check if the key is being held down
        if key_state_2:
            # Check if enough time has passed to repeat the action
            if pg.time.get_ticks() - key_time_2 > repeat_rate_2:
                # Repeat the action
                print("Key 2 repeated", key_time_2, repeat_rate_2)
                key_time_2 = pg.time.get_ticks()
        else:
            # Start the key press
            print("Key 2 pressed", key_time_2, repeat_rate_2)
            key_state_2 = True
            key_time_2 = pg.time.get_ticks()

    else:
        # End the key press
        if key_state_2:
            print("Key 2 released", key_time_2, repeat_rate_2)
            key_state_2 = False


    if keys[pg.K_SPACE]:
        # Check if the key is being held down
        if key_state_4:
            # Check if enough time has passed to repeat the action
            if pg.time.get_ticks() - key_time_4 > repeat_rate_hdown:
                # Repeat the action
                print("Key 2 repeated", key_time_4, repeat_rate_hdown)
                key_time_4 = pg.time.get_ticks()
        else:
            # Start the key press
            print("Key 2 pressed", key_time_4, repeat_rate_hdown)
            key_state_4 = True
            key_time_4 = pg.time.get_ticks()

    else:
        # End the key press
        if key_state_4:
            print("Key 2 released", key_time_4, repeat_rate_hdown)
            key_state_4 = False             

    # Handle events



    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            #sys.exit()  
        if (event.type) == pg.KEYDOWN:

            key = event.key
            #print("key:",keys)          

    # Update the screen
    pg.display.update()
