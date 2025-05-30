import datetime

import xml.dom.minidom
start_time_of_DOM=datetime.datetime.now()
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
print('The term which has the greatest number of <is_a> elements of molecular fuction is: ',GO_terms['molecular_function']['term'])
print('The number of <is_a> elements it is associated with is: ',GO_terms['molecular_function']['count'])
print('The term which has the greatest number of <is_a> elements of biological_process is: ',GO_terms['biological_process']['term'])
print('The number of <is_a> elements it is associated with is: ',GO_terms['biological_process']['count'])
print('The term which has the greatest number of <is_a> elements of cellular_component is: ',GO_terms['cellular_component']['term'])
print('The number of <is_a> elements it is associated with is: ',GO_terms['cellular_component']['count'])
end_time_of_DOM=datetime.datetime.now()
time_of_DOM=end_time_of_DOM-start_time_of_DOM
print('Time used by DOM is: ',time_of_DOM)

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
        elif tag=='is_a':
            self.is_a_count+=1
    def characters(self,content):
        if self.current_tag=='namespace':
            self.current_namespace+=content.strip()
        elif self.current_tag=='name':
            self.current_name+=content.strip()
    def endElement(self,tag):
        if tag=='term':
            if self.current_namespace in self.GO_terms:
                if self.is_a_count>self.GO_terms[self.current_namespace]['count']:
                    self.GO_terms[self.current_namespace]={'term':self.current_name,'count':self.is_a_count}
start_time_of_SAX=datetime.datetime.now()
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=GOHandler()
parser.setContentHandler(Handler)
parser.parse('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical14/go_obo.xml')
print('The term which has the greatest number of <is_a> elements of molecular fuction is: ',Handler.GO_terms['molecular_function']['term'])
print('The number of <is_a> elements it is associated with is: ',Handler.GO_terms['molecular_function']['count'])
print('The term which has the greatest number of <is_a> elements of biological_process is: ',Handler.GO_terms['biological_process']['term'])
print('The number of <is_a> elements it is associated with is: ',Handler.GO_terms['biological_process']['count'])
print('The term which has the greatest number of <is_a> elements of cellular_component is: ',Handler.GO_terms['cellular_component']['term'])
print('The number of <is_a> elements it is associated with is: ',Handler.GO_terms['cellular_component']['count'])
end_time_of_SAX=datetime.datetime.now()
time_of_SAX=end_time_of_SAX-start_time_of_SAX
print('Time used by SAX is: ',time_of_SAX)

#SAX runs fastest.
        


