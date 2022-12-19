echo $1
#DST=$1
#SRC=$2
# data downloaded
SRC=/run/media/lasercat/projects_001/OSOCR-data/

# cache dir 1 (100GiB~)
DST=/run/media/lasercat/writebuffer/deploy/

# cache dir 2 (GiB~)
CAC=/run/media/lasercat/writebuffer/cachededlmdbs/

# generated dataset dir (GiB~)
EXP=/run/media/lasercat/cache2/

CODE_ROOT=${PWD}/code


#
cd ${SRC}/art
rm -r ${DST}/art
mkdir -p ${DST}/art
tar -xvf train_task2_images.tar.gz  --directory ${DST}/art
cp *json* ${DST}/art/;
cd ../

mkdir -p ${DST}/ctw/gtar
mkdir -p ${DST}/ctw/itar
cd ${SRC}/ctw
cd itar
for i in $(ls);
do
   tar -xvf ${i} --directory ${DST}/ctw/itar;
done;
cd ../
tar -xvf ctw-annotations.tar.gz  --directory ${DST}/ctw/gtar;

cd ${SRC}/mlt
rm -r ${DST}/mlt
mkdir -p ${DST}/mlt/real
unzip Chinese.zip -d ${DST}/mlt/synth
unzip ImagesPart1.zip -d ${DST}/mlt/real
unzip ImagesPart2.zip -d ${DST}/mlt/real
cd ${DST}/mlt/real;
mv */* .
rmdir *
echo "Those mates have pngs, gifs, and etc etc in the images, converting em."
for x in *; do case $x in *.[Jj][Pp][Gg]) :;; *) convert -- "$x" "${x%.*}.jpg";rm $x;; esac; done
cd ${SRC}/mlt
unzip train_gt_t13.zip -d ${DST}/mlt/real


cd ${SRC}/lsvt
    mkdir -p ${DST}/lsvt
    tar -xvf train_full_images_0.tar.gz  --directory ${DST}/lsvt/;
    tar -xvf train_full_images_1.tar.gz --directory ${DST}/lsvt/;
    cp *json ${DST}/lsvt/;
    cd ${DST}/lsvt/;
    mkdir imgs;
    mv train_full_images_0/* imgs;
    mv train_full_images_1/* imgs;
    rmdir *
cd ${SRC}


cd ${SRC}/rctw_train
mkdir -p ${DST}/rctw_train
for i in $(ls | grep zip)
do
    unzip $i -d ${DST}/rctw_train;
done;
cd ${DST}/rctw_train
mkdir train
mv */* train/
rmdir *
cd ${SRC}


#
cd ${SRC}/hwdb
mkdir -p ${DST}/hwdb/train
mkdir -p ${DST}/hwdb/test
mkdir -p ${DST}/hwdb/comp

for i in $(ls | grep Train)
do
    unzip $i -d ${DST}/hwdb/train;
done;

for i in $(ls | grep Test)
do
    unzip $i -d ${DST}/hwdb/test;
done;

unzip competition-gnt.zip -d ${DST}/hwdb/comp

cp -r ${CODE_ROOT}/../fonts ${DST}/

cd ${CODE_ROOT}

export PYTHONPATH=${CODE_ROOT}

python osocr_tasks/tasksg1/ch_jap_osocr/make_dataset_2.py ${DST} ${CAC} ${EXP}
