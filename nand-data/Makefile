#
CONV 	= ./csvtohtml.py

TARGETS	= nanddata.html

all: $(TARGETS)

$(TARGETS): %.html: %.csv *.tmpl
	$(CONV) -f $<

clean:
	rm -f $(TARGETS)
