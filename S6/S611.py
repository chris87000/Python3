# une deuxième implémentation de RPCProxy

class RPCProxy:
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__(self, function):
        """
        Crée à la volée une méthode sur RPCProxy qui correspond
        à la fonction distante 'function'
        """
        def forwarder(*args):
            print(f"Envoi à {self.url}\nde la fonction {function} -- args= {args}")
            return "retour de la fonction " + function
        return forwarder
    
# création d'une instance de RPCProxy

rpc_proxy = RPCProxy (url='http://cloud.provider.com/JSONAPI', 
                      login='dupont',
                      password='***')

# cette partie du code, en tant qu'utilisateur de l'API, 
# est supposée connaître les détails
# des arguments à passer 
# et de comment utiliser les valeurs de retour
nodes_list = rpc_proxy.GetNodes ( 
    [ ('phy_mem', '>=', '32G') ] )

# reserver un noeud
node_lease = rpc_proxy.BookNode (
    { 'id' : 1002, 'phy_mem' : '32G' } )