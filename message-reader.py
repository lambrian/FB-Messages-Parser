import re
import mmap
from collections import defaultdict

THREAD_HEADER = '<div class="thread">'
MESSAGE_HEADER = '<div class="message">'
MESSAGE_AUTHOR_HEADER = '<span class="user">'
MESSAGE_BODY_HEADER = '<p>'
MESSAGE_DATE_HEADER = '<span class="meta">'

'''
Extracts message author and message body
'''
def process_message (f, curr_message_index):
    author_index = (f.find (MESSAGE_AUTHOR_HEADER, curr_message_index) +
    len(MESSAGE_AUTHOR_HEADER))
    body_index = (f.find (MESSAGE_BODY_HEADER, curr_message_index) + len
    (MESSAGE_BODY_HEADER))
    date_index = (f.find (MESSAGE_DATE_HEADER, curr_message_index) + len
    (MESSAGE_DATE_HEADER))
    
    author = f[author_index:f.find ('<', author_index)]
    body = f[body_index:f.find ('<', body_index)]
    date = f[date_index:f.find ('<', date_index)]
    print author, body, date

'''
Given the index of current thread index in file and index of next thread,
all messages in that thread are between these indices
'''
def process_thread_messages (f, curr_thread_index, next_thread_index):
    curr_message_index = f.find(MESSAGE_HEADER, curr_thread_index)
    while curr_message_index < next_thread_index:
        process_message (f, curr_message_index)
        curr_message_index = f.find (MESSAGE_HEADER, curr_message_index + 1)

'''
Processes all message threads
'''
def process_threads (f):
    curr_thread_index = f.find(THREAD_HEADER)
    while curr_thread_index > -1:
        curr_thread_index = curr_thread_index + len (THREAD_HEADER)
        thread_participants = f[curr_thread_index:f.find('<', curr_thread_index)]
        next_thread_index = f.find(THREAD_HEADER, curr_thread_index)
        if thread_participants == 'Jason Teplitz, Brian Lam':
            process_thread_messages (f, curr_thread_index, next_thread_index)
        curr_thread_index = next_thread_index

def main():
    f = open('_messages.htm').read().replace('\n', '')
    process_threads (f)

if __name__ == "__main__":
    main()
