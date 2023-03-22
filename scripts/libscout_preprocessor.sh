#!/usr/bin/env bash
set -e

function create_xml() {
    # $1 = version dir
    libname=$(awk -F/ '{print $(NF-1)}' <<< $1)
    libver=$(awk -F/ '{print $(NF-0)}' <<< $1)

    echo '<?xml version="1.0"?>' > $1/library.xml
    echo '<library>' >> $1/library.xml
    echo "<name>${libname}</name>" >> $1/library.xml
    echo '<category>Android</category>' >> $1/library.xml
    echo "<version>${libver}</version>" >> $1/library.xml
    echo '<releasedate></releasedate>' >> $1/library.xml
    echo '<comment></comment>' >> $1/library.xml
    echo '</library>' >> $1/library.xml
}

if [[ ! -d $1 ]] ; then
    echo "usage: ./libscout_preprocessor.sh <libs dir>"
    exit
fi

libfolders=$(find $1 -mindepth 1 -maxdepth 1 -type d)

for libfolder in $libfolders ; do
    aar_files=$(find $libfolder -mindepth 1 -maxdepth 1 -type f -name *.aar)
    for aar_file in $aar_files ; do
        version_dir=$(echo "$aar_file" | sed 's/.aar$//')
        mkdir -p $version_dir
        mv $aar_file $version_dir

        create_xml $version_dir
    done

    jar_files=$(find $libfolder -mindepth 1 -maxdepth 1 -type f -name *.jar)
    for jar_file in $jar_files ; do
        version_dir=$(echo "$jar_file" | sed 's/.jar$//')
        [[ -d $version_dir ]] && continue

        mkdir -p $version_dir
        mv $jar_file $version_dir

        create_xml $version_dir
    done
done
