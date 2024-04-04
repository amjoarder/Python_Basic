class Person:
    name = "Anonymous"
'''
    def changeName(self,name):
        self.__class__.name = "John" 
        
        #self.__class__.something == Person.something . Anonymous will be replaced by John in the class. or better to do this below
'''


        @classmethod
        def changeName(cls, name):
            cls.name = name


