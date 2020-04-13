# Python-Interpreter

The following python program is an interpreter that takes a text file with [PSeInt](http://pseint.sourceforge.net/) Pseudocode and translates it into Python code. 

The goal of this interpreter is two-fold:

1. Understand the logic necessary to develop simple programs, without the inconvenience of leading with a complicated syntax, which is ideal for beginners.
2. Once the user can actually write her own code, she can review the code generated in Python and in this way intuitively understand how that programming language works.

## How to use

Run the **Python** program called *Interpreter.py* , the program will then load the file "prueba1.iio" with the pseudocode we want to transalte to Python. You can modify this text file with different PSeInt Pseudocode.

**This file has to be in the same folder from which the program is running, otherwise, the user will have to enter the full path to the file.**

If the program finds an error with the input file, it will inform the user of the error and end the execution. Otherwise, the program will create the output file with the same name as the text file but with the Python code and in .py format.

The program can be run directly in the terminal and has 4 different option:

1. "Compile" which is simply going to translate the file. 
2. "Run" which is going to translate the file and then run the actual python program.
3. "Load" which let's the user load a .py file and run it.
4. "Exit" (self-explanatory)

## Example

* Pseudocode
  ```
  PROCESO principal;
    ESCRIBIR "Ingrese primer numero: ";
    DEFINIR num1 COMO REAL; 
    LEER num1;
    ESCRIBIR "Ingrese segundo numero: ";
    DEFINIR num2 COMO REAL; 
    LEER num2;
    ESCRIBIR "Ingrese tercer numero: ";
    DEFINIR num3 COMO REAL;
    LEER num3;
    SI ((num1 >= num2) Y (num1 >= num3));
      ESCRIBIR num1;
      SI (num2 >= num3);
        ESCRIBIR num2;
        ESCRIBIR num3;
      SINO;
        ESCRIBIR num3;
        ESCRIBIR num2;				
      FINSI;
    SINO;
      SI ((num2 >= num1) Y (num2 >= num3));
        ESCRIBIR num2;
        SI (num1 >= num3);
          ESCRIBIR num1;
          ESCRIBIR num3;
        SINO;
          ESCRIBIR num3;
          ESCRIBIR num1;				
        FINSI;
      SINO;
        SI ((num3 >= num1) Y (num3 >= num2));
          ESCRIBIR num3;
          SI (num1 >= num2);
            ESCRIBIR num1;
            ESCRIBIR num2;
          SINO;
            ESCRIBIR num2;
            ESCRIBIR num1;
          FINSI;
        FINSI;
      FINSI;	
    FINSI;

    ESCRIBIR "Ingrese numero: ";
    DEFINIR numero COMO ENTERO;
    LEER numero;
    DEFINIR contador COMO ENTERO;
    MIENTRAS (contador != numero) HACER;
      contador = contador+1;
      ESCRIBIR contador;
    FINMIENTRAS;
  FINPROCESO;
  ```
  
* Translated Output (Python)
  ```
  def main():
    print("Ingrese primer numero: ")
    num1 = 0.0
    num1 = input()
    print("Ingrese segundo numero: ")
    num2 = 0.0
    num2 = input()
    print("Ingrese tercer numero: ")
    num3 = 0.0
    num3 = input()
    if ((num1  >=  num2) and (num1  >=  num3)):
      print(num1)
      if (num2 >= num3):
        print(num2)
        print(num3)
      else:
        print(num3)
        print(num2)
    else:
      if ((num2  >=  num1) and (num2  >=  num3)):
        print(num2)
        if (num1 >= num3):
          print(num1)
          print(num3)
        else:
          print(num3)
          print(num1)
      else:
        if ((num3  >=  num1) and (num3  >=  num2)):
          print(num3)
          if (num1 >= num2):
            print(num1)
            print(num2)
          else:
            print(num2)
            print(num1)

    print("Ingrese numero: ")
    numero = 0
    numero = input()
    contador = 0
    while (int(contador) != int(numero)):
      contador = contador+1
      print(contador)
  main()
  ```
---
### Authors
* Joaquin Orantes
* Omar Eduardo Martinez



