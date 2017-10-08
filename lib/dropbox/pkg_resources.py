import xbmc

certPath = xbmc.translatePath("special://home/addons/script.module.dboxpy/lib/dropbox/trusted-certs.crt")

# foo = imp.load_source('trusted-certs.crt', certPath)
# foo.MyClass()

def resource_filename(*args): 
    return certPath