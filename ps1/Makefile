MAIN = ps1
SRC =
COVER =
BIB = bible

LATEX=rubber -f --pdf --synctex -s
XELATEX=rubber -f --pdf --synctex -s --module xelatex
BUILD=$(LATEX)

DEPENDS = $(MAIN).tex
ifneq ($(SRC),)
	DEPENDS += $(wildcard $(SRC)/*.tex)
endif
ifneq ($(COVER),)
	DEPENDS += $(COVER).tex
endif
ifneq ($(BIB),)
	DEPENDS += $(BIB).bib
endif

all: $(MAIN).pdf

%.pdf: %.tex $(DEPENDS)
	$(BUILD) $<
	rubber-info --check $<

clean:
	rubber --clean $(DEPENDS)
	rm -f $(MAIN).pdf

.PHONY : all clean
