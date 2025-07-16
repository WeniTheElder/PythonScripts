#!/home/ahmad-abdullatif/pythonProjects/pp_venv/bin/python3
"""
this module implements a cli tool pomodoro timer
the module uses click to parse arguments, time for program sleep, 
and notify2 for sending notifications

the user can change the duration of the work_time, break_time, and number of rounds
"""
import time
import click
import notify2
from playsound import playsound


notify2.init('Pomodoro timer')
work_message        = notify2.Notification("Pomodoro", "Time to work!")
short_break_message = notify2.Notification("Pomodoro", "Take a break!")
long_break_message  = notify2.Notification("Pomodoro", "time for a long break!")
finish_message      = notify2.Notification("you're done for today!, good job")
path_to_sound       = '/home/ahmad-abdullatif/pythonProjects/pomodoro_timer/mixkit-bell-notification-933.wav'
CYCLES              = 4


def countdown(time_in_secs,title):
    timer = time_in_secs
    
    while timer:
        secs = timer%60
        mins = int(timer/60)
        print(f'\r{title} | time left->',end = '')
        print(click.style(f'{mins:02d}:{secs:02d}',fg = 'red'),end = '')
        time.sleep(1)
        timer -= 1
    
    print('\ntime\'s up')


@click.command()
@click.option('-w','--work-time',default = 25, help = 'work duration in minutes', type = int)
@click.option('-b','--break-time',default = 5, help = 'break duration in minutes', type = int)
@click.option('-l','--long-break',default = 20, help = 'long break duration in minutes', type = int)
@click.option('-r','--rounds',default = 2, help = 'the number of rounds', type = int)
def main(work_time,break_time,long_break,rounds):
    session_counter = 1
    round_counter   = 0
    
    while round_counter < rounds:
        work_message.show()
        playsound(path_to_sound)
        print('--------------------------------')
        countdown(work_time*60,f'session {session_counter}')
        
        if session_counter < CYCLES:
            short_break_message.show()
            playsound(path_to_sound)
            countdown(break_time*60,f'break {session_counter}')
            session_counter += 1
        else:
            long_break_message.show()
            playsound(path_to_sound)
            countdown(long_break*60,'long break')
            round_counter += 1
            session_counter = 1
        
    print("you're done for today!, good job")
    finish_message.show()
    playsound(path_to_sound)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
