
def edadesMenorMayor(edades,nombres):
    nombreEdad = {}
    resultado=()

    for i in range(0,len(nombres)):   
        nombreEdad[nombres[i]] = edades[i]
    return nombreEdad

nombres = ["martin","juan","maxi"]
edades = [31,22,21]
print(edadesMenorMayor(edades,nombres))
