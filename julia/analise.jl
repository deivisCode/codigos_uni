using CSV

# Estrutura dun dato típico
struct Dato
    Nome::String
    Valor::Float64
    Erro::Float64
    Unidade::String
end

# vector para ir gardando datos concretos
Datos = Dato[]

# funcion para meter un dato novo no vector de datos
function NovoDato(
    Nome::String,
    Valor::Float64,
    Erro::Float64,
    Unidade::String)
    push!(Datos, Dato(Nome, Valor, Erro, Unidade))
end

NovoDato("impedancia_1" , 90.06 , 0.0672345 , "A")
NovoDato("impedancia_2" , 92.16 , 0.064     , "A")

CSV.write( "datos.csv", Datos )
