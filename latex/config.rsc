% Arquivo de configuracion de bibtool. Permite arreglar arquivos *.bib
% formateandoos de maneira que teñan claves únicas, indentacións correctas, etc.
% Bibtool non recoñece .config/ asique na miña .bashrc poño:
% export BIBTOOLRSC="$HOME/.config/bibtool/config.rsc"

resource                 = {braces}   % Estas extensións deberían vir ca distro
resource                 = {improve}  % de bibtool
resource                 = {biblatex} %
%resource                = {iso2tex}  % Este non furrula ben
resource                 = {check_y}  %
print.line.length        = 200
print.align.key          = 0
print.align              = 18
print.use.tab            = off
ignored.word             = {of}
ignored.word             = {and}
ignored.word             = {on}
ignored.word             = {to}
ignored.word             = {from}
suppress.initial.newline = on
select.case.sensitive    = off
key.format               = {%+3N(author)_%-5T(title)_%d(year)}
fmt.et.al                = ".etal"
fmt.inter.name           = "."
%fmt.name.name           = "."
%fmt.name.pre            = "."
%fmt.name.title          = ":"
fmt.title.title          = "."
%fmt.word.separator      = "_"
check.double.delete      = off
check.double             = off
key.number.separator     = "__"
key.base                 = digit
