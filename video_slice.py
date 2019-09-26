import os
import argparse
import math
from moviepy.editor import VideoFileClip


def get_duration(file_path):
    clip = VideoFileClip(file_path)
    return clip.duration


def slice_one_video(input_video, output_video, start_time, part_duration):
    cmd = "ffmpeg -i {0} -ss {1} -c copy -t {2} {3}".format(input_video, start_time, part_duration, output_video)
    print(cmd)
    res = os.popen(cmd)


def video_slice(input_video_path, output_video_path, slice_duration):
    video_names = os.listdir(input_video_path)
    for video_name in video_names:
        new_video_name = video_name.replace("-", "_")
        os.rename(os.path.join(input_video_path, video_name), os.path.join(input_video_path, new_video_name))
        video_path = os.path.join(input_video_path, new_video_name)
        duration = get_duration(video_path)
        slice_count = math.ceil(duration / slice_duration)
        part_duration = duration / slice_count
        for index in range(slice_count):
            input_video = os.path.join(input_video_path, new_video_name)
            video_name_noext = os.path.splitext(new_video_name)[0]
            ext = os.path.splitext(new_video_name)[1]
            output_video = os.path.join(output_video_path, video_name_noext + "_part_" + str(index) + ext)
            start_time = part_duration * index
            slice_one_video(input_video, output_video, start_time, part_duration)


if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_video_path", help="--input_video_path 输入视频的目录，可包括多个视频")
    parser.add_argument("--slice_duration", help="--slice_duration 每个视频的长度", default="3600")
    parser.add_argument("--output_video_path", help="--output_video_path 输出视频的目录")
    args = parser.parse_args()
    input_video_path_arg = args.input_video_path
    output_video_path_arg = args.output_video_path
    slice_duration_arg = args.slice_duration
    video_slice(input_video_path_arg, output_video_path_arg, int(slice_duration_arg))

