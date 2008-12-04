#
CONV 	= "../html.py"

TARGETS	= misc.html

all: $(TARGETS)

$(TARGETS): %.html: %.xml ../inc/*.tmpl ../menu1.xml menu2.xml
	$(CONV) -f $<

clean:
	rm -f $(TARGETS)
