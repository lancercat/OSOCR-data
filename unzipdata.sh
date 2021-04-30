cd art
tar -xvf train_task2_images.tar.gz
cd ../

cd ctw 
tar -xvf ctw-annotations.tar.gz
mkdir gtar
mv *json* gtar
cd ../

cd hwdb
mkdir train
mkdir test
for i in $(ls | grep Train)
do 
    unzip $i;
done;
mv *.gnt train

for i in $(ls | grep Test)
do 
    unzip $i;
done;
mv *.gnt test
mkdir comp
unzip competition-gnt.zip
mv *.gnt comp

cd ../




cd mlt 
unzip Chinese.zip
unzip ImagesPart1.zip
unzip ImagesPart2.zip
mkdir real
mv ImagesPart1/* real
mv ImagesPart2/* real
cd real
echo "Those mates have pngs, gifs, and etc etc in the images, converting em."
for x in *; do case $x in *.[Jj][Pp][Gg]) :;; *) convert -- "$x" "${x%.*}.jpg";rm $x;; esac; done
cd ../
unzip train_gt_t13.zip
mv *.txt real
rmdir *
cd ../


cd lsvt
    tar -xvf train_full_images_0.tar.gz
    tar -xvf train_full_images_1.tar.gz
    mkdir imgs;
    mv train_full_images_0/* imgs;
    mv train_full_images_1/* imgs;
    rmdir *
cd ../

cd rctw_train
for i in $(ls | grep zip)
do 
    unzip $i;
done;
mkdir train
mv */* train/
rmdir *
cd ../
# 
# cd gb1k
# tar -xvf FontSynth_v1.1.tar
# cd ../
