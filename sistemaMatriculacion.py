from sys import implementation
from utec import *
from personas import *


#Plan tecnólogo 
#Semestere 1
############################################################################################################
S1UC1 = UC(nombre = "Álgebra , Análisis y Geometría Analítica", code = 'S1UC1',ucregulares = None, ucaprobadas = None, semestre  = 1, creditos = 8)

S1UC2  = UC(nombre ="Mecanica, Ondas y Calor " , code ='S1UC' , ucregulares = None , ucaprobadas = None , semestre  =1 , creditos = 10 )

S1UC3 = UC(nombre = "Química General e inorgánica" , code = 'S1UC3' , ucregulares =None , ucaprobadas =None , semestre  = 1 , creditos = 9 )

S1UC4 = UC(nombre ="Taller Inicial de Tecnologías (Anual)" , code = 'S1UC4' , ucregulares =None , ucaprobadas = None, semestre  = 1, creditos = None )

S1UC5 = UC(nombre ="Salud y Sociedad" , code ='S1UC5' , ucregulares =None , ucaprobadas =None , semestre  = 1, creditos =8 )

S1UC6 = UC(nombre ="Programas Especiales" , code ='S1UC6' , ucregulares =None , ucaprobadas =None , semestre  = 1, creditos =2 )

S1UC7 = UC(nombre = "Inglés 1" , code ='S1UC7' , ucregulares =None , ucaprobadas =None , semestre  = 1, creditos =4 )

#Semestere 2
############################################################################################################
S2UC1 = UC(nombre = "Números Complejos y Ecuaciones Diferenciales", code = 'S2UC1', ucregulares = [S1UC1.code], ucaprobadas = None, semestre  = 2, creditos = 8)

S2UC2  = UC(nombre ="Electricidad y Magnetismo " , code ='S2UC' , ucregulares = [S1UC1.code,S1UC2.code] , ucaprobadas = None , semestre  =2 , creditos = 10 )

S2UC3 = UC(nombre = "Química Orgánica y Biológica" , code = 'S2UC3' , ucregulares =[S1UC3.code] , ucaprobadas =None , semestre  = 2 , creditos = 9 )

S2UC4 = UC(nombre ="Taller Inicial de Tecnologías (Anual)" , code = 'S2UC4' , ucregulares =None , ucaprobadas = None, semestre  = 2, creditos = 8 )

S2UC5 = UC(nombre ="Anatomía y Fisiologia Humanas" , code ='S2UC5' , ucregulares =[S1UC1.code,S1UC5.code] , ucaprobadas =None , semestre  = 2, creditos =8 )

S2UC6 = UC(nombre ="Programas Especiales" , code ='S2UC6' , ucregulares =None , ucaprobadas =None , semestre  = 2, creditos =2 )

S2UC7 = UC(nombre = "Inglés 2" , code ='S2UC7' , ucregulares =None , ucaprobadas =None , semestre  = 2, creditos = 4 )

#Semestere 3
############################################################################################################
S3UC1 = UC(nombre = "Ópticas y Radiaciones", code = 'S3UC1', ucregulares = [S1UC1.code,S1UC2.code], ucaprobadas = None, semestre  = 3, creditos = 10)

S3UC2  = UC(nombre ="Electrónica Analógica " , code ='S3UC' , ucregulares = [S2UC1.code,S2UC2.code,S2UC4.code] , ucaprobadas = [S1UC1,S1UC2] , semestre  =3 , creditos = 10 )

S3UC3 = UC(nombre = "Electrotecnia" , code = 'S3UC3' , ucregulares =[S2UC1,S2UC2] , ucaprobadas =None , semestre  = 3 , creditos = 9 )

S3UC4 = UC(nombre ="Instalaciones Hospitalarias" , code = 'S3UC4' , ucregulares =[S1UC3.code,S2UC5.code,S2UC2.code] , ucaprobadas = [S1UC1.code,S1UC5.code,S1UC2.code], semestre  = 3, creditos = 9 )

S3UC5 = UC(nombre ="Programación de Computadoras" , code ='S3UC5' , ucregulares =[S1UC1.code] , ucaprobadas =None , semestre  = 3, creditos =8 )

S3UC6 = UC(nombre ="Programas Especiales" , code ='S3UC6' , ucregulares =None , ucaprobadas =None , semestre  = 3, creditos =2 )

S3UC7 = UC(nombre = "Inglés 3" , code ='S3UC7' , ucregulares =None , ucaprobadas =None , semestre  = 3, creditos = 4 )

#Semestere 4
############################################################################################################
S4UC1 = UC(nombre = "Electrofisiología Clinica", code = 'S4UC1', ucregulares = [S2UC5.code,S3UC2.code], ucaprobadas = [S1UC1.code,S1UC5.code,S2UC1.code,S2UC2.code,S2UC4.code], semestre  = 4, creditos = 10)

S4UC2  = UC(nombre ="Electrónica Digital" , code ='S4UC' , ucregulares = [S3UC2.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S2UC4.code] , semestre  = 4 , creditos = 10 )

S4UC3 = UC(nombre = "Mecánica Maquinas y Materíales" , code = 'S4UC3' , ucregulares =[S1UC1.code,S1UC2.code] , ucaprobadas = None , semestre  = 4 , creditos = 9 )

S4UC4 = UC(nombre ="Imagenes Médicas" , code = 'S4UC4' , ucregulares =[S2UC5.code,S3UC1.code] , ucaprobadas = [S1UC1.code,S1UC5.code,S1UC2.code], semestre  = 4, creditos = 10 )

S4UC5 = UC(nombre ="Práctica Profesional Curriculas A(PPC A) - Internado Rotatorio - Anual" , code ='S4UC5' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] , ucaprobadas =None , semestre  = 4, creditos = None )

S4UC6 = UC(nombre ="Programas Especiales" , code ='S4UC6' , ucregulares =None , ucaprobadas =None , semestre  = 4, creditos =2 )

S4UC7 = UC(nombre = "Inglés 4" , code ='S4UC7' , ucregulares =None , ucaprobadas =None , semestre  = 4, creditos = 4 )

#Semestere 5
############################################################################################################
S5UC1 = UC(nombre = "Seguridad Eléctrica y Radiante", code = 'S5UC1', ucregulares = [S3UC3.code,S3UC4.code,S4UC1.code,S4UC4.code], ucaprobadas = [S1UC1.code,S1UC3.code,S2UC5.code,S2UC2.code,S3UC1.code], semestre  = 5, creditos = 10)

S5UC2  = UC(nombre ="Normativa sobre Equipamiento Médico" , code ='S5UC' , ucregulares = [S3UC3.code,S3UC4.code,S4UC1.code,S4UC3.code,S4UC4.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S1UC1.code,S1UC2.code,S3UC1.code] , semestre  = 5 , creditos = 8 )

S5UC3 = UC(nombre = "Taller de Mantenimiento de Equipos Médicos" , code = 'S5UC3' , ucregulares =[S3UC3.code,S3UC4.code,S4UC1.code,S4UC3.code,S4UC4.code] , ucaprobadas =[S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S1UC1.code,S1UC2.code,S3UC1.code] , semestre  = 5 , creditos = 10 )

S5UC4 = UC(nombre ="Matemática Avanzada I" , code = 'S5UC4' , ucregulares =[S2UC1.code,S3UC5.code] , ucaprobadas = [S1UC1.code], semestre  = 4, creditos = 9 )

S5UC5 = UC(nombre ="Práctica Profesional Curriculas A(PPC A) - Internado Rotatorio - Anual" , code ='S4UC5' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] ,  ucaprobadas =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] , semestre  = 4, creditos = 12)

S5UC6 = UC(nombre ="Programas Especiales" , code ='S5UC6' , ucregulares =None , ucaprobadas =None , semestre  = 5, creditos =2 )

S5UC7 = UC(nombre = "Inglés 5" , code ='S5UC7' , ucregulares =None , ucaprobadas =None , semestre  = 5, creditos = 4 )

#Semestere 6
############################################################################################################
S6UC1 = UC(nombre = "Instrumental de Laboratorio Clinico", code = 'S6UC1', ucregulares = [S2UC3.code,S3UC4.code], ucaprobadas = [S1UC3.code,S2UC5.code,S2UC2.code], semestre  = 6, creditos = 9)

S6UC2  = UC(nombre ="Informatica Médica" , code ='S6UC' , ucregulares = [S3UC3.code,S4UC1.code,S4UC4.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S2UC5.code,S3UC2.code,S3UC1.code] , semestre  = 6 , creditos = 8 )

S6UC3 = UC(nombre = "Instrumentación Médica Complementaria" , code = 'S6UC3' , ucregulares =[S3UC3.code,S3UC4.code,S4UC1.code,S4UC4.code] , ucaprobadas =[S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S3UC1.code] , semestre  = 6 , creditos = 10 )

S6UC4 = UC(nombre ="Matemática Avanzada II" , code = 'S6UC4' , ucregulares =[S5UC4.code] , ucaprobadas =[S2UC1.code,S3UC5.code], semestre  = 6, creditos = 9 )

S6UC5 = UC(nombre ="Fisíca Avanzada " , code ='S6UC5' , ucregulares =[S3UC1.code,S3UC3.code] , ucaprobadas =[S1UC1.code,S1UC2.code,S2UC1.code,S2UC2.code] , semestre  = 6, creditos =8 )

S6UC6 = UC(nombre ="PT Proyecto Final de Titulación"  , code ='S6UC6' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code, S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code, S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code,
S4UC1.code,S4UC2.code,S4UC3.code,S4UC4.code,S4UC5.code,S4UC6.code,S4UC7.code, S5UC1.code,S5UC2.code,S5UC3.code,S5UC4.code,S5UC5.code,S5UC6.code,S5UC7.code] , ucaprobadas =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,
S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code,
S4UC1.code,S4UC2.code,S4UC3.code,S4UC4.code,S4UC5.code,S4UC6.code,S4UC7.code,
S5UC1.code,S5UC2.code,S5UC3.code,S5UC4.code,S5UC5.code,S5UC6.code,S5UC7.code,] , semestre  = 6, creditos = 8  )

S6UC7= UC(nombre ="Programas Especiales" , code ='S6UC7' , ucregulares =None , ucaprobadas =None , semestre  = 6, creditos =2 )

S6UC8 = UC(nombre = "Inglés 6" , code ='S6UC8' , ucregulares =None , ucaprobadas =None , semestre  = 6, creditos = 4 )

alumno1=Estudiantes("Martin","Machado",43471650,31,3,2018)
print(alumno1.getAtributos)
#######################################################
#implementacion##
print(S4UC5.getAtributos())
plan=IBIO2019(S1UC1,S1UC2,S1UC3,S1UC4,S5UC1,S1UC6,S1UC7,S6UC8)
#print(plan.getUCplan2019())
#smestre1= plan.getSemestre(6)#entrega el plan de estudio dicriminado por semestre
#print(smestre1)
# print(len(smestre1))