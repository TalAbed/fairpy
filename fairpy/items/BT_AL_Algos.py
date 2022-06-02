# "Two-Person Fair Division of Indivisible Items: An Efficient, Envy-Free Algorithm"
# by : Steven J. Brams, D. Marc Kilgour, Christian Klamler
# June 2013
# https://www.ams.org/notices/201402/rnoti-p130.pdf
# the article presents two algorithms of fair division of items, which is envy-free.
# the algorithms only depends on the players rate of the items (zero importance for the items values)
# המאמר מציג 2 אלגוריתמים לחלוקה הוגנת נטולת קנאה המבוססת אך ורק על האופן שבו השחקנים מדרגים את החפצים
# אין תלות בערך של כל חפץ

def remove(playerA: list, playerB: list):
    playerA.remove(playerB[0])
    playerB.remove(playerA[0])
    del playerA[0]
    del playerB[0]
    return playerA, playerB

def BT (playerA: list, playerB: list):
    """
    >>> BT([1,2,3,4],[2,3,4,1])
    ([1], [2], [3, 4])

    >>> BT([1,2,3,4,5,6], [2,3,5,4,1,6])
    ([1, 4], [2, 5], [3, 6])

    >>> BT([1,2,3,4], [1,2,3,4])
    ([], [], [1, 2, 3, 4])
    """
    A = []
    B = []
    CP = []
    while len(playerA)>0:
        if playerA[0] != playerB[0]:
            A.append(playerA[0])
            B.append(playerB[0])
            remove(playerA, playerB)
        else:
            CP.append(playerA[0])
            del playerA[0]
            del playerB[0]
    return A, B, CP

def AL (playerA: list, playerB: list):
    """
    >>> AL([1,2,3,4],[2,3,4,1])
    ([1, 3], [2, 4], [])

    >>> AL([1,2,3,4,5,6], [2,3,5,4,1,6])
    ([1, 3], [2, 5], [4, 6])

    >>> AL([1,2,3,4], [1,2,3,4])
    ([], [], [1, 2, 3, 4])
    """
    A = []
    B = []
    CP = []
    originA = playerA.copy()
    originB = playerB.copy()
    # make the first allocation
    first = False
    while not first:
        #print("in")
        if playerA[0]==playerB[0]:
            CP.append(playerA[0])
            del playerA[0]
            del playerB[0]
        else:
            A.append(playerA[0])
            B.append(playerB[0])
            remove(playerA, playerB)
            first = True
    #make rest of the allocations
    t=1
    given = False
    #print(originA, originB)
    #print(playerA, playerB)
    while len(playerA)>0:
        print("return",A,B,CP)
        print("kelet", playerA, playerB)
        if playerA[0] != playerB[0]:
            #print("in first if")
            A.append(playerA[0])
            B.append(playerB[0])
            remove(playerA, playerB)
            #print("bad", playerA, playerB)
        else:
            tied_item = playerA[0]
            #print("ti",tied_item)
            del playerA[0]
            del playerB[0]
            for item in playerA:
                if not given:
                    B.append(tied_item)
                    A.append(item)
                    index = originA.index(item)
                    counter=0
                    for b in B:
                        if originA.index(b)<index:
                            counter+=1
                    if counter<=t:
                        given = True
                        playerB.remove(item)
                        playerA.remove(item)
                    else:
                        B.remove(tied_item)
                        A.remove(item)
                        t+=1
            #print("shit", playerA, playerB)
            t=1
            for item in playerB:
                if not given:
                    A.append(tied_item)
                    B.append(item)
                    index = originB.index(item)
                    counter=0
                    for a in A:
                        if originB.index(a)<index:
                            counter+=1
                    if counter<=t:
                        given = True
                        #print("lalala",playerA[0], playerB[0])
                        #print("wello", playerA, playerB)
                        playerA.remove(item)
                        playerB.remove(item)
                    else:
                        A.remove(tied_item)
                        B.remove(item)
                        t+=1
            if given == False:
                CP.append(playerA[0])
                remove(playerA, playerB)
            t+=1
            #print(A,B,CP)
    return A,B,CP

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())