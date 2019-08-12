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

def xunfollow():
    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text"
        "='ranksea Unfollower WEDNESDAY Started @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=5000, allFollowing=True,
                                   style="RANDOM", unfollow_after=3 * 60 * 60,
                                   sleep_delay=200)

        except Exception:
            print(traceback.format_exc())

    requests.get(
        "https://api.telegram.org/bot439604565:AAE3K9FIReY512NNgb1GryjhdX35L_2RDYw/sendMessage?chat_id=505840575&text"
        "='ranksea Unfollower WEDNESDAY Stopped @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))


# schedulers
# schedule.every().day.at("09:30").do(follow)
# schedule.every().day.at("13:30").do(follow)
# schedule.every().day.at("17:30").do(follow)

# schedule.every().day.at("00:05").do(unfollow)
xunfollow();

# schedule.every().wednesday.at("03:00").do(xunfollow)

while True:
    schedule.run_pending()
    time.sleep(1)