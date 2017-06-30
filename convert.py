#!/usr/bin/env python

import yaml
import jinja2
import sys

#print(sys.path)

list = []
with open("data.yaml", 'r') as stream:
    try:
        docs=yaml.load(stream)
        print(docs)
        #print(type(docs))
        #for dict in docs:
        #  #print(dict)
        #  #print(type(dict))
        #  for key in dict:
        #     print(dict[key])
        env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
        template = env.get_template('templ_text_scroll.txt')
        print(template.render(list=docs))

    except yaml.YAMLError as err:
        print(err)

