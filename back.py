from flask import Flask, request, jsonify
import yt_dlp
import urllib.parse

app = Flask(__name__)

@app.route('/api/download', methods=['POST'])
def download():
    url = request.form.get('url')

    # Decode the URL
    decoded_url = urllib.parse.unquote(url)

    # Initialize yt-dlp
    ydl_opts = {
        'format': 'best',  # You can adjust the format based on your requirements
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(decoded_url, download=False)  # Set download to False
            if 'entries' in info:
                download_links = [entry['url'] for entry in info['entries']]
            else:
                download_links = [info['url']]
            return jsonify(download_links)
        except yt_dlp.utils.DownloadError as e:
            app.logger.error(f'yt-dlp DownloadError: {str(e)}')
            return jsonify({'error': f'DownloadError: {str(e)}'})
        except Exception as e:
            app.logger.error(f'Error during extraction: {str(e)}')
            return jsonify({'error': f'ExtractionError: {str(e)}'})

    # Specify the compression settings
    #compression_quality = 0.2  # Adjust this value based on your desired quality

    # Download the video and save it temporarily
    #video = download_links
    #os.system(f'youtube-dl -o "{video}" {url}')

    # Load the video clip
    #video_clip = VideoFileClip(video)

    # Compress the video with the specified quality
    #compressed_path = 'compressed_video.mp4'
    #video_clip.write_videofile(compressed_path, codec='libx264', fps=video_clip.fps, bitrate=f'{compression_quality}M')

    # Clean up temporary files
    #os.remove(video)

    # Send the compressed video file for download
    #return send_file(compressed_path, as_attachment=True, download_name=f'{title}.mp4')

if __name__ == '__main__':
    app.run(debug=True)
