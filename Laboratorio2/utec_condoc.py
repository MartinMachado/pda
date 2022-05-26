from pickle import FALSE, TRUE


class UC:
    """Clase unidad curricular "UC" recibe como parametros Nombre, code, ucregulares, ucaprobadas, semestre, creditos
    y sonn guardados como atributos de esa clase"""
    def __init__(self,nombre:str,code:str,ucregulares:list, ucaprobadas:list, semestre:int, creditos:int)->None:
        self.nombre=nombre
        self.code=code
        self.ucregulares=ucregulares
        self.ucaprobadas=ucaprobadas
        self.semestre=semestre
        self.creditos=creditos
    #Metodos
    def getAtributos(self):
        """Metódo getAtributos retorna los atributos referidos a una unidad curricular"""
        return [self.nombre,self.code,self.ucregulares,self.ucaprobadas,self.semestre,self.creditos]


alumnosInscriptos = []
#Plan tecnólogo 
"""Se crea el plan de Tecnológo en Ingeniería Biomédica el cual se compone por obtejos del Tipo UC"""
#Semestere 1
############################################################################################################
S1UC1 = UC(nombre = "Álgebra , Análisis y Geometría Analítica", code = 'S1UC1',ucregulares = [], ucaprobadas = [], semestre  = 1, creditos = 8)

S1UC2  = UC(nombre ="Mecanica, Ondas y Calor " , code ='S1UC2', ucregulares = [] , ucaprobadas = [] , semestre  =1 , creditos = 10 )

S1UC3 = UC(nombre = "Química General e inorgánica" , code = 'S1UC3', ucregulares =[] , ucaprobadas =[] , semestre  = 1 , creditos = 9 )

S1UC4 = UC(nombre ="Taller Inicial de Tecnologías (Anual)" , code = 'S1UC4', ucregulares =[] , ucaprobadas = [], semestre  = 1, creditos = [] )

S1UC5 = UC(nombre ="Salud y Sociedad" , code ='S1UC5', ucregulares =[] , ucaprobadas =[] , semestre  = 1, creditos =8 )

S1UC6 = UC(nombre ="Programas Especiales" , code ='S1UC6', ucregulares =[] , ucaprobadas =[] , semestre  = 1, creditos =2 )

S1UC7 = UC(nombre = "Inglés 1" , code ='S1UC7', ucregulares =[] , ucaprobadas =[] , semestre  = 1, creditos =4 )

#Semestere 2
############################################################################################################
S2UC1 = UC(nombre = "Números Complejos y Ecuaciones Diferenciales", code = 'S2UC1', ucregulares = [S1UC1.code], ucaprobadas = [], semestre  = 2, creditos = 8)

S2UC2  = UC(nombre ="Electricidad y Magnetismo " , code ='S2UC2', ucregulares = [S1UC1.code,S1UC2.code] , ucaprobadas = [] , semestre  =2 , creditos = 10 )

S2UC3 = UC(nombre = "Química Orgánica y Biológica" , code = 'S2UC3', ucregulares =[S1UC3.code] , ucaprobadas =[] , semestre  = 2 , creditos = 9 )

S2UC4 = UC(nombre ="Taller Inicial de Tecnologías (Anual)" , code = 'S2UC4', ucregulares =[] , ucaprobadas = [], semestre  = 2, creditos = 8 )

S2UC5 = UC(nombre ="Anatomía y Fisiologia Humanas" , code ='S2UC5', ucregulares =[S1UC1.code,S1UC5.code] , ucaprobadas =[] , semestre  = 2, creditos =8 )

S2UC6 = UC(nombre ="Programas Especiales" , code ='S2UC6', ucregulares =[] , ucaprobadas =[] , semestre  = 2, creditos =2 )

S2UC7 = UC(nombre = "Inglés 2" , code ='S2UC7', ucregulares =[] , ucaprobadas =[] , semestre  = 2, creditos = 4 )

#Semestere 3
############################################################################################################
S3UC1 = UC(nombre = "Ópticas y Radiaciones", code = 'S3UC1', ucregulares = [S1UC1.code,S1UC2.code], ucaprobadas = [], semestre  = 3, creditos = 10)

S3UC2  = UC(nombre ="Electrónica Analógica " , code ='S3UC2' , ucregulares = [S2UC1.code,S2UC2.code,S2UC4.code] , ucaprobadas = [S1UC1,S1UC2] , semestre  =3 , creditos = 10 )

S3UC3 = UC(nombre = "Electrotecnia" , code = 'S3UC3' , ucregulares =[S2UC1,S2UC2] , ucaprobadas =[] , semestre  = 3 , creditos = 9 )

S3UC4 = UC(nombre ="Instalaciones Hospitalarias" , code = 'S3UC4' , ucregulares =[S1UC3.code,S2UC5.code,S2UC2.code] , ucaprobadas = [S1UC1.code,S1UC5.code,S1UC2.code], semestre  = 3, creditos = 9 )

S3UC5 = UC(nombre ="Programación de Computadoras" , code ='S3UC5' , ucregulares =[S1UC1.code] , ucaprobadas =[] , semestre  = 3, creditos =8 )

S3UC6 = UC(nombre ="Programas Especiales" , code ='S3UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 3, creditos =2 )

S3UC7 = UC(nombre = "Inglés 3" , code ='S3UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 3, creditos = 4 )

#Semestere 4
############################################################################################################
S4UC1 = UC(nombre = "Electrofisiología Clinica", code = 'S4UC1', ucregulares = [S2UC5.code,S3UC2.code], ucaprobadas = [S1UC1.code,S1UC5.code,S2UC1.code,S2UC2.code,S2UC4.code], semestre  = 4, creditos = 10)

S4UC2  = UC(nombre ="Electrónica Digital" , code ='S4UC2' , ucregulares = [S3UC2.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S2UC4.code] , semestre  = 4 , creditos = 10 )

S4UC3 = UC(nombre = "Mecánica Maquinas y Materíales" , code = 'S4UC3' , ucregulares =[S1UC1.code,S1UC2.code] , ucaprobadas = [] , semestre  = 4 , creditos = 9 )

S4UC4 = UC(nombre ="Imagenes Médicas" , code = 'S4UC4' , ucregulares =[S2UC5.code,S3UC1.code] , ucaprobadas = [S1UC1.code,S1UC5.code,S1UC2.code], semestre  = 4, creditos = 10 )

S4UC5 = UC(nombre ="Práctica Profesional Curriculas A(PPC A) - Internado Rotatorio - Anual" , code ='S4UC5' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] , ucaprobadas =[] , semestre  = 4, creditos = [] )

S4UC6 = UC(nombre ="Programas Especiales" , code ='S4UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 4, creditos =2 )

S4UC7 = UC(nombre = "Inglés 4" , code ='S4UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 4, creditos = 4 )

#Semestere 5
############################################################################################################
S5UC1 = UC(nombre = "Seguridad Eléctrica y Radiante", code = 'S5UC1', ucregulares = [S3UC3.code,S3UC4.code,S4UC1.code,S4UC4.code], ucaprobadas = [S1UC1.code,S1UC3.code,S2UC5.code,S2UC2.code,S3UC1.code], semestre  = 5, creditos = 10)

S5UC2  = UC(nombre ="Normativa sobre Equipamiento Médico" , code ='S5UC2', ucregulares = [S3UC3.code,S3UC4.code,S4UC1.code,S4UC3.code,S4UC4.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S1UC1.code,S1UC2.code,S3UC1.code] , semestre  = 5 , creditos = 8 )

S5UC3 = UC(nombre = "Taller de Mantenimiento de Equipos Médicos" , code = 'S5UC3', ucregulares =[S3UC3.code,S3UC4.code,S4UC1.code,S4UC3.code,S4UC4.code] , ucaprobadas =[S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S1UC1.code,S1UC2.code,S3UC1.code] , semestre  = 5 , creditos = 10 )

S5UC4 = UC(nombre ="Matemática Avanzada I" , code = 'S5UC4' , ucregulares =[S2UC1.code,S3UC5.code] , ucaprobadas = [S1UC1.code], semestre  = 4, creditos = 9 )

S5UC5 = UC(nombre ="Práctica Profesional Curriculas A(PPC A) - Internado Rotatorio - Anual" , code ='S4UC5' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] ,  ucaprobadas =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] , semestre  = 4, creditos = 12)

S5UC6 = UC(nombre ="Programas Especiales" , code ='S5UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 5, creditos =2 )

S5UC7 = UC(nombre = "Inglés 5" , code ='S5UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 5, creditos = 4 )

#Semestere 6
############################################################################################################
S6UC1 = UC(nombre = "Instrumental de Laboratorio Clinico", code = 'S6UC1', ucregulares = [S2UC3.code,S3UC4.code], ucaprobadas = [S1UC3.code,S2UC5.code,S2UC2.code], semestre  = 6, creditos = 9)

S6UC2  = UC(nombre ="Informatica Médica" , code ='S6UC2' , ucregulares = [S3UC3.code,S4UC1.code,S4UC4.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S2UC5.code,S3UC2.code,S3UC1.code] , semestre  = 6 , creditos = 8 )

S6UC3 = UC(nombre = "Instrumentación Médica Complementaria" , code = 'S6UC3' , ucregulares =[S3UC3.code,S3UC4.code,S4UC1.code,S4UC4.code] , ucaprobadas =[S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S3UC1.code] , semestre  = 6 , creditos = 10 )

S6UC4 = UC(nombre ="Matemática Avanzada II" , code = 'S6UC4' , ucregulares =[S5UC4.code] , ucaprobadas =[S2UC1.code,S3UC5.code], semestre  = 6, creditos = 9 )

S6UC5 = UC(nombre ="Fisíca Avanzada " , code ='S6UC5' , ucregulares =[S3UC1.code,S3UC3.code] , ucaprobadas =[S1UC1.code,S1UC2.code,S2UC1.code,S2UC2.code] , semestre  = 6, creditos =8 )

S6UC6 = UC(nombre ="PT Proyecto Final de Titulación"  , code ='S6UC6' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code, S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code, S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code,
S4UC1.code,S4UC2.code,S4UC3.code,S4UC4.code,S4UC5.code,S4UC6.code,S4UC7.code, S5UC1.code,S5UC2.code,S5UC3.code,S5UC4.code,S5UC5.code,S5UC6.code,S5UC7.code] , ucaprobadas =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,
S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code,
S4UC1.code,S4UC2.code,S4UC3.code,S4UC4.code,S4UC5.code,S4UC6.code,S4UC7.code,
S5UC1.code,S5UC2.code,S5UC3.code,S5UC4.code,S5UC5.code,S5UC6.code,S5UC7.code,] , semestre  = 6, creditos = 8  )

S6UC7= UC(nombre ="Programas Especiales" , code ='S6UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 6, creditos =2 )

S6UC8 = UC(nombre = "Inglés 6" , code ='S6UC8' , ucregulares =[] , ucaprobadas =[] , semestre  = 6, creditos = 4 )

#Fin del pplan de estudios Tecnolo
#######################################################


class IBIO2019():
    """ Clase IBIO2019"""
    def __init__(self,*unidadCurricular:UC) -> None:
        """Constrcutor de la clase IBIO2019 que recibe como parametros el nombre de una unidad curricular como objeto de la clase UC
        y lo almacena como atributo"""
        self.unidadCurricular=unidadCurricular
    
    def getUCplan2019(self):
        plan=[]        
        for i in range(0,len(self.unidadCurricular)):
            plan.append(self.unidadCurricular[i].code)
        return plan

    def getSemestre(self,numSemestre:int): #OBTENER MATERIAS POR SEMESTRES
        semestre1=[]        
        for i in range(0,len(self.unidadCurricular)):
            if self.unidadCurricular[i].semestre==numSemestre:
                semestre1.append(self.unidadCurricular[i].code)
        return semestre1
    
#plan2019 = [S1UC1,S1UC2,S1UC3,S1UC4,S1UC5,S1UC6,S1UC7,S2UC1,S2UC2,S2UC3,S2UC4,S2UC5,S2UC6,S2UC7,S3UC1,S3UC2,S3UC3,S3UC4,S3UC5,S3UC6,S4UC7,S4UC1,S4UC2,S4UC3,S4UC4,S4UC5,S4UC6,S4UC7,S5UC1,S5UC2,S5UC3,S5UC4,S5UC5,S5UC6,S5UC7,S6UC1,S6UC2,S6UC3,S6UC4,S6UC5,S6UC6,S6UC7,S6UC8]
   
class Persona():
    """ Se crea una clase persona que sera comun a las demas, recibe como parametros nombre de Persona, Apellidos, CI, y edad Persona 
    los cuales se almacenan como atributos de la clase algunos privados y otros no"""
    def __init__(self,nombrePersona:str, apellidos:str, CI:int, edadPersona:int):
        self.nombrePersona=nombrePersona
        self.apellidos=apellidos
        self._CI=CI        
        self.edadPersona=edadPersona
    
    def getCI(self):
        """Método para retornar la CI de la persona"""
        return self._CI
    
    def setCI(self, newCI:int):
        """ Método para agregar una nueva CI"""
        self._CI = newCI      

class Estudiantes(Persona):

    """Clase eestudiantes que hereda atributos de la clase persona, y recibe como nuevos parametros año de ingreso,
    uc's incripta, uc regulares, y uc aprobadas."""
    def __init__(self, nombrePersona: str, apellidos: str, CI: int, edadPersona: int, aIngreso:int,ucinscripta=[],ucregulares=[],ucaprobadas=[]):
        super().__init__(nombrePersona, apellidos, CI, edadPersona)
        self.aIngreso=aIngreso
        self._accCode=3
        self.ucaprobadas=ucaprobadas
        self.ucregulares=ucregulares
        self.ucinscripta=ucinscripta
        self.ucINSC=[x.code for x in ucinscripta]
        self.ucREGU=[x.code for x in ucregulares]
        self.ucAPROB=[x.code for x in ucaprobadas]
        
        archivo="lista_de_alumnos.txt"     

        verificacion=open(archivo,'r').read().split()
        lista=[]
        for i in range(0,len(verificacion)):
            lista.append(verificacion[i])
        cedula=str(CI)
        if cedula in lista:
            pass
        else:
            registro=open(archivo, 'a')
            registro.write(str(CI)+" "+str(nombrePersona)+" "+str(apellidos)+" "+str(edadPersona)+" "+str(aIngreso)+" "+str(self.ucINSC)+" "+str(self.ucREGU)+" "+str(self.ucAPROB)+"\n")
            registro.close()
    #Metodos
    def getCode(self):
        """Método para obtener el codigo de acceso asignado al estudiante"""
        return self._accCode
    #Metodo para insicpcion a UC con condicion segun previas y regulares
    def ucInscriptas(self):
        """Método para retornar a las UC que se encuentra inscripto el estudiante"""
        return self.ucINSC
    def ucAprobadas(self):
        """Método para obtener y retornar las uc Aprobadas que tiene el estudiante"""
        return self.ucAPROB
    def ucRegulares(self):
        """Método para obtener y retornar las uc Regulares que tiene el estudiante"""
        return self.ucREGU

class Secetaria(Persona):
    """Clase secretaria que hereda algunos atributos de la clase persona."""
    def __init__(self, nombrePersona: str, apellidos: str, CI: int, edadPersona: int):
        super().__init__(nombrePersona, apellidos, CI, edadPersona)
        self._accCode=2
    
    def getCode(self):
        """Método para obtener el codigo de acceso"""
        return self._accCode

    #Metodos
    def matricularEst(self,estudiante:Estudiantes,unidadcurricular:UC, matricula:bool):
        """Método para matricular estudiantes que recibe como parametros un objeto estudiante, la unidad curricular
        y un boleano si la matricula es posible o no."""
        if matricula is TRUE:
            estudiante.ucinscripta.append(unidadcurricular)
        elif(matricula is FALSE):
            estudiante.ucinscripta.remove(unidadcurricular)
    

class Coridnadora(Persona):
    """Clase cordinadora herencia atributos de la clase Persona y agrega nuevos atributos, pose métodos como obtener un codigo de acceso """
    def __init__(self, nombrePersona: str, apellidos: str, CI: int, edadPersona: int):
        super().__init__(nombrePersona, apellidos, CI, edadPersona)
        self._accCode=1
    
    def getCode(self):
        """Método para obtener el codigo de acceso de la coordinadora"""
        return self._accCode

#############################FUNCIONES#################################################

def inscripcionUCestudiantes(usuario,alumno,UC,semestre):
        """Función para inscripción por parte del estudíante, recibe como parametros el usuario que realiza la actividad, el alumno a inscribir las unidad curricular a inscribir
        y el semestre en el que se encuentra esa unidad curricular.
        En dicho método ingresan personas con permisos para realizar la actividad, en caso de no tener permisos no se le permite acceso. Posteriormente se chequea si el estudiante ya esta inscripto en esta UC, en caso contrario se comprueba que cumpla con las previatura de la UC, si esta todo correcto
        el estudiante es agregado a una lista de alumnos inscriptos.
        Si el estudiante no cumple con las previaturas se le hace saber que no puede inscribirse a dicha unidad curricular"""
        #estudiante Matriculacion
        import json
        codigoAcceso = usuario.getCode()
        if codigoAcceso==3 or codigoAcceso==2:    
            if UC in alumno.ucinscripta:
                print("Estudiante ya esta inscripto en esta UC")
            elif UC.ucregulares == alumno.ucregulares or UC.ucaprobadas == alumno.ucaprobadas and semestre == UC.semestre:
                alumno.ucinscripta.append(UC)    
                filename = 'lista_de_alumnos.json'                
                entry = {UC.nombre:[{alumno.getCI(): [alumno.nombrePersona,alumno.apellidos]}]}
                data = {}
                data["Alumnos Inscriptos"] = []
                #data["Alumnos Inscriptos"].append(entry)
                data["Alumnos Inscriptos"][0]={UC.nombre:[]}
                filename="lista_de_alumnos.json"
                with open(filename, "w") as file:
                    json.dump(data, file,indent=3)
                
                print("Se inscribio en la UC: %s" % (UC.nombre))
            else:
                print("No se puede matricular en la UC: %s por no tener regulares o aprobadas las previaturas" % (UC.nombre))
        else:
            print("No tiene el acceso para matricular estudiantes")