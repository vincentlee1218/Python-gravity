# README.md
# # Python-gravity

# Oct-12-2018


def calcFallTime(t, v, h):
    h=-16*t*t+v*t+h
    return h


print "Calculate the height you will achieve"

time=0.6 
velocity=16
height=16

final=calcFallTime(time, velocity, height)
print "After 1.6 seconds with a starting"
print "velocity of 16 ft/sec and a starting"
print "height of 16 feet"
print ""
print "You will achieve "+str(final)+" feet"
