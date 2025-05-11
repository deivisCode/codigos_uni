#import "@preview/fletcher:0.5.7" as fletcher: diagram, node, edge
#import "@preview/cetz:0.3.4" as cetz

#set page(
    // width: auto,
    // height: auto,
    paper: "a4",
    flipped: true,
    margin: (x: 0em, y: 0em),
)

// Deixo esto comentado como referencia
//
// #diagram(
//     // debug: 3,
//     axes: (ltr, btt),
//     spacing: (12mm, 6mm),
//     {
//         node((1, 1), $ f $, name: <f1>)
//         node((0, 1), $ f $, name: <f2>)
//     },
//     node(
//         (0, 0), // posicion
//         [nodo], // contidos
//         name: <paco>, // para poder referencialo logo
//         // inset: 1em, // espacio entre contenido e o outline
//         // outset: 1mm, // espacio entre nodo e onde agarran os edges
//         // fill: red.lighten(50%),
//         // stroke: blue,
//         width: 40pt,
//         height: auto,
//         // enclose : (<f1>, <f2>) // qué nodos agrupar
//         corner-radius: 5mm,
//     ),
//     edge(
//         // vertices: ((0, 0), (1, 1)),
//         vertices: (<paco>,<f1>),
//         label: text(size: 5pt)[$hom$],
//         label-pos: 0.4, // posicion ao longo da frecha
//         label-side: left,
//         label-sep: 1mm,
//         label-angle: right, // ou 90deg
//         // decorations: cetz.decorations.wave.with(amplitude:0.1),
//         marks: ">->",
//         // dash: "dotted",
//         // extrude: (-2,2),
//         shift:2pt,
//         // bend:-90deg,
//         corner: left,
//         corner-radius: 10pt,
//         crossing: true
//     ),
// )

#set align(center)
#v(2em)
#text(size: 20pt)[#smallcaps[Estruturas alxébricas de relevancia]]
#line(length: 90%)

#let esp = 0
#let mag = 1
#let sem = 2
#let mon = 3
#let gru = 4

#diagram(
    // debug: 1,
    // axes: (ltr, btt),
    spacing: (0mm, 9mm),
    // node-stroke: red,
    cell-size:(30pt,30pt),
    // edge-corner-radius: 10pt,
    node-inset:1em,
    {
        node(
            (0, mag),
            align(left)[
                *Magma* $(X, plus.circle )$ \
                - $plus.circle$ operación binaria e interna
            ],
            name: <magma>,
        )

        node(
            (0, sem),
            align(left)[
                *Semigrupo* $(X, plus.circle )$ \
                - Magma + $plus.circle$ asociativa
            ],
            name: <semigrupo>,
        )

        node(
            (0, mon),
            align(left)[
                *Monoide* $(X, plus.circle )$ \
                - Semigrupo + $exists$ neutro $e$
            ],
            name: <monoide>,
        )

        node(
            (0, gru),
            align(left)[
                *Grupo* $(X, plus.circle )$ \
                - Monoide + $exists$ simétrico $forall x in X$
            ],
            name: <grupo>,
        )

        node(
            (1,mag),
            align(left)[
                *Anel non asociativo* $(A,plus.circle,dot)$ \
                - $(A,plus.circle)$ grupo \
                - $(A,dot)$ magma
                - $dot$ distributivo respecto de $plus.circle$
                    + $(a plus.circle b)dot c = (a dot c) plus.circle (b dot c)$
                    + $c dot (a plus.circle b)= (c dot a) plus.circle (c dot b)$
            ],
            name: <anel>
        )

        node(
            (1, sem),
            align(left)[
                *Anel asociativo* $(A,plus.circle,dot)$ \
                - $(A,plus.circle)$ grupo \
                - $(A,dot)$ semigrupo
                - $dot$ distributivo respecto de $plus.circle$
            ],
            name: <anel_asociativo>,
        )

        node(
            (1, mon),
            align(left)[
                *Anel Unitario* $(A,plus.circle,dot)$ \
                - $(A,plus.circle)$ grupo
                - $(A,dot)$ monoide
                - $dot$ distributivo respecto de $plus.circle$
            ],
            name: <anel_unitario>,
        )

        node(
            (1, gru),
            align(left)[
                *Corpo* $(A,plus.circle,dot)$ \
                - $(A,plus.circle)$ grupo
                - $(A-{0},dot)$ grupo
                - $dot$ distributivo respecto de $plus.circle$
                Se $dot$ é conmutativa, Campo
            ],
            name: <corpo>,
        )

        node(
            (2, esp),
            align(left)[
                *Espazo Lineal*, $((G,plus.circle), (KK,+,dot), circle.stroked.small)$ \
                - $(G,plus.circle)$ grupo \
                - $(KK,+,dot)$ corpo \
                - $circle.stroked.small$ operación entre o Grupo e o Corpo
            ],
            name: <espazo_lineal>,
        )

        node(
            (2, mag),
            align(left)[
                *Álxebra sobre un Corpo* $KK$\
                - Espazo lineal $((V,plus.circle), (KK,+,dot), circle.stroked.small)$ \
                - Anel non Asociativo $(V,plus.circle,dot)$
            ],
            name: <alxebra>
        )

        node(
            (2, sem),
            align(left)[
                *Álxebra Asociativa* \
                - Espazo lineal $((V,plus.circle), (KK,+,dot), circle.stroked.small)$ \
                - Anel asociativo $(V,plus.circle,dot)$
            ],
            name: <alxebra_asociativa>
        )

        node(
            (2, mon),
            align(left)[
                *Álxebra Asociativa con unidad* \
                - Espazo lineal $((V,plus.circle), (KK,+,dot), circle.stroked.small)$ \
                - Anel asociativo unitario $(V,plus.circle,dot)$
            ],
            name: <alxebra_asociativa_unidade>
        )

        node(
            (3, mag),
            align(left)[
                *Álxebra de Lie* \
                - Álxebra sobre un corpo $KK$
                Produto do anel $[dot,dot]$ cumpre: \
                - Bilineal
                - Antisimétrica
                - Identidade de Jacobi $[x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0$
            ],
            name: <alxebra_lie>
        )

    },
)
