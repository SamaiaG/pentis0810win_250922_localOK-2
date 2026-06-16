import pygame

class Timer:
    #__init__ method that takes a duration parameter, which is the duration of the timer in milliseconds - wenn initiiert
    def __init__(self, duration):
        self.duration = duration
        self.start_time = pygame.time.get_ticks()   #get the time in milliseconds
        self.is_running = True

    #update method checks if the timer is still running and updates its state accordingly
    def update(self):
        if self.is_running:
            time_passed = pygame.time.get_ticks() - self.start_time
            #If the timer has reached its duration, it sets its is_running attribute to False.
            if time_passed >= self.duration:
                self.is_running = False

    #restart method resets the timer and starts it again,
    def restart(self):
        self.start_time = pygame.time.get_ticks()
        self.is_running = True

    # while the stop method stops the timer.
    def stop(self):
        self.is_running = False


timer1 = Timer(5000)  # A timer that lasts for 5 seconds
timer2 = Timer(10000) # A timer that lasts for 10 seconds

running = True

while running:
    # Update the timers
    timer1.update()
    timer2.update()

    # Check if the timers have finished
    if not timer1.is_running:
        print("timer1")
        # Do something when timer1 has finished

    if not timer2.is_running:
        print("timer2")
        # Do something when timer2 has finished
