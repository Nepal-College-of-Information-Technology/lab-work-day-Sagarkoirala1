## Title:Basic sound processing and manipulation using python
---
## Objectives:
1. Load and play a sample sound clip(drum.wav)
2. Process and manipulate and audio signal
3. Perform audio using sign wave
4. Visualize audio waveform and spectrum properties
 ---
## Background Theory:

### 1. Sound and audio represention
  
  Sound is an analog wave created by vibrations, and audio representation converts this continuous signal into a digital format for computer processing. Digital audio stores sound as numerical samples over time, enabling playback, editing, and analysis.

  Features:

   i) Represents sound using amplitude vs. time.

   ii) Enables storage in formats like WAV, MP3, FLAC.

   iii) Allows digital processing such as filtering and noise reduction.

   iv) Can be viewed in time-domain or frequency-domain.

   Example: A microphone recording your voice becomes a list of sample values like [0.2, 0.4, 0.1, …].

  
### 2.Sampling and Quantization
  
  Sampling captures sound at regular time intervals, while quantization assigns each sample a discrete numeric value. Together, they convert analog audio into digital form.

  Features:

   i) Sampling rate decides clarity (e.g., 44.1 kHz for music).

   ii) Bit depth affects precision and dynamic range (e.g., 16-bit).

  iii) Higher values give better quality and less noise.

   iv) Based on Nyquist Theorem to avoid aliasing.

   Example: Telephone audio uses 8 kHz sampling, while studio audio uses 48 kHz for higher detail.

### 3. PyDub
  
  PyDub is a Python library used for simple and efficient audio editing and manipulation.

  Features:

   i) Supports cutting, merging, and slicing audio.

   ii) Allows volume control, fade-in/out, and speed change.
  

  iii) Converts between formats (MP3 ↔ WAV).
  

   iv) Easy to use with FFmpeg backend.
  

   Example: Trim a 10-second audio clip to 5 seconds using audio[:5000].

### 4. Librose
  
  Librosa is an advanced Python library used for audio analysis, especially in music and machine-learning applications.

  Features:

   i) Generates spectrograms and mel-spectrograms.

  ii) Extracts MFCCs, chroma, tempo, and pitch.
  
 iii)  Provides tools for visualization and signal processing.
 
  iv) Used in speech recognition, music classification, and feature extraction.
  
   Example: Using Librosa to create a spectrogram to analyze the frequency content of a song.
   
   ---
  

## Procedure

 i. The required libraries, such as Pydub, Librosa, NumPy, and Matplotlib, had been imported.

ii. The sample audio file (drum.wav) had been loaded using either Pydub.

iii. The audio had been played in Python to verify that it had been loaded correctly.

iv. The audio had been processed and manipulated by performing tasks such as adjusting the volume, cutting or trimming sections, adding simple effects, and resampling or changing the playback speed.

v. The audio signal had been analyzed by converting it into a waveform (time-domain plot).

vi. The spectrogram had been computed and displayed using Librosa to observe the frequency content of the audio.

vii. A simple audio signal, such as a sine wave, had been synthesized using NumPy .

viii. The synthesized signal had been visualized in both waveform and spectrogram form.

ix. Finally, the processed audio had been saved or exported using Pydub or Librosa.

---

## Output
The audio file drum.wav was successfully loaded and played using Pydub or Librosa. The waveform clearly displayed the time-domain representation, and the spectrogram showed the frequency distribution over time. A synthetic sine wave was created using NumPy, with both its waveform and spectrogram visualized successfully. The processed audio, including trimming, volume adjustment, and resampling, was exported correctly.

---

## Conclusion
In this lab, audio was successfully loaded, analyzed, and processed using Pydub, Librosa, NumPy, and Matplotlib. Waveforms and spectrograms demonstrated time and frequency characteristics, while a synthetic sine wave was generated and visualized. The experiment highlighted key audio manipulations like trimming, volume adjustment, and resampling, reinforcing practical skills in digital audio processing.
