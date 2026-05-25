from time import time
from time import strftime
from time import localtime

print(f"Seconds since January 1, 1970: {time():,.4f} or \
    {time():.2e} in scientific notation")
print(strftime("%b %d %Y", localtime()))
