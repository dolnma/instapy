"""
This template is written by @Mehran
What does this quickstart script aim to do?
- My quickstart is just for follow/unfollow users.
NOTES:
- It uses schedulers to trigger activities in chosen hours and also, sends me
  messages through Telegram API.
"""

# -*- coding: UTF-8 -*-
import time
from datetime import datetime
import schedule
import traceback
import requests

from instapy import InstaPy
from instapy import smart_run

insta_username = 'ranksea'
insta_password = 'Ww9zU5l61ldrJKlo'


def get_session():
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      nogui=True,
                      multi_logs=False)

    return session


def follow():
    # Send notification to my Telegram
    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text='ranksea Follower Started @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        counter = 0

        while counter < 5:
            counter += 1

            try:
                # settings
                session.set_relationship_bounds(enabled=True, potency_ratio=1.21)
                session.set_do_comment(enabled=True, percentage=30)
                session.set_comments([
                                        u'What an amazing shot! :heart_eyes: What do '
                                        u'you think of my recent shot?',
                                        u'What an amazing shot! :heart_eyes: I think '
                                        u'you might also like mine. :wink:',
                                        u'Wonderful!! :heart_eyes: Would be awesome if '
                                        u'you would checkout my photos as well!',
                                        u'Wonderful!! :heart_eyes: I would be honored '
                                        u'if you would checkout my images and tell me '
                                        u'what you think. :wink:',
                                        u'This is awesome!! :heart_eyes: Any feedback '
                                        u'for my photos? :wink:',
                                        u'This is awesome!! :heart_eyes:  maybe you '
                                        u'like my photos, too? :wink:',
                                        u'I really like the way you captured this. I '
                                        u'bet you like my photos, too :wink:',
                                        u'I really like the way you captured this. If '
                                        u'you have time, check out my photos, too. I '
                                        u'bet you will like them. :wink:',
                                        u'Great capture!! :smiley: Any feedback for my '
                                        u'recent shot? :wink:',
                                        u'Great capture!! :smiley: :thumbsup: What do '
                                        u'you think of my recent photo?'],
                                    media='Photo')
                session.set_do_like(True, percentage=70)
                session.set_delimit_liking(enabled=True, max=100, min=0)
                session.set_delimit_commenting(enabled=True, max=20, min=0)

                # activity
                session.follow_by_tags(['counterstrike', 'csgo', 'global', 'esports'], amount=10)
                session.like_by_tags(['counterstrike', 'csgo', 'global', 'esports'], amount=300)
                session.unfollow_users(amount=25, allFollowing=True,
                                       style="LIFO",
                                       unfollow_after=3 * 60 * 60,
                                       sleep_delay=450)

            except Exception:
                print(traceback.format_exc())

    # Send notification to my Telegram
    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text='ranksea Follower Stopped @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))


def unfollow():
    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text"
        "='ranksea Unfollower Started @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=600, allFollowing=True,
                                   style="RANDOM", sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text"
        "='ranksea Unfollower Stopped @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))


def xunfollow():
    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text"
        "='InstaPy Unfollower WEDNESDAY Started @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=1000, allFollowing=True,
                                   style="RANDOM", unfollow_after=3 * 60 * 60,
                                   sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text"
        "='InstaPy Unfollower WEDNESDAY Stopped @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))


# schedulers
follow()
schedule.every().day.at("07:40").do(follow)
schedule.every().day.at("11:30").do(follow)
schedule.every().day.at("13:30").do(follow)
schedule.every().day.at("17:30").do(follow)
schedule.every().day.at("19:05").do(follow)
schedule.every().day.at("22:17").do(follow)

schedule.every().day.at("00:05").do(unfollow)

# schedule.every().wednesday.at("03:00").do(xunfollow)

while True:
    schedule.run_pending()
    time.sleep(1)