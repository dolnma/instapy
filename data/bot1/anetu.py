import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'anettfryms'
insta_password = 'alfa123456'

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
                        min_followers=45,
                        min_following=77)
        session.set_user_interact(amount=4,
				 percentage=50,
                  randomize=True,
                   media='Photo')
        session.set_do_comment(True, percentage=20)
        session.set_do_follow(True, percentage=80)
        session.set_comments(['That is cool! \u270A', 'So much fun!!', 'Nice!!' , 'Well done! :)', 'Good job! :))'])

        # actions
        for cycle in range(20):
            print("\n\nLOOP {}\n".format(cycle+1))
            session.unfollow_users(amount=200, allFollowing=True, style="FIFO", unfollow_after=0, sleep_delay=0)

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