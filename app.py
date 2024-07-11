from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flash messages

BASE_DOWNLOAD_FOLDER = '/BASE/DIRECTORY/FOR/DOWNLOADS/'
os.makedirs(BASE_DOWNLOAD_FOLDER, exist_ok=True)

def is_download_in_progress():
    return os.path.exists('download.lock')

def start_download():
    with open('download.lock', 'w') as f:
        f.write('')

def end_download():
    os.remove('download.lock')

def download_video(url, subdir, params, quality, format, base_download_folder):
    download_folder = os.path.join(base_download_folder, subdir.strip('/'))
    os.makedirs(download_folder, exist_ok=True)
    
    command = ['yt-dlp']
    
    if '--write-thumbnail' in params:
        command.append('--write-thumbnail')
    
    if '--write-sub --write-auto-sub --sub-lang en --sub-format srt --convert-subs srt' in params:
        command.extend(['--write-sub', '--write-auto-sub', '--sub-lang', 'en', '--sub-format', 'srt', '--convert-subs', 'srt'])
    
    if '--sponsorblock-remove all' in params:
        command.extend(['--sponsorblock-remove', 'all'])
    
    if quality != 'best':
        command.extend(['-f', f'bestvideo[height<={quality}]+bestaudio/bestvideo+bestaudio/best[height<={quality}]'])
    else:
        command.extend(['-f', 'bestvideo+bestaudio'])
    
    command.append(url)
    
    if format == 'mkv':
        command.extend(['--merge-output-format', 'mkv'])
    elif format == 'avi':
        command.extend(['--merge-output-format', 'avi'])
    elif format == 'webm':
        command.extend(['--merge-output-format', 'webm'])
    # Default to mp4 if format is not specified or is mp4
    # yt-dlp uses mp4 as default if no --merge-output-format is specified
    
    # Execute the command
    try:
        subprocess.run(command, cwd=download_folder, check=True)
    except subprocess.CalledProcessError as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if is_download_in_progress():
        flash('A download is already in progress. Please wait until it is finished.')
        return redirect(url_for('index'))
    
    start_download()
    try:
        urls = request.form.get('batch_urls', '').splitlines() if 'batch' in request.form else [request.form['url']]
        subdir = request.form['subdir']
        params = request.form.getlist('params')
        quality = request.form['quality']
        format = request.form['format']
        
        for url in urls:
            if url.strip():
                download_video(url, subdir, params, quality, format, BASE_DOWNLOAD_FOLDER)
        
        return redirect(url_for('success'))
    except Exception as e:
        return str(e)
    finally:
        end_download()

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
