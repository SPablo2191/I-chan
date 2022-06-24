import csv
class imp_doc:
    def minuscula(self,lista):
        for i in range (len(lista)):
            lista[i]=lista[i].lower()
    #---------recuperar contenido del csv---------------
    def leer_csv(self):
        with open('preguntas_respuesta.csv', newline='',encoding='utf-8') as File:  
            reader = csv.reader(File,delimiter=';')
            preguntas=list(reader)
        return preguntas
    def escribir_csv(self,fila):
        f = open('preguntas_respuesta.csv','a', newline='',encoding='utf-8')
        f.write(fila)
        f.close()

    def vectorizar_matriz(self,lista1,lista,columna):
        for i in range (len(lista1)):
            lista.append(lista1[i][columna].lower())
