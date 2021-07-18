"""
Oppgave 1.2.3:
Gitt en alder i sekunder, kalkuler hvor gammel noen ville vært på:
    - Jorda:   omløpstid 365.25 jorddager, eller 31557600 sekunder.
    - Merkur:  omløpstid 0.2408467 jordår.
    - Venus:   omløpstid 0.61519726 jordår.
    - Mars:    omløpstid 1.8808158 jordår.
    - Jupiter: omløpstid 11.862615 jordår.
    - Saturn:  omløpstid 29.447498 jordår.
    - Uranus:  omløpstid 84.016846 jordår.
    - Neptun:  omløpstid 164.79132 jordår.
"""

class SpaceAge:
    seconds = 0
    earth_years = 0

    EARTH = 1
    MERCURY = 0.2408467
    VENUS = 0.61519726
    MARS = 1.8808158
    JUPITER = 11.862615
    SATURN = 29.447498
    URANUS = 84.016846
    NEPTUNE = 164.79132

    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = seconds/31557600

    def years(self, planet):
        return round(self.earth_years / planet, 2)
    
    def on_earth(self):
        return self.years(SpaceAge.EARTH)

    def on_mercury(self):
        return self.years(SpaceAge.MERCURY)
    
    def on_mars(self):
        return self.years(SpaceAge.MARS)

    def on_jupiter(self):
        return self.years(SpaceAge.JUPITER)

    def on_saturn(self):
        return self.years(SpaceAge.SATURN)

    def on_uranus(self):
        return self.years(SpaceAge.URANUS)

    def on_neptune(self):
        return self.years(SpaceAge.NEPTUNE)

calculateAge = SpaceAge(35000000)

print(calculateAge.on_earth()) # skal gi 1.11