#!C:\Users\vahagnv\AppData\Local\Programs\Python\Python39\python.exe
"""
TODO list
add arguments
    -c <config file>
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import youtube_dl
import argparse


def get_arguments():
    """get arguments from terminal"""
    parser = argparse.ArgumentParser(description="""
                         Description: Automatically downloads audio(mp3) or video(mp4) from YouTube.
                         Developer: Vahagn Vardanyan(email: v.h.v.vahagn@gmail.com)
                         Required (not built in python3) libraries: 
                            Selenium (pip install selenium),
                            youtube_dl (pip install youtube_dl)
                         """, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-t", help="Define download file format/type (mp3 or mp4. Default: mp3)",
                        choices=["mp3", "mp4"], default="mp3")
    parser.add_argument("-aq", help="Define quality of mp3 (128/192/320. Default: 320kbps). (only for mp3)",
                        choices=["320", "192", "128"], default="320")
    parser.add_argument("-vq", help="Define preferred quality of video (1080/720. Default: 1080p)",
                        choices=["1080", "720"], default="1080")
    parser.add_argument("-ss", help="Define start time, Default: 0:0. (only for mp3)", default="0:0")
    parser.add_argument("-to", help="Define end time, Default: end. (only for mp3)", default="end")
    parser.add_argument("-o", help="Define output folder, Default: Current dir", default=".")
    parser.add_argument("-s", help="Define search string. If not defined,it will asked in terminal", default=False)
    parser.add_argument("-url", help="Define url of video in youtube", default=False)
    # parser.add_argument("-c", help="to define config file path", default="./config.txt")
    return parser.parse_args()


def get_url_from_youtube(search_str: str, driver):
    """Get and returns url from youtube for given string. if not found returns False"""
    try:
        driver.get('https://www.youtube.com/')
        # driver.maximize_window()
        sleep(1)
        search = driver.find_element_by_name("search_query")
        print(f"Searching video by name '{search_str}' in YouTube...")
        search.send_keys(search_str)
        sleep(1)
        search.send_keys(Keys.ENTER)
        sleep(5)
        print(f"Opening first found video ...")
        driver.find_element_by_tag_name("ytd-video-renderer").click()
        # driver.find_element_by_xpath("//*[@id='thumbnail']/yt-img-shadow").click()
        # driver.find_element_by_id("video-title").click()
        sleep(5)
    except NoSuchElementException:
        print(f"Couldn't find/open video by name '{search_str}' in youtube")
        return False
    else:
        print("Getting the URL ...")
        return driver.current_url
    finally:
        driver.close()
        driver.quit()


def is_working_url(url):
    """checks if the url is valid url of youtube"""
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != 'generic':
            return True
    return False


def init_chrome():
    """Initialisation of chrome browser"""
    driver_path = "C:\\vahagn\\python\\chromedriver.exe"
    wd_options = webdriver.ChromeOptions()
    wd_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # to not get errors in console
    return webdriver.Chrome(executable_path=driver_path, options=wd_options)


def download(v_url, file_type, output_folder, audio_quality, video_quality, start_time, end_time):
    """Downloading from youtube by url in mp3 or mp4 format(using youtube_dl lib)"""
    # video_info = youtube_dl.YoutubeDL().extract_info(url=v_url, download=False)  # all info about video
    # filename = f"{video_info['title']}.{video_info['ext']}"  #file name by title and format
    filename = "%(title)s.%(ext)s"  # name the file by title of video and format
    if end_time == "end":
        postprocessor_args = ['-ss', f'{start_time}']
    else:
        postprocessor_args = ['-ss', f'{start_time}', '-to', f'{end_time}']
    format_options_dict = \
        {
            "mp3":
                {
                    'format': "bestaudio/best",                         # choice of quality
                    'keepvideo': False,                                 # only keep the audio
                    'outtmpl': output_folder + "\\" + filename,         # set name and output folder
                    'noplaylist': True,                                 # only download single song, not playlist
                    'postprocessors':
                        [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': audio_quality,
                        }],                                             # convert to mp3 by preferred quality
                    'postprocessor_args': postprocessor_args            # set start and end time
                },
            "mp4":
                {
                    'format': f"bestvideo[height<={video_quality}]+bestaudio/best[height<={video_quality}]",
                    'outtmpl': output_folder + "\\" + filename,
                    'noplaylist': True,                                 # only download single song, not playlist
                }
        }

    with youtube_dl.YoutubeDL(format_options_dict[file_type]) as ydl:
        ydl.download([v_url])


try:
    args = get_arguments()
    if args.url:
        if is_working_url(args.url):
            video_url = args.url
        else:
            raise Exception("Defined invalid url!!!")
    else:
        if not args.s:
            args.s = input("search text not defined.\nPlease enter text to search: ")
        browser = init_chrome()
        video_url = get_url_from_youtube(args.s, browser)

    if video_url:
        print(video_url)
        download(video_url, args.t, args.o, args.aq, args.vq, args.ss, args.to)
    else:
        raise Exception("Download failed")
except Exception as ex:
    print(ex)
else:
    print("Successfully finished !!!")
