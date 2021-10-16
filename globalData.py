
'''
=====================
Gamemode Queue Values
=====================
Normal = 400
Ranked Solo/Duo = 420
Ranked Flex = 440
ARAM = 450
'''

#Initialize Functions
""" def initChampDict() -> dict:
    latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
    champ_dict = {}

    for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[int(row['key'])] = row['id']
    return champ_dict """

gameModeCode = {'normal': 400, 'rankedSolo': 420, 'rankedFlex': 440, 'aram': 450, None: None}

champ_dict = {266: 'Aatrox', 103: 'Ahri', 84: 'Akali', 12: 'Alistar', 32: 'Amumu', 34: 'Anivia', 1: 'Annie', 523: 'Aphelios', 22: 'Ashe', 136: 'AurelionSol', 268: 'Azir', 432: 'Bard', 
53: 'Blitzcrank', 63: 'Brand', 201: 'Braum', 51: 'Caitlyn', 164: 'Camille', 69: 'Cassiopeia', 31: 'Chogath', 42: 'Corki', 122: 'Darius', 131: 'Diana', 119: 'Draven', 36: 'DrMundo', 
245: 'Ekko', 60: 'Elise', 28: 'Evelynn', 81: 'Ezreal', 9: 'Fiddlesticks', 114: 'Fiora', 105: 'Fizz', 3: 'Galio', 41: 'Gangplank', 86: 'Garen', 150: 'Gnar', 79: 'Gragas', 104: 'Graves', 
120: 'Hecarim', 74: 'Heimerdinger', 420: 'Illaoi', 39: 'Irelia', 427: 'Ivern', 40: 'Janna', 59: 'JarvanIV', 24: 'Jax', 126: 'Jayce', 202: 'Jhin', 222: 'Jinx', 145: 'Kaisa', 429: 'Kalista', 
43: 'Karma', 30: 'Karthus', 38: 'Kassadin', 55: 'Katarina', 10: 'Kayle', 141: 'Kayn', 85: 'Kennen', 121: 'Khazix', 203: 'Kindred', 240: 'Kled', 96: 'KogMaw', 7: 'Leblanc', 64: 'LeeSin', 
89: 'Leona', 876: 'Lillia', 127: 'Lissandra', 236: 'Lucian', 117: 'Lulu', 99: 'Lux', 54: 'Malphite', 90: 'Malzahar', 57: 'Maokai', 11: 'MasterYi', 21: 'MissFortune', 62: 'MonkeyKing', 
82: 'Mordekaiser', 25: 'Morgana', 267: 'Nami', 75: 'Nasus', 111: 'Nautilus', 518: 'Neeko', 76: 'Nidalee', 56: 'Nocturne', 20: 'Nunu', 2: 'Olaf', 61: 'Orianna', 516: 'Ornn', 80: 'Pantheon', 
78: 'Poppy', 555: 'Pyke', 246: 'Qiyana', 133: 'Quinn', 497: 'Rakan', 33: 'Rammus', 421: 'RekSai', 58: 'Renekton', 107: 'Rengar', 92: 'Riven', 68: 'Rumble', 13: 'Ryze', 360: 'Samira', 
113: 'Sejuani', 235: 'Senna', 147: 'Seraphine', 875: 'Sett', 35: 'Shaco', 98: 'Shen', 102: 'Shyvana', 27: 'Singed', 14: 'Sion', 15: 'Sivir', 72: 'Skarner', 37: 'Sona', 16: 'Soraka', 
50: 'Swain', 517: 'Sylas', 134: 'Syndra', 223: 'TahmKench', 163: 'Taliyah', 91: 'Talon', 44: 'Taric', 17: 'Teemo', 412: 'Thresh', 18: 'Tristana', 48: 'Trundle', 23: 'Tryndamere', 
4: 'TwistedFate', 29: 'Twitch', 77: 'Udyr', 6: 'Urgot', 110: 'Varus', 67: 'Vayne', 45: 'Veigar', 161: 'Velkoz', 254: 'Vi', 112: 'Viktor', 8: 'Vladimir', 106: 'Volibear', 19: 'Warwick', 
498: 'Xayah', 101: 'Xerath', 5: 'XinZhao', 157: 'Yasuo', 777: 'Yone', 83: 'Yorick', 350: 'Yuumi', 154: 'Zac', 238: 'Zed', 115: 'Ziggs', 26: 'Zilean', 142: 'Zoe', 143: 'Zyra'}


id_dict = {'Aatrox': 266, 'Ahri': 103, 'Akali': 84, 'Alistar': 12, 'Amumu': 32, 'Anivia': 34, 'Annie': 1, 'Aphelios': 523, 'Ashe': 22, 'AurelionSol': 136, 'Azir': 268, 'Bard': 432, 
'Blitzcrank': 53, 'Brand': 63, 'Braum': 201, 'Caitlyn': 51, 'Camille': 164, 'Cassiopeia': 69, 'Chogath': 31, 'Corki': 42, 'Darius': 122, 'Diana': 131, 'Draven': 119, 
'DrMundo': 36, 'Ekko': 245, 'Elise': 60, 'Evelynn': 28, 'Ezreal': 81, 'Fiddlesticks': 9, 'Fiora': 114, 'Fizz': 105, 'Galio': 3, 'Gangplank': 41, 'Garen': 86, 'Gnar': 150, 
'Gragas': 79, 'Graves': 104, 'Hecarim': 120, 'Heimerdinger': 74, 'Illaoi': 420, 'Irelia': 39, 'Ivern': 427, 'Janna': 40, 'JarvanIV': 59, 'Jax': 24, 'Jayce': 126, 'Jhin': 202, 
'Jinx': 222, 'Kaisa': 145, 'Kalista': 429, 'Karma': 43, 'Karthus': 30, 'Kassadin': 38, 'Katarina': 55, 'Kayle': 10, 'Kayn': 141, 'Kennen': 85, 'Khazix': 121, 'Kindred': 203, 
'Kled': 240, 'KogMaw': 96, 'Leblanc': 7, 'LeeSin': 64, 'Leona': 89, 'Lillia': 876, 'Lissandra': 127, 'Lucian': 236, 'Lulu': 117, 'Lux': 99, 'Malphite': 54, 'Malzahar': 90, 
'Maokai': 57, 'MasterYi': 11, 'MissFortune': 21, 'MonkeyKing': 62, 'Mordekaiser': 82, 'Morgana': 25, 'Nami': 267, 'Nasus': 75, 'Nautilus': 111, 'Neeko': 518, 'Nidalee': 76, 
'Nocturne': 56, 'Nunu': 20, 'Olaf': 2, 'Orianna': 61, 'Ornn': 516, 'Pantheon': 80, 'Poppy': 78, 'Pyke': 555, 'Qiyana': 246, 'Quinn': 133, 'Rakan': 497, 'Rammus': 33, 'RekSai': 421, 
'Renekton': 58, 'Rengar': 107, 'Riven': 92, 'Rumble': 68, 'Ryze': 13, 'Samira': 360, 'Sejuani': 113, 'Senna': 235, 'Seraphine': 147, 'Sett': 875, 'Shaco': 35, 'Shen': 98, 'Shyvana': 102, 
'Singed': 27, 'Sion': 14, 'Sivir': 15, 'Skarner': 72, 'Sona': 37, 'Soraka': 16, 'Swain': 50, 'Sylas': 517, 'Syndra': 134, 'TahmKench': 223, 'Taliyah': 163, 'Talon': 91, 'Taric': 44, 
'Teemo': 17, 'Thresh': 412, 'Tristana': 18, 'Trundle': 48, 'Tryndamere': 23, 'TwistedFate': 4, 'Twitch': 29, 'Udyr': 77, 'Urgot': 6, 'Varus': 110, 'Vayne': 67, 'Veigar': 45, 'Velkoz': 161, 
'Vi': 254, 'Viktor': 112, 'Vladimir': 8, 'Volibear': 106, 'Warwick': 19, 'Xayah': 498, 'Xerath': 101, 'XinZhao': 5, 'Yasuo': 157, 'Yone': 777, 'Yorick': 83, 'Yuumi': 350, 'Zac': 154, 
'Zed': 238, 'Ziggs': 115, 'Zilean': 26, 'Zoe': 142, 'Zyra': 143}
'''
pacChamps = {'Lux': 1282360, 'Thresh': 746700, 'Ahri': 608349, 'Soraka': 582946, 'Yasuo': 558957, 'Ekko': 501921, 'Zed': 411244, 'Udyr': 408503, 'Jhin': 407662, 'Ezreal': 399079, 
'Jinx': 391718, 'Kayn': 388319, 'MasterYi': 387714, 'Diana': 385214, 'Talon': 384375, 'Darius': 360735, 'Pyke': 335555, 'Pantheon': 332690, 'Blitzcrank': 327660, 'Ashe': 323228, 'Kassadin': 302816, 
'Teemo': 298608, 'Sona': 286855, 'Orianna': 275968, 'Leona': 273226, 'Janna': 273018, 'Nautilus': 272870, 'Khazix': 269916, 'Caitlyn': 268147, 'Sett': 260820, 'Garen': 259353, 'Morgana': 253587, 
'Shen': 245710, 'MissFortune': 240500, 'Gnar': 240496, 'Lucian': 235893, 'Jax': 235865, 'Quinn': 232668, 'Kennen': 227579, 'Evelynn': 225887, 'Fizz': 219286, 'Irelia': 217588, 'Mordekaiser': 211914, 
'Nami': 208533, 'Nasus': 206074, 'TahmKench': 204822, 'Kaisa': 204506, 'Vi': 195641, 'Kindred': 194126, 'Azir': 193401, 'Akali': 192801, 'Fiora': 189101, 'LeeSin': 184550, 'Bard': 178484, 'Aatrox': 176903, 
'Malzahar': 174594, 'Twitch': 174271, 'Katarina': 173382, 'Tristana': 172139, 'Swain': 170959, 'Vladimir': 167207, 'Sylas': 162716, 'Rammus': 160848, 'Veigar': 154248, 'TwistedFate': 152361, 'Zoe': 151928, 
'Karthus': 151605, 'Xayah': 149431, 'Brand': 146297, 'Shaco': 143303, 'Jayce': 141556, 'Nunu': 140363, 'Varus': 140185, 'Malphite': 139884, 'Ornn': 136002, 'Alistar': 131127, 'Vayne': 130782, 'Riven': 130242, 
'Gangplank': 130120, 'Volibear': 127848, 'Nocturne': 127414, 'Galio': 127146, 'Kayle': 124949, 'Syndra': 124786, 'Graves': 124162, 'Hecarim': 123231, 'XinZhao': 118728, 'Braum': 116969, 'Camille': 116368, 
'Tryndamere': 110591, 'Annie': 109633, 'Fiddlesticks': 108326, 'Chogath': 107550, 'Poppy': 105945, 'Shyvana': 104088, 'Singed': 103734, 'Draven': 102462, 'Karma': 101772, 'Sion': 101541, 'Maokai': 101413, 
'Velkoz': 98748, 'Rakan': 97976, 'JarvanIV': 97381, 'Trundle': 95090, 'MonkeyKing': 94742, 'Ziggs': 94321, 'Nidalee': 94293, 'Taliyah': 91328, 'Renekton': 91216, 'Xerath': 89335, 'Warwick': 87032, 
'Yuumi': 86235, 'Leblanc': 85508, 'Rengar': 85137, 'Senna': 79225, 'Urgot': 76601, 'Ryze': 75653, 'KogMaw': 74850, 'Zilean': 73109, 'Kled': 72406, 'Aphelios': 72112, 'Lulu': 72008, 'Gragas': 71970, 
'Sivir': 71819, 'Amumu': 71620, 'Skarner': 68904, 'Yone': 67847, 'Olaf': 67098, 'Ivern': 65654, 'AurelionSol': 63553, 'Zac': 62995, 'Rumble': 62982, 'Lissandra': 60109, 'Sejuani': 56568, 'Viktor': 51972, 
'Qiyana': 50317, 'DrMundo': 48651, 'Illaoi': 45644, 'Kalista': 44181, 'Heimerdinger': 41876, 'Anivia': 41585, 'Neeko': 39573, 'Corki': 34774, 'Elise': 33861, 'RekSai': 32435, 'Taric': 30204, 'Zyra': 29292, 
'Seraphine': 28850, 'Lillia': 27353, 'Yorick': 18084, 'Cassiopeia': 17433, 'Samira': 12020}'''