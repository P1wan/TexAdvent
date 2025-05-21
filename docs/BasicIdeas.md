- Location(Room)
- Observables(Anything that receives a description?)
- Interactables(Objects/Creatures one can interact with)
- Interactions(Actions one can make)

Abstract Structure(object oriented):
- Rooms
- Structures(Things that are stationary)
- Items(Things that are not stationary)
- NPCs(Any "Object" That has more dynamic interactions, descriptions and potentially can change rooms)
- Combinations(Any union of two or more objects that results in a change of state for themselves or another object, potentially removing them and adding a new object of their combination, resulting in a change of state for another object and so on, might be simply pushed into interactions itself)
- Interactions(? possibly not an object itself but just a structure to be used, need to find the optimal way to deal with words and their interpretations): Actions one can perform to alter the state of objects, including performing combinations
- Parser: identifies player intent via a structure of (verb) (noun) (optional connector) (optional nown), parser will follow a data structure that groups appropriate words with interaction keys and possibly a fuzzy matching system to suggest corrections, interaction keys will identify things by finding the correct option(if mentioning an object, ensure the object is interactable, by being in the same room, being on the person, or some other detail)
-- noun: refers to objects or concepts such as direction
-- verb: describes interactions, ways to alter the state of objects and perform combinations


possibilities of words:
basic verbs:
USE
LOOK
REMEMBER(to list help regarding something, a word, an object, lore elements)
MOVE
GRAB/RELEASE(grabbing something and moving might result in dragging it?)
STORE(to put on a place, such as backpack or a container?)
LISTEN(can be used to just hear if there are any specific sound descriptions on a place, or LISTEN TO to listen to a specific object or hear what an NPC has to say)
SPEAK: ability to say something, can be spoken aloud for puzzles or other mechanics, or SPEAK TO (noun) to say something directly to an NPC or something else, possibly ensure keyword-based dialogue with question suggestions that can be asked by typing a suggested keyword, and allowing user to type a random word to ask a question about something, possibly with the ASK and TELL keywords to inquire about something or tell something.


Possible Specific Verbs:
verbs that can fit under USE, possibly:
-- ATTACK
-- ENTER
-- OPEN
-- THROW

Connectors:
- AT, ON, UNDER, ABOVE, BEHIND
-- Useable on LOOK, to look under or behind something, throw above or under, depends on the complexity, system should allow for solutions to be simple enough if programmed that way


Nouns:
- nouns will usually be defined by the objects in the game, such as rooms, structures, NPCs and so on
- other nouns can be universal like:
-- SELF, ME or other variations to refer to the protagonist
-- Cardinal directions(NORTH, SOUTH, EAST, WEST) and general directions such as UP, DOWN


Combat: will, at least for now, be simply a puzzle like any other, if you have the correct weapon and are in the correct state, attacking the enemy(perhaps in the correct way) will result in a victory, otherwise you are defeated

Certain things could happen automatically if they are programmed to do so(automatic interactions? or general rules), if user says a speak command and there is only one NPC in the room, they might begin talking to the NPC, since they would be heard, if an interaction happens by placing something somewhere, that something will leave the player's inventory unless they grab it again, but if something like an NPC appears magically by the waving of a wand, they might be set to dissapear when the player leaves the room
