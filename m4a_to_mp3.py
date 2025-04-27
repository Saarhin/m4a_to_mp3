from pydub import AudioSegment
import os

def convert_m4a_to_mp3(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.m4a'):
            m4a_path = os.path.join(input_folder, filename)
            mp3_filename = os.path.splitext(filename)[0] + '.mp3'
            mp3_path = os.path.join(output_folder, mp3_filename)
            
            try:
                audio = AudioSegment.from_file(m4a_path, format='m4a')
                audio.export(mp3_path, format='mp3')
                print(f"Converted: {filename} -> {mp3_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    input_folder = "./Files/m4a"    # Put your .m4a files here
    output_folder = "./Files/mp3"  # Converted .mp3 files will go here
    
    convert_m4a_to_mp3(input_folder, output_folder)
