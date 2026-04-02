class Pentominoes:
    def __init__(self, num_pentominoes):
        self.pentominoes = [
            [
                [0,0,0,0,0,
                1,1,1,1,1,
                0,0,0,0,0,
                0,0,0,0,0,
                0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,
                0,2,0,0,0,
                0,2,2,0,0,
                0,0,2,0,0,
                0,0,2,0,0],
            ],
            [
                [0,0,0,0,0,
                0,3,3,3,0,
                0,0,3,0,0,
                0,0,3,0,0,
                0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,
                0,0,0,4,0,
                0,0,4,4,0,
                0,4,4,0,0,
                0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,0,0,
                0,0,5,5,0],
            ],
            [
                [0,0,0,0,0,
                0,0,0,6,0,
                0,0,6,6,0,
                0,0,6,0,0,
                0,0,6,0,0],
            ],
            [
                [0,0,0,0,0,
                0,0,8,0,0,
                0,0,8,0,0,
                0,0,8,0,0,
                0,8,8,0,0],
            ],
            [
                [0,0,0,0,0,
                0,9,9,0,0,
                0,9,9,0,0,
                0,0,9,0,0,
                0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,
                0,0,10,10,0,
                0,0,10,10,0,
                0,0,10,0,0,
                0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,
                0,0,0,11,0,
                0,0,11,11,0,
                0,0,0,11,0,
                0,0,0,11,0],
            ]
        ]
        
        self.num_pentominoes = num_pentominoes
        self.selected_pentominoes = self.pentominoes[:num_pentominoes]
        #self.bool2lab = bool2lab
#bool2lab = True
num_pentominoes = 10  # Example: Selecting 5 pentominoes
pentominoes = Pentominoes(num_pentominoes)

#print(pentominoes.selected_pentominoes[5])
