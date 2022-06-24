#--------librerias------------
#inteligencia artificial
import random
import stanza
import string
#machine learning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#editor
from Imp_csv import imp_doc  #importamos esta libreria para poder leer la lista de preguntas
class i_chan_Bot:
    preguntas=[]
    nlp = stanza.Pipeline('es')
    editor=imp_doc()
    preguntas=editor.leer_csv()
    lista_preguntas=[]
    lista_respuestas=[]
    editor.vectorizar_matriz(preguntas,lista_preguntas,0)
    editor.vectorizar_matriz(preguntas,lista_respuestas,1)
    def LemTokens(self,tokens):
        aux=""
        for i in range(len(tokens)):
            aux=aux+tokens[i]+" "
        doc=self.nlp(aux)
        vector=[]
        for sent in doc.sentences:
            for word in sent.words:
                vector.append(word.lemma)
        return vector #recibe una lista de strings, y va uno por uno realizando el proceso de lematizacion

    remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation) #arma una lista para eliminar signos de puntuacion
    def RespuestasPeronistas(self,entrada):
        respuesta=""
        if(entrada=="¿De que trata este proyecto?"):
            respuesta="El objetivo de este proyecto es el desarrollo de un chatbot para la pagina web del grupo de investigación IDEAS de la Facultad de ingeniería de la universidad católica de Salta, presente en una interfaz conversacional sencilla y que integre tecnologías Machine Learning y Procesamiento de Lenguaje Natural (PLN), con las que pueda responder cualquier consulta del usuario relacionada a las actividades del grupo.<br /><br /><br /><br /><br /><br /><br /><br /><br /><br />"
        if(entrada=="¿Qué es IDEAS?"):
            respuesta="Es un grupo de incubación de trabajos de investigación de alumnos de la Facultad de ingeniería de la universidad católica de Salta."
        if(entrada=="Como funciona 'I-Chan'?"):
            respuesta="A partir de que el usuario formula su consulta, ‘I-Chan’ inicia un proceso de tratamiento, análisis y evaluación empleando procesos como la lematización y herramientas de medida como el TF-IDF y la similitud de Coseno a fin de poder hallar la semejanza entre la consulta hecha y las preguntas disponibles en su base de datos; si existe alguna con un grado de similitud alto se retornara la respuesta a dicha pregunta."
        return respuesta



    def LemNormalize(self,text):
        doc = self.nlp(text.lower().translate(self.remove_punct_dict))
        aux=[]
        for i, sentence in enumerate(doc.sentences):
            for token in sentence.tokens:
                aux.append(token.text)
        return self.LemTokens(aux)
    #-----------------------------------------------RESPUESTA Saludo----------------------------------------------------
    lista_saludos_usuario=["Hola",
    "Buenos Dias",
    "buenas noches",
    "buenas tardes",
    "Que onda?",
    ]
    lista_saludos_bot=[
        "Hola! Mucho Gusto Soy I-Chan, Bot Diseñado para responder tus dudas del Grupo IDEAS, Que te gustaria consultarme?",
        "Saludos! Soy I-Chan, Un gusto conocerte, de que te gustaria hablar?",
        "Buenos Dias, soy el bot conversacional del grupo IDEAS, Cualquier duda que tengas puedo responderla"
    ]
    lista_charla_usuario=["¿Como estas?",
    "¿Todo bien?",
    "¿Cómo vas?",
    "¿Qué tal?",
    "¿Cómo estás?",
    "¿Cómo está?",
    "Como Andas?",
    "¿Cómo va?"]
    lista_charla_bot=[
        "Muy bien, Muchas gracias por preguntar!",
        "Genial! Listo para responder cualquier duda que tengas del grupo",
        "Estoy muy bien! y espero que tu tambien😁"
    ]
    #pasar a minuscula las oraciones
    editor.minuscula(lista_saludos_usuario)
    editor.minuscula(lista_charla_usuario)
    #-----------------------------------------------
    def saludos(self,entrada_usuario):
            print("entro en modulo 'saludos'")
            self.lista_saludos_usuario.append(entrada_usuario)
            vector_tfidf=TfidfVectorizer(tokenizer=self.LemNormalize,encoding='utf-8',strip_accents='unicode')
            tfidf=vector_tfidf.fit_transform(self.lista_saludos_usuario)
            matriz_coseno=cosine_similarity(tfidf[-1],tfidf)
            flat=matriz_coseno.flatten() #convierte en vector la matriz
            flat.sort() #ordena el vector de menor a mayor
            freq_max_tfidf=flat[-2]
            self.lista_saludos_usuario.remove(entrada_usuario)
            print(" precision: ",freq_max_tfidf)
            if(freq_max_tfidf>0.5):
                return random.choice(self.lista_saludos_bot)
    def charla_Basica(self,entrada_usuario):
            print("entro en modulo 'charla basica'")
            self.lista_charla_usuario.append(entrada_usuario)
            vector_tfidf=TfidfVectorizer(tokenizer=self.LemNormalize,encoding='utf-8',strip_accents='unicode')
            tfidf=vector_tfidf.fit_transform(self.lista_charla_usuario)
            matriz_coseno=cosine_similarity(tfidf[-1],tfidf)
            flat=matriz_coseno.flatten() #convierte en vector la matriz
            flat.sort() #ordena el vector de menor a mayor
            freq_max_tfidf=flat[-2]
            self.lista_charla_usuario.remove(entrada_usuario)
            print(" precision: ",freq_max_tfidf)
            if(freq_max_tfidf>0.5):
                return random.choice(self.lista_charla_bot)


    #------------------------------------------------RESPUESTA AGRADECIMIENTO Y DESPEDIDA---------------------------------------------------------------
    lista_despedida_usuario=["Adiós",
    "Nos vemos",
    "Saludos",
    "Hasta pronto",
    "Hasta siempre",
    "Hasta luego",
    "Hasta nunca",
    "Hasta mañana",
    "Hasta la otra semana",
    "Hasta el próximo fin de semana.",
    "Te veo luego",
    "Chao",
    "Chau",
    "¡Cuídate!",
    "Nos estamos viendo"]
    lista_despedida_bot=[
        "Adiós",
    "Nos vemos",
    "Saludos",
    "Hasta pronto",
    "Chau"
    ]
    lista_agradecimiento_usuario=[
        "Muchas Gracias",
        "Gracias",
        "Te lo agradezco"
    ]
    lista_respuestas_bot=[
        "De nada",
    "Es un placer",
    "Estoy para servirle"
    ]
    editor.minuscula(lista_despedida_usuario)
    editor.minuscula(lista_agradecimiento_usuario)
    def Respuesta_Despedida(self,entrada_usuario):
            print("entro en modulo 'despedida'")
            self.lista_despedida_usuario.append(entrada_usuario)
            vector_tfidf=TfidfVectorizer(tokenizer=self.LemNormalize,encoding='utf-8',strip_accents='unicode')
            tfidf=vector_tfidf.fit_transform(self.lista_despedida_usuario)
            matriz_coseno=cosine_similarity(tfidf[-1],tfidf)
            flat=matriz_coseno.flatten() #convierte en vector la matriz
            flat.sort() #ordena el vector de menor a mayor
            freq_max_tfidf=flat[-2]
            self.lista_despedida_usuario.remove(entrada_usuario)
            print(" precision: ",freq_max_tfidf)
            if(freq_max_tfidf>0.5):
                return random.choice(self.lista_despedida_bot)
    def Respuesta_Agradecimiento(self,entrada_usuario):            
            print("entro en modulo 'agradecimiento'")
            self.lista_agradecimiento_usuario.append(entrada_usuario)
            vector_tfidf=TfidfVectorizer(tokenizer=self.LemNormalize,encoding='utf-8',strip_accents='unicode')
            tfidf=vector_tfidf.fit_transform(self.lista_agradecimiento_usuario)
            matriz_coseno=cosine_similarity(tfidf[-1],tfidf)
            flat=matriz_coseno.flatten() #convierte en vector la matriz
            flat.sort() #ordena el vector de menor a mayor
            freq_max_tfidf=flat[-2]
            self.lista_agradecimiento_usuario.remove(entrada_usuario)
            print(" precision: ",freq_max_tfidf)
            if(freq_max_tfidf>0.5):
                return random.choice(self.lista_respuestas_bot)
    #--------------------------------------------------RESPUESTA INFORMATIVA-----------------------------------------------------------------------------
    #comparar similitud con pregunta "entrenada"
    def comp_pregunta(self,entrada_usuario):
        print("Esta comparando preguntas")
        i_respuesta=""
        self.lista_preguntas.append(entrada_usuario)
        vector_tfidf=TfidfVectorizer(tokenizer=self.LemNormalize,encoding='utf-8',strip_accents='unicode')
        tfidf=vector_tfidf.fit_transform(self.lista_preguntas)
        matriz_coseno=cosine_similarity(tfidf[-1],tfidf)
        idx=matriz_coseno.argsort()[0][-2]
        flat=matriz_coseno.flatten() #convierte en vector la matriz
        flat.sort() #ordena el vector de menor a mayor
        freq_max_tfidf=flat[-2]
        print(" precision: ",freq_max_tfidf)
        if(round(freq_max_tfidf,1)<0.5):
            return self.comp_respuesta_informativa(entrada_usuario,idx,freq_max_tfidf)
        else:
            i_respuesta=i_respuesta+self.lista_respuestas[idx]
            self.lista_preguntas.remove(entrada_usuario)
            return i_respuesta

    def comp_respuesta_informativa(self,entrada_usuario,indice_comp,freq_comp):
        print("entro en comparar respuestas")
        i_respuesta=""
        self.lista_respuestas.append(entrada_usuario)
        vector_tfidf=TfidfVectorizer(tokenizer=self.LemNormalize,encoding='utf-8',strip_accents='unicode')
        tfidf=vector_tfidf.fit_transform(self.lista_respuestas)
        matriz_coseno=cosine_similarity(tfidf[-1],tfidf)
        idx=matriz_coseno.argsort()[0][-2]
        flat=matriz_coseno.flatten() #convierte en vector la matriz
        flat.sort() #ordena el vector de menor a mayor
        freq_max_tfidf=flat[-2]
        print(" precision: ",freq_max_tfidf)
        if(freq_comp!=0 or freq_max_tfidf!=0):
                    if(freq_comp<freq_max_tfidf and round(freq_comp,1)<=0.2):
                        if(round(freq_max_tfidf,1)<0.2):
                            i_respuesta=i_respuesta+"Perdon soy incapaz de responder tu consulta 😥. Podria reformular su pregunta?"
                            self.lista_respuestas.remove(entrada_usuario)
                            return i_respuesta
                        else:
                            i_respuesta=i_respuesta+self.lista_respuestas[idx]
                            self.lista_respuestas.remove(entrada_usuario)
                            registro_csv=entrada_usuario+";"+self.lista_respuestas[idx]
                            self.editor.escribir_csv(registro_csv)
                            preguntas=self.editor.leer_csv()
                            self.lista_preguntas.clear()
                            self.lista_respuestas.clear()
                            self.editor.vectorizar_matriz(self.preguntas,self.lista_preguntas,0)
                            self.editor.vectorizar_matriz(self.preguntas,self.lista_respuestas,1)
                            return "La respuesta mas aproximada a tu pregunta es: <br/>"+i_respuesta
                    else:
                        i_respuesta=i_respuesta+self.lista_respuestas[indice_comp]
                        self.lista_respuestas.remove(entrada_usuario)
                        registro_csv=entrada_usuario+";"+self.lista_respuestas[indice_comp]
                        self.editor.escribir_csv(registro_csv)
                        preguntas=self.editor.leer_csv()
                        self.lista_preguntas.clear()
                        self.lista_respuestas.clear()
                        self.editor.vectorizar_matriz(self.preguntas,self.lista_preguntas,0)
                        self.editor.vectorizar_matriz(self.preguntas,self.lista_respuestas,1)
                        return "La respuesta mas aproximada a tu pregunta es: <br/>"+i_respuesta
        else:
            i_respuesta=i_respuesta+"Perdon soy incapaz de responder tu consulta 😥. Podria reformular su pregunta?"
            self.lista_respuestas.remove(entrada_usuario)
            return i_respuesta

    #--------------------------------------------Analisis de pregunta---------------------------------------------------------
    def Responder(self,entrada_usuario):
        if(self.saludos(entrada_usuario)==None):
            if(self.charla_Basica(entrada_usuario)==None):
                if(self.Respuesta_Despedida(entrada_usuario)==None):
                    if(self.Respuesta_Agradecimiento(entrada_usuario)==None):
                        return self.comp_pregunta(entrada_usuario)
                    else:
                        return self.Respuesta_Agradecimiento(entrada_usuario)
                else:
                    return self.Respuesta_Despedida(entrada_usuario)
            else:
                return self.charla_Basica(entrada_usuario)
        else:
            return self.saludos(entrada_usuario)

