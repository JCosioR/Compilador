grammar Comp;

inicio : 'Universe' '(' nombre ')' '{' instrucciones* '}';

nombre:;

instrucciones
    : declararVariables;

expr
    : expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # SumRes
    | '(' expr ')'             # Parentesis
    | NUM                      # Numero
    | VAR                      # Variable     // ← nuevo
    ;

VAR : [a-zA-Z_][a-zA-Z_0-9]* ;   // nombre de variable
NUM : [0-9]+ ('.' [0-9]+)? ;

/*
    Todos los proyectos deben tener un cascaron
    C - void main(int){
    }
        int main(){return 0;}

    JS -

    Java -  class N{}

    Xenia::();

    MyCat{}

    + 

    Definir gramatica al menos que funcione declarar vaable y asignar valores
    En calc nos fuimos directo a la asignacion y valida si ya existe previamente la variable
    
 */