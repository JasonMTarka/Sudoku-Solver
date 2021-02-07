
NAMES = ("topleft",
        "topmid", 
        "topright",
        "midleft",
        "center",
        "midright",
        "botleft",
        "botmid",
        "botright")

LOCATIONS = {
        "topleft": {
                "topleft": (0,0),
                "topmid": (0,1),
                "topright": (0,2),
                "midleft": (1,0),
                "center": (1,1),
                "midright": (1,2),
                "botleft": (2,0),
                "botmid": (2,1),
                "botright": (2,2)
        },
        "topmid":{
                "topleft": (0,3),
                "topmid": (0,4),
                "topright": (0,5),
                "midleft": (1,3),
                "center": (1,4),
                "midright": (1,5),
                "botleft": (2,3),
                "botmid": (2,4),
                "botright": (2,5)
        },
        "topright":{
                "topleft": (0,6),
                "topmid": (0,7),
                "topright": (0,8),
                "midleft": (1,6),
                "center": (1,7),
                "midright": (1,8),
                "botleft": (2,6),
                "botmid": (2,7),
                "botright": (2,8)
        },
        "midleft":{
                "topleft": (3,0),
                "topmid": (3,1),
                "topright": (3,2),
                "midleft": (4,0),
                "center": (4,1),
                "midright": (4,2),
                "botleft": (5,0),
                "botmid": (5,1),
                "botright": (5,2)
        },
        "center":{
                "topleft": (3,3),
                "topmid": (3,4),
                "topright": (3,5),
                "midleft": (4,3),
                "center": (4,4),
                "midright": (4,5),
                "botleft": (5,3),
                "botmid": (5,4),
                "botright": (5,5)
        },
        "midright":{
                "topleft": (3,6),
                "topmid": (3,7),
                "topright": (3,8),
                "midleft": (4,6),
                "center": (4,7),
                "midright": (4,8),
                "botleft": (5,6),
                "botmid": (5,7),
                "botright": (5,8)
        },
        "botleft":{
                "topleft": (6,0),
                "topmid": (6,1),
                "topright": (6,2),
                "midleft": (7,0),
                "center": (7,1),
                "midright": (7,2),
                "botleft": (8,0),
                "botmid": (8,1),
                "botright": (8,2)
        },
        "botmid":{
                "topleft": (6,3),
                "topmid": (6,4),
                "topright": (6,5),
                "midleft": (7,3),
                "center": (7,4),
                "midright": (7,5),
                "botleft": (8,3),
                "botmid": (8,4),
                "botright": (8,5)
        },
        "botright":{
                "topleft": (6,6),
                "topmid": (6,7),
                "topright": (6,8),
                "midleft": (7,6),
                "center": (7,7),
                "midright": (7,8),
                "botleft": (8,6),
                "botmid": (8,7),
                "botright": (8,8)
        }
}

SUDOKUS = {

"Easy #1":[
	[1,0,0,9,0,4,0,8,2],
	[0,5,2,6,8,0,3,0,0],
	[8,6,4,2,0,0,9,1,0],
	[0,1,0,0,4,9,8,0,6],
	[4,9,8,3,0,0,7,0,1],
	[6,0,7,0,1,0,0,9,3],
	[0,8,6,0,3,5,2,0,9],
	[5,0,9,0,0,2,1,3,0],
	[0,3,0,4,9,7,0,0,8]
	],
"Easy #2":[
	[0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]
        ],
"Easy #3":[
	[0,0,0,8,5,0,0,0,7],
        [3,8,2,0,0,0,0,0,0],
        [9,0,7,0,3,0,1,8,4],
        [0,2,8,0,0,6,0,3,0],
        [4,0,9,0,0,0,8,0,1],
        [0,3,0,9,0,0,4,7,0],
        [7,1,3,0,6,0,2,0,8],
        [0,0,0,0,0,0,5,1,6],
        [2,0,0,0,9,8,0,0,0]
        ],
"Medium #1":[
	[0,0,0,1,0,5,0,6,8],
        [0,0,0,0,0,0,7,0,1],
        [9,0,1,0,0,0,0,3,0],
        [0,0,7,0,2,6,0,0,0],
        [5,0,0,0,0,0,0,0,3],
        [0,0,0,8,7,0,4,0,0],
        [0,3,0,0,0,0,8,0,5],
        [1,0,5,0,0,0,0,0,0],
        [7,9,0,4,0,1,0,0,0]
        ],
"Medium #2":[
	[0,0,0,4,8,0,2,0,9],
        [0,0,0,0,7,0,0,5,1],
        [0,8,3,0,2,0,0,0,0],
        [0,0,4,0,0,0,0,0,0],
        [7,6,0,0,0,0,0,0,2],
        [0,5,0,7,0,9,0,0,0],
        [0,0,7,0,0,5,9,0,4],
        [0,0,0,0,0,0,5,0,0],
        [4,0,0,8,0,0,6,7,0]
        ],
"Hard #1":[
	[6,0,0,0,0,0,5,3,0],
        [0,0,0,0,0,2,7,0,0],
        [5,0,7,0,9,6,0,1,8],
        [0,0,6,0,0,1,0,8,0],
        [0,9,8,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,0,0],
        [0,0,0,0,0,0,9,0,0],
        [0,0,0,2,0,0,0,4,3],
        [3,1,0,0,0,9,0,6,2]
        ],
"Super Hard #1":[
	[4,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,9,0,0,0],
	[0,0,0,0,0,0,7,8,5],
	[0,0,7,0,4,8,0,5,0],
	[0,0,1,3,0,0,0,0,0],
	[0,0,6,0,7,0,0,0,0],
	[8,6,0,0,0,0,9,0,3],
	[7,0,0,0,0,5,0,6,2],
	[0,0,3,7,0,0,0,0,0]
	]
}
