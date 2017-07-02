#!/usr/bin/env python

"""Usage:
  ./convert [ -h | -i | -t | -c ]

Options:
  -h          Show this help
  -i          Convert image to vertical scroll box
  -t          Convert text to vertical scroll box
  -c          Convert command list to html
"""


import yaml
import jinja2
from docopt import docopt

def main(docopt_args):

    def help():
        print('')
        print('./convert.py -h | -i | -t  | -c')
        print('-----------------------------------')
        print('-h :  Help')
        print('-i :  images + comments')
        print('       Fill your data in data_image_scroll.yaml')
        print('-t :  text scrolling')
        print('       Fill your data in data_text_scroll.yaml')
        print('-c :  Code format')
        print('       Fill your data in data_command.yaml')


    if docopt_args['-h']:
        help()
        exit()

    else:
        if docopt_args['-i']:
            data = "data_image_scroll.yaml"
            template = "templ_image_scroll.txt"
        elif docopt_args['-t']:
            data = "data_text_scroll.yaml"
            template = "templ_text_scroll.txt"
        elif docopt_args['-c']:
            data = "data_command.yaml"
            template = "templ_command.txt"
        else:
            help()
            exit(1)


    def yamlToHtml(dat, templ):
        with open(dat, 'r') as stream:
            try:
                docs=yaml.load(stream)
                env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
                template = env.get_template(templ)
                #print(template.render(list=docs))
                return template.render(list=docs)

            except yaml.YAMLError as err:
                print(err)

    print(yamlToHtml(data, template))

if __name__ == '__main__':
    # parse arguments based on docstring
    arguments = docopt(__doc__, version='v0.1')
    # Run the program with the validated args
    main(arguments)