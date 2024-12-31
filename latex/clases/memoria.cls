% Esta é unha clase que contén os paquetes, formatos e configuracións
% principales que uso nas miñas memorias. Para usalo solo hai que poñer este
% arquivo no mesmo directorio que o documento principal e cargalo con
% \documentclass{memoria}. A clase esta está chea de opcións comentadas para
% telas aquí presentes no caso de querer usalas


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{memoria}[2024/09/02 Clase das memorias de Deivis]

% Usar a clase article como base
\LoadClass[12pt]{article}


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
    top            = 20mm,  % marxe superior
    left           = 20mm,  % marxe esquerdo
    right          = 20mm,  % marxe dereito
    bottom         = 20mm,  % marxe inferior
% notas ao marxe ------------------------------------------------
    marginparsep   = 6mm,     % separacion co corpo
    marginparwidth = 15mm,    % grosor
    % nomarginpar    = true,    % desactivar notas no marxe (tamaño 0)
% encabezado ----------------------------------------------------
    headsep        = 5mm,   % separación co corpo
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


% MATES BASICAS ================================================================

% Matemáticas xerais. Inclue amsmath
\RequirePackage{mathtools} 

% Colección extendida de símbolos matemáticos. Inclue amsfonts
\RequirePackage{amssymb} 

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
\RequirePackage{multirow} % tablas con celdas unidas
\RequirePackage{booktabs} % non e necesario pero aos nerds de Latex gustalle


% DATOS EXTERNOS ==============================================================
% Cargar datos. Véxase o tuto de python_e_latex/cargar_datos
% \RequirePackage{datatool}
% \DTLsetseparator{,}
% \DTLloaddb[
%     noheader, % non temos unha primeira fila cos nomes
%     keys={nome,valor,erro,unidade} % en cambio usamos estos nomes pas columnas
% ]{datos}{resultados.csv} % nome da base de datos, e nome do ficheiro


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

% Comandos para cargar datos en LaTeX usando datatool. Útil para as memorias.
\newcommand{\DTLfetchsave}[5]{%
  \edtlgetrowforvalue{#1}{\dtlcolumnindex{#1}{#2}}{#3}%
  \dtlgetentryfromcurrentrow{#5}{\dtlcolumnindex{#1}{#4}}%
}
\newcommand{\cantidade}[1]{%
  \begingroup
  \DTLfetchsave{datos}{nome}{#1}{valor}{\valor}%
  \DTLfetchsave{datos}{nome}{#1}{erro}{\erro}%
  \DTLfetchsave{datos}{nome}{#1}{unidade}{\unidade}%
  \qty{\valor\pm\erro}{\unidade}% <-- aquí é onde se usa siunitx
  \endgroup
}


% Para que o texto ao pe de paxina non esté indentado (quitarlle sangrías)
% \RequirePackage[hang,flushmargin]{footmisc}


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
\setlength\parindent{0pt}  % tamaño da indentación
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
