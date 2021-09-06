'''
Mergesort algortime
'''
def mergeSort(lijst):
    if len(lijst) > 1:

        # Bepaal het midden van de lijst (let op 9/2 = 4)
        midden = len(lijst) // 2

        # Splits de lijst in twee.
        links = lijst[:midden]
        rechts = lijst[midden:]

        # Sorteer beide helften
        mergeSort(links)
        mergeSort(rechts)

        i = j = k = 0

        while i < len(links) and j < len(rechts):
            if links[i] < rechts[j]:
                lijst[k] = links[i]
                i += 1
            else:
                lijst[k] = rechts[j]
                j += 1
            k += 1


        while i < len(links):
            lijst[k] = links[i]
            i += 1
            k += 1

        while j < len(rechts):
            lijst[k] = rechts[j]
            j += 1
            k += 1

'''
Main code
'''
lijst = [10, 7, 8, 9, 1, 5]
mergeSort(lijst)

print("De gesorteerde lijst is:")
for i in range(len(lijst)):
    print(lijst[i])