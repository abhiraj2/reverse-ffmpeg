# reverse-ffmpeg
Simple script that utilizes the FFMPEG library to reverse a video without giving stress on RAM



# Requirements

Following Python libraries are required:
  * os
  * sys
  * idla (for building the exe)
  * cx_Freeze (for the building the exe)
The release binaries include all these

*It is assumed that both ffmpeg and ffprobe are in your PATH variable, if they aren't you'll need to add them or change the reverse-ffmpeg.py lines accordingly.*

# Working

Pass the video file path as the first argument when running using any CLI, e.g. `reverse-ffmpeg C:/Videos/test.mp4`

The program extracts each frame of the video and rearranges them in the descending order, the audio file is simply reversed with the areverse tag since it has minial memory usage.

The frame by frame extraction of the video does not give any pressure on the RAM, rather the Disk Space is heavily abused, 

e.g. reversing a 1 min 38 sec 1080p60 youtube video requires a free space of around 32 GB (I KNOW!), but the good part is that there is no compression during the process also, the space is recovered at the end.

# Necessity

The only necessity for this to exist is because the ffmpeg reverse option uses godammn too much memory and since I don't have that much RAM but have a 1 TB HDD, I make use of it. 
e.g. the 1 min 38 sec youtube video crashed my entire PC 3 times while reversing the video.
