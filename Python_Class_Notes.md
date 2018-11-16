# Implement a Class

## Create a UML and implement a class

# Create a UML

Class Name: Dogue

Fields: Color, Number of Ears

Methods: Bark(), Run()

# Select something generic you like

A Pokemon

A Poke Bowl

A Poughkeepsie

An Animal

A Plant

A game

A Media (movie, song etc etc)

# Step 2 characteristics and abstract away

Pokemon : attack and defense

Poke bowl : toppings and sauce

Poughkeepsie: Is a town in NY

Animal : Number of ears, and number of feet

# Find 2 things it does

Pokemon: Attack, Defend

Poke Bowl: Make, Sell, go on sale

Poughkeepsie: Swelter, Freeze, Vote Democrat

Animal: Fight, Flight, Feed

# Create a UML, a class, and an object

1. Create a UML
2. Create a class definition based on UML
3. Instantiate an object of that class and run the code. 

# Optional : After you are done

```
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
```

# A Triangle is a polygon

```
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
```

# Run the code

```
t=Triangle()
t.inputSides()
t.dispSides()
t.findArea()
```

# Media

Python relies on modules to extend its capabilities.

There are many modules for sound and movies.

Enthought Canopy uses an audio processing module for sound: See piazza.

Unfortunately, we cannot add new modules with the set up we have.

Due to DeepFreeze any changes made on this system gets undone upon shutdown.
