Results Dic:
{
'cat_01.jpg': ['cat', 'lynx', 0, 0, 0],
'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 0],
'cat_02.jpg': ['cat', 'tabby, tabby cat, cat', 1, 0, 0],
'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 1, 1],
'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 0, 0],
'gecko_02.jpg': ['gecko', 'banded gecko, gecko', 1, 0, 0],
'cat_07.jpg': ['cat', 'egyptian cat, cat', 1, 0, 0],
'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1, 0, 0],
'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 0, 0],
'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 0, 0],
'Collie_03797.jpg': ['collie', 'collie', 1, 0, 0],
'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 0, 0],
'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 0, 0],
'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail, cottontail rabbit, rabbit', 1, 0, 0],
'polar_bear_04.jpg': ['polar bear', 'ice bear, polar bear, ursus maritimus, thalarctos maritimus', 1, 0, 0],
'Poodle_07956.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 0],
'fox_squirrel_01.jpg': ['fox squirrel', 'fox squirrel, eastern fox squirrel, sciurus niger', 1, 0, 0],
'Beagle_01170.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1],
'Boston_terrier_02285.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 0, 0],
'skunk_029.jpg': ['skunk', 'skunk, polecat, wood pussy', 1, 0, 0],
'Boston_terrier_02303.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 0, 0],
'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1, 1, 1],
'Beagle_01141.jpg': ['beagle', 'beagle', 1, 1, 1],
'Basenji_00974.jpg': ['basenji', 'basenji', 1, 0, 0],
'gecko_80.jpg': ['gecko', 'tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui', 0, 0, 0],
'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 0, 0],
'Boxer_02426.jpg': ['boxer', 'boxer', 1, 1, 1],
'Basenji_00963.jpg': ['basenji', 'basenji', 1, 0, 0],
'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 0, 0],
'Golden_retriever_05182.jpg': ['golden retriever', 'golden retriever', 1, 0, 0],
'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1, 0, 0],
'great_horned_owl_02.jpg': ['great horned owl', 'ruffed grouse, partridge, bonasa umbellus', 0, 0, 0],
'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 0, 0],
'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 1, 0, 0],
'Beagle_01125.jpg': ['beagle', 'beagle', 1, 1, 1],
'Great_pyrenees_05367.jpg': ['great pyrenees', 'kuvasz', 0, 0, 1],
'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1, 1, 1],
'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel, english cocker spaniel, cocker', 1, 1, 0],
'Golden_retriever_05257.jpg': ['golden retriever', 'golden retriever', 1, 0, 0],
'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1, 0, 0]
}


"""
results_dic will have the following adjusted format:

key = pet image filename (ex: Beagle_01141.jpg)
value = List with:

index 0 = Pet Image Label (ex: beagle)
index 1 = Classifier Label (ex: english foxhound)
index 2 = Labels match?, 0/1 where 1 = labels match , 0 = labels don't match (ex: 0)
index 3 = Pet Image Label is a dog?, 0/1 where 1= Pet Image Label is a dog, 0 = Pet Image Label isn't a dog (ex: 1)
index 4 = Classifier Label is a dog?,0/1 where 1= Classifier Label is a dog, 0 = Classifier Label isn't a dog (ex: 1)

"""
example_dictionary = {'Beagle_01141.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1]}

