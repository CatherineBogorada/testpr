import sys
for line in sys.stdin:
	ip,userid,country,bannerid,payout=line.strip().split('\t')
    print (country,payout)
