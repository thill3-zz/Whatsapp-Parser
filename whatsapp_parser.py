import pandas as pd
import re
import datetime as dt

text_message_file = open(filename)
file_text = text_message_file.read()

def get_date_from_wa(input_line):
    get_date = re.compile('.*?,')
    date = get_date.match(input_line)
    month, day, year = get_date_parts(date.group())

    year = '20'+year #Note that here 'year' is two digits, so the full year should prepend '20'
    month = month.rjust(2,'0')
    day = day.rjust(2,'0')

    if date:
        return year, month, day
    else:
        return(None)

def get_time_from_wa(input_line):
    get_time = re.compile(',.*?- ')
    time = get_time.search(input_line)

    hour, minute = get_time_parts(time.group())
    hour = hour.rjust(2,'0')
    minute = minute.rjust(2,'0')

    if time:
        return hour, minute
    else:
        return(None)

def get_person_from_wa(input_line):
    person = re.search('- .*?:', input_line)
    if person:
        return person.group()
    else:
        return(None)

def get_message_text_from_wa(input_line):
    try:
        get_message = re.compile(': .*$')
        message_text = get_message.search(input_line)
        message_text = message_text.group()
        message_text = message_text[2:]
    except:
        get_message = re.compile('- .*$')
        message_text = get_message.search(input_line)
        message_text = message_text.group()
    return(message_text)

def get_date_parts(input_date):
    return re.findall(r"[\w']+", input_date)

def get_time_parts(input_time):
    return re.findall(r"[\w']+", input_time)

#Set up the dataframe
cols = ['Current_DT','Time_Diff_in_s', 'Sender', 'Message_Text']
whatsapp_data = pd.DataFrame(columns = cols)

file_lines = file_text.splitlines()
prev_datetime = dt.datetime(year = 1, month = 1, day = 1, hour = 1, minute = 1)
i = 0
progress_interval = 500
start = 0
limit = None

for line in file_lines[start:limit]:
    i += 1

    starts_with_digit = re.compile('^\d/')
    if starts_with_digit.match(line):


        year1, month1, day1 = get_date_from_wa(line)
        year1 = int(year1)
        month1 = int(month1)
        day1 = int(day1)

        hour1, minute1 = get_time_from_wa(line)
        hour1 = int(hour1)
        minute1 = int(minute1)

        curr_dt = dt.datetime(year1, month1, day1, hour1, minute1)

        time_diff = curr_dt - prev_datetime

        try:
            person = get_person_from_wa(line)[2:][:-1]
        except:
            person = 'System'

        message_text = get_message_text_from_wa(line)


    else:
        message_text = line
        time_diff = dt.timedelta(0)
        #print('message: ', message_text)

    new_row = pd.DataFrame([[curr_dt, time_diff.total_seconds(), person, message_text]], columns = cols)
    if i%progress_interval == 0:
        print('count: ', i)
    prev_datetime = curr_dt
    whatsapp_data = whatsapp_data.append(new_row, ignore_index = True)

print('final count: ', i)
print('whatsapp data: ',whatsapp_data)

whatsapp_data.to_csv(r'WhatsApp_Conversation_Parsed.csv', index = False)

print('final count: ', i)
print('whatsapp data: ',whatsapp_data)
