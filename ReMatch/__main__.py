import argparse
from .TOA import TOA
from .TBA import TBA
import twitch
import youtube_dl
from googleapiclient.

def main(video_id, archive_type,  event_key, event_type):
    if archive_type == 'twitch':
        twitch_client = twitch.TwitchClient(client_id="a57grsx9fi8ripztxn8zbxhnvek4cp")
        twitch_client.videos.download_vod(video_id)
        timestamp = twitch_client.videos.get_by_id(video_id).get('created_at')
    elif archive_type == 'youtube':
        ydl_opts = {
            'format': 'best',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://youtube.com/watch?v={video_id}"])
        timestamp =
    else:
        print("Unsupported video type!")
        return exit(1)
    if event_type == 'ftc':
        TOA.DB_setup(TOA(), event_key)
    elif event_type == 'frc':
        TBA.DB_setup(TBA(), event_key)
    else:
        print("Unsupported event type!")
        return exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process match streams into individual match clips")
    parser.add_argument('video_id', help="ID of VOD or YT video")
    parser.add_argument('video_type', help="Only twitch or youtube are supported at this time, "
                                           "please specify which one the stream archive is")
    parser.add_argument('event_key', help="Put in the event key")
    parser.add_argument('event_type', help="FTC or FRC are the only ones that will be supported for the time being")
    args = parser.parse_args().__dict__
    main(args['video_id'], args['video_type'], args['event_key'], args['event_type'])