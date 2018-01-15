
# Load External Modules
import mingus
from mingus.containers import Note
from mingus.containers import Composition
from mingus.containers import Track
from mingus.containers import Bar
from datetime import datetime

# Custom Module
from NoteGenerator import NoteGenerator
from NoteGenerator import note_collection

# Constants

FIRST = 0
SECOND = 1
THIRD = 2
FOURTH = 3

# Prefix

pre = "test - "

# Start Composition

composition = Composition()
composition.set_author('Melody Nieun', 'nh889@nyu.edu')
composition.set_title('First Melody Composition with Python')

# Start a track (which will be a part of the composition defined above)
track = Track()

# Start a bar (which will be a part of the track defined above)
bar = Bar()

# Generate the first note
notes = note_collection(['D', 'A'])
generator = NoteGenerator(notes=notes, duration=4)#, conditions={0: condition1})
generator.add_notes_to(bar, count=1) # This line add the first note to the bar defined above
prev_notes = generator.added_notes

# Generate the second note
notes = note_collection(['D', 'F#', 'A'])
allowed_condition_1 = lambda parameters: True if (parameters['prev_note'] != parameters['current_note']) else False
generator = NoteGenerator(notes=notes, duration=4, allowed_conditions=[allowed_condition_1], parameters={'prev_note': prev_notes[FIRST]})
generator.add_notes_to(bar, count=1) # This line add the second note to the bar defined above

# Add bar to the track
track.add_bar(bar)

# Add track to the composition
composition.add_track(track)

# Print the summary of the composition
print(composition)

# Export to a MIDI file
mingus.midi.midi_file_out.write_Composition(pre + "melody generated at " + str(datetime.now()) + ".mid", composition, bpm=80, repeat=0, verbose=False)