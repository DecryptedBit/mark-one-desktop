from abc import abstractmethod

from src.converters.base_converter import BaseConverter

from_types = [
    ("commonmark", "CommonMark Markdown"),
    ("creole", "Creole 1.0"),
    ("csv", "CSV table"),
    ("docbook", "DocBook"),
    ("docx", "Word docx"),
    ("dokuwiki", "DokuWiki markup"),
    ("epub", "EPUB"),
    ("fb2", "FictionBook2 e - book"),
    ("gfm", "GitHub - Flavored Markdown"),
    ("haddock", "Haddock markup"),
    ("html", "HTML"),
    ("ipynb", "Jupyter notebook"),
    ("jats", "JATS XML"),
    ("jira", "Jira wiki markup"),
    ("json", "JSON"),
    ("latex", "LaTeX"),
    ("markdown", "Pandoc’s Markdown"),
    ("markdown_mmd", "MultiMarkdown"),
    ("markdown_phpextra", "PHP Markdown Extra"),
    ("markdown_strict", "original unextended Markdown"),
    ("mediawiki", "MediaWiki markup"),
    ("man", "roff man"),
    ("muse", "Muse"),
    ("native", "native Haskell"),
    ("odt", "ODT"),
    ("opml", "OPML"),
    ("org", "Emacs Org mode"),
    ("rst", "reStructuredText"),
    ("t2t", "txt2tags"),
    ("textile", "Textile"),
    ("tikiwiki", "TikiWiki markup"),
    ("twiki", "TWiki markup"),
    ("vimwiki", "Vimwiki")
]

to_types = [
    ("asciidoc", "AsciiDoc"),
    ("beamer", "LaTeX beamer slide show"),
    ("commonmark", "CommonMark Markdown"),
    ("context", "ConTeXt"),
    ("docbook4", "DocBook 4"),
    ("docbook5", "DocBook 5"),
    ("docx", "Word docx"),
    ("dokuwiki", "DokuWiki markup"),
    ("epub3", "EPUB v3 book"),
    ("epub2", "EPUB v2"),
    ("fb2", "FictionBook2 e - book"),
    ("gfm", "GitHub - Flavored Markdown"),
    ("haddock", "Haddock markup"),
    ("html5", "HTML5 / XHTML polyglot markup"),
    ("html4", "XHTML 1.0 Transitional"),
    ("icml", "InDesign ICML"),
    ("ipynb", "Jupyter notebook"),
    ("jats_archiving", "JATS XML, Archiving and Interchange Tag Set"),
    ("jats_articleauthoring", "JATS XML, Article Authoring Tag Set"),
    ("jats_publishing", "JATS XML, Journal Publishing Tag Set"),
    ("jats", "alias for jats_archiving"),
    ("jira", "Jira wiki markup"),
    ("json", "JSON version of native AST"),
    ("latex", "LaTeX"),
    ("man", "roff man"),
    ("markdown", "Pandoc’s Markdown"),
    ("markdown_mmd", "MultiMarkdown"),
    ("markdown_phpextra", "PHP Markdown Extra"),
    ("markdown_strict", "original unextended Markdown"),
    ("mediawiki", "MediaWiki markup"),
    ("ms", "roff ms"),
    ("muse", "Muse"),
    ("native", "native Haskell"),
    ("odt", "OpenOffice text document"),
    ("opml", "OPML"),
    ("opendocument", "OpenDocument"),
    ("org", "Emacs Org mode"),
    ("pdf", "PDF"),
    ("plain", "plain text"),
    ("pptx", "PowerPoint slide show"),
    ("rst", "reStructuredText"),
    ("rtf", "Rich Text Format"),
    ("texinfo", "GNU Texinfo"),
    ("textile", "Textile"),
    ("slideous", "Slideous HTML and JavaScript slide show"),
    ("slidy", "Slidy HTML and JavaScript slide show"),
    ("dzslides", "DZSlides HTML5 + JavaScript slide show"),
    ("revealjs", "reveal.js HTML5 + JavaScript slide show"),
    ("s5", "S5 HTML and JavaScript slide show"),
    ("tei", "TEI Simple"),
    ("xwiki", "XWiki markup"),
    ("zimwiki", "ZimWiki markup")
]


class PandocConverter(BaseConverter):
    @staticmethod
    def get_name():
        return "Pandoc"

    @staticmethod
    def get_from_types():
        return from_types

    @staticmethod
    def get_to_types():
        return to_types

    def __init__(self, from_type_index, to_type_index):
        self.set_from_type(from_type_index)
        self.set_to_type(to_type_index)

    def convert(self, content):
        return "Not working yet"

    def set_from_type(self, from_type_index):
        self.from_type = self.get_from_types()[from_type_index]

    def get_from_type(self):
        return self.from_type

    def set_to_type(self, to_type_index):
        self.to_type = self.get_to_types()[to_type_index]

    def get_to_type(self):
        return self.to_type
