# This bot was created by Reddit user /u/BigBaldSheep
# Please message him with any questions

# Bot version 0.1

# Create a Reddit bot that randomly compliments one user
# It grabs a link from one of the approved subreddits,
# then goes to the comment section. From the first 200 commenters,
# it randomly chooses one. It then comments a random
# compliment. It chooses a comment from a list that I provide.
# The bot then waits 30 minutes before doing this again.

#import statements
import praw
import time
import random

#user agent
user_agent = ("Random Compliments: 0.1: by /u/BigBaldSheep"
              "inset github here")

#login to reddit
r = praw.Reddit(user_agent = user_agent)
#r.login('bot_username', 'bot_password') #depricated, fix

#create a list of the things already commented on
#Note, this will only be current for as long as the bot is running
already_commented = [] #ignore for now

#create a list of the approved subreddits
#this will contain the list of randomly chosed subs
approved_subreddits = ['all'] #ignore for now

#get the list of compliments from my text file
compliment_list = open("compliments.txt").readlines()

def get_random_submission(submission, limit):
    #get random integer, used to grab from generator
    rand_num = random.randrange(0,limit)

    #loop through the generator, until hitting random number
    #note, this is not efficients, has too many calls to the generator
    #fix on future update
    for i in range(limit):
        sub = next(submission)
        if i == rand_num:
            return sub

# Begin main loop
#while True:
    # grab the compliment we plan on using
    compliment = "So I just want you to know that " + random.choice(compliment_list) + "\n\nI'm a bot, version 0.1. Message /u/BigBaldSheep for info"

    #randomly choose a sub to go to
    chosen_sub = random.choice(approved_subreddits)

    #grab the top list of inputs for the subs
    submissions = r.get_subreddit(chosen_sub).get_top(limit=15) #grab top 15

    # get the random submission from the list
    submission = get_random_submission(submissions, 15)

    # randomly choose a comment and compliment, if the post doesn't already have a compliment
    if submission not in already_commented:
        random.choice(sub.comments).reply(compliment)
        already_commented.append(submission)
    
    #sleep for 30 minutes
    time.sleep(1800)
