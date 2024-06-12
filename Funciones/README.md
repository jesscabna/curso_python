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
 
 
 
 
 ### Argumen tos nominales  
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

  
## funciones internas  de python(tarea )
     
    
    






