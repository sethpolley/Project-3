import os.path
import urllib.request

# import modules

done_variable = 0

# define variable that needs to be = 1 for the program to end

total_requests = 0

# define total requests variable

total_request_period = 0

# define total requests for the 6 month period
while done_variable == 0:

    if os.path.isfile('http_access_log.txt'):
        with open('http_access_log.txt', 'r') as http_info:
            lines = http_info.readlines()
        for i in lines:
            if i.find('Oct/1995') != -1:
                total_requests += 1
                total_request_period += 1
            elif i.find('Sep/1995') != -1:
                total_requests += 1
                total_request_period += 1
            elif i.find ('Aug/1995') != -1:
                total_requests += 1
                total_request_period += 1
            elif i.find ('Jul/1995') != -1:
                total_requests += 1
                total_request_period += 1
            elif i.find ('Jun/1995') != -1:
                total_requests += 1
                total_request_period += 1
            elif i.find ('May/1995') != -1:
                total_requests += 1
                total_request_period += 1
            elif i.find ('11/Apr/1995') != -1:
                total_requests += 1
                total_request_period += 1
            else:
                total_requests += 1
        done_variable = 1
    else:
        local_copy = 'http_access_log.txt'
        # define log file variable
        local_copy, headers = urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log', local_copy)

        # create local file called 'http_access_log' with data from the URL provided

print('The total requests made in 6 months are:', total_request_period)
print('The total requests made in the log file were:', total_requests)
