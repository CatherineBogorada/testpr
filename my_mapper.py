#! /usr/bin/env python

import sys
for line in sys.stdin:
	ip,userid,country,bannerid,payout=line.strip().split('\t')
	print >>sys.stdout,"%s\t%d" % (country,payout)
