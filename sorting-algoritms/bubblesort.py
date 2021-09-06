'''
Bubblesort algortime
'''
def bubbleSort(lijst):
    n = len(lijst)

    # Loop door alle cijfers in je lijst
    for i in range(n - 1):

        # Pak alleen de cijfers die je nog niet hebt gepakt.
        # Deze neemt alleen de cijfers mee die nog niet op de juiste plek staan.
        for j in range(0, n - i - 1):

            # Als je een cijfer tegenkomt dat groter is dan je zelf bent, wissel dan van positie.
            if lijst[j] > lijst[j + 1]:
                lijst[j], lijst[j + 1] = lijst[j + 1], lijst[j]

'''
Main code
'''

lijst = [10, 7, 8, 9, 1, 5]
bubbleSort(lijst)

print("De gesorteerde lijst is:")
for i in range(len(lijst)):
    print(lijst[i])