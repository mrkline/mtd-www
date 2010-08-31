#!/usr/bin/env python

import sys, getopt, csv, operator

fdout = sys.stdout
head = "header.tmpl"
foot = "footer.tmpl"

# Print the usage information
def usage():
        print "Usage:"
        print "  csvtohtml.py [-f] <source>"
	print "Options:"
	print "  -f		write to file <source.html> instead of stdout"
        return

def csvToHTML(file):
	reader = csv.reader(open(file))
	allbutsize_col = 0
	exception_col = 0
	tmp = open(head, 'r')
	fdout.write(tmp.read())
	tmp.close()
	fdout.write('<table>\n')
	row = reader.next()
	for i in range(len(row)):
		if (row[i] == "All but Size"):
			allbutsize_col = i
		elif (row[i] == "Full Support"):
			exception_col = i
	fdout.write('<thead>\n')
	fdout.write('<tr>')
	for column in row:
		fdout.write('<th>' + column + '</th>')
	fdout.write('</tr>\n')
	fdout.write('</thead>\n')
	sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False)
	sortedlist = sorted(sortedlist, key=operator.itemgetter(5), reverse=False)
	sortedlist = sorted(sortedlist, key=operator.itemgetter(4), reverse=False)
	fdout.write('<tbody>\n')
	for row in sortedlist:
		if (row[exception_col] == "FALSE"):
			if (row[allbutsize_col] == "TRUE"):
				fdout.write('<tr class="wrong-size">')
			else:
				fdout.write('<tr class="exception">')
		else:
			fdout.write('<tr>')
		for column in row:
			fdout.write('<td>' + column + '</td>')
		fdout.write('</tr>\n')
	fdout.write('</tbody>\n')
	fdout.write('</table>\n')
	tmp = open(foot, 'r')
	fdout.write(tmp.read())
	tmp.close()

writefile = 0

try:
        (options, arguments) = getopt.getopt(sys.argv[1:],'f')
except getopt.GetoptError, ex:
        print
        print "ERROR:"
        print ex.msg
        usage()
        sys.exit(1)
        pass

for option, value in options:
        if option == '-f':
                writefile = 1
        pass

if not arguments:
        print "No source file specified"
        usage()
        sys.exit(1)
        pass

if writefile > 0:
        fname = arguments[0].split('.')[0]
        fname = fname + ".html"
        fdout = open(fname, 'w')

csvToHTML(arguments[0])

if writefile > 0:
        fdout.close()
