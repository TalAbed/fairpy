# "Two-Person Fair Division of Indivisible Items: An Efficient, Envy-Free Algorithm"
# by : Steven J. Brams, D. Marc Kilgour, Christian Klamler
# June 2013
# https://www.ams.org/notices/201402/rnoti-p130.pdf
# the article presents two algorithms of fair division of items, which is envy-free.
# the algorithms only depends on the players rate of the items (zero importance for the items values)
# המאמר מציג 2 אלגוריתמים לחלוקה הוגנת נטולת קנאה המבוססת אך ורק על האופן שבו השחקנים מדרגים את החפצים
# אין תלות בערך של כל חפץ

def BT (playerA: list, playerB: list):
    """
    >>> BT([1,2,3,4],[2,3,4,1])
    [1], [2], [3,4]

    >>> BT([1,2,3,4,5,6], [2,3,5,4,1,6])
    [1,4], [2,5], [3,6]

    >>> BT([1,2,3,4], [1,2,3,4])
    [], [], [1,2,3,4]
    """
    return [],[],[]

def AL (playerA: list, playerB: list):
    """
    >>> AL([1,2,3,4],[2,3,4,1])
    [1,3], [2,4], []

    >>> AL([1,2,3,4,5,6], [2,3,5,4,1,6])
    [1,3], [2,5], [4,6]

    >>> AL([1,2,3,4], [1,2,3,4])
    [], [], [1,2,3,4]
    """
    return [],[],[]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())