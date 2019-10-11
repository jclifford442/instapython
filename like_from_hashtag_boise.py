# !/usr/bin/python2.7

import argparse
import os
import sys
import random
from instapy import InstaPy
from instapy import smart_run

sys.path.append(os.path.join(sys.path[0], "../"))

#Takes arguments from command line
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")

args = parser.parse_args()

#Logs in
session = InstaPy(username=args.u, password=args.p,
                  proxy_address=args.proxy,
                  headless_browser=True)

# let's go! :>
with smart_run(session):
    hashtags = ['boisemodel', 'boiseidaho', 'boiseriver']

    # hashtags = ['boiseidaho', 'boise', 'boisefoothills',
    #             'boisestate',
    #             'boiseries', 'boiserie', 'boiseriver',
    #             'boiseartist', 'boiselife',
    #             'boisebucketlist', 'downtownboise', 'visitboise',
    #             'thisisboise',
    #             'bo', 'travelyoga', 'travelgram', 'sunsetporn',
    #             'lonelyplanet',
    #             'igtravel', 'instapassport', 'travelling', 'instatraveling',
    #             'travelingram',
    #             'mytravelgram', 'skyporn', 'traveler', 'sunrise',
    #             'sunsetlovers', 'travelblog',
    #             'sunset_pics', 'visiting', 'ilovetravel',
    #             'photographyoftheday', 'sunsetphotography',
    #             'explorenature', 'landscapeporn', 'exploring_shotz',
    #             'landscapehunter', 'colors_of_day',
    #             'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
    #             'thegreatoutdoors']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=40, times=1)
    session.set_do_comment(enabled=True, percentage=30)
    session.set_comments([
                             u'What an amazing shot!',
                             u'stuck_out_tongue_winking_eye:',
                             u':musical_note: :musical_note:',
                             u'This is awesome!! :heart_eyes:',
                             u'Great shot :movie_camera:. I '
                             u'bet you like my photos',
                             u'Whoa!! :racehorse:',
                             u'Boise!! :fire:'],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d"],
                                 sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=21,
                                 peak_likes_daily=101,
                                 peak_comments_hourly=6,
                                 peak_comments_daily=31,)

    session.set_user_interact(amount=1, randomize=False, percentage=40)

    # activity
    session.like_by_tags(my_hashtags, amount=60, media=None)
    session.unfollow_users(amount=94, instapy_followed_enabled=True, instapy_followed_param="all", style="RANDOM",
                           unfollow_after=48 * 60 * 60, sleep_delay=602)
    # session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
    #                        style="FIFO", unfollow_after=24 * 60 * 60,
    #                        sleep_delay=501)

