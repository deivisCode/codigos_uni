#import "@preview/zero:0.5.0": num

#let crear_titulo(
    autoria,
    titulo,
    subtitulo,
    grupo,
    correo,
) = {
    set align(center)
    text(30pt)[ *#title()* ]
    v(1em)
    line(length: 100%)
    v(1em)
    subtitulo
    v(1em)
    smallcaps[#autoria. Grupo #grupo]
    v(1em)
    text[#link("mailto:" + correo)]
    v(1em)
    line(length: 100%)
}


#let usar_estilo(
    autoria   : "Autoria",
    titulo    : "Titulo",
    subtitulo : "Subtitulo",
    grupo     : "G1",
    correo    : "correo@correo.com",
    documento

) = {

    set document(
        title  : titulo,
        author : autoria
    )
    set text(
        size      : 10pt,
        lang      : "gl",
        font      : "New Computer Modern",
        region    : "ES",
        script    : "latn",
        dir       : ltr,
        hyphenate : true,
    )
    set page(
        margin:(x: 1.5cm, y: 1.5cm),
    )

    show link: set text(blue, font : "New Computer Modern Sans")
    show link: underline

    crear_titulo(autoria, titulo, subtitulo, grupo, correo)

    pagebreak()

    set page(
        paper     : "a4",
        numbering : "1",
        columns   : 2,
        margin    : (x: 2cm, y: 2cm),
    )
    set par(justify: true)
    set heading(numbering: "1.")
    set math.equation(numbering: "[1]")
    documento

}

#let resultados = csv("datos.csv", row-type: dictionary)

// Esto lee un arquivo en formato CSV do estilo:
//
// Nome,Valor,Erro,Unidade
// impedancia_1,90.06,0.0672345,A
// impedancia_2,92.16,0.064,A
//
// Os nomes das columnas son relevantes.
//
// Facer #dato("impedancia_1") devolve ( 90.060 +- 0.067 ) A
#let dato(nome) = {
    let d = resultados.find(dict => dict.at("Nome") == nome)
    [
        (
            #num(
                round: (mode: "uncertainty", precision: 2),
                str(d.Valor) + "+-" + str(d.Erro),
            )
        )
        #d.Unidade
    ]
}
