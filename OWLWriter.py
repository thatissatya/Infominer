class owl:
    def __init__(self,n,f):
        self.oname=n
        self.header='''<?xml version="1.0" encoding="UTF-8"?>\n <Ontology xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"    xsi:schemaLocation="http://www.w3.org/2002/07/owl# http://www.w3.org/2009/09/owl2-xml.xsd" xmlns="http://www.w3.org/2002/07/owl#" xml:base="http://example.com/'''+self.oname+'''" ontologyIRI="http://example.com/'''+self.oname+'''" > <Prefix name="CF" IRI="'''+self.oname+'''#"/> <Import>http://example.com/'''+self.oname+'''</Import>\n\n'''
        self.content=[]
        self.footer='\n</Ontology>'
        self.file=f

    def cont(self):
        t=''
        for i in self.content:
            t+=i+'\n'
        return t    
    def subclass(self,sub,sup):
        c='<SubClassOf><Class IRI="#'+sub+'"/> <Class IRI="#'+sup+'"/></SubClassOf>\n'
        self.content.append(c)

    def properti(self,sub,prop,sup):
        c='<SubClassOf>   <Class IRI="#'+sub+'"/> <ObjectAllValuesFrom>  <ObjectProperty IRI="#'+prop+'"/><Class IRI="#'+sup+'"/> </ObjectAllValuesFrom>    </SubClassOf>'
        self.content.append(c)

    def write(self):
        f=open(self.file,'w')
        f.write(self.header)
        f.write(self.cont())
        f.write(self.footer)
        f.close()

