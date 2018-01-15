
import mingus
from mingus.containers import Note
import mingus.core.notes as notes

from mingus.containers import Composition
from mingus.containers import Track
from mingus.containers import Bar
from mingus.containers import NoteContainer
from mingus.midi import midi_file_out
import mingus.core.chords as chords
import random
from datetime import datetime

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def note_collection(notes):
    ar = []

    for note in notes:
        ar.append(Note(note))

    return ar

class NoteGenerator:
    def __init__(self, notes, duration = 4, conditions=None, allowed_conditions=[], parameters= {}):
        self.notes = notes
        self.type = type
        self.duration = duration
        self.conditions = conditions
        self._current_position = 0
        self.allowed_conditions = allowed_conditions
        self.parameters=parameters
        self.added_notes = []

    def get_note(self):

        note = None
        is_valid = True
        initial = True

        while (is_valid==False or initial == True):
            is_valid = True
            initial = False
            rand_index = random.randrange(0, len(self.notes))
            note = self.notes[rand_index]

            dic = merge_two_dicts ({'current_note': note}, self.parameters)

            for single_condition in self.allowed_conditions:

                if single_condition(dic) != True:
                    is_valid=False

        self._current_position += 1
        return note

    def add_notes_to(self, bar, count):
        added_notes = []
        for index in range(0, count):
            note = self.get_note()
            is_added = bar.place_notes(note, self.duration)
            if is_added==False:
                break
            added_notes.append(note)
        self.added_notes = added_notes