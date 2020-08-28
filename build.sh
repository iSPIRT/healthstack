rm -rf build
mkdir build
mkdir build/spec
find src -name \*.html -exec cp {} build \;
find src -name \*.md -exec cp {} build \;
cp -r src/media build/media
cp -r src/static build/static

for filename in spec/*.yaml; do
    basename=$(basename "$filename")
    jsonfilename="${basename%.*}.json"
    echo $basename $jsonfilename
    node_modules/yamljs/bin/yaml2json $filename > build/spec/$jsonfilename
    python3 make_api_docs.py $jsonfilename
done


