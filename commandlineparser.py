#!/usr/bin/env python3
# usecase: monitor list of disk partitons and generate
# a report for those that are fuller than specified thershold

# req: accept command line args and 
# options like this 
''' check-partitions --help
 options: 
 - h --help
 -t THRESHOLD --threshold=THRESHOLD
 -s --single just check once, dont loop 
 -m MAILBOX --mailbox=MAILBOX mail report to this mailbox'''

 # use optparse module 
 # argparse

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-t', '--threshold',
                 dest='threshold',
                 type='int',
                 default=90,
                 help='set thershold (%)')
parser.add_option('-s', '--single',
                 action='store_true',
                  dest='singleshot',
                 default=False,
                 help='Just check once, dont loop')
parser.add_option('-m', '--mailbox',
                 dest='mailbox',
                 help='mail report to this mailbox')

(options, args) = parser.parse_args()

print('singleshot is %r' % options.singleshot)
print('mailbox is %s' % options.mailbox)
print('threshold is %d' % options.threshold)
print('non-option argument list is %s' % str(args))



# import sys
# # arg[0]  is used to invoke the prg 
# for arg in sys.argv[1:]:
#     print(arg, end=' ')
# print()