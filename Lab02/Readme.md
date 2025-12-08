## Title:Basic sound processing and manipulation using python
## Objectives:
1. Load and play a sample sound clip(drum.wav)
2. Process and manipulate and audio signal
3. Perform audio using sign wave
4. Visualize audio waveform and spectrum properties
## Background Theory:
* Sound and audio represention
  
  Sound is an analog wave created by vibrations, and audio representation converts this continuous signal into a digital format for computer processing. Digital audio stores sound as numerical samples over time, enabling playback, editing, and analysis.

  Features:

   i) Represents sound using amplitude vs. time.

   ii) Enables storage in formats like WAV, MP3, FLAC.

   iii) Allows digital processing such as filtering and noise reduction.

   iv) Can be viewed in time-domain or frequency-domain.

   Example: A microphone recording your voice becomes a list of sample values like [0.2, 0.4, 0.1, …].

  
* Sampling and Quantization
  
  Sampling captures sound at regular time intervals, while quantization assigns each sample a discrete numeric value. Together, they convert analog audio into digital form.

  Features:

   i) Sampling rate decides clarity (e.g., 44.1 kHz for music).

   ii) Bit depth affects precision and dynamic range (e.g., 16-bit).

  iii) Higher values give better quality and less noise.

   iv) Based on Nyquist Theorem to avoid aliasing.

   Example: Telephone audio uses 8 kHz sampling, while studio audio uses 48 kHz for higher detail.

* PyDub
  
  PyDub is a Python library used for simple and efficient audio editing and manipulation.

  Features:

   i) Supports cutting, merging, and slicing audio.

   ii) Allows volume control, fade-in/out, and speed change.

  iii) Converts between formats (MP3 ↔ WAV).

   iv) Easy to use with FFmpeg backend.

   Example: Trim a 10-second audio clip to 5 seconds using audio[:5000].

* Librose
  
  Librosa is an advanced Python library used for audio analysis, especially in music and machine-learning applications.

  Features:

   i) Generates spectrograms and mel-spectrograms.

  ii) Extracts MFCCs, chroma, tempo, and pitch.

 iii) Provides tools for visualization and signal processing.

  iv) Used in speech recognition, music classification, and feature extraction.

  Example: Using Librosa to create a spectrogram to analyze the frequency content of a song.

## Procedure
## Output
## Conclusion
