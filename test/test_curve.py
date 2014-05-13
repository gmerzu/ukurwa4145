from ukurwa4145 import curve, Point, Field

def test_compute():
    with curve() as domain:
        help_compute(domain)

def help_compute(domain):

    pointQ = Point(0x00AFF3EE09CB429284985849E20DE5742E194AA631490F62BA88702505629A6589, 
                  0x01B345BC134F27DA251EDFAE97B3F306B4E8B8CB9CF86D8651E4FB301EF8E1239C)

    print pointQ

    r = 0x61862343DBE63F38EA5041F60E33DFF508164DD691F4E4EBCB1B69B2A1D07C4E
    s = 0x0F131F2A6961079F956A85CED6B34DE0AC22E594532ACBDB0BF8CF170EAAFB91

    mulQ = pointQ * r
    print mulQ

    assert mulQ.x.v == 0x7686afc24faac788d7983666f0c67689cdb31a21b72ccc904ffb526e510f0efe
    assert mulQ.y.v == 0x165a812d76a4c438e691bfdc4a1c39fc77104bf41caf041fec8627884e8efa8cc

    mulS = domain.base * s
    print mulS

    assert mulS.x.v == 0xd9bf820f8d7d4b664efb1dfe20f6b602fa58b933425f23f4ec3f616943556f91
    assert mulS.y.v == 0x17a6a7d179782ac23e1b89083114f45d666db08bcde1691432ed4c446e0291c54

    pointR = mulS + mulQ

    print pointR

    r1 = Field.mul(0x71C910BAC9C494E0F2A6DBDD369C542AAF95E0CF842155C2F76595117EB0F26D, pointR.x.v)
    print hex(Field.truncate(r1))

