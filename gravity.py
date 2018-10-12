# README.md
# # Python-gravity

# Oct-12-2018

GRAVITY_EARTH=9.8
TIME=0.6
VELOCITY_0=16
HEIGHT_0=16
TIMEUNIT_LONG="second"
TIMEUNIT_PLUR="seconds"
TIMEUNIT_SHORT="sec"
LENGTHUNIT_LONG="feet"
LENGTHUNIT_PLUR="feet"
LENGTHUNIT_SHORT="ft"

def calcFallTime(t, v, h):
    h=-GRAVITY_EARTH/2*t*t+v*t+h
    return h

print "Calculate the height you will achieve"

time=TIME
velocity=VELOCITY_0
height=HEIGHT_0

final=calcFallTime(time, velocity, height)
print "After "+str(TIME)+" "+TIMEUNIT_SHORT+" with a starting"
print "velocity of "+str(HEIGHT_0)+" "+LENGTHUNIT_SHORT+"/"+TIMEUNIT_SHORT+" and a starting"
print "height of "+str(HEIGHT_0)+" "+LENGTHUNIT_PLUR
print ""
print "You will achieve "+str(final)+" "+LENGTHUNIT_PLUR
