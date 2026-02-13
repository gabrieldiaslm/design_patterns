def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
        
    return get_class
    print(the_class)
    return the_class

@singleton
class Teste:
    def __init__(self):
        print('teste oi teste')


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'tema escuro'
        self.font = '18px'

if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'tema claro'
    print(as1.tema)
    
    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)