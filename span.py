# -*- coding: utf-8 -*-
from jinja2 import Template
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from template import span_template  # template 

# Dictionary with items for template
a1002_span = {'source_number':'10', 'source_descr':'span_source', 'source_interf':'Gi0/0/0', 'id':'10', 'ip':'10.1.1.1', 'dest_number':'20', 'dest_descr':'span_dest', 'dest_interf':'Gi0/0/3'} 
span_conf = 'span.cnf'  # File with configuration for asr1002x 
with open(span_conf, 'w') as f:
    f.write(span_template.render( a1002_span ))  # write config to file



