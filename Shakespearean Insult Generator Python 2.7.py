import random

class Insult:
# The personalized Shakespearean Insult Generating Kit
# Now you too can insult like Shakespeare!
  def __init__(self, first="Jack", last="Black"):
    self.first=first
    self.last=last
    self.insult1=["artless", "baudy", "churlish", "craven", "errant","Fawning","lumpish"]
    self.insult2=["flap-mouthed", "half-witted", "rump-fed", "toad-spotted"]
    self.insult3=["lump of baggage", "pig's bladder", "codpiece", "foot-licker", "wagtail"]
    self.phrase=""

  def insultMe(self):
    self.phrase = self.insult1[ random.randint(0,len(self.insult1)-1) ]
    self.phrase += self.insult2[random.randint(0,len(self.insult2)-1) ]
    self.phrase += self.insult3[random.randint(0,len(self.insult3)-1) ]

    print self.first, self.last
    print "Thou art a ",self.phrase

myInsult=Insult()
myInsult.insultMe()
thineInsult=Insult("Charles", "the Bald")
thineInsult.insultMe()

