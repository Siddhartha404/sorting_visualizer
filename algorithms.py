import pygame
#Bubble sort
def bubbleSort(arry, drawArray, delay=50):
    n = len(arry)
    for i in range(n):
        for j in range(n-i-1):
            #since we are comparing j and j+1 we will put then into a function that will draw it later
            drawArray(arry,[j,j+1])
            swap = False
            if arry[j] > arry[j+1]:
                swap = True
                pygame.time.delay(delay)

                arry[j],arry[j+1] = arry[j+1],arry[j]
                #updating after the swap
                drawArray(arry,[j,j+1],swap)
                pygame.time.delay(delay)
                
#Quick Sort
