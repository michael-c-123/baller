# baller

a tool to help us say "we ball"

runs on selenium python using google chrome webdriver (chromium)

put in PATH: https://sites.google.com/chromium.org/driver/


## Usage

```
we ball

positional arguments:
  username
  password

options:
  -h, --help            show this help message and exit
  --match-type {1,2}, -m {1,2}
                        1 singles, 2 doubles
  --date DATE, -d DATE  date in MM/DD/YYYY
  --times START END, -t START END
                        times in ?H:mm XM
  --court COURT, -c COURT
                        court 1-8
  --wait, --no-wait     debug flag to wait for registration time (default:
                        True)
  --submit, --no-submit
                        debug flag to submit reservation request (default:
                        True)
  --close, --no-close   debug flag to close webdriver at end (default: True)
```

Example:
```
python3 browser_script.py \
'username' \
'password' \
-d '01/01/2022' \
-t '8:00 AM' '10:00 AM' \
-c 2
```
