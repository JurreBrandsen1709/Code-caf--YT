'''
Partitie algoritme (QuickSort helper)
'''
def partitie(lijst, start_index, eind_index):
    cursor = start_index - 1
    laatste_element = lijst[eind_index]

    for huidig in range(start_index, eind_index):

        # Als het huidige nummer kleiner of gelijk is aan het laaste element
        if lijst[huidig] <= laatste_element:

            # Verhoog dan de index van je cursor en wissel de twee getallen om
            cursor = cursor + 1
            lijst[cursor], lijst[huidig] = lijst[huidig], lijst[cursor]

    lijst[cursor + 1], lijst[eind_index] = lijst[eind_index], lijst[cursor + 1]
    return cursor + 1

'''
QuickSort algoritme
'''
def quickSort(lijst, start_index=0, eind_index=0):
    if len(lijst) == 1:
        return lijst

    if start_index < eind_index:
        partitie_index = partitie(lijst, start_index, eind_index)

        # Sorteer de elementen voor en na de partitie apart
        quickSort(lijst, start_index, partitie_index - 1)
        quickSort(lijst, partitie_index + 1, eind_index)