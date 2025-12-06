import os
from pydub import AudioSegment

def split_audio_files(input_paths, output_dir, chunk_length_sec=40, start_index=1):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    chunk_length_ms = chunk_length_sec * 1000
    file_counter = start_index

    for file_path in input_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File not found - {file_path}")
            continue

        print(f"Processing file: {file_path}")
        try:
            # Load the audio file
            # pydub handles various formats, but requires ffmpeg for mp3
            audio = AudioSegment.from_file(file_path)
            
            total_length_ms = len(audio)
            
            # Loop through the audio file in chunks
            for i in range(0, total_length_ms, chunk_length_ms):
                chunk = audio[i:i + chunk_length_ms]
                
                # If you want to ignore the last chunk if it's too short (e.g., < 10 seconds), uncomment below:
                # if len(chunk) < 10000:
                #     continue

                # Construct output filename: maithili_1.mp3, maithili_2.mp3, ...
                output_filename = f"newari_{file_counter}.mp3"
                output_path = os.path.join(output_dir, output_filename)
                
                # Export the chunk
                chunk.export(output_path, format="mp3")
                
                file_counter += 1
            
            print(f"Finished processing {file_path}. Next index starts at {file_counter}.")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            print("Make sure ffmpeg is installed and added to your PATH.")

    print("All processing complete.")

if __name__ == "__main__":
    # --- CONFIGURATION ---
    
    # 1. PATHS TO YOUR 3 AUDIO FILES
    # Replace these strings with the actual paths to your MP3 files
    input_audio_files = [
        r"D:/PatternRecon/nepaliSongsClassify/dataset/1_newari.mp3",
        r"D:/PatternRecon/nepaliSongsClassify/dataset/2_newari.mp3",
        r"D:/PatternRecon/nepaliSongsClassify/dataset/3_newari.mp3",
        r"D:/PatternRecon/nepaliSongsClassify/dataset/4_newari.mp3",
        r"D:/PatternRecon/nepaliSongsClassify/dataset/5_newari.mp3"
    ]
    
    output_folder_path = r"D:/PatternRecon/nepaliSongsClassify/dataset/newari"
    
    # Change start_index to the number you want to start counting from
    split_audio_files(input_audio_files, output_folder_path, start_index=1)
