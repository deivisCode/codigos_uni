% Esta é unha clase que contén os paquetes, formatos e configuracións
% principales que uso nas miñas memorias. Para usalo solo hai que poñer este
% arquivo no mesmo directorio que o documento principal e cargalo con
% \documentclass{memoria}. A clase esta está chea de opcións comentadas para
% telas aquí presentes no caso de querer usalas


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{memoria}[2024/08/29 Clase das memorias de Deivis]

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
    right          = 30mm,  % marxe dereito
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


% MATES BASICAS ================================================================
\RequirePackage{amsmath} % entornos matemáticos
\RequirePackage{amssymb} % colección extendida de símbolos matemáticos
% \RequirePackage{amsthm}  % creación de estructuras tipo teoremas, definicións, etc.

% Para crear o estilo dun teorema hai que facer:
% \newtheoremstyle{estilopropio}
%     {}{}  % espazo encima/abaixo
%     {}    % tipo de letra do corpo
%     {}    % indentación
%     {}    % tipo de letra do encabezado
%     {:}   % signo de puntuacion logo do encabezado
%     {1em} % espaciado logo do encabezado
%     {%      estructura do encabezado
%         \textbf{\underline{\thmname{#1}}}%
%         \textit{\thmnote{ (#3)}}%
%     }
% \theoremstyle{estilopropio} % usar o estilo para os teoremas
% \newtheorem*{teorema}{Teorema} % definir o entorno 'teorema'


% BIBLIOGRAFÍA =================================================================
\RequirePackage[ % necesario ter instalado 'biber'
    style = numeric,
    natbib = true
]{biblatex}
\addbibresource{bibliografia.bib}


% FIGURAS ======================================================================
\RequirePackage{graphicx} % pa facilitar o uso de \includegraphics
\RequirePackage{float}    % permite a colocación 'H' dos floats
% \RequirePackage{subfig}   % para colcar varias imaxes xuntas


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

% UNIDADES =====================================================================
% Para usar unidades e numeros de forma corrrecta e estándar con \num{},
% \unit{}, \qty{}, etc.
\RequirePackage{siunitx}
\sisetup{
    output-decimal-marker={.},
    % exponentes ------------------------
    exponent-mode=threshold,
    exponent-thresholds=-3:2, % non usar exponentes 10^{-2,-1, 0, 1}
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
    inline-per-mode=single-symbol,
    display-per-mode=fraction,
}



% CORES ========================================================================
% 'xcolor' pa definir cores e toda a vaina. Opción 'table' pa poder colorear
% celdas usando \cellcolor
\RequirePackage[table]{xcolor}


% OLVIDONA =====================================================================
% paquetes que non recordo pa que os quero
% \RequirePackage{enumitem}


% EXTRAS =======================================================================
% Para encaixar mellor o texto (a veces fállame pero vese ben)
% \RequirePackage{microtype}

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
    citecolor={green!45!black}, % Cores queme gustan
    urlcolor={blue!80!black}    %
}

% FORMATEADO ===================================================================

% Usa un interlineado maior para separar párrafos en vez de usar sangría
\setlength\parindent{0pt}             % eliminar a indentación
\setlength\parskip{0.7em}             % aumentar o tamaño do interlineado entre párrafos
% \renewcommand*{\baselinestretch}{2.0} % interlineado global


