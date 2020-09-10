source ~/scipystack/bin/activate

for image in {0..100}
do
  python3 easy_mode.py $image
done

ffmpeg -i image_%03d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p out_easy_mode.mp4 > /dev/null

rm image_*.png

