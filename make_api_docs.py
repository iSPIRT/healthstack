import sys
import os
import json

api_spec_file_name = sys.argv[1]
api_spec_file_name_without_ext = api_spec_file_name.replace('.json', '')

cwd = os.path.dirname(os.path.realpath(__file__))
template_file_path = os.path.join(cwd, 'src/template.html')

content = open(template_file_path).read().replace('SPEC_FILE', api_spec_file_name)

build_path = os.path.join(cwd, 'build', api_spec_file_name_without_ext + '.html')
open(build_path, 'w').write(content)

json_file_path = os.path.join(cwd, 'build/spec', api_spec_file_name)
content = open(json_file_path).read()

spec = json.loads(content)
spec['info']['x-logo'] = {
      "url": "./media/ispirt-logo.svg",
      "href": "/"
    }
open(json_file_path, 'w').write(json.dumps(spec, indent=2))