import sys, urllib2

try:
	urllib2.urlopen(sys.argv[1])
except IndexError:
	print "Argument missing"
	sys.exit(1)
except urllib2.URLError:
	print "Impossible to load URL"
	sys.exit(1)
except ValueError:
	print "Unknown URL format"
	sys.exit(1)
except Exception, e:
	print e
	sys.exit(1)
	
print "The URL is valid"