from argparse import ArgumentParser
from video import ClickCapture, wait_for_click


def main(args):

    video_iter = ClickCapture(VIDEO_PATH,
                              fps=args.fps)

    for frame in video_iter:
        video_iter.show(frame)
        if (video_iter.current_frame - ClickCapture.clicked_frames[-1]) > args.force_click:
            wait_for_click(video_iter)
        

    print('All clicked frames:', ClickCapture.clicked_frames)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--video', required=True, help="path of the video to be watched")
    parser.add_argument('--fps', default=30, type=int, help="fps ratio to show the video")
    parser.add_argument('--force-click', type=int, default=30, help="maximum frames that can elapse without the user click")

    args = parser.parse_args()
    main(args)
