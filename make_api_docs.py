import sys
import os

api_spec_file_name = sys.argv[1]
api_spec_file_name_without_ext = api_spec_file_name.replace('.json', '')

cwd = os.path.dirname(os.path.realpath(__file__))
template_file_path = os.path.join(cwd, 'src/template.html')

content = open(template_file_path).read().replace('SPEC_FILE', api_spec_file_name)

build_path = os.path.join(cwd, 'build', api_spec_file_name_without_ext + '.html')
open(build_path, 'w').write(content)