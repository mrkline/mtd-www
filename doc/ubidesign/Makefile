#
# Makefile
#

DOC     = ubidesign.pdf
SRC	= ubidesign.xml ubiboot.xml # reviewinfo.xml
TEX     = $(DOC:.pdf=.tex)
PNG     = ubi_mtd_integration.png scrub_block_in_fs_volume.png \
	nand-headers.png ipl_spl_volumes.png ipl_operations.png

all: $(PNG) $(DOC)

#%.pdf: %.xml
#	docbook-2-pdf  $< || docbook2pdf $<

$(DOC): $(SRC)
	docbook-2-pdf $< || docbook2pdf $<


%.png: %.fig
	fig2dev -L png -m 2 $< $@

clean:
	$(RM) *~ *.old core $(TEX) $(PNG) *.fot *.bak *.jtex \
		*.out *.aux *.log jadetex.cfg

distclean: clean
	$(RM) $(DOC)
