
import moviepy.editor as mp

def addAudioFiles(videoPath, *audioList):
    audioList = audioList[0]
    videoFile = mp.VideoFileClip(videoPath)
    videoClips = []

    for i in range(len(audioList)):
        if i < 1:
            end = audioList[i]['start_in']
            clip = videoFile.subclip(0, end)
            videoClips.append(clip)

        else:
            start_in = audioList[i - 1]['start_in']
            end_in = audioList[i]['start_in']
            audio = mp.AudioFileClip(audioList[i - 1]['audio_path'])
            clip = videoFile.subclip(start_in, end_in).set_audio(audio)
            videoClips.append(clip)

    start_in = audioList[i - 1]['start_in']
    end_in = audioList[i]['start_in']
    audio = mp.AudioFileClip(audioList[i - 1]['audio_path'])
    clip = videoFile.subclip(start_in, videoFile.duration).set_audio(audio)
    videoClips.append(clip)
    
    finalVideo = mp.concatenate_videoclips(videoClips)
    finalVideo.write_videofile('out.mp4')
            
       


addAudioFiles('test.mp4', (
    {'audio_path': '1.mp3', 'start_in': 20}, 
    {'audio_path': '2.mp3', 'start_in': 30},
    {'audio_path': '2.mp3', 'start_in': 40}, 
    {'audio_path': '2.mp3', 'start_in': 50})
)
