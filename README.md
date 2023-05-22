# ZoologicoMaravilla
Proyecto Zoológico/Jeysa Blandon/David Salazar

Este proyecto es una simulación de programa de un zoológico, subida en la nube como una aplicación, en la cual 
interactúa el usuario como si fuera el trabajador o dueño del zoológico, permitiendo crear 
habitats, crear animales, agregarlos a un habitat, ver la información de las habitats y sus 
animales, editar la alimentación y ejecutar ciertas acciones básicas de los animales.

>Por medio de este link podrás ver el diagrama del proyecto:
> https://drive.google.com/file/d/1zXjpDog5POwmmweIJ8GGd6y8SA__m-Nb/view?usp=sharing

>Por medio de este link podrás entrar a la aplicación del proyecto en la nube:
> https://jeysa30-zoologicomaravilla-main-dysnsq.streamlit.app


# Funcionamiento del programa
Nuestro programa esta implementado con el sistema de modelo, vista y controlador:

## Modelos:
En el modelo de nuestro programa se encuentran las clases principales, que son las siguientes:

* Zoologico
: Nuestra clase zoologico contiene una lista de habitats y un registro de los animales que
  fueron creados en el zoologico, además tiene los id´s del proximo habitat que se va a crear
  y del proximo animal, dandole un id unico a cada objeto nuevo de estas clases que se crea 
  en el programa.  
 

  La clase tiene los métodos básicos para agregar un habitat a la lista de habitats y otro para
  agregar un animal a la lista de registro, como los animales pueden pasar de estar en el 
  registro del zoologico a estar en un habitat, también esta el método de eliminar del registro.
  Esta clase además tiene metodos para seleccionar opciones mediante un selectbox de la
  libreria streamlit, como el método listarAnimalesRegistro que muestra la información de los 
  animales que se encuentran en el registro del zoologico para que el usuario pueda elegir uno,
  otro método que sirve para algo similar es listarHabitats, pero en este se muestra la
  información de los habitats creados que cumplan con la condición de los requisitos del animal
  que se le pasa como parametro, por otro lado, si queremos ver todos los animales que tiene el
  zoologico dentro de cada una de sus habitats está el método listarAnimalesHabitats, el cual
  recorre cada habitat y mustra la información de cada animal para que el usuario pueda
  seleccionar alguno.


* Habitat
: Esta clase tiene como atributos, el nombre, la temperatura máxima y minima 
  que alcanza el habitat, la cantidad máxima de animales que puede contener el habitat, la
  cantidad de animesles que se encuentran en el habitat, el tipo de dieta que pueden tener los
  animales que van a vivir en esa habitat, el id del habitat, para que sea un objeto unico, y 
  por ultimo una lista que contiene animales.  
 

  En esta clase tenemos un método que sirve para agregar el animal a la lista de animales, lo
  más importante de esta clase es que se usa la definición de herencia, para así poder crear
  los 4 tipos de habitats que se pueden crear (Desierto, selva, polar, acuatico), en cada una
  de estas clases hijas hay 2 atributos nuevos, para que así se diferencien entre si.

* Animal
: En esta clase tenemos los atributos nombre, la especie pertenciente al animal, la temperatura
  promedio en la que puede vivir el animal, su respectivo id, la edad, el estado de salud actual,
  la cantidad de horas que puede dormir, y un atributo que maneja la cantidad de horas que le 
  quedan por dormir en ese día (Atributo temporal), la cantidad de kg de comida que puede comer 
  al día, y otro atributo que maneja la cantidad de kg que le quedan por comer en el día 
  (Atributo temporal), un atributo booleano para saber si el animal ya jugo en el día y por 
  ultimo un atributo dieta el cual es otra clase de la que se hablara más adelante.

* Dieta
: Como se menciono anteriormente la clase dieta esta incluida en la clase animal, esta clase 
  cuenta con 3 atributos, los cuales son el nombre de la dieta, ya sea omnivoro, carnivoro o 
  herbivoro, otro atributo que es una lista que guarda los alimentos que pueden comer los animales
  con ese tipo de dieta, y otra lista que guarda los alimentos que el usuario le puede agregar a 
  la alimentación del animal(para cada dieta son listas diferentes).  
 

  Esta clase tiene un método que agrega los alimentos a las listas anteriormente mencionadas,
  tiene otros métodos que sirven para agregar y eliminar un alimento a 
  la lista que le pasemos como parametro, esto es así para utilizar el mismo método para agregar
  y eliminar a las 2 listas de la clase, tenemos 2 métodos parecidos a los que tenemos en la clase
  zoologico, los cuales son listarAlimentos y listarPosiblesAlimentos, estos nos muestran los
  alimentos que estan en alguna de las 2 listas de la clase, para que de esta forma el usuario 
  seleccione uno.

## Vista:
En la vista de nuestro programa tenemos una clase que se encarga de mostrarle y pedirle la
información al usuario.

* Zoo
: Como se mencionó anteriormente esta clase se encarga de la interacción con el usuario, esto lo
  hace mediante los 2 atributos, que tienen la clase zoologico y la clase controladora.  
 

  los métodos que tenemos en esta clase son, menuZoo que se encarga de mostrar mediante un 
  expander el menu al usuario de las opciones que puede realizar en el zoologico, con sus 
  respectivos buttons retrornando el número del boton presionado, otro método de la clase es 
  menuHabitat, el cual le muestra al usuario con una selectbox los 4 tipos de habitats que puede
  crear, con sus respectivas temperaturas, también retorna el número de la opción escogida;
  para poder seleccionar el tipo de dieta del animal y del habitat tenemos el método elegirDieta
  que también le muestra al usuario las opciones de dietas mediante un selectbox; hay además otros
  métodos para solicitarle datos al usuario, al igual que para mostrarle información; así mismo
  contamos con el método menuAccion, que le permite al usuario ver mediante buttons, 3 tipos de 
  acciones que puede hacer el animal; como también esta el método menuAlimento, en el cual se le
  muestran 2 buttons al usuario, para que pueda agregar o eliminar un alimento de la dieta del
  animal; por ultimo esta el método mostrarTodoZoo, este lo que hace es mostrarle la información al
  usuario de todas las habitat que hay en el zoologico y los animales que estan dentro de estos.
  
## Controlador:
En el controlador de nuestro programa tenemos una clase que nos permite conectar las clases que
están en el modelo y la vista para así implementar toda la lógica necesaria.

* ZoologicoController  
: Para poder hacer la conexion y la implementación de la lógica del programa esta clase debe 
  tener como atributos la clase modelo principal(Zoologico) y la clase vista(Zoo).  


  El primer método de esta clase es ejecutarMenu, este recibe el número del boton que oprimio
  el usuario en el menuZoo y ejecuta el método correspondiente.  


  El siguiente método es crearHabitat en el cual llamamos el método de la vista menuHabitat, que
  nos da el tipo de habitat seleccionada por el usuario, además se llama otro método de la vista
  elegirDieta, que retorna el tipo de dieta selecionada para el habitat que se va a crear, también
  se le pide a la vista la cantidad maxima de animales que pueden vivir en el habitat, después 
  dependiendo de lo que nos retorne el método menuHabitat creamos una u otra clase hija de la 
  clase habitat, al final solo se agrega al zoologico si se presiona el boton y se tienen todos
  los campos del habitat con un valor valido.  


  El tercer método que podemos encontrar en la clase es crearAnimal en la cual se le pide al 
  usuario mediante la clase vista todos los datos que corresponden al animal, cuando se terminan
  de llenar estos datos el usuario debe presionar el boton para que el animal se cree con toda la
  información y se agregue al registro del zoologico.  


  Otro método perteneciente a la clase es agregarAnimalHabitat, este llama el método de la clase
  zoologico listarAnimalesRegistro y retorna el animal que eligio el usuario, después este animal
  se le pasa como parametro al método listarHabitats para que el usuario seleccione el habitat
  a donde se agregara el animal que se eligio, cuando el usuario oprima el boton y los 2 campos 
  esten llenos se agregara este animal al habitat seleccionada y se eliminara del registro.  


  También se encuentra el método modificarAlimentacion, en el se llama un método del modelo 
  listarAnimalesHabitats para que el usuario seleccione el animal que le va a modificar la
  alimentación, además el método menuAlimento de la clase vista retorna la opción que quiere
  elegir el usuario, dependiendo de la opción se listan los alimentos que se pueden agregar a la
  dieta del animal o los que se pueden eliminar de su dieta y se ejecuta dicha acción.  


  por ultimo, tenemos el método accionesAnimales, este método se encarga de las acciones que pueden
  realizar los animales, igual que en el método anterior se llama listarAnimalesHabitats para que
  el usuario elija el animal, después se llama el método de la vista menuAccion, para saber que 
  accion va a realizar el animal y dependiendo de la accion se le pide al usuario los datos, como 
  la cantidad de horas o de kg y si esta cantidad ingresada es menor o igual a la cantidad 
  temporal se ejecuta la acción o para el caso de jugar, se revisa si el atributo es False o True
  para que el animal pueda realizar la acción.

# Evidencia del funcionamiento del programa

* Menú principal del zoológico:
: ![Menu principal.jpg](Menu%20principal.jpg)

* Se muestra la opción donde se crear un habitat:
: -Creamos el habitat polar
![Se crea el habitat.jpg](Se%20crea%20el%20habitat.jpg)

* Se muestra la opción donde se crea un animal:
: ![Crea y agrega un animal al zoologico 1.jpg](Crea%20y%20agrega%20un%20animal%20al%20zoologico%201.jpg)
![Crea y agrega un animal al zoologico 2.jpg](Crea%20y%20agrega%20un%20animal%20al%20zoologico%202.jpg)

* Se agrega el animal a un habitat si cumple los requisitos:
: ![agregar un animal a un habitat .jpg](agregar%20un%20animal%20a%20un%20habitat%20.jpg)

* Se modifica el alimento del animal ya estando en el habitat:
: -Agregar alimento
![Modificar alimento agregar.jpg](Modificar%20alimento%20agregar.jpg)
- Eliminar alimento
![Modificar alimento eliminar.jpg](Modificar%20alimento%20eliminar.jpg)

* Se realiza las siguientes acciones al animal:
: -Acción de comer
![animal comer.jpg](animal%20comer.jpg)
-Acción de dormir
![animal dormir.jpg](animal%20dormir.jpg)
-Acción de jugar
![animal jugar.jpg](animal%20jugar.jpg)

* Por ultimo se puede ver la información del zoológico:
: ![ver informacion.jpg](ver%20informacion.jpg)
![ver info 1.jpg](ver%20info%201.jpg)
![ver info 2.jpg](ver%20info%202.jpg)