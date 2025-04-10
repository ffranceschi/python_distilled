class Duck:
    def walk(self):
        print('Waddle')
class Trombonist:
    def noise(self):
        print('Blat!')
class DuckBonist(Duck, Trombonist):
    pass


d = DuckBonist()
d.walk() # -> Waddle
d.noise()