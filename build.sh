rm -rf build
mkdir build
mkdir build/spec
find src -name \*.html -exec cp {} build \;
find src -name \*.md -exec cp {} build \;
cp -r src/media build/media

for filename in src/spec/*.yaml; do
    basename=$(basename "$filename")
    filenamewithoutext="${basename%.*}.json"
    echo $basename $filenamewithoutext
    node_modules/yamljs/bin/yaml2json $filename > build/spec/$filenamewithoutext
done


