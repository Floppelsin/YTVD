from pytubefix import YouTube
import pyfiglet 

#Change those variables to your path
video_path = '\Videos' 
audio_path = '\Audios'

#Welcome text
figlet = pyfiglet.Figlet(font='slant')
welcome_text = figlet.renderText('Welcome to ytvd!')
print(f'{welcome_text}\n')

#Function that downloads the video 
def get_video(yt):
    print('getting the highest resolution...')
    high_resolution = yt.streams.get_highest_resolution()
    print('downloading...')
    high_resolution.download(video_path)
    print(f'download successfuly to the {video_path}')

#function that downloads the audio
def get_audio(yt):
    print('getting audio...')
    audio = yt.streams.get_audio_only()
    print('Downloading...')
    audio.download(audio_path)
    print(f'successfuly download to the {audio_path}')

#Main cycle
while True:
    #set up link
    url = input('Enter the url: ')
    yt = YouTube(url)

    #Print some information
    print(f'\nTitle: {yt.title}')
    print(f'Length: {yt.length}s')
    print(f'Views: {yt.views}\n')

    #Ask user what to do with url 
    print('What do you want to do?') 
    print('V - Download the video A - download the audio EX - Exit the program\n')
    choise = input('Your choise: ')
    
    if choise == 'V':
        print('Starting...')
        get_video(yt)
    elif choise == 'A':
        print('Starting...')
        get_audio(yt)
    elif choise == 'EX':
        print('Exiting...')
        break
    else:
        print('Unknow command please try again')
