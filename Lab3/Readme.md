

## *MIDI Note Processing and Algorithmic Music Generation*

---

## *Objectives*
- Print MIDI channels, notes, and their corresponding frequencies.  
- Generate simple beat, harmony, and melody patterns using MIDI notes.  
- Play individual MIDI tracks (.mid files).  
- Convert MIDI tracks into standard audio (.wav) files using Python tools.

---

## *Background Theory*

### *1. MIDI Standard*

MIDI (Musical Instrument Digital Interface) is a digital communication standard used to transmit musical performance data between electronic instruments and computers. It sends event-based instructions, not actual audio signals.

The MIDI standard supports 16 channels, allowing multiple instruments to be controlled simultaneously. Musical data such as note_on, note_off, velocity, and control changes are represented using 7-bit values (0–127). MIDI note numbers map to musical pitches, for example, 60 = Middle C and 69 = A4 (440 Hz).

MIDI files are compact, device-independent, and widely used for music production, synchronization, and editing.
  - Example: 60 = Middle C, 69 = A4 (440 Hz)

### *Frequency Formula*

To convert a MIDI note number n to its frequency: f = 440 × 2^((n - 69) / 12)


---

### *2. Music Theory (Basic)*
 - Beat:
The basic unit of time in a musical composition that defines the rhythm.

 - Harmony:  
   The combination of two or more musical notes played simultaneously to form chords.

 - Melody:
   A sequential pattern of musical notes arranged in time, forming the main tune of a piece of music.

---

### *3. Python Libraries Used*

- Mido:
Used for reading, writing, and analyzing MIDI files in Python.

- Pygame:
Used for playing MIDI files and handling basic audio playback.

---

## *Procedure*

i. The required Python libraries (mido, math, and pygame) had been imported to support MIDI processing, frequency calculation, and audio playback.

ii. The input MIDI file had been loaded using the mido.MidiFile() function.

iii. The MIDI file had been iterated message by message to identify all note_on events.

iv. The MIDI note numbers and channel values had been extracted and printed for analysis.

v. A function had been defined to convert MIDI note numbers into corresponding frequencies using the standard formula.

vi. A beat pattern had been generated to provide rhythmic structure.

vii. A harmony track had been generated using simple triads based on the root notes.

viii. A melody sequence had been generated from the extracted MIDI notes.

ix. The generated beat, harmony, and melody sequences had been saved as separate MIDI files named beat.mid, harmony.mid, and melody.mid.

x. The melody MIDI file had been loaded into the pygame mixer and had been played.

xi. The generated MIDI files had been converted into WAV format, provided that a compatible synthesizer or MIDI backend had been available.

---

## *Output*

- Printed MIDI:
  - Channels  
  - Notes  
  - Frequencies  

- Generated MIDI tracks:
  - beat.mid
  - harmony.mid
  - melody.mid

- Played audio using Pygame.

- Converted .wav files from MIDI tracks.

---

## *Conclusion*

This lab explored MIDI processing using Python. MIDI note information was extracted and converted into corresponding frequencies. Musical patterns such as beats, harmony, and melody were generated programmatically. The generated MIDI files were played and converted into standard audio formats. This experiment enhanced understanding of the MIDI protocol, basic music theory concepts, and Python-based algorithmic music generation.
