'''
Insertionsort algoritme
'''
def insertionSort(lijst):

    # We lopen door de hele lijst en slaan het eerste element over
    # omdat dit ons start punt is
    for i in range(1, len(lijst)):

        # Dit is ons huidig element.
        cursor = lijst[i]

        # Blijf het huidige element verplaatsen tot het op de juiste plek staat.
        j = i - 1
        while j >= 0 and cursor < lijst[j]:
            lijst[j + 1] = lijst[j]
            j -= 1
        lijst[j + 1] = cursor


'''
Main code
'''
lijst = [10, 7, 8, 9, 1, 5]
insertionSort(lijst)

print("De gesorteerde lijst is:")
for i in range(len(lijst)):
    print(lijst[i])