import sched, time, ctypes


def do_something(sc): 
    ctypes.windll.user32.LockWorkStation()
    # do your stuff
    s.enter(break_time, 1, do_something, (sc,))

break_time = 60*60
s = sched.scheduler(time.time, time.sleep)
s.enter(break_time, 1, do_something, (s,))
s.run()
