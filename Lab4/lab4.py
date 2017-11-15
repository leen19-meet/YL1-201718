class Animal(object):
    def __init__(self,sound,name,age,favorite_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
    def eat(self,food):
        print("Yummy!!" + self.name + " is eating " + food)
    def description(self):
        print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)
    def make_sound(self, times):
        print(self.sound*times) 

    
a = Animal("meaw","bissy",3,"green")
a.eat("meat")
a.description()

a.make_sound(3)

class Person(object):
    def __init__(self,name,age,city,gender):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
    def eat2(self,food):
        print("Yummy!!" + self.name + " is eating " + food)
    def song(self,song_name):
        print("Wow!" + self.name + " loves this song:" + song_name)

b=Person("Jane",18,"Haifa","female")
b.eat2("pancakes")
b.song("Hotel-california")
#problem3-extra 
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)
    


idontknow = Song(["i","dont","know"])
idontknow.sing_me_a_song()

