def fui_importado():
    print("o modulo ex_main foi importado")
    print("a propriedade __name__ e: " + __name__)

def fui_executado():
    print("o modulo ex_main foi executado")
    print("a propriedade __name__ e: " + __name__)

if __name__ == "__main__":
    fui_executado()
else:
    fui_importado()
