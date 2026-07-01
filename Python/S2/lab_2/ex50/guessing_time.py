from lab_2.ex49.timing import StopWatch
import random

number = random.randint(10, 20)

print(f"the time to guess is {number} sec!")
input("Ready? Push any key to start the timer! ")
watch = StopWatch()
input()
elapsed = watch.elapsed()
offset = elapsed - number
print(f"your time was: {elapsed} seconds (difference: {offset})")
if -1 < offset < 1:
    print("are you cheating? that was way to precise!")
elif -3 < offset < 3:
    print("that was alright, adequate some might say.")
else:
    print("I know you can do better! better luck next time.")
