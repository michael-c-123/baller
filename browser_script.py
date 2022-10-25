
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import argparse
import datetime, time
import re

now = datetime.datetime.now()
READY_TIME = datetime.datetime(now.year, now.month, now.day, 8, 44, 30)
FIRE_TIME = datetime.datetime(now.year, now.month, now.day, 8, 45, 1)

parser = argparse.ArgumentParser(description='we ball')
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('--date', '-d', help='date in MM/DD/YYYY', required=True)
parser.add_argument('--times', '-t', help='times in ?H:mm XM', nargs=2, metavar=('START', 'END'), required=True)
parser.add_argument('--court', '-c', help='court 1-8', type=int, choices=range(1,9), metavar='COURT', required=True)
parser.add_argument('--match-type', '-m', type=int, choices=[1,2], default=2, help='1 singles, 2 doubles (default: 2)')
parser.add_argument('--wait', action=argparse.BooleanOptionalAction, default=True, help='debug flag to wait for registration time')
parser.add_argument('--submit', action=argparse.BooleanOptionalAction, default=True, help='debug flag to submit reservation request')
parser.add_argument('--close', action=argparse.BooleanOptionalAction, default=True, help='debug flag to close webdriver at end')
args = parser.parse_args()

args_good = False
if not re.search(r'\d\d/\d\d/\d\d\d\d', args.date):
    print('date in MM/DD/YYYY')
elif not re.search(r'1?\d:\d\d [AP]M', args.times[0]):
    print('times in ?H:mm XM')
elif not re.search(r'1?\d:\d\d [AP]M', args.times[1]):
    print('times in ?H:mm XM')
else:
    args_good = True
if not args_good:
    quit()

def timestamp():
    return '[{:%H:%M:%S}]'.format(datetime.datetime.now())

if args.wait:
    now = datetime.datetime.now()
    sleep = (READY_TIME - now).seconds
    print(f'{timestamp()} WAITING FOR {str(datetime.timedelta(seconds=sleep))}', flush=True)
    time.sleep(sleep)

options = Options()
options.headless = args.wait and args.submit and args.close
try:
    print(f'{timestamp()} LAUNCHING BROWSER', flush=True)
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 120)

    driver.get('https://www.10sportal.com/club/login/caswell-tennis-center/')

    desktop_button = driver.find_element(By.ID, 'appVersion')
    desktop_button.click()

    username_field = wait.until(
        EC.presence_of_element_located((By.ID, 'j_username'))
    )
    password_field = driver.find_element(By.ID, 'j_password')

    username_field.send_keys(args.username)
    password_field.send_keys(args.password)

    login = driver.find_element(By.XPATH, '//*[@id="loginform"]/fieldset/input[2]')
    wait.until(ready_to_fire)
    login.click()

    wait.until(
        EC.presence_of_element_located((By.ID, 'user-bar'))
    )

    if args.wait:
        print(f'{timestamp()} WAITING TO FIRE', flush=True)
        ready_to_fire = lambda _: datetime.datetime.now() >= FIRE_TIME
        wait.until(ready_to_fire)
    print(f'{timestamp()} FIRING', flush=True)
    driver.get('https://www.10sportal.net/entity/scheduler/index.html')

    match_type = Select(
        wait.until(
            EC.presence_of_element_located((By.NAME, 'listMatchTypeID'))
        )
    )
    appt_date = driver.find_element(By.NAME, 'apptDate')
    start_time = driver.find_element(By.NAME, 'startTime')
    end_time = driver.find_element(By.NAME, 'endTime')
    court = Select(driver.find_element(By.NAME, 'court'))
    submit = driver.find_element(By.NAME, 'submit')

    match_type.select_by_value(str(args.match_type))
    appt_date.send_keys(Keys.CONTROL, 'a')
    appt_date.send_keys(Keys.BACKSPACE)
    appt_date.send_keys(args.date)
    appt_date.send_keys(Keys.ESCAPE)
    start_time.send_keys(args.times[0])
    start_time.send_keys(Keys.ESCAPE)
    end_time.send_keys(args.times[1])
    end_time.send_keys(Keys.ESCAPE)
    court.deselect_by_value('0')
    court.select_by_value(str(225 + args.court))
    
    if args.submit:
        submit.click()
    print(f'{timestamp()} DONE', flush=True)
finally:
    if args.close and args.submit:
        driver.close()  