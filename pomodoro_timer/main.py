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
import vlc


CYCLES              = 4
path_to_sound       = '/home/ahmad-abdullatif/pythonProjects/pomodoro_timer/sound.wav'
path_to_png         = '/home/ahmad-abdullatif/pythonProjects/pomodoro_timer/tomato.png'

notify2.init('Pomodoro timer')
sound = vlc.MediaPlayer(path_to_sound)

work_message        = notify2.Notification("Pomodoro", "Time to work!", path_to_png)
short_break_message = notify2.Notification("Pomodoro", "Take a break!", path_to_png)
long_break_message  = notify2.Notification("Pomodoro", "time for a long break!", path_to_png)
finish_message      = notify2.Notification("Pomodoro","you're done for today!, good job", path_to_png)


def notify(notification):
    sound.stop()
    notification.show()
    sound.play()

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
        notify(work_message)
        print('--------------------------------')
        countdown(work_time*60,f'session {session_counter}')
        
        if session_counter < CYCLES:
            notify(short_break_message)
            countdown(break_time*60,f'break {session_counter}')
            session_counter += 1
        else:
            notify(long_break_message)
            countdown(long_break*60,'long break')
            round_counter += 1
            session_counter = 1
        
    notify(finish_message)
    print("you're done for today!, good job")


if __name__ == '__main__':
    main()
