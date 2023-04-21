#This is a program that will choose a random item from your list and output it using cowsay
import random
import cowsay

#You can add your movie titles to this list
movies=['Movie 1',
        'Movie 2',
        'Movie 3',
        ]

random_movie=random.choice(movies)
cowsay.cow(f'You should watch {random_movie}.')