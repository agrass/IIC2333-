############## READ ME ######################
Nuestro programa funciona con un menu principal desde el cual se pueden ejecutar 
las siguientes funciones:
menu: Imprimir Menu
top: Funcion Top
read: Carga un Archivo
1: Llamar
2: Enviar Mensaje
3: Ver Agenda de Contactos
4: Agregar Nuevo Contacto
5: Ver Historial de Llamadas
6: Ver Historial de Mensajes
q: Salir

Todos los procesos son agendados mediante un scheduler.  La funcion read manda 
los procesos al scheduler para ser agendados y estos procesos son ejecutados
en su debido tiempo sin embargo no son mostrados en pantalla para poder ejecutar
otros procesos paralelamente. Para poder ver cuando cada proceso es ejecutado 
ver el archivo log donde se guarda el proceso y el momento en el cual fue 
ejecutado un proceso.

Tarea 2 :
El algoritmo de agendamiento en el scheduler fue cambiado a Round Robin con
dos ciclos como tiempo. Agregamos a la cola ready envejecimiento por prioridad 
cada cinco ciclos. Para sincronizar los procesos que bloquean utilizamos locks, 
existe un lock por cada periferico. Cuando una proceso pasa a estado running
verifica los perifericos bloqueados, si ya esta tomado el lock pasa a waiting,
si no esta tomado el lock lo toma y bloquea otros procesos. Al mismo tiempo la 
cola waiting chequea el estado de los locks en cada ciclo, en caso de liberarse
se traspasan todos los procesos a estado ready que ya no esten bloqueados.
Un proceso suelta los locks cuando pasa a estado finish.