% Esta é unha clase que contén os paquetes, formatos e configuracións
% principales que uso nos meus apuntes (privados). Para usalo solo hai que
% poñer este arquivo no mesmo directorio que o documento principal e cargalo
% con \documentclass{apuntes}. A clase esta está chea de opcións comentadas
% para telas aquí presentes no caso de querer usalas


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{apuntes}[2024/09/02 Clase das memorias de Deivis]

% Usar a clase libro como base
\LoadClass[11pt,a4paper]{book}


% IDIOMA =======================================================================
\RequirePackage[galician]{babel} % usar galego (como debe ser)

% Para desactivar o sistema de abreviacións, que conflite cas comas decimales
% e en concreto cas opcions de 'siunitx'. Tamén se podería usar \decimalcomma,
% \decimalpoint ou \galiciandecimal{.}, pero eso solo determinaría qué simbolo
% usar en concreto. Eu quero desactivar a funcionalidade por completo
\renewcommand\shorthandsgalician{}

% Usar babel pode fastidiar as citas con biblatex, asique hai que usar 'csquotes'
\RequirePackage{csquotes}


% XEOMETRÍA DO DOCUMENTO =======================================================
\RequirePackage[
% xeral ---------------------------------------------------------
    paper          = a4paper, % tamaño do papel
    % landscape      = false,   % orientación do papel
    % portrait       = true,    % outra maneira de dar a orientacion
    % layout         = a6paper, % area útil, independente do tamaño do papel
    % layouthoffset  = 10mm,    % desplazamento independente do papel
    % layoutvoffset  = 10mm,    % tamaños independentes
    % layoutwidth    = 150mm,   % (non sei como explicar qué fan XD)
    % layoutheight   = 190mm,   %
% marxes do corpo -----------------------------------------------
    top            = 25mm,  % marxe superior
    left           = 20mm,  % marxe esquerdo
    right          = 30mm,  % marxe dereito
    bottom         = 25mm,  % marxe inferior
% notas ao marxe ------------------------------------------------
    marginparsep   = 6mm,     % separacion co corpo
    marginparwidth = 15mm,    % grosor
    % nomarginpar    = true,    % desactivar notas no marxe (tamaño 0)
% encabezado ----------------------------------------------------
    headsep        = 9mm,   % separación co corpo
    headheight     = 10mm,  % grosor
    % nohead         = true,  % desactivar o encabezado
% pe de paxina --------------------------------------------------
    footnotesep    = 10mm,  % separacion corpo inferior e parte superior do pe de paxina
    footskip       = 15mm,  % separacion corpo inferior e parte inferior do do pe de paxina
    % nofoot         = true,  % desactivar o pe de paxina
% incluir encabezados e pes de paxina no corpo do documento -----
    % includehead,
    % includefoot,
    % includemp,
% debug ---------------------------------------------------------
    % showframe,  % mostra estructura
    % showcrop,   % mostrar tamaño útil (ver opcions layout=xxx)
    % pass        % desactivar todo excepto showframe
]{geometry}

% FORMAS E TAL =================================================================

% Para crear un cadro con texto dentro to guapo
% \RequirePackage{framed}

% Pa definir cores e toda a vaina.
\RequirePackage{xcolor}
% Opción 'table' pa poder colorear celdas usando \cellcolor

% tamen pa facer fondos, caixas bordes e tal
\RequirePackage{tcolorbox}


% MATES BASICAS ================================================================

% Matemáticas xerais. Inclue amsmath
\RequirePackage{mathtools}

% Colección extendida de símbolos matemáticos. Inclue amsfonts
\RequirePackage{amssymb}

% creación de estructuras tipo teoremas, definicións, etc.
\RequirePackage{amsthm}

% Estilos para usar nos teoremas, definicións, etc.
\newtheoremstyle{estiloteorema}
    {}{}% espazo encima/abaixo
    {}% tipo de letra do corpo
    {}% indentación
    {}% tipo de letra do encabezado
    {:}% signo de puntuacion logo do encabezado
    {1em}% espaciado logo do encabezado
    {% estructura do encabezado
    \textbf{\underline{\thmname{#1}}}%
    \textbf{\thmnumber{ #2}}%
    \textit{\thmnote{ (#3)}}%
    }

\newtheoremstyle{estilodefinicion}
    {}{}%
    {}%
    {}%
    {}%
    {:}%
    {1em}%
    {% estructura do encabezado
    \textbf{\thmname{#1}}%
    \textbf{\thmnumber{ #2}}%
    \textsc{\thmnote{ (#3)}}%
    }

\theoremstyle{estiloteorema} % usar o estilo para os teoremas
\newtheorem{teorema}{Teorema} % definir o entorno 'teorema'

\theoremstyle{estilodefinicion} % usar o estilo para as definicions
\newtheorem{definicion}{Definición} % definir o entorno 'definicion'

% Agora usamos 'tcolorbox' para colorear o entorno este. Esto redefine o
% entorno que sexa pa que esté coloreado, asique é util non solo para
% teoremas/defs, etc. Recomendado por @egreg
\tcolorboxenvironment{definicion}{
    colback     = blue!7!white, % cor do fondo
    colframe    = black,         % cor do borde
    toprule     = 1pt,         % grosor do borde superior
    bottomrule  = 1pt,         % grosor do borde inferior
    leftrule    = 0pt,         % grosor do borde esquerdo
    rightrule   = 0pt,         % grosor do borde dereito
    % boxrule     = 0pt,         % grosor xeral do borde (top,right.left,bottom)
    left        = 2pt,         % separacion ao borde esquerdo
    right       = 2pt,         % separacion ao borde dereito
    top         = 2pt,         % separacion ao borde superior
    bottom      = 2pt,         % separacion ao borde inferior
    % boxsep      = 1pt,         % separacion xeral (top,right,left,bottom)
    oversize    = 2pt,         % nin idea XD
    sharp corners,             % esquinas afiladas. Pode especificarse cales solo
    % arc         = 2mm,         % curvatura das esquina
    before skip = \topsep,     %
    after skip  = \topsep,     %
}

% o mismo pero pa teoremas
\tcolorboxenvironment{teorema}{
    colback     = red!7!white,
    colframe    = black,
    toprule     = 1pt,
    bottomrule  = 1pt,
    leftrule    = 0pt,
    rightrule   = 0pt,
    % boxrule     = 0pt,
    left        = 2pt,
    right       = 2pt,
    top         = 2pt,
    bottom      = 2pt,
    % boxsep      = 1pt,
    oversize    = 2pt,
    sharp corners,
    % arc         = 2mm,
    before skip = \topsep,
    after skip  = \topsep,
}

% Para DERIVADAS de todo tipo
\RequirePackage{diffcoeff}
%                        sobreescribir
%           orden deriv. orden deriv. (non me acordo como se usa)
%               |           |
% \difx.name.**[orden]<override>{variable(s)}{diferenciando}[pto. eval]
%            ||
%            |funcion antes da derivada
%            funcion despois da derivada
%
% TIPOS:
%   diff, difs, difc    -> normal,inline,operador
%   diffp, difsp, difcp -> igual pero parciales
%   difj                -> jacobiano
%   difl                -> formas diferenciales
% EXEMPLOS:
% \diff{f(x)}{x}                          % normal
% \difs[2]{f(x)}{x}                       % orden 2, inline
% \difc[3]{f(x)}{x}[x=0]                  % orden 3, operador, evaluada nun punto
% \diffp*{f(x)}{x}                        % parcial, diferenciando fora da fracción
% \diff{\sin(x)}{x}[0]^{\mkern-10mu\pi/2} % \mkern para evaluacion superior bonita
%
% \difoverride{a+b-c}            % exponente no numerador
% \diffp[a,b,c]{F(x,y,z)}{a,y,x} % [a,b,c] no denominador

% Para INTEGRALES de todo tipo
\RequirePackage{esint}
% pode usarse a opcion [intlimits] para que os limites da integral estén máis
% arriba/abaixo do normal
% COMANDOS:
% \i{4}nt, \idotsint, \[var]oi{2}nt, \varoi{2}nt, \[var]ointctrclockwise,
% \[var]ointclockwise

% Letras caligraficas moi reviradas, \mathscr
\RequirePackage{mathrsfs}

% Polinomios sinxelos. \polynomial{}, \polynomialfrac{}{}
\RequirePackage{polynomial}


% BIBLIOGRAFÍA =================================================================
\RequirePackage[ % necesario ter instalado 'biber'
    style = alphabetic,
    natbib = true
]{biblatex}
\addbibresource{bibliografia.bib}
% IMPORTANTE:
% A bibliografía suele dar bastante polo cu, polo que hai que tomar precaucións.
% - Usar 'biblatex' en vez de bibtex, para unhas citas mais bonicas e
%   sencillas. Espero subir algo máis detallado neste aspecto no futuro
% - 'biblatex' necesita de 'biber', un programa aparte que noramalmente ven
%   instalado cas distros de latex. UN DETALLE PUÑETERO: hai que ter MOITO
%   coidado cas versions de 'biblatex' e de 'biber', actualizalas por separado
%   pode dar dores de cabeza (podo confirmalo). Checkear ao final da páxina
%   https://biblatex-biber.sourceforge.net/ para a compatibilidade de versións
% - A maiores, sería boa cousa manter unha bibliografía de calidade. Existe
%   'bibtool' que permite formatear arquivos *.bib, ordenalos, xerar nomes das
%   entradas, filtrar por claves, etc. (moi útil, igual subo algún tip desto)


% FIGURAS ======================================================================
% \RequirePackage{graphicx}    % pa facilitar o uso de \includegraphics
% \graphicspath{ {./imaxes/} } % diretorio por defecto das imaxes (comodo)

% \RequirePackage{float}      % permite a colocación 'H' dos floats
% \RequirePackage{subcaption} % para colcar varias imaxes xuntas e tal

% \RequirePackage{transparent} % imaxes transparentes
% \RequirePackage{eso-pic}     % Imaxes encima do texto


% CAPTIONS =====================================================================
% Para cambiar cousas relacionadas cos estilos das figuras, tablas, etc.
\RequirePackage{caption}
% estilos das figuras
\captionsetup[figure]{
    labelfont=bf, % tipografia usada
    % name=Figurilla% % nome
}
\captionsetup[table]{
    labelfont=bf,
    % name=Tabla%
}


% TABLAS =======================================================================
% \RequirePackage{multirow} % tablas con celdas unidas
% \RequirePackage{booktabs} % non e necesario pero aos nerds de Latex gustalle


% UNIDADES =====================================================================
% Para usar unidades e numeros de forma corrrecta e estándar con \num{},
% \unit{}, \qty{}, etc. (coidado, siunitx v.3 \qty conflite con physics \qty)
\RequirePackage{siunitx}
\sisetup{
    output-decimal-marker={.},
    % exponentes ------------------------
    exponent-mode=threshold,
    % exponent-thresholds=-3:2, % non usar exponentes 10^{-2,-1, 0, 1}
    % redondear -------------------------
    % round-mode=figures, % cifras sig
    % round-mode=places, % cantos decimales
    round-mode=uncertainty, % cifras sig da incerteza (necesario usar erro)
    round-precision=2,
    uncertainty-mode = separate,
    print-unity-mantissa=false,
    % unidades --------------------------
    inter-unit-product = \ensuremath{{}\cdot{}}, % separacion entre unidades
    % per-mode=power-positive-first, % so furrula con metodo interpretado puro
    per-mode=symbol, % so furrula con metodo interpretado puro
    inline-per-mode=single-symbol,
    % display-per-mode=fraction,
    list-separator={, },
    list-final-separator={ e },
    list-pair-separator={ e }
}



% ENCABEZADO/PE DE PAXINA =====================================================

% Pa facilitar a creacion cun par de comandos
\RequirePackage{fancyhdr}
\pagestyle{fancy}

% eventualmente debería comentar que fai esto...
\renewcommand{\chaptermark}[1]{ \markboth{#1}{} }
\renewcommand{\sectionmark}[1]{ \markright{#1}{} }

% contidos dos encabezados
\fancyhead[EL]{\chaptername\ \thechapter} % par esquerda
\fancyhead[ER]{\leftmark}                 % par dereita
\fancyhead[OL]{}                          % impar esquerda
\fancyhead[OR]{\rightmark}                % impar dereita

% variables útiles, sacado do latex wikibook (lédeo)
% \leftmark      current chapter name printed like ”CHAPTER 3. THIS IS THE % CHAPTER TITLE”
% \rightmark     current section name printed like ”1.6. THIS IS THE SECTION % TITLE”
% \chaptername   the name chapter in the current language. If this is English, it % will display ”Chapter”
% \thechapter    current chapter number
% \thesection    current section numbe

% Liñas de separacion. É facil cambialas e poñerlle ornamentos. Para o simbolo
% dunha orbita uso 'svrsymbols'. Pode usarse un ornamento calqueira. O
% importante é redefinir 'headrule'. Exemplo copiado de overleaf
% \RequirePackage{svrsymbols}
% \renewcommand\headrule{
%     \vspace{-6pt}
%     \hrulefill
%     \raisebox{-5.4pt}
%     {\Huge\quad$\orbit$\quad}
%     \hrulefill
% }

% Para os grosores das liñas
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0pt}

% Outra opcion é usar este paquete, pero apenas o mirei
% \pagestyle{myheadings}
% \markboth{PAR}{IMPAR}

% Para que o texto ao pe de paxina non esté indentado (quitarlle sangrías)
\RequirePackage[hang,flushmargin]{footmisc}

% Para os epígrafes, tipicas frases ao comezo dun capítulo
\RequirePackage{epigraph}


% LISTAS =======================================================================
% Pa configurar facilmente listas e tal. Permite opcions tipo
% \begin{enumerate}[label=(arabic*)]
% \RequirePackage{enumitem}

% Para facelo a man, pode facerse o sequinte. Poden poñerse dentro do
% entorno correspondente e ser locales
\renewcommand{\labelitemi}{\arabic{itemi}}
\renewcommand{\labelitemii}{\arabic{itemi}.\arabic{itemii}}
\renewcommand{\labelenumi}{\arabic{enumi}}
\renewcommand{\labelenumii}{\arabic{enumi}.\arabic{enumii}}
\renewcommand{\labelenumiii}{\arabic{enumi}.\arabic{enumii}.\arabic{enumiii}}
\renewcommand{\labelenumiv}{\arabic{enumi}.\arabic{enumii}.\arabic{enumiii}.\arabic{enumiv}}


% EXTRAS =======================================================================
% Para encaixar mellor o texto (a veces fállame pero vese ben)
\RequirePackage{microtype}

% Para crear un cadro con texto dentro to guapo
% \RequirePackage{framed}

% Para colocar texto de 'proba' pa ver se as cousas encaixan ben
% \RequirePackage{lipsum} % dummy text


% LINKS ========================================================================
% Indice
\RequirePackage{makeidx}
% \makeindex

% hyperref debe ir ao final
\RequirePackage{hyperref}
\hypersetup{
    colorlinks,  % Colorear os links
    linkcolor={red!55!black},   %
    citecolor={green!45!black}, % Cores que me gustan
    urlcolor={blue!80!black}    %
}


% FORMATEADO XERAL =============================================================

% Usa un interlineado maior para separar párrafos en vez de usar sangría
% \setlength\parindent{0pt}  % tamaño da indentación
\setlength\parskip{0.7em}  % aumentar o tamaño do interlineado entre párrafos
% \renewcommand*{\baselinestretch}{2.0} % interlineado global

% para os conteos
% \numberwithin{equation}{section}
% \numberwithin{table}{section}
% \numberwithin{figure}{section}

% non me acordo que facia
% \clubpenalty=10000
% \widowpenalty=10000

% COMANDOS ÚTILES ==============================================================
% Para o valor absoluto. Copiado das memorias de alguén
\providecommand{\abs}[1]{\lvert#1\rvert}
