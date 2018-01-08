# la version naïve de la classe RPCProxy

class RPCProxy:
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def _forward_call(self, functionname, *args):
        """
        helper method that marshalls and forwards 
        the function and arguments to the remote end
        """
        print(f"""Envoi à {self.url}
de la fonction {functionname} -- args= {args}""")
        return "retour de la fonction " + functionname
    
    def GetNodes (self, *args):
        return self._forward_call ('GetNodes', *args)
    def BookNode (self, *args):
        return self._forward_call ('BookNode', *args)
    def ReleaseNode (self, *args):
        return self._forward_call ('ReleaseNode', *args)
    
# création d'une instance de RPCProxy

rpc_proxy = RPCProxy(url='http://cloud.provider.com/JSONAPI', 
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

