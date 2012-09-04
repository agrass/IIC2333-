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