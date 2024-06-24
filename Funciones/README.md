# FUNCIONES 
Matematica,enmte  una funcion es una operacion  que toma uno o as vaslores llamados
` argumrnts ` y produce3 un valor dominado 
` resultado `.
> [!NOTE]
>  Todos los lenguajes de programacion tienen funciones  incorporadas (` funciones internas`), y  funciones creadas por el usuario (` funciones externas`)

En programacion  una funcion es un subprograma , es unan estructura  que nos permite agrupar  codigos y  sus principales  objetivos son : 
- ` NO REPETIR ` Fracmento de codigo
-  ` REUTILIZAR`  EL CODIGO en distintos escenarios 
  

  ## estructura de una funcion  
  una funcion  viene ` defenida ` por un` nombre ` , sus `parametros ` y su valor de `retorno ` una vez creada la funcion  podremos solicitar su ejecucion `invocando `
  la funcion por su `nombre `.
  ## definir una funcion en python
para definir una funcion en python  primero utilizaremos la palabra reservada ` Def `  segida por el `nombre`  de la funcion . a continuacion espesificaremos LOS `PARAMETROS `  con ` ()` sim es una funcion sin parametros , `(a)` si es una funcion con parametros ,  si se tuviera  mas de un parametro iran sepaRADOS  por `,` ,  finalizaremos la linea con `:`  en la siguiemte linea sin olvidar  el identado , comenzaremos el `cuerpo ` de la funcion  ( micro programa )  se puede tener uno o mas sentencias ,  finalmente devera `retornar`  un resultado con la palabra  reservada `return`.
> [!TIP]
> como retorno tambien se puede utlizar  la ` funcion interna ` , `print ()` ,  para depuracion de codigo  no es recomendable usarlo  en producccion . 
>  `print` dentro de una funcion es una herramienta para depurar un codigo 
**ejemplo:**
```python
def saludo ():
    saludo="hola mundo "
    saludo_dos="como estas"
    return f{saludo},{saludo_dos}
    #print(f"{saludo},{saludo_dos}")
print(saludo())    
#saludo()
```
## invocar una funcion 
 para invocar , (o lamar , ejecutar ) una funcion solo tendremos  quye escribir un `nombre`  de la funcion segido por `()` párentesis .
 ```python
 def saludo():
    print("hola")
 #invocando la funcion 
 # saludo()
 ```
 ## retorna un valor 
  las funciones pueden retorar un valor  (o devolver ) un valor 
  ```python
  def uno():
    return 1
  uno ()
  ```
  > [!WARNING]
> no confundir  ` print ()` con `return`  el valor retornado por `return ` nos permiten usarlo  fuera desu contexto . y `print()` solo mostrara  el literal por terminal .
**ejemplo**
* en el archivo de `lecture.py`


##  retornando multiples valores
 el secreto es hacerlo mediante  un tipo de dato estructurado 
 ```python
 def varios ():
    return 3,3,4
 varios()  
 #retorna (2,3,4)
 def lista ():
    return ["hola",45] 
    #retorna ["hola" ,45]
  lista ()
  def dicc ():
    return {"nombre":"jose","edad ": 45}  
dicc ()
#retorna {"nombre":"jose","edad ": 45}  
 ```

 ## parametros y argumentos
 si una funcion  no disousiera de valopres  de entrada estariaq limitada  en su actuacion  es por ello ello que los  `parametros`  no permiten variar  los datos que comsume  una funcion  para obtener  disitintos  resultados 
 **ejemplo** 
 *crear una funcion que  un valor numerico y retorna su raiz cuadrada*
 ```python
 def sqrt(valor);
 return valor**(1/2)
 sqrt(4)
 #NOTA: EN ESTE CASO EL VALOR 4 ES UN ARGUMENTO DE UNA FUNCION 
 ```
 CUANDO LLAMAMOS  a una funcion con `argumentos` los valores de estos argumentos se copian en los correspondientes `parametros ` dentro de la funcion 
 ```python
 def  ejm (a,b,c):
  return a+b+c
 ejm(4,5,6) 
 ```
 
 
 
 
 ### Argumentos nominales  
  en esta aproxi,acion  no son copiados  en un orden especificos  si nom que **se asingnan por nombre a cada paramtro** .  ello nos permite  evitar el problema  conocre o recordar  cua es el orden  de los parametros en la defenicion  de la funcion  . 
  para utilizarlo , basta con realizar una asignacion  de cda argumento  en la propia llamada de la funcion 
  **Ejemplo**
  ```python
  def build_cpu(familia,num_core,frecuencia):
    print(f"""
    el cpu es de la familia {familia},
    con{num_core} cores y con una  frecuenmcia de {frecuemcia}
    
    
     """)
     # haciendo uso de argumentos nominales 
     build_cpu(num_core=4,familia="intel" ,frecuencia=2.7)
     # uso de argumentos pocicionales
     build_cpu("intel" , 4,2.7)
     
```
### Parametros por defectos
  es posible especificar valores por defectos em los parametro de una funcion  en el caso de que no se proporcione  un valor al argumento  en la llamadqa de la funcion   el parametro correspondiente  tomara unm valor defenidom, por defecto
  **ejemplo**
  ```python
  def alumno(nom,app,estado="aprobado"):
    alumnos=("ruth","castillo")   
    alumnos("antoni","cruzes","desaprobado")

  ```
  ## desempaquetado/ empaquetado de argumentos(tarea)

  Python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para argumentos posicionales como para argumentos nominales.
  ### Empaquetar/Desempaquetar argumentos posicionales
  Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una tupla.
  **Ejemplo**
  ```python
  #Para superar esta «limitación» vamos a hacer uso del * para empaquetar los argumentos posicionales:
  def _sum(*values):
    print(f'{values=}')
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result


_sum(4, 3, 2, 1)
#values=(4, 3, 2, 1)
10

#Existe la posibilidad de usar el asterisco * en la llamada a la función para desempaquetar los argumentos posicionales:
values = (4, 3, 2, 1)

_sum(values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in _sum
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'

# Desempaquetado: _sum(4, 3, 2, 1)
_sum(*values)
values=(4, 3, 2, 1)
10
```
### Empaquetar/Desempaquetar argumentos nominales
Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos indicando que los argumentos pasados a la función se empaqueten en un diccionario.
**Ejemplo**
```python
#queremos encontrar la persona con mayor calificación de un examen. Haremos uso del ** para empaquetar los argumentos nominales:
def best_student(**marks):
    print(f'{marks=}')
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student


best_student(ana=8, antonio=6, inma=9, javier=7)

#marks={'ana': 8, 'antonio': 6, 'inma': 9, 'javier': 7}
#'inma'


#Al igual que veíamos previamente, existe la posibilidad de usar doble asterisco ** en la llamada a la función para desempaquetar los argumentos nominales:
marks = dict(ana=8, antonio=6, inma=9, javier=7)

best_student(marks)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: best_student() takes 0 positional arguments but 1 was given

# Desempaquetado: best_student(ana=8, antonio=6, inma=9, javier=7)
best_student(**marks)
marks={'ana': 8, 'antonio': 6, 'inma': 9, 'javier': 7}
'inma'
```

  
## funciones internas  de python(tarea )

### Funciones list, type y tuple
- List(). Con esta función se puede crear un listado y aportan un gran nivel de flexibilidad al trabajar con conjuntos de datos.
- Type(). Se trata de una función básica de Python que se utiliza principalmente con objetivos de depuración de código.
- Tuple(). Permiten crear una lista, pero con dos características diferentes (inmutabilidad, pues sus valores no pueden ser modificados, y rapidez, pues su uso acelera el proceso de cálculo).
  

### Funciones de texto
- Print(). Una función básica de Python y que también podemos encontrar en la mayoría de lenguajes de programación, y cuyo fin es mostrar en pantalla un valor (texto o valores).
- Len(). Función para contar el número de caracteres de una cadena de entrada y devolver su valor.
- Replace(). Otra función de texto interesante de este lenguaje de programación que permite sustituir caracteres dentro de una cadena.
- Str(). Conocido también como string, es una función que devuelve la representación de cadena de un número (presenta una secuencia inmutable de caracteres Unicode).
- Ord(). Es una función que muestra el valor ASCII de una cadena de un carácter determinado.
- Input(). Es una función que se utiliza para la entrada de datos por parte de un usuario en los programas desarrollados en Python.
- Chr(). Devuelve la cadena correspondiente a un número entero en relación con el código Unicode (por ejemplo, chr(97)) devuelve la cadena “a”.
  
### Funciones numéricas
- Sum(). Una función muy interesante que facilita la suma de valores de una lista o tupla en Python (siempre hablando de números como valores).
- Min(). Con esta función se puede hallar el número más pequeño dentro de una lista, tupla o dos o más argumentos.
- Max(). La función contraria a Min() que, en lugar del número más pequeño, devuelve el valor más grande o mayor.
- Range(). Función de Python para generar una sucesión de números enteros de forma personalizada.
- Round(). Cuando se trabaja con números matemáticos es importante disponer de una función capaz de realizar redondeos después de la coma, siendo esta la función de Python que se encarga de este proceso.
- Hex (). Esta función que se incorporó a partir de la versión 3 de Python, convierte un número entero en una cadena hexadecimal con prefijo “0x”.
- Abs(). Al utilizar esta función sobre un número se obtiene su valor absoluto.
- Id(). Se trata de una función nativa que muestra un número entero que es único para cada objeto en memoria.
- Bin(). Convierte un número entero en una cadena binaria incluyendo el prefijo “0b”.
- float (). El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales. Si vienes de otros lenguajes, tal vez conozcas el tipo doble, lo que significa que tiene el doble de precisión que un float. En Python las cosas son algo distintas, y los float son en realidad double.
- int (). Los enteros en Python o también conocidos como int, son un tipo de datos que permite representar números enteros, es decir, positivos y negativos no decimales. 
- boleano(). Al igual que en otros lenguajes de programación, en Python existe el tipo bool o booleano. Es un tipo de dato que permite almacenar dos valores True o False.



## TIPOS DE FUNCIONES 
### FUNCIONES ANONIMAS (funciones lambda)
una funcion que no tiene nombre , no hacen uso de la palabra reserbvada def 
```python
lamba:"hola"
#normal

def saludo():
  return "hola"
```
### funciones closure 
na funcion que no tiene nombre
` def saludo (nombre):`
### funciones callback
 son funciones que por parametros reciben otra funcion
`int (input("ingresde un numero"))`

### programacion funcional 
la programacion fun cionaal no requiere que sepas como se desarrolla el proceso de la ejecusi0on
***ejemplo**



```python
lista=[5,7,6,4,1,]
def num_minimo(l):
  minimo=l[0]
  for n in l:
    if n < minimo:
    minimo=n
    return minimo

 ```   

 #### averiguar sobre map() ,  filter() , reduce()

     
    
    






