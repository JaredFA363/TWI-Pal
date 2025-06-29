import sounddevice as sd
import numpy as np
from pynput import keyboard
from scipy.io.wavfile import write
import tempfile
import os
from faster_whisper import WhisperModel

"""class FasterWhisperTranscriber:
    def __init__(self, model_size="tiny", sample_rate=44100):
        self.model_size = model_size
        self.sample_rate = sample_rate
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")
        self.is_recording = False
        
    # Start recording audio
    def on_press_space(self, key):
        if key == keyboard.Key.space:
            if not self.is_recording:
                self.is_recording = True
                print("Recording started...")
    
    # Stop recording audio
    def on_release_space(self, key):
        if key == keyboard.Key.space:
            if self.is_recording:
                self.is_recording = False
                print("Recording stopped.")
                return False
            
    # Record audio
    def record_audio(self):
        recording = np.array([], dtype='float32').reshape(0, 2)
        frames_per_buffer = int(self.sample_rate * 0.1)
        with keyboard.Listener(on_press=self.on_press_space, on_release=self.on_release_space) as listener:
            while True:
                if self.is_recording:
                    audio_chunk = sd.rec(frames_per_buffer, samplerate=self.sample_rate, channels=2, dtype='float32')
                    sd.wait()
                    recording = np.vstack([recording, audio_chunk])
                if not self.is_recording and len(recording) > 0:
                    break
            listener.join()
        return recording
    
    # Save audio to a temporary file
    def save_audio(self, recording):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
            write(temp_file.name, self.sample_rate, recording)
            return temp_file.name
        
    # Transcribe audio from a file
    def transcribe_audio(self, file_path):
        segments, info = self.model.transcribe(file_path, beam_size=5)
        print(f"Detected language: {info.language}")
        transcription = ""
        for segment in segments:
            print(segment.text)
            transcription += segment.text + " "
        os.remove(file_path)
        return transcription.strip()
    
    def run(self):
        print("Press and hold the spacebar to start recording...")
        recording = self.record_audio()
        if len(recording) > 0:
            file_path = self.save_audio(recording)
            transcription = self.transcribe_audio(file_path)
            print("Transcription:", transcription)
        else:
            print("No audio recorded.")

if __name__ == "__main__":
    transcriber = FasterWhisperTranscriber()
    transcriber.run()"""

import sounddevice as sd
import numpy as np
from pynput import keyboard

def test_microphone(sample_rate=44100):
    print("Hold the spacebar to record your voice...")

    is_recording = False
    recording = np.array([], dtype='float32').reshape(0, 1)
    frames_per_buffer = int(sample_rate * 0.1)

    def on_press(key):
        nonlocal is_recording
        if key == keyboard.Key.space and not is_recording:
            print("Recording started...")
            is_recording = True

    def on_release(key):
        nonlocal is_recording
        if key == keyboard.Key.space and is_recording:
            print("Recording stopped.")
            is_recording = False
            return False  # Stop the listener

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        device_index = 17
        while True:
            if is_recording:
                audio_chunk = sd.rec(frames_per_buffer, samplerate=sample_rate, channels=1, dtype='float32', device=device_index)
                sd.wait()
                recording = np.vstack([recording, audio_chunk])
            if not is_recording and recording.shape[0] > 0:
                break
        listener.join()

    print("Playing back your recording...")
    sd.play(recording, samplerate=sample_rate, device=None)
    sd.wait()
    print("Playback finished.")

# Example usage
if __name__ == "__main__":
    test_microphone()

