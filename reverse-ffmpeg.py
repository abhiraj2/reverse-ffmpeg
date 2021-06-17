import os, sys, subprocess

default_dir = os.path.join(os.path.expanduser('~'), 'Videos/')


if not os.path.exists(default_dir + "test"):
    os.mkdir(default_dir + "test")
else:
    print("path exists\n " + default_dir + "test")
    
if not os.path.exists(default_dir + "test/pics"):
    os.mkdir(default_dir + "test/pics")
else:
    print("path exists\n" + default_dir + "test/pics")
    
if not os.path.exists(default_dir + "test/pics/new"):
    os.mkdir(default_dir + "test/pics/new")
else:
    print("path exists\n" + default_dir + "test/pics/new")
    
    


if (len(sys.argv) > 1):
    filename = sys.argv[1]
    total_frames = int(os.popen(("ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 {0}").format(filename)).read())
    fps = os.popen(('ffmpeg -i {0} 2>&1 | sed -n "s/.*, \\(.*\\) fp.*/\\1/p"').format(filename)).read().strip()

    resolution = os.popen(('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {0}').format(filename)).read().strip()
    library = os.popen(("ffprobe -loglevel error -show_entries stream=pix_fmt -of csv=p=0 {0}").format(filename)).read().strip()
    print(filename + "\n" + str(total_frames) + "\n" + fps + "\n" + resolution + "\n" + library)


    os.system(('ffmpeg -i {0} ' + os.path.join(default_dir + "test/") + 'pics/img%d.bmp').format(filename))

    print(('ffmpeg -i {0} ' + os.path.join(default_dir + "test/") + 'pics/img%d.bmp').format(filename))

    for i in range(total_frames, 0, -1):
       print("moving - " + str(i), end="\r")
       os.system('mv ' + os.path.join(default_dir + "test/") + 'pics/img' + str(i) + '.bmp ' + os.path.join(default_dir + "test/") + 'pics/new/img' + str(total_frames - i + 1) + '.bmp')

    os.system(('ffmpeg -i {0} -af areverse ' + os.path.join(default_dir + "test/") + 'reversed_audio.aac').format(filename))
    print((f"ffmpeg -r {fps} -f image2 -s {resolution} -i {os.path.join(default_dir + 'test/pics/new/')}img%d.bmp -vcodec libx264 -crf 25  -pix_fmt {library} {os.path.join(default_dir + 'test/')}output.mp4"))
    os.system((f"ffmpeg -r {fps} -f image2 -s {resolution} -i {os.path.join(default_dir + 'test/pics/new/')}img%d.bmp -vcodec libx264 -crf 25 -pix_fmt {library} {os.path.join(default_dir + 'test/')}output.mp4")) 

    print("Hello")

    os.system(f"ffmpeg -i {os.path.join(default_dir + 'test/')}output.mp4 -i {os.path.join(default_dir + 'test/')}reversed_audio.aac -c:v copy -c:a copy {default_dir}FinalOutput.mp4")

    os.system(f"rm -r {os.path.join(default_dir + 'test')}")

else:
    print("No Filename was provided. Exiting")