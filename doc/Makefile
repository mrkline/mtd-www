#
CONV 	= "../html.py"

TARGETS	= general.html jffs2.html ubifs.html nand.html logfs.html \
	ubi.html git.html onenand.html

all: $(TARGETS)

$(TARGETS): %.html: %.xml ../inc/*.tmpl ../menu1.xml menu2.xml
	$(CONV) -f $<

clean:
	rm -f $(TARGETS)
