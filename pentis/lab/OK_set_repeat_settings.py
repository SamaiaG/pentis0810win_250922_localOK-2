import pygame as pg

pg.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))

# Set the repeat rates for each key
repeat_rate_1 = 100  # milliseconds
repeat_rate_2 = 200  # milliseconds

# Initialize the key states
key_state_1 = False
key_state_2 = False
key_time_1 = 0
key_time_2 = 0

key_repeat_settings = {
    pg.K_x: (0, 0),  # Key X with no repeat
    pg.K_y: (0, 0),  # Key Y with no repeat
    pg.K_a: (0, 0),  # Key A with no repeat
    pg.K_RIGHT: (200, 50),  # Key RIGHT with repeat delay of 200ms and interval of 50ms
    pg.K_LEFT: (200, 50),  # Key LEFT with repeat delay of 200ms and interval of 50ms
    pg.K_DOWN: (200, 50),  # Key DOWN with repeat delay of 200ms and interval of 50ms
}

# The game loop
while True:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            #sys.exit()

    # Get the state of the keys
    keys = pg.key.get_pressed()
    # Handle key 1
    if key in key_repeat_settings:
        repeat_delay, repeat_interval = key_repeat_settings[key]
        pg.key.set_repeat(repeat_delay, repeat_interval)
        key_state[key] = pg.time.get_ticks() + repeat_delay  
        print(key_state) 
        # Check if the key is being held down
        if keys in key_repeat_settings:
            # Check if enough time has passed to repeat the action
            if pg.time.get_ticks() - key_time_1 > repeat_rate_1:
                # Repeat the action
                print("Key 1 repeated")
                key_time_1 = pg.time.get_ticks()
        else:
            # Start the key press
            print("Key 1 pressed")
            key_state_1 = True
            key_time_1 = pg.time.get_ticks()

    else:
        # End the key press
        if key_state_1:
            print("Key 1 released")
            key_state_1 = False

        # Handle key 2
    if keys[pg.K_RETURN]:
        # Check if the key is being held down
        if key_state_2:
            # Check if enough time has passed to repeat the action
            if pg.time.get_ticks() - key_time_2 > repeat_rate_2:
                # Repeat the action
                print("Key 2 repeated")
                key_time_2 = pg.time.get_ticks()
        else:
            # Start the key press
            print("Key 2 pressed")
            key_state_2 = True
            key_time_2 = pg.time.get_ticks()
#
    else:
        # End the key press
        if key_state_2:
            print("Key 2 released")
            key_state_2 = False

    # Update the screen
    pg.display.update()
