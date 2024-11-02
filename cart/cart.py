

class Cart():

    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # if session key doesnt exist, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # make sure cart is available on all pages of site
        self.cart = cart

    
    def add(self, product):  #, quantity
        
        product_id = str(product.id)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            #self.cart[product_id] = int(product_qty)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)