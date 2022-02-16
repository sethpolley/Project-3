import urllib.request

# import module 
local_copy = 'http_access_log'
# define log file variable

local_copy, headers = urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log', local_copy)

# create local file called 'http_access_log' with data from the URL provided
