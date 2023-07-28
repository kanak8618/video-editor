from moviepy.editor import *

print("!!!------choose any one option for edit the video------!!!")
print("1 :- Take Screenshot")
print("2 :- Set Margin")
print("3 :- Marge Videos")
print("4 :- Extrace Audio from video & Set audio in video")
print("5 :- Add WaterMark")
print("6 :- Split screen 4 videos")
print("7 :- Video to GIF")


a = int(input("Enter your choice :- "))

match a:
    case 1:
        clip = VideoFileClip(input("Enter .mp4 path :- "))
        clip.save_frame(input("Enter ss name for save :- "),int(input("Enter second :- ")))  #default take ss at 1sec
        print("!!! Success---")

    case 2:
        a = input("you want to make a subclip ?(Y/N)")
        if a == 'y':
            clip = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")), int(input("End sec. :- ")))
            clip = clip.margin(int(input("Margin :- ")))
            clip.write_videofile(input("Save As :- "))
        elif a == 'n':
            clip = VideoFileClip(input("Enter .mp4 path :- "))
            clip = clip.margin(int(input("Margin :- ")))
            clip.write_videofile(input("Save As :- "))
        print("!!! Success---")

    case 3:
        a = input("you want to make a subclip ?(Y/N)")
        if a == 'y':
            clip1 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")), int(input("End sec. :- ")))
            clip2 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")), int(input("End sec. :- ")))
            clip2 = clip2.set_position(int(input("X  :- ")),int(input("Y  :- ")))
            final_video = concatenate_videoclips([clip1,clip2])
            final_video.write_videofile(input("Save As :- "))
        elif a == 'n':
            clip1 = VideoFileClip(input("Enter .mp4 path :- "))
            clip2 = VideoFileClip(input("Enter .mp4 path :- "))
            clip2 = clip2.set_position(int(input("X  :- ")), int(input("Y  :- ")))
            final_video = concatenate_videoclips([clip1, clip2])
            final_video.write_videofile(input("Save As :- "))
        print("!!! Success---")

    case 4:
        a = input("A: convert in Audio -? \nB: Extract Audio ?(a/b)")
        if a == 'a':
            clip1 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")), int(input("End sec. :- ")))
            clip1.audio.write_audiofile(input("Save As :- "))   # video convert in audio

        elif a == 'b':
            print("NOTE :- Video and audio file should have same time")
            clip1 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))
            clip1 = clip1.without_audio()   # Remove audio from video

            audio_file = AudioFileClip(input("Enter .mp3 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))
            final_video = clip1.set_audio(audio_file)
            final_video.write_videofile(input("Save As .MP4 :- "))
        print("!!! Success---")

    case 5:  # For Add watermark in video must need the ImageMagick software in your system
        clip = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")), int(input("End sec. :- ")))
        text_clip = TextClip(input("WaterMark :- "),int(input("Fontsize. :- ")),input("Color :- "))
        text_clip = text_clip.set_position('center').set_diration(10)
        video = CompositeVideoClip([clip,text_clip])
        video.write_videofile(input("Save As .MP4 :- "))
        print("!!! Success---")

    case 6:
        clip1 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))
        clip2 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))
        clip3 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))
        clip4 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))

        # a=int(input("enter :- "))
        # for i in range(a):
        #     clip1 = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))

        comb = clips_array([[clip1,clip2],[clip3,clip4]])
        comb.write_videofile(input("Save As .MP4 :- "))

    case 7:
        a= input("want to You rotate .GIF ? (y/n)")
        if a=='y':
            clip = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- "))).rotate(int(input("Rotat deg :- ")))
        elif a=='n':
            clip = VideoFileClip(input("Enter .mp4 path :- ")).subclip(int(input("Start sec. :- ")),int(input("End sec. :- ")))
        clip.write_gif(input("Save As .GIF :- "))
    case _:
        print("Invalid choice !!!-----")




