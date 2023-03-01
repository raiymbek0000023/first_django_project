from db.models import *
import datetime

platform_title=['snes', 'Wii', 'nes', 'Gb', 'Ds', 'x360', 'ps2', 'ps3','ps4', 'ps5']
for i in platform_title:
    platform = Platform(title = i)
    platform.save()

publisher_title=['Nintendo', 'microsoft', 'take_two', 'sony_company', 'activision', 'ubisoft', 'sega','atari', 'shooter', 'electronic']
for i in publisher_title:
    publisher = Publisher(title=i)
    publisher.save()

Genre_title=['Sports', 'Platform', 'racing', 'Pole-Playing', 'Puzzle', 'Misc', 'action','shooter', 'fighting', '505_games']
for i in Genre_title:
    genre = Genre(title=i)
    genre.save()

content_title=['Sports', 'Platform', 'racing', 'Pole-Playing', 'Puzzle', 'Misc', 'action','shooter', 'fighting', '505_games']
age_limit=[8, 9, 10, 12, 7, 14, 17, 18, 5, 19]
descriptions=['gfdhbsgdvfh', 'vgef', 'wuvshfd', 'gsvdfh', 'ugwvjhf', 'uwgevjhdfb', 'rsgjvdfh', 'jtbhf', 'jhgdsfj', 'jbsbdf']
for (a,b,c) in zip(content_title, age_limit, descriptions):
    cont=ContentRating(title=a, ageLimit=b, description=c)
    cont.save()

product=Products(title="gta5", description="hghgh", 
        platform=Platform.objects.get(id=5),
        relaeseDate='2005-12-1',
        publisher=Publisher.objects.get(id=2), price=1550, 
        contentrating=ContentRating.objects.get(id=3), 
        genre=Genre.objects.get(id= 1), isAvaible=True)
product.save()





platform = Platform.objects.get(id=3)
print(platform.__dict__)

prod=Products(title = "Need for speed", 
              description = "smthing about game", 
              platform=Platform.objects.get(id=1),
              relaeseDate='2016-11-17', publisher=Publisher.objects.get(id=2),
              price=2500, contentrating=ContentRating.objects.get(id=2), genre=Genre.objects.get(id=2),
              isAviable = False)
prod.save()

prod=Products(title = "GTA |V", 
              description = " series of games that incorporate driving and action gameplay styles", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2015-6-26', publisher=Publisher.objects.get(id=1),
              price=2500, contentrating=ContentRating.objects.get(id=3), genre=Genre.objects.get(id=3),
              isAviable = True)
prod.save()

prod=Products(title = "GTA |||", 
              description = " series of games that incorporate driving and action gameplay styles", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2014-10-27', publisher=Publisher.objects.get(id=1),
              price=2500, contentrating=ContentRating.objects.get(id=4), genre=Genre.objects.get(id=3),
              isAviable = True)
prod.save()

prod=Products(title = "GTA ||", 
              description = " series of games that incorporate driving and action gameplay styles", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2014-10-27', publisher=Publisher.objects.get(id=1),
              price=1500, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=3),
              isAviable = False)
prod.save()

prod=Products(title = "GTA san andreas", 
              description = " series of games that incorporate driving and action gameplay styles", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2009-10-20', publisher=Publisher.objects.get(id=1),
              price=1500, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=3),
              isAviable = True)
prod.save()

prod=Products(title = "GTA Vice city", 
              description = " series of games that incorporate driving and action gameplay styles", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2008-9-5', publisher=Publisher.objects.get(id=1),
              price=1500, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=3),
              isAviable = False)
prod.save()

prod=Products.objects.bulk_create([
    Products(title = "Super mario", 
              description = " Mario is always bright and cheerful and instantly recognizable with his blue overalls, red cap, and trademark moustache.", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2010-10-27', publisher=Publisher.objects.get(id=2),
              price=1500, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=10),
              isAviable = True),
    Products(title = "Super mario land", 
              description = " Mario is always bright and cheerful and instantly recognizable with his blue overalls, red cap, and trademark moustache.", 
              platform=Platform.objects.get(id=2),
              relaeseDate='2011-10-27', publisher=Publisher.objects.get(id=2),
              price=1500, contentrating=ContentRating.objects.get(id=4), genre=Genre.objects.get(id=10),
              isAviable = True),
    Products(title = "mario cart ds", 
              description = " Mario is always bright and cheerful and instantly recognizable with his blue overalls, red cap, and trademark moustache.", 
              platform=Platform.objects.get(id=5),
              relaeseDate='2010-10-27', publisher=Publisher.objects.get(id=2),
              price=1500, contentrating=ContentRating.objects.get(id=1), genre=Genre.objects.get(id=3),
              isAviable = True),
])

prod.save()

prod=Products.objects.bulk_create([
    Products(title = "Fifa 10", 
              description = " football game.", 
              platform=Platform.objects.get(id=7),
              relaeseDate='2009-10-27', publisher=Publisher.objects.get(id=3),
              price=1500, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=1),
              isAviable = True),
    Products(title = "Fifa 11", 
              description = " football game.", 
              platform=Platform.objects.get(id=7),
              relaeseDate='2010-10-27', publisher=Publisher.objects.get(id=3),
              price=1500, contentrating=ContentRating.objects.get(id=2), genre=Genre.objects.get(id=1),
              isAviable = True),
    Products(title = "Fifa 12", 
              description = " football game.", 
              platform=Platform.objects.get(id=7),
              relaeseDate='2011-10-27', publisher=Publisher.objects.get(id=3),
              price=1500, contentrating=ContentRating.objects.get(id=2), genre=Genre.objects.get(id=1),
              isAviable = True),
    Products(title = "Fifa 13", 
              description = " football game.", 
              platform=Platform.objects.get(id=1),
              relaeseDate='2012-10-27', publisher=Publisher.objects.get(id=3),
              price=1500, contentrating=ContentRating.objects.get(id=4), genre=Genre.objects.get(id=1),
              isAviable = True),
    Products(title = "Fifa 14", 
              description = " football game.", 
              platform=Platform.objects.get(id=1),
              relaeseDate='2013-10-27', publisher=Publisher.objects.get(id=3),
              price=1500, contentrating=ContentRating.objects.get(id=2), genre=Genre.objects.get(id=1),
              isAviable = True),
])
prod.save()
prod=Products.objects.bulk_create([
    Products(title = "Call of duty black ops 3", 
              description = " strike game.", 
              platform=Platform.objects.get(id=7),
              relaeseDate='2012-01-25', publisher=Publisher.objects.get(id=5),
              price=1000, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=8),
              isAviable = True),
    Products(title = "Call of duty black ops 2", 
              description = " strike game.", 
              platform=Platform.objects.get(id=5),
              relaeseDate='2014-05-27', publisher=Publisher.objects.get(id=5),
              price=1700, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=8),
              isAviable = False),
    Products(title = "Call of duty modern warfar 2", 
              description = " strike game.", 
              platform=Platform.objects.get(id=6),
              relaeseDate='2017-04-27', publisher=Publisher.objects.get(id=5),
              price=2450, contentrating=ContentRating.objects.get(id=1), genre=Genre.objects.get(id=8),
              isAviable = False),
    Products(title = "Call of duty modern warfar 3]", 
              description = " strike game.", 
              platform=Platform.objects.get(id=7),
              relaeseDate='2018-05-27', publisher=Publisher.objects.get(id=5),
              price=3580, contentrating=ContentRating.objects.get(id=4), genre=Genre.objects.get(id=8),
              isAviable = True),
    Products(title = "Call of duty 5", 
              description = " strike game.", 
              platform=Platform.objects.get(id=5),
              relaeseDate='2019-06-24', publisher=Publisher.objects.get(id=5),
              price=1500, contentrating=ContentRating.objects.get(id=5), genre=Genre.objects.get(id=8),
              isAviable = True)
])
prod.save()

prod=Products.objects.bulk_create([
    Products(title = "Medal of Honor: frontline", 
              description = "that game is about war.", 
              platform=Platform.objects.get(id=4),
              relaeseDate='2014-01-25', publisher=Publisher.objects.get(id=6),
              price=2500, contentrating=ContentRating.objects.get(id=3), genre=Genre.objects.get(id=8),
              isAviable = True),
    Products(title = "Uncharted 3: Drake's Deception", 
              description = "Set two years after Among Thieves (2009), the single-player story follows", 
              platform=Platform.objects.get(id=6),
              relaeseDate='2007-04-25', publisher=Publisher.objects.get(id=6),
              price=3790, contentrating=ContentRating.objects.get(id=8), genre=Genre.objects.get(id=5),
              isAviable = False),    

    Products(title = "Crush bandicoot", 
              description = "The game's premise chronicles the creation of the titular Crash, a bandicoot who has been uplifted by the mad scientist Doctor Neo Cortex. ", 
              platform=Platform.objects.get(id=10),
              relaeseDate='2005-08-25', publisher=Publisher.objects.get(id=6),
              price=1650, contentrating=ContentRating.objects.get(id=9), genre=Genre.objects.get(id=2),
              isAviable = True), 
    Products(title = "Left 4 dead 2", 
              description = "Game is about zombies ", 
              platform=Platform.objects.get(id=9),
              relaeseDate='2011-08-25', publisher=Publisher.objects.get(id=6),
              price=5000, contentrating=ContentRating.objects.get(id=9), genre=Genre.objects.get(id=2),
              isAviable = True), 
    Products(title = "gears of war", 
              description = "game is about war", 
              platform=Platform.objects.get(id=7),
              relaeseDate='2017-08-25', publisher=Publisher.objects.get(id=6),
              price=4800, contentrating=ContentRating.objects.get(id=9), genre=Genre.objects.get(id=2),
              isAviable = True)
])
prod.save()
prod=Products.objects.bulk_create([
    Products(title = "Assasin's Creed V", 
              description = "that game is about war.", 
              platform=Platform.objects.get(id=1),
              relaeseDate='2011-01-25', publisher=Publisher.objects.get(id=7),
              price=2600, contentrating=ContentRating.objects.get(id=6), genre=Genre.objects.get(id=6),
              isAviable = True)
])
prod.save()

prod=Products.objects.bulk_create([
    Products(title = "splatoon 2", 
              description = "Splatoon is a third-person shooter developed and published by Nintendo", 
              platform=Platform.objects.get(id=10),
              relaeseDate='2017-03-01', publisher=Publisher.objects.get(id=8),
              price=2810, contentrating=ContentRating.objects.get(id=7), genre=Genre.objects.get(id=6),
              isAviable = False)
])

prod.save()
prod=Products.objects.bulk_create([
    Products(title = "Battlefield 3 ", 
              description = " game is about war", 
              platform=Platform.objects.get(id=10),
              relaeseDate='2019-11-29', publisher=Publisher.objects.get(id=10),
              price=4890, contentrating=ContentRating.objects.get(id=7), genre=Genre.objects.get(id=10),
              isAviable = True)
])
prod.save()
