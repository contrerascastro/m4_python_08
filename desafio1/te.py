class Te():
    duracion = "365 días"
    pass
    
    def asigna_precio(self, precio: int):
        self.precio = precio
        
    def asigna_recomendacion(self, recomendacion: str):
        self.recomendacion = recomendacion
    
    def asigna_preparacion(self, preparacion: str):
        self.preparacion = preparacion
    
te_negro_300g = Te()
te_negro_300g.asigna_precio(3000)
te_negro_300g.asigna_recomendacion("Beber preferentemente en el desayuno")
te_negro_300g.asigna_preparacion("Deje 3 minutos el te en el recipiente y estará listo")
print(te_negro_300g.precio, te_negro_300g.recomendacion, te_negro_300g.preparacion)

te_negro_500g = Te()
te_negro_500g.asigna_precio(5000)
te_negro_500g.asigna_recomendacion("Beber preferentemente en el desayuno")
te_negro_500g.asigna_preparacion("Deje 3 minutos el te en el recipiente y estará listo")
print(te_negro_500g.precio, te_negro_500g.recomendacion, te_negro_500g.preparacion)

te_verde_300g = Te()
te_verde_300g.asigna_precio(3000)
te_verde_300g.asigna_recomendacion("Beber preferentemente al mediodía")
te_verde_300g.asigna_preparacion("Deje 5 minutos el te en el recipiente y estará listo")
print(te_verde_300g.precio, te_verde_300g.recomendacion, te_verde_300g.preparacion)

te_verde_500g = Te()
te_verde_500g.asigna_precio(5000)
te_verde_500g.asigna_recomendacion("Beber preferentemente al mediodía")
te_verde_500g.asigna_preparacion("Deje 5 minutos el te en el recipiente y estará listo")
print(te_verde_500g.precio, te_verde_500g.recomendacion, te_verde_500g.preparacion)

infusion_hierbas_300g = Te()
infusion_hierbas_300g.asigna_precio(3000)
infusion_hierbas_300g.asigna_recomendacion("Beber preferentemente al atardecer")
infusion_hierbas_300g.asigna_preparacion("Deje 6 minutos la hierba en el recipiente y estará listo")
print(infusion_hierbas_300g.precio, infusion_hierbas_300g.recomendacion, infusion_hierbas_300g.preparacion)

infusion_hierbas_500g = Te()
infusion_hierbas_500g.asigna_precio(5000)
infusion_hierbas_500g.asigna_recomendacion("Beber preferentemente al atardecer")
infusion_hierbas_500g.asigna_preparacion("Deje 6 minutos la hierba en el recipiente y estará listo")
print(infusion_hierbas_500g.precio, infusion_hierbas_500g.recomendacion, infusion_hierbas_500g.preparacion)



#Otra forma de estructurar los precios y recomendación de consumo

precios = {
    te_negro_300g : 3000,
    te_negro_500g : 5000,
    te_verde_300g : 3000,
    te_verde_500g : 5000,
    infusion_hierbas_300g : 3000,
    infusion_hierbas_500g : 5000
}

preparacion = {
    te_negro_300g : "3 minutos",
    te_negro_500g : "3 minutos",
    te_verde_300g : "5 minutos",
    te_verde_500g : "5 minutos",
    infusion_hierbas_300g : "6 minutos",
    infusion_hierbas_500g : "6 minutos"
}

recomendación = {
    te_negro_300g : "desayuno",
    te_negro_500g : "desayuno",
    te_verde_300g : "medio día",
    te_verde_500g : "medio día",
    infusion_hierbas_300g : "atardecer",
    infusion_hierbas_500g : "atardecer"
}



