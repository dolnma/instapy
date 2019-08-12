import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'dollysdev'
insta_password = 'Oo8ApySJHc69Qcha'

# set 
# headless_browser=True 
# if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True,
                  nogui=True)
def Job():
    try:
        session.login()

        # settings
        session.set_relationship_bounds(enabled=True,
                    potency_ratio=-1.21,
                    delimit_by_numbers=True,
                    max_followers=4590,
                        max_following=5555,
                        min_followers=10,
                        min_following=10)
        session.set_user_interact(amount=4,
				 percentage=50,
                  randomize=True,
                   media='Photo')
        session.set_do_comment(True, percentage=80)
        session.set_do_follow(True, percentage=80)
        session.set_comments(['That is cool! \u270A', 'Wow! :) :heart_eyes:', ':heart_eyes: :heart_eyes: :heart_eyes:' , ':+1: :punch:', 'Seems good :pray: :pray:', ':pray:', 'cool :wink:', ':thumbsup:', 'i like it :thumbsup: :thumbsup:', ':muscle:'])

        # actions
        for cycle in range(20):
            print("\n\nLOOP {}\n".format(cycle+1))
            session.like_by_tags(['webdesign', 'coding', 'javascript', 'webdev'], amount=20)
            session.interact_user_followers(['worldcode', 'creativroom', 'thebeeest'], amount=20, randomize=True)
            # session.unfollow_users(amount=200, allFollowing=True, style="FIFO", unfollow_after=1, sleep_delay=0)
            # time.sleep(50)   #take a 50 seconds of break after finishing the feature above
            # session.unfollow_users(amount=60, InstapyFollowed=(True), style="FIFO", sleep_delay=501)
            # session.unfollow_users(amount=40, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=450)
            # time.sleep(30)   #take some more break after finishing unfollows
            # time.sleep(60)
            # session.follow_by_tags(['webdesign', 'coding', 'frontend'], amount=30)

    except Exception as exc:
        # if changes to IG layout, upload the file to help us locate the change
        if isinstance(exc, NoSuchElementException):
            file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            with open(file_path, 'wb') as fp:
                fp.write(session.browser.page_source.encode('utf8'))
            print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
                '*' * 70, file_path))
        # full stacktrace when raising Github issue
        raise
        # pass

    finally:
        # end the bot session
        # session.end()
        Job()

Job()