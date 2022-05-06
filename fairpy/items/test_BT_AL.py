import unittest
from fairpy.fairpy.items import BT_AL_Algos

class TestBT(unittest.TestCase):

    def test_bt(self):
        A, B, CP = BT_AL_Algos.BT(playerA=[1,2,3,4], playerB=[2,3,4,1])
        assert (A==[1] and B==[2] and CP==[3,4])

        A, B, CP = BT_AL_Algos.BT(playerA=[1,2,3,4,5,6], playerB=[2,3,5,4,1,6])
        assert (A==[1,4] and B==[2,5] and CP==[3,6])

        A, B, CP = BT_AL_Algos.BT(playerA=[1,2,3,4], playerB=[1,2,3,4])
        assert (A==[] and B==[] and CP==[1,2,3,4])

    def test_al(self):
        A, B, CP = BT_AL_Algos.BT(playerA=[1,2,3,4], playerB=[2,3,4,1])
        assert (A==[1,3] and B==[2,4] and CP==[])

        A, B, CP = BT_AL_Algos.BT(playerA=[1,2,3,4,5,6], playerB=[2,3,5,4,1,6])
        assert (A==[1,3] and B==[2,5] and CP==[4,6])

        A, B, CP = BT_AL_Algos.BT(playerA=[1,2,3,4], playerB=[1,2,3,4])
        assert (A==[] and B==[] and CP==[1,2,3,4])

if __name__ == "__main__":
    unittest.main()
