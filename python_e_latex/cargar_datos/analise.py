
# Importo a funcion que garda os datos en formato csv ben ordenados
from gardadato import garda_dato

# Supoñamos que tamos cun tremendo análise de datos e que acabamos de calcular
# o valor da constante G, cun valor de 59, erro de 0.2, e unidades de kg/m s^2.
G_valor    = 59
G_erro     = 0.20
G_unidades = "kg.m/s^2"

# DETALLES:
#
# Estos datos despois van lerse en LaTeX co paquete siunitx polo que é
# necesario que teñan un formato específico. Para os números, é sinxelo. Poden
# ir tal cual, ou incluso podemos pasalos a cadenas de texto e facerlle cousas
# como G_valor = "<59". No caso das unidades, podemos usar un método
# 'simbólico', ousexa cousas como G_unidades = "kg.m.J/Hz^2" (fixarse nos
# puntos) ou un método 'interpretado' como G _unidades =
# "\kilogram\meter\joule\per\hertz\squared". O segundo método permite un pouco
# máis de customizacion dende o paquete siunitx, pero é algo mais incomoda de
# escribir. En calqueira caso, ambas son válidas. Véxase
# https://ctan.fisiquimicamente.com/macros/latex/contrib/siunitx/siunitx.pdf

# A idea de todo esto é poder manexar esta cantidade, (valor, erro, unidade)
# dende python, e que se actualice automaticamente no noso documento de LaTeX
# sin ter que cambiar manualmente os valores nun sitio e noutro, o cal suele
# levar a equivocacions. So necesito usar a funcion definida no arquivo aparte
garda_dato("constante_G", G_valor, G_erro, G_unidades)

# E xa está. Na parte de python non hai que facer nada máis. De feito, non hai
# nin por qué usar a función 'garda_dato', o único importante é xerar o arquivo
# co formato específico, o cal pode facerse de moitas maneiras
#
# Neste caso, a funcion 'garda_dato' vai gardar os 4 datos
# (nome,valor,erro,unidades) no arquivo "resultados.csv". Este arquivo pode ser
# usado por outros programas para facer máis cálculos, como gráficas ou outros
# axustes. Non é mais que texto plano. O relevante é que podemos cargar
# directamente estos datos (unidades incluidas) en LaTeX. O arquivo pode verse
# algo así:
#
# variable_3,88,0.9,s.kg^20
# constante_W,90,3.2,m.kg^2
# constante_G,59,0.2,kg/(m.s^2)
