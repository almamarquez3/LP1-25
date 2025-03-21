class Dibujador:


    def dibujo_perro(self):
        # Los dibujos tienen el problema de que si usan triple
        # comillas, se te meten los espacios o rompes la
        # indentacion. Son cosas feas de Python.
        # hay varias formas de solucionarlo
        # creo que la mas simple es usar el caracter enter
        # se escribe \n, eso mete enters.
        return "^..^      /\n/_/\\_____/\n   /\\   /\\\n  /  \\ /  \\"
    
    def dibujo_gato(self):
        # Otra forma es meter en varias variables
        # y juntarlas con enters usando join.
        # aunque aca hay que usar listas y puede
        # que no se entienda
        linea_1 = "                        _"
        linea_2 = "                       | |"
        linea_3 = "                       | |"
        linea_4 = "                       | |"
        linea_5 = "  |\\                   | |"
        linea_6 = "  |\\                   | |"
        linea_7 = " /, ~\\                / /"
        linea_8 = "X     `-.....-------./ /"
        linea_9 = " ~-. ~  ~              |"
        linea_10 = "    \\             /    |"
        linea_11 = "     \\  /_     ___\\   /"
        linea_12 = "     | /\\ ~~~~~   \\ |"
        linea_13 = "     | | \\        || |"
        linea_14 = "     | |\\ \\       || )"
        linea_15 = "    (_/ (_/      ((_/"
        return '\n'.join([
            linea_1, linea_2, linea_3, linea_4, linea_5,
            linea_6, linea_7, linea_8, linea_9, linea_10,
            linea_11, linea_12, linea_13, linea_14,
            linea_15
        ])
    
    def dibujo_pez(self):
        # Tambien usando + entre strings
        # combinado con el caracter \n
        # este puede ser el mas claro tal vez
        linea_1 = "      /`·.¸"
        linea_2 = "     /¸...¸`:·"
        linea_3 = " ¸.·´  ¸   `·.¸.·´)"
        linea_4 = ": © ):´;      ¸  {"
        linea_5 = " `·.¸ `·  ¸.·´\\`·¸)"
        linea_6 = "     `\\´´\\¸.·´"
        parte_superior = linea_1 + '\n' + linea_2 + '\n' + linea_3 + '\n'
        parte_inferior = linea_4 + '\n' + linea_5 + '\n' + linea_6
        return  parte_superior + parte_inferior





