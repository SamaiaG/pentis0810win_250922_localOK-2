                # Switch key repeat settings based on the pressed key
                if key in key_repeat_settings:
                    repeat_delay, repeat_interval = key_repeat_settings[key]
                    
                    
                    pg.key.set_repeat(repeat_delay, repeat_interval)
                    key_state[key] = pg.time.get_ticks() + repeat_delay



                if key in key_repeat_settings:
                    repeat_delay, repeat_interval = key_repeat_settings[key]

                    # Check if the current key is in no-repeat mode
                    if key in key_repeat_mode and key_repeat_mode[key] == 0:
                        pg.key.set_repeat(repeat_delay, repeat_interval)
                        key_state[key] = pg.time.get_ticks() + repeat_delay
                        key_repeat_mode[key] = 1  # Switch to repeat mode
                    else:
                        pg.key.set_repeat(0)  # Set global repeat for non-switching keys

                    # If the current key is not in key_repeat_mode, add it and set to repeat mode
                    if key not in key_repeat_mode:
                        key_repeat_mode[key] = 1






if key in key_repeat_settings:
                    repeat_delay, repeat_interval = key_repeat_settings[key]

                    # Check if the current key is in no-repeat mode
                    if key in key_repeat_mode and key_repeat_mode[key] == 0:
                        pg.key.set_repeat(repeat_delay, repeat_interval)
                        key_state[key] = pg.time.get_ticks() + repeat_delay
                        key_repeat_mode[key] = 1  # Switch to repeat mode
                    else:
                        pg.key.set_repeat(0)  # Set global repeat for non-switching keys

                    # If the current key is not in key_repeat_mode, add it and set to repeat mode
                    if key not in key_repeat_mode:
                        key_repeat_mode[key] = 1







            if key in key_repeat_settings:
                repeat_delay, repeat_interval = key_repeat_settings[key]

                # Check if the current key is in no-repeat mode
                if key in key_repeat_mode and key_repeat_mode[key] == 0:
                    pygame.key.set_repeat(repeat_delay, repeat_interval)
                    key_state[key] = pygame.time.get_ticks() + repeat_delay
                    key_repeat_mode[key] = 1  # Switch to repeat mode
                else:
                    pygame.key.set_repeat(1, 1)  # Set global repeat for non-switching keys

                # If the current key is not in key_repeat_mode, add it and set to repeat mode
                if key not in key_repeat_mode:
                    key_repeat_mode[key] = 1                        