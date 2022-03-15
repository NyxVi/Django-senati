class Carrito:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
    
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.product_id)
        if id not in self.carrito.keys():
            self.carrito[id]= {
                "producto_id" : producto.product_id,
                "nombre" : producto.name,
                "descripcion" : producto.description,
                "categoria" : producto.category,
                "precio" : producto.price,
                "cantidad" : 1
            }
            
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += producto.price
        
        self.guardar_carrito()
        
        
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    
    def eliminar(self, producto):
        id = str(producto.product_id)   
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
            
    
    def restar(self, producto):
        id = str(producto.product_id)   
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= producto.price
            if self.carrito[id]["cantidad"] <=0: self.eliminar(producto)
            self.guardar_carrito()
            
    def limpiar(self):
            self.session["carrito"] = {}
            self.session.modified = True