from pickle import FALSE, TRUE
from utec import Estudiantes,Secetaria,UC,IBIO2019,Coridnadora,inscripcionUCestudiantes
import utec


# print(S4UC5.getAtributos())
# plan=IBIO2019(S1UC1,S1UC2,S1UC3,S1UC4,S1UC5,S1UC6,S1UC7,S2UC1,S2UC2,S2UC3,S2UC4,S2UC5,S2UC6,S2UC7,S3UC1,S3UC2,S3UC3,S3UC4,S3UC5,S3UC6,S4UC7,S4UC1,S4UC2,S4UC3,S4UC4,S4UC5,S4UC6,S4UC7,S5UC1,S5UC2,S5UC3,S5UC4,S5UC5,S5UC6,S5UC7,S6UC1,S6UC2,S6UC3,S6UC4,S6UC5,S6UC6,S6UC7,S6UC8)
# print(plan.getUCplan2019())
#print(alumno1.ucinscripta)
#smestre1= plan.getSemestre(1)#entrega el plan de estudio dicriminado por semestre
#print(smestre1)
# print(len(smestre1))
# print(alumno1.inscripcionUC(S1UC1))
# print(alumno1.ucInscriptas())

# sec1.matricularEst(alumno2,utec.S3UC1,TRUE)
# print(alumno2.ucinscripta)
# sec1.matricularEst(alumno2,utec.S3UC1,FALSE)
sec1=Secetaria("Virginia","Catala",4333443,30)
cord1=Coridnadora("Cecilia","Escandon",45556663,25)
alumno1=Estudiantes("Maximiliano","Vespa",111111,22,2018,[utec.S1UC5,utec.S1UC6,utec.S1UC7])
alumno2=Estudiantes("Juan","Bentos",2222222,22,2018,[utec.S2UC5,utec.S2UC6,utec.S2UC7],[utec.S1UC5,utec.S1UC6,utec.S1UC7])
#alumno2=Estudiantes("Maxi","Vespa",45557845,22,2018,[utec.S2UC1,utec.S2UC2,utec.S2UC3,utec.S2UC5,utec.S2UC6,utec.S2UC7],[utec.S1UC1,utec.S1UC2,utec.S1UC3],[utec.S1UC5,utec.S1UC6,utec.S1UC7])
#inscripcionUCestudiantes(sec1,alumno1,utec.S1UC2,1)
#inscripcionUCestudiantes(alumno2,alumno2,utec.S3UC4,3)
cord1.getListaEst()
