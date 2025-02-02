class Libro():
    __cuenta = 0
    def __init__(self, titulo, autor, editorial, year, aumentar):
        #self.__num_ejemplar = int(num_ejemplares)
        if aumentar == True:
            Libro.__cuenta = Libro.__cuenta + 1 #Aumenta cuando se crea un libro
        self.__id_libro = Libro.__cuenta # id unico!
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__year = year
        #Libro.__cuenta = Libro.__cuenta + 1 #Aumenta cuando se crea un libro


    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_editorial(self):
        return self.__editorial

    def get_year(self):
        return self.__year

    def get_id_libro(self):
        return str(self.__id_libro)


    def __str__(self):
        return "Titulo: {}, Autor: {}, Editorial: {}, Año: {}, id: {}".format( self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_year(), self.get_id() )
