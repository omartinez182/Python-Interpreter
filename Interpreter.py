#Proyecto realizado por:
#Omar Martinez, carnet 1210636
#Joaquin Orantes, carnet 19007763

import re
import numpy as np
import os

tabs = int(0)
archivo = None
archivoSalida = None
regexDefinir = "DEFINIR ([a-z][a-z0-9A-Z_]*) COMO (ENTERO|REAL|LOGICO|TEXTO);"
regexSet = '([a-z][a-zA-Z0-9_]*)<-([0-9.]+|".*"|Falso|Verdadero|([a-zA-Z0-9_.]*\s?(\+|\*|\-|\/)\s?[a-zA-Z0-9_.]+)|[a-zA-Z]*);'
regexWrite = "ESCRIBIR ('?.*'?);"
regexRead = 'LEER ([a-zA-Z][a-z0-9A-Z_]*);'
regexIF = '(?i)SI \(([\w ]+)([><=]|>=|<=|!=|==)([\w ]+)\);'
regexIFAND = '(?i)SI \(\(([\w ]+)([><=]|>=|<=|!=|==)([\w ]+)\) Y \(([\w ]+)([><=]|>=|<=|!=|==)([\w ]+)\)\);'
regexIFOR = '(?i)SI \(\(([\w ]+)([><=]|>=|<=|!=|==)([\w ]+)\) O \(([\w ]+)([><=]|>=|<=|!=|==)([\w ]+)\)\);'
regexELSE = '(?i)SINO;'
regexENDIF = '(?i)FINSI;'
regexCONT = '(?i)CONTADOR ([><=]|>=|<=|!=|==)([\d ]+);'
regexWHILE = '(?i)MIENTRAS \(([\w ]+)([><=]|>=|<=|!=|==)([\w ]+)\) HACER;'
regexENDWHILE = '(?i)FINMIENTRAS;'
regexCOMP = '([\w\d\+\-\\\* ]+)([><=]|>=|<=|!=|==)([\w\d\+\-\\\* ]+);'
regexCompile = "(COMPILE|compile|Compile) ([a-zA-Z0-9]+).iio"
regexRun = "(RUN|run|Run) ([a-zA-Z0-9]+).iio"
regexLoad = "(LOAD|load|Load) ([a-zA-Z0-9]+).py"


#El archivo de pseudocodigo debe incluir la extension .iio
def main(archivo, archivoSalida):
    nombreArchivo = "prueba1" #nombre del archivo que contiene el pseudocodigo
    archivo = open(nombreArchivo+".iio", "r") #abrir el archivo en modo de lectura
    archivoSalida = open(nombreArchivo+".py", "w") #abrir el archivo en modo escritura donde se va a escribir el código python
    tabs = 0
    ifs = 0
    endifs = 0

    print("Traduciendo...")

    i=0
    for linea in archivo.readlines():  #leer el archivo línea por línea
        i=i+1 #contar el número de línea en el archivo
        linea = linea.rstrip()

        if(linea.strip() == ''):
            archivoSalida.writelines('\n')
        elif(linea[-1:] != ';'): #Determinar si la línea de pseudocódico temina en ";", si no es así, se detiene el programa
            print("*** La linea " + str(i)   + " no finaliza en ';', se ha detenido el programa.")
            archivoSalida.writelines("#*** La linea " + str(i)   + " no finaliza en ';', se ha detenido el programa.")
            quit()

        if(linea.strip() != '' and tabs >= 1 and linea.lower().strip() != "finproceso;"): #Validar que la indentación de la línea es la adecuada
            if (bool(re.search(regexELSE, linea)) == True or bool(re.search(regexENDIF, linea)) == True or bool(re.search(regexENDWHILE, linea)) == True):
                tabsentexto = linea.count('\t')+1
            else:
                tabsentexto = linea.count('\t')
            
            if tabs != tabsentexto:
                print('tabs:' + str(tabs) +' '+ 'tabsentexto: ' + str(tabsentexto))
                print("Problema de indentacion en código, línea: " + str(i) + '.')
                archivoSalida.writelines('#***Problema de indentacion encontrado en pseudocodigo. El programa interprete fue detenido.***')
                quit()
        
        if linea.lower().strip() == "proceso principal;":
            archivoSalida.writelines('def main():' + '\n')
            #print('def main():' + '\n')
            tabs = 1
        
        if linea.lower().strip() == "finproceso;":
            archivoSalida.writelines('main()' + '\n')
            #print('main():' + '\n')
        
        #1 Traducir declaración de variables y tipos de datos
        if(bool(re.search(regexDefinir, linea)) == True): #valida expresión regular para crear código
            codigo = re.findall(regexDefinir, linea) #extrae elementos de la expresión regular
            nombreVariable = codigo[0][0] #extraemos nombre de la variable de la casilla 0
            tipoVariable = codigo[0][1] #extraemos tipo de la variable de la casilla 0
            if(tipoVariable == "ENTERO"):
                valorVariable = "0"
            elif(tipoVariable == "TEXTO"):
                valorVariable = '""'
            elif(tipoVariable == "LOGICO"):
                valorVariable = "False"
            elif(tipoVariable == "REAL"):
                valorVariable = "0.0"
            else:
                print("Error, el tipo de dato no se reconoce.")
            archivoSalida.writelines('\t' * tabs + nombreVariable + " = " + valorVariable + '\n')
            #print(linea.lstrip('\t') + " -> " + nombreVariable + " = " + valorVariable + '\n')
        
        #2 Traducir una operación aritmética y si el valor de la variable booleana es falso o verdadero
        elif(bool(re.search(regexSet, linea)) == True):
            codigo = re.findall(regexSet, linea)
            codigo = codigo[0]
            nombreVariable = codigo[0]
            valorVariable = codigo[1]
            if(valorVariable == "Verdadero"):
                valorVariable = "True"
            elif(valorVariable == "Falso"):
                valorVariable = "False"
            archivoSalida.writelines('\t' * tabs + nombreVariable + " = " + valorVariable + '\n')
            #print(linea.lstrip('\t') + " -> " + nombreVariable + " = " + valorVariable)

        #3 Traducir línea de solicitud de ingreso de datos al usuario
        elif(bool(re.search(regexRead, linea)) == True):
            codigo = re.findall(regexRead, linea)
            entrada = str(codigo[0])
            nombreVariable = 'input()'
            archivoSalida.writelines('\t' * tabs + entrada + " = " + nombreVariable + '\n')
            #print(linea.lstrip('\t') + " -> " + entrada + " = " + nombreVariable + '\n')

        #4 Traducir línea de escritura de datos en pantalla
        elif(bool(re.search(regexWrite, linea)) == True):
            codigo = re.findall(regexWrite, linea)
            entrada = str(codigo[0])
            nombreVariable = 'print(' + entrada + ')'
            archivoSalida.writelines('\t' * tabs + nombreVariable + '\n')
            #print(linea.lstrip('\t') + " -> " + nombreVariable + '\n')

        #5 Traducir condición IF
        elif (bool(re.search(regexIF, linea)) == True):
            ifs = ifs + 1
            tabs = tabs + 1
            codigo = re.findall(regexIF, linea)
            codigo = np.array(codigo)
            lineap = 'if (' + str(codigo[:,0]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[0:1,1]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[:,2]).lstrip("[' ").rstrip("'] ") + "):"
            archivoSalida.writelines('\t' * (tabs-1) + lineap + '\n')
            #print(linea.lstrip('\t') + " -> " + 'if (' + str(codigo[:,0]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[0:1,1]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[:,2]).lstrip("[' ").rstrip("'] ") + "):" + '\n')
        
        #5.1 Traducir condición IF con 1 operador AND
        elif (bool(re.search(regexIFAND, linea)) == True):
            ifs = ifs + 1
            tabs = tabs + 1
            codigo = re.findall(regexIFAND, linea)
            codigo = np.array(codigo)
            lineap = 'if ((' + str(codigo[:,0:3]).replace("'","").replace("[","").replace("]","") + ") and (" + str(codigo[:,3:6]).replace("'","").replace("[","").replace("]","") + ")):"
            archivoSalida.writelines('\t' * (tabs-1) + lineap + '\n')
            #print(linea.lstrip('\t') + " -> " + lineap + '\n')

        #5.2 Traducir condición IF con 1 operador OR
        elif (bool(re.search(regexIFOR, linea)) == True):
            ifs = ifs + 1
            tabs = tabs + 1
            codigo = re.findall(regexIFOR, linea)
            codigo = np.array(codigo)
            lineap = 'if ((' + str(codigo[:,0:3]).replace("'","").replace("[","").replace("]","") + ") or (" + str(codigo[:,3:6]).replace("'","").replace("[","").replace("]","") + ")):"
            archivoSalida.writelines('\t' * (tabs-1) + lineap + '\n')
            #print(linea.lstrip('\t') + " -> " + lineap + '\n')
        
        #6 Traducir condicion ELSE
        elif (bool(re.search(regexELSE, linea)) == True):
            archivoSalida.writelines('\t' * (tabs-1) + 'else:' + '\n')
            #print(linea.lstrip('\t') + " -> Else:"+ '\n')

        #7 Identificar fin de condición IF
        elif (bool(re.search(regexENDIF, linea)) == True):
            tabs = tabs - 1
            endifs = endifs + 1
        
        #8 Identificar contador
        elif (bool(re.search(regexCONT, linea)) == True):
            archivoSalida.writelines(linea.replace(";","") + '\n')
            #print(linea.lstrip('\t') + " -> " + linea.replace(";","").lstrip('\t') + '\n')

        #9 Traducir condición WHILE
        elif (bool(re.search(regexWHILE, linea)) == True):
            ifs = ifs + 1
            tabs = tabs + 1
            codigo = re.findall(regexWHILE, linea)
            codigo = np.array(codigo)
            lineap = 'while ('"int(" + str(codigo[:,0]).lstrip("[' ").rstrip("'] ") + ") " + str(codigo[0:1,1]).lstrip("[' ").rstrip("'] ") + " int(" + str(codigo[:,2]).lstrip("[' ").rstrip("'] ") + ")):"
            archivoSalida.writelines('\t' * (tabs-1) + lineap + '\n')
            #print(linea.lstrip('\t') + " -> " + 'while (' + str(codigo[:,0]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[0:1,1]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[:,2]).lstrip("[' ").rstrip("'] ") + "):" + '\n')

        #10 Identificar fin de ciclo WHILE
        elif (bool(re.search(regexENDWHILE, linea)) == True):
            tabs = tabs - 1
        
        #11 Identificar comparaciones entre dos variables
        elif (bool(re.search(regexCOMP, linea)) == True):
            codigo = re.findall(regexCOMP, linea)
            codigo = np.array(codigo)
            lineap = str(codigo[:,0]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[0:1,1]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[:,2]).lstrip("[' ").rstrip("'] ")
            archivoSalida.writelines('\t' * (tabs) + lineap + '\n')
            #print(linea.lstrip('\t') + " -> " + str(codigo[:,0]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[0:1,1]).lstrip("[' ").rstrip("'] ") + " " + str(codigo[:,2]).lstrip("[' ").rstrip("'] ") + "" + '\n')
    print("Archivo generado")

def interpretarArchivo(nombre):
    print("Interpretando ....")
    file = open(nombre, "r")
    os.system(file.name)

def getNombreArchivo(primerLinea, regex):
    subLinea = re.findall(regex, primerLinea)[0]
    return subLinea[1]


def inicializarArchivos(nombreArchivo):
    global archivo
    global archivoSalida
    archivo = open(nombreArchivo + ".iio", "r")
    archivoSalida = os.system(nombreArchivo + ".py")
    #archivoSalida = open(nombreArchivo + ".py", "w")

   
def start():
    global tabs
    global archivoSalida
    global archivo
    firstline = input("#>>")
    if bool(re.search(regexCompile, firstline)):
        main(archivo, archivoSalida)
        #inicializarArchivos(getNombreArchivo(firstline, regexCompile))

    elif bool(re.search(regexRun, firstline)):
        nombre = getNombreArchivo(firstline, regexRun)
        main(archivo, archivoSalida)
        inicializarArchivos(nombre)

    elif bool(re.search(regexLoad, firstline)):
        interpretarArchivo(getNombreArchivo(firstline, regexLoad) + ".py")

    elif firstline == "exit":
        print("Saliendo ....")
    else:
        print("ERROR, COMANDO NO RECONOCIDO")

start()
