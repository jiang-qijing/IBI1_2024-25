from datetime import datetime

import xml.dom.minidom
start=datetime.now()
go_obo=xml.dom.minidom.parse('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical14/go_obo.xml')
root_element=go_obo.documentElement
terms=root_element.getElementsByTagName('term')
GO_terms={'molecular_function':{'term':'','count':0},
          'biological_process':{'term':'','count':0},
          'cellular_component':{'term':'','count':0},}
for term in terms:
    namespace=term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    name=term.getElementsByTagName('name')[0].firstChild.nodeValue
    is_a=term.getElementsByTagName('is_a')
    is_a_count=len(is_a)
    if namespace in GO_terms:
        if is_a_count>GO_terms[namespace]['count']:
            GO_terms[namespace]={'term':name,'count':is_a_count}
print(GO_terms)
end=datetime.now()
time_of_DOM=end-start
print(time_of_DOM)

import xml.sax
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag=''
        self.current_namespace=''
        self.current_name=''
        self.is_a_count=0
        self.GO_terms={'molecular_function':{'term':'','count':0},
                       'biological_process':{'term':'','count':0},
                       'cellular_component':{'term':'','count':0},}
    def startElement(self,tag,attributes):
        self.current_tag=tag
        if tag=='term':
            self.current_namespace=''
            self.current_name=''
            self.is_a_count=0
    def characters(self,content):
        if self.current_tag=='namespace':
            self.current_namespace+=content
        elif self.current_tag=='name':
            self.current_name+=content
        elif self.current_tag=='is_a':
            self.is_a_count+=1
    def endElement(self,tag):
        if tag=='term':
            if self.current_namespace in self.GO_terms:
                if self.is_a_count>self.GO_terms[self.current_namespace]['count']:
                    self.GO_terms[self.current_namespace]={'term':self.current_name,'count':self.is_a_count}
        self.current_tag=""
start=datetime.now()
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=GOHandler()
parser.setContentHandler(Handler)
parser.parse('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical14/go_obo.xml')
print(Handler.GO_terms)
end=datetime.now()
time_of_SAX=end-start
print(time_of_SAX)

#SAX runs fastest.
        


