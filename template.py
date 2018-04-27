# -*- coding: utf-8 -*-
from jinja2 import Template
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

span_template = Template(u"""

monitor session {{source_number}} type erspan-source 
    description {{source_descr}}
    source interface {{source_interf}} 
    destination 
      erspan-id {{id}}
      ip address {{ip}} 
      origin ip address {{ip}} 
! 
! 
monitor session {{dest_number}} type erspan-destination 
    description {{dest_descr}} 
    destination interface {{dest_interf}} 
    source 
     erspan-id {{id}}
     ip address {{ip}}
""")
