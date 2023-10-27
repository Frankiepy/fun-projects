def one2020():
    nums = [1313,1968,1334,1566,820,1435,1369,1230,1383,1816,1396,1974,1911,1989,1824,1430,1709,1204,1792,1800,1703,2009,1467,1400,1315,1985,1598,1215,1574,1770,1870,1352,1544,1339,188,1347,1986,2003,1538,1839,1688,1350,1191,1961,1578,1946,1548,1975,1745,1631,1390,1811,1586,1409,247,1600,1565,1929,1854,1602,1773,1815,1887,1689,1266,1573,1534,1939,1909,1273,1386,1713,1268,1611,1348,1478,1857,1916,1113,936,1603,1716,1875,1855,1834,1701,1279,1346,1503,1797,1287,1447,1475,1950,1614,1261,1442,1299,1465,896,1481,1804,1931,1849,1675,1726,355,1485,1343,1697,1735,1858,1205,1345,1281,253,1808,1557,1964,1771,1891,1583,1896,1398,1930,1258,1338,1208,1328,1493,1963,1374,1212,1223,1501,2004,1591,1954,115,1972,1814,1643,1270,1349,1297,1399,1969,1237,1228,1379,1779,1765,1427,1464,1247,1967,1577,1719,1559,1274,1879,1504,1732,1277,1758,1721,1936,1605,1358,1505,1411,1823,1576,1682,1439,1901,1940,1760,1414,1193,1900,1990,1781,1801,1239,1729,1360,1780,1848,1468,1484,1280,1278,1851,1903,1894,1731,1451,549,1570]
    count = -1
    count2 = 0 
    count3 = 1
    while count3 <= 198: #there is 198 nums i think
        count += 1
        count2 += 1
        if count == 199 or count2 == 199:
            count = 0
            count3 += 1
            count2 = count3
        if nums[count] + nums[count2] == 2020:
            print(nums[count], 'and', nums[count2])
def oneparttwo2020():
    nums = [1313,1968,1334,1566,820,1435,1369,1230,1383,1816,1396,1974,1911,1989,1824,1430,1709,1204,1792,1800,1703,2009,1467,1400,1315,1985,1598,1215,1574,1770,1870,1352,1544,1339,188,1347,1986,2003,1538,1839,1688,1350,1191,1961,1578,1946,1548,1975,1745,1631,1390,1811,1586,1409,247,1600,1565,1929,1854,1602,1773,1815,1887,1689,1266,1573,1534,1939,1909,1273,1386,1713,1268,1611,1348,1478,1857,1916,1113,936,1603,1716,1875,1855,1834,1701,1279,1346,1503,1797,1287,1447,1475,1950,1614,1261,1442,1299,1465,896,1481,1804,1931,1849,1675,1726,355,1485,1343,1697,1735,1858,1205,1345,1281,253,1808,1557,1964,1771,1891,1583,1896,1398,1930,1258,1338,1208,1328,1493,1963,1374,1212,1223,1501,2004,1591,1954,115,1972,1814,1643,1270,1349,1297,1399,1969,1237,1228,1379,1779,1765,1427,1464,1247,1967,1577,1719,1559,1274,1879,1504,1732,1277,1758,1721,1936,1605,1358,1505,1411,1823,1576,1682,1439,1901,1940,1760,1414,1193,1900,1990,1781,1801,1239,1729,1360,1780,1848,1468,1484,1280,1278,1851,1903,1894,1731,1451,549,1570]
    count = -1
    count2 = 0 
    count3 = 1
    count4 = 1
    count5 = 0
    while count3 <= 199: #there is 198 nums i think
        count += 1
        count2 += 1
        if count == 199 or count2 == 199:
            count = -1
            count3 += 1
            count2 = count3
        if count3 == 198:
            count = -1
            count3 = 0
            count4 += 1
            count5 = count4
        if nums[count] + nums[count2] + nums[count5] == 2020:
            print(nums[count], 'and', nums[count2], 'and', nums[count5])
def two2020():
    passwords = [[4,5, 'm', 'mmpth'],
        [1,7, 'r', 'rszchrrrzgr'],
        [2,5, 'w', 'dgqtwwkwwc'],
        [10,11, 'w', 'ldslpwbbqwpwtd'],
        [3,4, 's', 'sszss'],
        [1,6, 'l', 'llmjxlbt'],
        [8,11, 'c', 'ccctccccccw'],
        [1,11, 'l', 'tllllllplllzjllgz'],
        [5,8, 'j', 'ljjjjjjqcw'],
        [11,12, 's', 'sssssqsslsvhfs'],
        [7,10, 'f', 'fffffmfqfffffff'],
        [3,8, 'm', 'mmmsqmmmh'],
        [3,9, 'w', 'dwzvsttjw'],
        [7,8, 'l', 'llllflhg'],
        [10,13, 'f', 'jfkwhzrtktphc'],
        [5,6, 'p', 'pvldppqvcd'],
        [9,17, 's', 'sssssssstssssssscsss'],
        [4,7, 'k', 'zlwhcwkrckwkskxkgh'],
        [12,14, 'n', 'nnnnnnwncnnjnn'],
        [6,8, 'g', 'gkwzbwhgmgrqqlksswg'],
        [7,8, 'd', 'drpbhdvwddd'],
        [6,8, 'd', 'dlmphvwbnnddrd'],
        [5,6, 'm', 'mmzmmmpm'],
        [6,13, 'x', 'xdcxhkqqxznxwhtxdxt'],
        [4,14, 'c', 'pncwncdcccccdmwccccc'],
        [14,15, 's', 'gsrsssssbsssstkssmb'],
        [1,3, 'm', 'dhmzmlnfmsm'],
        [8,12, 'l', 'llmlrllchlwhlktpxdf'],
        [3,5, 'g', 'njgkglgx'],
        [11,14, 'v', 'vvvvmwvkvtqvgxvvvlvv'],
        [1,4, 'h', 'hhhq'],
        [1,2, 'l', 'dfrmsp'],
        [4,5, 'n', 'nkknnkrflkpnnn'],
        [10,12, 'w', 'dwwwwwwlwwww'],
        [13,14, 'h', 'xnhhhrvwpnkmhx'],
        [11,12, 'l', 'lllllklrllrx'],
        [12,14, 'd', 'ldrvtddrddvdqgj'],
        [10,11, 'p', 'bxpqplqtqzhjv'],
        [2,5, 't', 'bmltz'],
        [8,10, 'j', 'ljjjjjjmjjj'],
        [5,6, 'x', 'xxxvll'],
        [5,7, 'b', 'bxbbbbbk'],
        [5,11, 't', 'ttjmsttwtdh'],
        [2,3, 'p', 'dmxxrpnppd'],
        [1,4, 'x', 'xxxxxgx'],
        [3,6, 'v', 'vwcvvv'],
        [4,5, 'l', 'lqpll'],
        [14,20, 'p', 'psxqnpfpnmpsppppppsp'],
        [16,18, 'g', 'lgggkgggggggggggglg'],
        [3,5, 'b', 'tbfbbg'],
        [6,8, 'n', 'nsnnnnnnnw'],
        [2,4, 'p', 'dppndlmtnt'],
        [11,15, 'q', 'tqqqqqqqqqqqqqq'],
        [13,14, 'r', 'rrrrrrrrrrrrbx'],
        [3,6, 's', 'shsssfc'],
        [7,9, 'l', 'mlghdlhwfbcqmv'],
        [1,2, 'k', 'mlwk'],
        [13,17, 'v', 'hbvlqvknvvsvzvvvvv'],
        [3,4, 'g', 'bmngrgttz'],
        [9,10, 'h', 'hhmhhhhhtc'],
        [1,15, 'm', 'nmmmmmmmmmmmmmmm'],
        [12,13, 'k', 'kkkkkkkkkjnfckk'],
        [1,8, 'k', 'skkkzkkkk'],
        [5,7, 'j', 'jjjjjjhj'],
        [12,14, 'g', 'gmgxwglgggggbggqgg'],
        [9,11, 'p', 'pppxppqpprlgpp'],
        [14,15, 'j', 'cpjjjjjjjjjjjjjj'],
        [4,12, 'l', 'lnblzbdmpwwrbmnr'],
        [3,8, 'd', 'dddhdmcrddnddnddjl'],
        [5,9, 'g', 'kghqfsggf'],
        [18,20, 'g', 'gggggggggggggggggngw'],
        [3,5, 'q', 'rkqlqfzvwqqqksntqdz'],
        [8,16, 'm', 'dkmmzgmdmmmhwmxmxm'],
        [7,9, 'q', 'qnqhtkqqqqqqjvcs'],
        [1,3, 'm', 'mmlm'],
        [1,10, 'b', 'bjfkmblmbbtvxzp'],
        [4,5, 'c', 'ccldccsq'],
        [4,7, 'k', 'dzbkksrkkkbkwd'],
        [1,7, 'r', 'rrrrrrp'],
        [9,10, 'g', 'qgggtgnlszgggs'],
        [6,7, 'g', 'ggsgjfq'],
        [10,11, 'n', 'nnnnnnnngnnn'],
        [3,4, 'c', 'ftchcgcvlgzckdrg'],
        [13,15, 'p', 'pppnppppppppzhpplhp'],
        [2,7, 'k', 'xnlhlxsdzkvhw'],
        [5,8, 'm', 'mmmbmqmnfmtm'],
        [7,8, 'd', 'sdddddcjd'],
        [3,4, 'b', 'fnjr'],
        [8,14, 'c', 'cccccrjcccccccchcfqc'],
        [6,11, 'm', 'mmmmmmmmmmmmmmmmmmmm'],
        [5,7, 'l', 'lllllwhtl'],
        [5,7, 'z', 'zzbzrzg'],
        [6,10, 'n', 'ncnznxzcwvcn'],
        [2,4, 'f', 'xpkffxmlwtgzjppcdf'],
        [19,20, 'c', 'cccccccccccccxcccclf'],
        [4,14, 'w', 'wwlmwwfpwwzjdww'],
        [11,17, 'f', 'fvfffvfffffxffffff'],
        [12,13, 's', 'gtshbpzgxnsss'],
        [5,6, 'm', 'mmsjjgmd'],
        [15,17, 'x', 'xxxxxxxwxxxxxxhxx'],
        [5,9, 'f', 'kgfjmbctt'],
        [6,7, 'k', 'wkknmkk'],
        [2,4, 'c', 'cccc'],
        [5,9, 's', 'grsgskjnsmsg'],
        [3,5, 'q', 'qqqqqps'],
        [9,11, 'f', 'fffbfbfffffjfffcffkg'],
        [7,9, 'q', 'qqqqknqqcmqqqq'],
        [17,18, 'x', 'xxxxxxxxxxxxxxxxxq'],
        [2,10, 'j', 'cmhglhqjdg'],
        [10,11, 'h', 'pnhzhkgxbhkdm'],
        [8,12, 'j', 'qjjjjwjjjlzjbjjdcjj'],
        [15,16, 'q', 'qqqqqqqqqqkckvrq'],
        [6,15, 'f', 'fkfffffffsfcknf'],
        [4,17, 'c', 'vgpsglczjdfcnqtbnl'],
        [10,11, 'k', 'mmxktwkkwbvfkkdkkknj'],
        [11,12, 's', 'ssssssspsssk'],
        [3,5, 'l', 'lcqdh'],
        [2,3, 'm', 'mqqq'],
        [6,7, 'k', 'fkkkjkv'],
        [13,15, 'g', 'gqlgdsgggggxggg'],
        [7,9, 'r', 'jvnkhhrrrvrsfxkrtd'],
        [14,15, 'f', 'ffrffffffffqpkllfxff'],
        [3,4, 'd', 'gjvf'],
        [9,12, 'x', 'hxxxrxqwxxjxxq'],
        [5,7, 'k', 'wdkkkdfttqkdkng'],
        [6,7, 'x', 'xxxvxhx'],
        [6,13, 'c', 'ccsclccccfmcdb'],
        [5,17, 'c', 'cdccsvcccccccccck'],
        [14,15, 's', 'sssssssssksssnx'],
        [6,7, 'j', 'jjjwhqt'],
        [14,15, 's', 'kssssssssssspcss'],
        [3,6, 'w', 'tnmlbhw'],
        [1,4, 'g', 'lqgrtcgn'],
        [1,11, 'b', 'drrwhbwzqdj'],
        [7,8, 'r', 'vrnvdtrr'],
        [4,8, 'w', 'vwwwwwwwww'],
        [6,7, 'v', 'vvvvvvn'],
        [7,14, 't', 'sxtxhdxcwqdgrtqs'],
        [2,7, 'w', 'ptgsdwghvjwmwbgrqqs'],
        [1,2, 'l', 'llllgll'],
        [3,4, 'n', 'npnnbg'],
        [3,5, 'h', 'mxhhhwhf'],
        [10,15, 'j', 'bjjjtnjppjjjzcjjsw'],
        [8,11, 'r', 'srkkhrrcwrbrptr'],
        [2,4, 't', 'qttwv'],
        [8,9, 't', 'tfhtldttt'],
        [5,15, 'r', 'lwdmlgrrrrtrrrpxgrp'],
        [8,9, 'd', 'ddcddddgwd'],
        [3,4, 'b', 'cbbb'],
        [11,12, 'm', 'vmmnxtdxmmnm'],
        [2,5, 'r', 'rwrvc'],
        [1,10, 's', 'sssxsfsssssws'],
        [1,4, 'v', 'kvlxvvv'],
        [5,17, 'h', 'dhqhhhlxhhhhqhhbhhnc'],
        [7,9, 'd', 'bdddpkdnfrnmb'],
        [3,6, 'x', 'qvstbxvkqfnxwnk'],
        [16,18, 'm', 'mlmpnmmstmmlmcmbmh'],
        [8,9, 'h', 'hhhhhhvhhhhhhhx'],
        [7,10, 't', 'tqcttwwttg'],
        [1,9, 'm', 'gmvlmmmqmtpfm'],
        [3,4, 'p', 'ppppp'],
        [7,17, 'd', 'xddgqhdddcptxdhxc'],
        [1,11, 'f', 'ffffffffffff'],
        [13,14, 'r', 'dmsrnztgrrlvgt'],
        [10,11, 'r', 'rrrrrrrrrrvr'],
        [4,5, 'l', 'llllll'],
        [4,9, 'k', 'kkkkbkkkd'],
        [3,5, 'b', 'vsbbbtrnqzbbd'],
        [2,12, 'j', 'sjgjnjmhjgcjjcnjjj'],
        [5,15, 'h', 'lqhvhhtxkhchmhh'],
        [7,14, 'l', 'sllsfllllllllllllll'],
        [12,14, 'v', 'pvvvvvvvvvvvvv'],
        [4,5, 'j', 'jjgjjjg'],
        [11,13, 'q', 'qqqqmqqqqqdqxq'],
        [7,9, 'p', 'ppppppphpnp'],
        [5,6, 's', 'ssrssz'],
        [8,14, 'j', 'jjjjjjjjjjjjjjj'],
        [6,8, 'j', 'jtxjdjmjxjjjrjq'],
        [14,16, 'd', 'ddddddddkdddddjd'],
        [4,6, 'h', 'hhhhwhxh'],
        [5,12, 'h', 'hhphwjhjhhhhhnhhbh'],
        [5,9, 'm', 'mmmjxhpkmmhmttjdmk'],
        [5,9, 'c', 'cxcvgtccttwn'],
        [6,11, 'r', 'bcrrwznbgtrrrr'],
        [3,4, 't', 'fpttlttxjwcqmtbw'],
        [2,4, 'b', 'dmxkbrgpjqtlnq'],
        [2,7, 'r', 'rdrfprqprkgwpxrrw'],
        [10,13, 'c', 'ccckpcsccwccccc'],
        [5,7, 'l', 'vlllllkl'],
        [4,11, 'x', 'xxxjxxxxvxtx'],
        [1,5, 'h', 'hhhhh'],
        [7,12, 's', 'sjssssxnssmsj'],
        [4,5, 'w', 'wthmw'],
        [6,7, 'f', 'fkppffq'],
        [7,8, 'c', 'cgktccccckcccc'],
        [1,2, 'q', 'lhnsqrk'],
        [2,6, 'm', 'dvmmmm'],
        [3,6, 'x', 'dbxxlxkf'],
        [7,14, 'd', 'ddsdjslpkfddxjjjkdt'],
        [14,16, 'c', 'ccqcvctjcccrccgc'],
        [1,3, 'd', 'dddrkddddkmxr'],
        [7,10, 'w', 'gpwgskmxsjv'],
        [4,5, 'v', 'bxhgm'],
        [6,7, 'w', 'whwhfqw'],
        [1,4, 'x', 'sxxxrx'],
        [2,4, 'g', 'ggdggg'],
        [15,16, 'h', 'hhhbhhhhhhhhhhhh'],
        [8,9, 's', 'ssssxsksshss'],
        [4,6, 'w', 'wwwlwqw'],
        [6,8, 'd', 'sdpqddddmddw'],
        [14,15, 'j', 'jjjjjjjnjjjmnjj'],
        [2,9, 'p', 'pvzstcclp'],
        [18,19, 'g', 'fgggggggglpgggggztg'],
        [15,17, 'z', 'zzzznzzzzfzzvztzhzzz'],
        [10,11, 'j', 'pjjkjkjjjgj'],
        [7,12, 'w', 'dwbwwbzwwwbvwmwc'],
        [3,11, 'g', 'vgggwqnwspgg'],
        [8,13, 'w', 'wwwwwwczwnwtww'],
        [1,11, 'm', 'mjdtsvwmcqmvd'],
        [2,3, 'c', 'vcccc'],
        [6,17, 'k', 'wskkkkkkkkgjkzkkkgmk'],
        [8,12, 'g', 'mghgrngjggvjgg'],
        [4,7, 'p', 'pppsppp'],
        [6,9, 'v', 'vvvvvrvvv'],
        [5,14, 'j', 'jjmqlzjbjjjlmjjjjj'],
        [1,13, 'f', 'fkbnffffffffpfff'],
        [3,9, 'r', 'vrfrxtvwh'],
        [2,4, 'k', 'fkskpjkkbh'],
        [15,19, 'd', 'dddddddddddddddddhdd'],
        [1,16, 's', 'swtmgswssfwsxpsssss'],
        [12,13, 's', 'ssssssssssslssss'],
        [1,2, 'q', 'wvzvbb'],
        [9,14, 'd', 'pddddqgcdddjddx'],
        [4,6, 'x', 'vbqpxxbkxmx'],
        [1,5, 'q', 'qzqqqqqwfmtqfq'],
        [7,17, 'l', 'mdlcllllhrlllhpllcl'],
        [9,10, 'q', 'qqqqqstcgcxqqq'],
        [6,11, 'x', 'txtxhxxmxhxxx'],
        [7,8, 'c', 'ccccccppc'],
        [12,13, 'v', 'vmvmvvvvvvvvxvl'],
        [10,12, 'r', 'rrrrrzrrglrrrrkr'],
        [2,4, 's', 'ssbsv'],
        [15,17, 'g', 'ggggggggggggggggf'],
        [2,7, 'g', 'sgvgtgghmtxd'],
        [16,17, 's', 'ssssssssssssssvzsss'],
        [4,6, 'n', 'nnnnqnn'],
        [10,15, 't', 'mvtttvtftqzmtjt'],
        [10,11, 'q', 'qqqqbqqwqrzqqp'],
        [6,14, 'h', 'hjhhhchhhhjhdd'],
        [11,15, 'b', 'zbwhdjksbqbdbmb'],
        [5,12, 'r', 'mrnggrwzrhrrrr'],
        [9,16, 'm', 'jmmmmmmmmqwmmcxmfmm'],
        [7,8, 'h', 'qsmhhhtsbhhhjhwl'],
        [2,3, 'h', 'hkghhm'],
        [1,4, 'k', 'nkkkk'],
        [3,4, 'z', 'zzzz'],
        [11,13, 'j', 'jrjjgbgjxrqjrmjjgckj'],
        [3,7, 'w', 'wwwqqlwdb'],
        [6,9, 'b', 'fsbbbqbbqmbb'],
        [13,16, 'n', 'nnnnnnnnnnnnnnnn'],
        [5,7, 'b', 'cbbqmbbrhbbz'],
        [2,3, 'l', 'xjzkbwgfwwcwll'],
        [13,14, 'z', 'zzzzzzzzzzzzzzzz'],
        [6,7, 'c', 'ccccccc'],
        [4,10, 'l', 'lhlslmlwmwbllv'],
        [4,5, 'h', 'rqhhhhh'],
        [3,4, 't', 'dmtttmxhtqz'],
        [6,17, 'n', 'nnxcnncnnvgcnnrnrmn'],
        [3,4, 'x', 'xxmxxx'],
        [8,10, 'j', 'jjjjjjtjtvjj'],
        [5,11, 'd', 'ldldbnndddddsgdpgj'],
        [1,8, 'n', 'nsjvhncn'],
        [3,8, 'f', 'fffffssffxfffhl'],
        [1,3, 'q', 'kwnq'],
        [3,5, 'k', 'krkcklkhkspqmqm'],
        [3,4, 'k', 'dklm'],
        [11,14, 'j', 'jjjjjjjjjjjjjjj'],
        [16,17, 'v', 'vvvvvvfvvvvvvvvmx'],
        [5,6, 'm', 'mmmmmm'],
        [10,11, 'l', 'wdlgllqlslf'],
        [5,6, 't', 'prbwttmtpvwr'],
        [6,20, 'c', 'cwcctqccthccrpccccct'],
        [5,12, 's', 'sssssbssssszs'],
        [10,11, 'k', 'mkkjklhkktkkkdvkqqkm'],
        [11,12, 'n', 'nnnnrnnsngnn'],
        [2,5, 'p', 'ppppl'],
        [7,11, 'f', 'mvmdfmdwfffffwfrjfqk'],
        [13,16, 'r', 'rzsrdsrrrrrrprpjrb'],
        [13,14, 'c', 'ccccccdccccctc'],
        [13,18, 'n', 'nnnnnnnnnnnncnnnnnn'],
        [4,10, 'r', 'rvrrdhflcrtwzz'],
        [2,9, 'p', 'prpczpbpt'],
        [3,8, 'q', 'qqqqcksqqtx'],
        [4,5, 'd', 'xxdpmdbvddn'],
        [3,4, 'j', 'jjlj'],
        [2,3, 'n', 'nrnnnsnn'],
        [3,4, 'w', 'pnwkwdn'],
        [1,5, 'w', 'wlwgw'],
        [10,14, 'x', 'xxxxxxxxxxxxxxx'],
        [5,15, 'k', 'kkkkfskkhkkkqpf'],
        [3,4, 'b', 'bbbbf'],
        [3,4, 'r', 'jrrr'],
        [3,6, 'h', 'htkhhhhh'],
        [15,16, 'g', 'gggggggggggggvgt'],
        [17,18, 's', 'ssssssssssgssssssz'],
        [14,15, 'm', 'pkngmmpjmxmmmms'],
        [4,10, 'f', 'rsmxvsghdlfff'],
        [16,17, 'z', 'zvzhzzczdvzkzzghg'],
        [16,18, 'v', 'vvvvvvvvvvvvvjvvvv'],
        [6,9, 't', 'tttttmttttt'],
        [5,6, 'j', 'hjwxgbjf'],
        [3,6, 'k', 'kkkkkh'],
        [9,13, 'd', 'ddpgdfddddddd'],
        [14,15, 'x', 'xxxxxxxxxxxxxxx'],
        [1,4, 'v', 'vqvqkrjx'],
        [4,5, 'h', 'hjhhnh'],
        [2,3, 'v', 'jvvsrgsvfqlv'],
        [9,10, 'm', 'mmmmmmmmmm'],
        [2,5, 'f', 'ffnfpff'],
        [4,6, 'b', 'bbbbbg'],
        [8,9, 'p', 'ppjwqpjbnpppwp'],
        [5,6, 'l', 'lldlllll'],
        [9,10, 'g', 'gvgqggtgggggg'],
        [6,9, 'x', 'jxxxxxwxqqvxx'],
        [1,4, 'w', 'lwwgbt'],
        [16,17, 'd', 'jcdmgkmfvvlqphbddvhc'],
        [1,12, 's', 'sssslssssssnsss'],
        [4,5, 'p', 'cjnppjllxbrp'],
        [13,14, 'n', 'jmzjhttnkkgnnn'],
        [11,12, 't', 'vrgtrgjrdmtcfzx'],
        [16,17, 'l', 'lllllnmlvldlllrwmlc'],
        [13,16, 'm', 'mbdmmmmmmhmsmmmmtb'],
        [3,6, 'z', 'zszzzzz'],
        [1,6, 'h', 'hhhqhrbh'],
        [3,5, 'n', 'rlnnnn'],
        [17,19, 'x', 'xxxcxxxvxxxxxxxxxxkx'],
        [3,10, 'r', 'rccrrrhrrx'],
        [4,7, 'h', 'hhhdhhh'],
        [3,6, 'g', 'hgfzpmpgg'],
        [1,2, 'x', 'xxqhhx'],
        [5,6, 'm', 'jmmmmzf'],
        [1,2, 'j', 'bjjj'],
        [2,3, 'q', 'gqst'],
        [3,4, 'g', 'ggggmbghk'],
        [3,4, 'f', 'fnfdf'],
        [5,6, 'q', 'qpqtdg'],
        [2,3, 't', 'ptctz'],
        [5,6, 'd', 'pddvdddsd'],
        [1,4, 'f', 'ffftff'],
        [3,5, 'b', 'bbdbg'],
        [13,17, 'f', 'fgfckcdfffftffxfffff'],
        [3,4, 'w', 'wwkxsw'],
        [2,12, 'l', 'hvgqmbqlrnzls'],
        [1,2, 'f', 'szff'],
        [6,7, 'q', 'sqqqqnqq'],
        [1,4, 'p', 'ppvd'],
        [3,7, 'c', 'cwscbkgc'],
        [4,12, 's', 'sssfsssspsfsgss'],
        [4,10, 't', 'jstttgststtghzp'],
        [5,6, 'j', 'jjjjtj'],
        [5,9, 'k', 'ffkdktkkhbbwkkj'],
        [9,15, 'k', 'kkkkkzkkkcbkkkkkkkkk'],
        [3,17, 'w', 'wwgwnnkswwpqwkwdhw'],
        [15,20, 'l', 'wlllllslllllrllllllk'],
        [4,5, 'r', 'rrrfm'],
        [2,6, 'l', 'flllnll'],
        [12,13, 's', 'ssssssssssscwn'],
        [9,10, 'r', 'zpqrrrrrfn'],
        [10,13, 'h', 'xhhfhzchhjhhtdrhhzh'],
        [6,7, 'b', 'bbbbnrbb'],
        [2,12, 'f', 'tffjcjtlnvgf'],
        [2,4, 'g', 'gtgkg'],
        [11,14, 'n', 'nnnnnnbrnnnpnnn'],
        [15,17, 'j', 'jjjjjjjjjjjdjjvjv'],
        [10,13, 'r', 'brgrrrfrmfrrxrgrrrs'],
        [3,13, 'v', 'vwvjsftzkvcxvdbxfs'],
        [17,19, 'f', 'fffffffffmffffffffff'],
        [1,4, 'g', 'vggxg'],
        [5,16, 'm', 'csckdfxglfpzmrhcmbnn'],
        [4,15, 'z', 'gzqjzczzzzjzzhjbz'],
        [13,14, 'w', 'wwwlwwwwwwwwht'],
        [11,13, 'j', 'cjjdjjjjsjjjkjjjh'],
        [4,15, 'w', 'wwwqwwzwwmwwtww'],
        [1,2, 'p', 'ppjcp'],
        [6,10, 'f', 'ffjffrfffsgm'],
        [17,19, 'q', 'qqqqqqqqqqqqqqqqqqqq'],
        [3,4, 'g', 'gmgz'],
        [10,14, 's', 'fpsssdmssdsgsgvss'],
        [9,10, 'm', 'mmmmmmmmmmmm'],
        [1,5, 'c', 'fcgns'],
        [5,9, 't', 'ttcgtttrtttttq'],
        [4,5, 'v', 'vvrvvv'],
        [2,4, 'w', 'xwpw'],
        [5,12, 'd', 'trdhrqlqwrlsrdfh'],
        [3,8, 'n', 'bbnnnzrnnjdnb'],
        [8,10, 'w', 'wwwrwdwjgz'],
        [5,6, 'd', 'ddddjr'],
        [1,3, 'p', 'ppqppp'],
        [10,19, 'f', 'dfbjgffmpvnkhfwjfff'],
        [3,6, 'k', 'kkkkkkkp'],
        [5,7, 't', 'vqtxtxtvk'],
        [14,15, 'c', 'cccclccccccctcctwc'],
        [2,13, 'x', 'tmxxzxklxgzxxp'],
        [16,17, 'b', 'bbbrbbbbbbbbbbbbbb'],
        [6,11, 'h', 'gmzhhhhmrhqhhm'],
        [7,9, 'k', 'kkkkkkqkck'],
        [4,7, 'v', 'pgvdvvx'],
        [12,19, 'f', 'fffffffffffxffffffff'],
        [2,5, 'p', 'mphtpp'],
        [6,13, 't', 'ctttvwtntqttttq'],
        [3,11, 't', 'xntrzxtlnwt'],
        [17,18, 'l', 'llllllllllllllllll'],
        [2,5, 'c', 'zczpcfdzblnkcvj'],
        [1,5, 'z', 'fzzzmz'],
        [6,11, 'f', 'tdcffpffwqlfffg'],
        [16,17, 'h', 'hhhhchhhhshhhhhdhh'],
        [13,14, 'm', 'msmmmkmmmjmmmmzmmnm'],
        [6,13, 's', 'nhbscsgcssxsrsssx'],
        [5,17, 'q', 'qqvqqqhqrkqqqqgqqq'],
        [2,4, 't', 'vqtbt'],
        [2,5, 't', 'wfdrsrt'],
        [6,7, 'f', 'ffffzdx'],
        [3,13, 'r', 'pmrtkvdcrxrnrzw'],
        [14,18, 'r', 'wrrqrrcrrlrjmrrkrt'],
        [15,17, 'j', 'jjjjjjjcjjjjjjxjt'],
        [8,9, 'h', 'zmhhlmhhhdhhhhg'],
        [6,15, 'l', 'lllllnlfllllllll'],
        [3,5, 'n', 'nnfnb'],
        [16,17, 's', 'sssssssslssssssss'],
        [8,9, 'k', 'kdkjkkkskkk'],
        [2,5, 'z', 'gzzmzhdplnwwvlsjnzv'],
        [4,15, 'r', 'rvmrbsrtrfdqrrb'],
        [6,7, 'l', 'llllllc'],
        [4,7, 'g', 'dnggxhgggg'],
        [8,9, 'f', 'fftffkdff'],
        [6,9, 'r', 'rrrvrprbrz'],
        [2,6, 'q', 'qwqqqqq'],
        [7,9, 'h', 'mzhpwnkhh'],
        [3,4, 'm', 'mmlh'],
        [1,15, 'v', 'vjpkvdzvzdlklpn'],
        [1,3, 'r', 'rrggvr'],
        [8,13, 'd', 'dwrpdsdjhlddqddhdwdp'],
        [3,4, 'r', 'fvrrsprrmrrrjgr'],
        [4,5, 's', 'zsrssvss'],
        [6,7, 'd', 'dfdwtcvgvcdfdqdwd'],
        [6,12, 'n', 'rhnjnndnfnwql'],
        [3,5, 'l', 'hvlxlcnclqllrw'],
        [10,14, 'l', 'llllllllljlllplll'],
        [6,10, 'b', 'bbbbbbbbbbbbbbbbb'],
        [8,11, 'q', 'qqqqqqqtqqqq'],
        [7,8, 'r', 'rrrrrrxf'],
        [1,4, 'k', 'jkkkzsmbtng'],
        [13,17, 'r', 'rrrrrrlrprrdrrrrl'],
        [1,7, 't', 'dfgnvtl'],
        [2,6, 'v', 'qvvdsm'],
        [8,9, 'l', 'lltlrlljb'],
        [3,4, 'm', 'mdmm'],
        [17,18, 't', 'ttttttttttttjtxttwtt'],
        [9,11, 'b', 'bbbbbbbbbbpb'],
        [2,3, 'b', 'bwnbr'],
        [4,10, 't', 'tfdtltstdft'],
        [8,10, 'z', 'zzfzzzztzzz'],
        [6,8, 'q', 'qqqqqqqmqnqqq'],
        [7,11, 'r', 'rzrrrrzrrrr'],
        [11,13, 'k', 'kkkklklbkmklk'],
        [17,18, 'l', 'slllllblllllllllclll'],
        [10,14, 's', 'ssssssssswssssssss'],
        [3,4, 's', 'hwssssgjsp'],
        [7,10, 'g', 'fbggxgtbngg'],
        [6,7, 'z', 'tzzzhzjz'],
        [3,7, 'g', 'ggggggcrg'],
        [16,20, 'g', 'grgghjcnlmkszxrgtgvv'],
        [1,16, 'n', 'prqnwnngbgtjsvsj'],
        [13,14, 'z', 'zszlgqdgtqbzzlpkzz'],
        [4,8, 'f', 'ffftffnnfp'],
        [15,18, 's', 'jrdgssszdxkzhlsfzs'],
        [7,8, 'l', 'llllllbplllllll'],
        [7,10, 'l', 'llllbllllll'],
        [5,9, 'b', 'bbbbwbbblb'],
        [4,5, 'g', 'gdwhdg'],
        [2,3, 'v', 'jnfvvv'],
        [11,13, 'h', 'hhhhhxhhhmzhbj'],
        [11,13, 'r', 'wbrrrrxgwlvwd'],
        [10,12, 'm', 'gxmpmmmgmmmmm'],
        [11,12, 'h', 'hhhhzhhhhjhnhhh'],
        [2,13, 'g', 'kzkztgnlbqhlgx'],
        [4,7, 'z', 'zktzzzzx'],
        [1,7, 'q', 'pqrxqqhfpglwqts'],
        [6,7, 'f', 'pffvfbtf'],
        [6,7, 'l', 'tlljjlllnll'],
        [4,17, 'f', 'flffpffffdfqffscff'],
        [2,4, 'q', 'bqxqrqrrq'],
        [6,8, 'l', 'lllnllfll'],
        [9,12, 'r', 'xrgrrjrrrkgrrqrnr'],
        [14,19, 'r', 'rrrrrrrrrrrrrrrrrrrr'],
        [18,19, 'w', 'lbqrkdwwwqgrklcwxwwh'],
        [9,10, 'n', 'nnnnnnnnnn'],
        [7,13, 'b', 'bbbbbbbbbbbbb'],
        [5,7, 'k', 'hkbfskqkjktwkk'],
        [9,10, 'c', 'tlvmtfcpccwwz'],
        [3,7, 'r', 'rzzrspmp'],
        [7,11, 'g', 'gghzgglgggt'],
        [4,5, 'p', 'pbpwp'],
        [3,6, 'q', 'qqrqqv'],
        [3,13, 'm', 'mmmwxmmlmnvmmmmmm'],
        [2,6, 'p', 'ppplqpfpp'],
        [11,15, 't', 'ttttttctttltctgt'],
        [2,7, 'm', 'cmnhjqm'],
        [1,6, 'm', 'mzjmtmmmmmdw'],
        [1,10, 'j', 'jzgjcjjjjspjjjjjgjmj'],
        [4,7, 'r', 'vmxtrrnrxnnq'],
        [8,16, 'h', 'hhhhhqhfhhhhhhhhhh'],
        [4,10, 'z', 'kcmkzmzpzts'],
        [14,15, 'j', 'jjjjjjjjjzjjjjj'],
        [6,11, 'x', 'xxkmxxcxxvx'],
        [15,16, 'v', 'vvvvvvvvvvvvvvgt'],
        [6,7, 'w', 'wwwwwgqz'],
        [5,7, 'd', 'dkdpmcddjdd'],
        [6,12, 's', 'sssssssssssvs'],
        [8,10, 'q', 'fcpwtgqqqz'],
        [4,5, 'w', 'wwwwgwww'],
        [8,11, 'q', 'qqqqqqqnqqbqqr'],
        [3,4, 'd', 'dddwddd'],
        [9,12, 'x', 'qxcgxxxxvdxdkzxxxxx'],
        [3,8, 'k', 'kqcsjxszvscfvm'],
        [4,7, 'd', 'mgdddddhkdqb'],
        [3,7, 'x', 'xjxxljlsfrfnhsxxlv'],
        [4,9, 'g', 'xgsxgtgggxmgg'],
        [1,4, 'p', 'tppknptkp'],
        [3,7, 'z', 'gzzbzzz'],
        [1,5, 'p', 'ppgpz'],
        [15,16, 'f', 'fzfffffffffffffwff'],
        [5,11, 't', 'tzttvqltfxtg'],
        [6,7, 'v', 'vhqvzpvv'],
        [2,6, 'f', 'fmffftfff'],
        [9,13, 'd', 'dxrdgddddrddddqpgdd'],
        [7,8, 'r', 'rrrrrnlnrr'],
        [5,6, 't', 'btttwm'],
        [13,14, 'g', 'gggggggggghgblgg'],
        [12,19, 'r', 'qkgrvfnsrwzrqsrhrrs'],
        [15,17, 'j', 'jjjjjjjjjjnjjjhjd'],
        [4,9, 't', 'btmrbcgttjht'],
        [16,17, 'n', 'nnnnnnnnvnnnnnnznn'],
        [3,7, 'l', 'lltlllglll'],
        [12,14, 'v', 'vvvvvvvvvvvvvv'],
        [1,3, 'q', 'qqqq'],
        [12,14, 'f', 'flbfphvwfdffjf'],
        [10,11, 'z', 'lszzzzzzzzzzz'],
        [3,9, 'k', 'lvzkkhkkp'],
        [4,6, 'j', 'fmrjccsjrzjqkfvn'],
        [5,11, 'x', 'xxxxvmxxxxcxx'],
        [1,9, 'c', 'wcccccccjxcvccccc'],
        [1,4, 'l', 'sblllll'],
        [1,2, 'x', 'xnvlnxs'],
        [4,5, 'f', 'nffccfff'],
        [8,9, 'p', 'vpppppprz'],
        [1,6, 'd', 'vfcqmddw'],
        [6,7, 'b', 'bbbbbbb'],
        [7,13, 'n', 'nnnnnnnnnnnnwg'],
        [3,6, 'q', 'zqqqqqqqqqpqqqq'],
        [1,9, 'g', 'gbggggdgglgmg'],
        [9,13, 'b', 'wbbbxnbbqbbbbkbb'],
        [4,5, 'g', 'gggwr'],
        [3,9, 'r', 'vnqvvhprzmbhrcb'],
        [10,11, 'm', 'mmmmmmmmmpm'],
        [4,7, 'c', 'cgrbccdbcz'],
        [5,8, 'r', 'rbvrrrrr'],
        [7,11, 'd', 'ddddjdmddfhvdn'],
        [1,2, 'k', 'zjkk'],
        [2,11, 'w', 'wtwwwwwwwwsw'],
        [7,8, 'b', 'bkbbbbfbbxd'],
        [2,4, 'w', 'wwnjswwmgbwrwwm'],
        [9,18, 'j', 'jjjjjjjjkjjjjjjjjs'],
        [6,7, 't', 'tttttvwtttt'],
        [10,11, 'v', 'wvvvbvvvvvvvm'],
        [17,20, 'd', 'ddddddddddddhddddddn'],
        [2,12, 'q', 'qdqqqqqqqqqxqqqqqq'],
        [5,7, 'w', 'rjdswwwwwwqmmpww'],
        [1,9, 'b', 'bbbbbbbbxcbbbb'],
        [4,5, 'q', 'qqqwxp'],
        [10,15, 'n', 'nnmnnnnnncnnnnvn'],
        [10,17, 'f', 'fnfffffffffffffcff'],
        [2,3, 'p', 'krpx'],
        [8,10, 'c', 'cvsccclwccrcjjclc'],
        [5,9, 't', 'fpnhtmtqtvwcss'],
        [10,13, 'r', 'rrxrrrrrrfrrrr'],
        [6,9, 'l', 'lllllwllt'],
        [11,15, 'n', 'dnnnnnnhsxgnnhsn'],
        [14,16, 'b', 'bbbbbbcbbbnbwkbsbm'],
        [3,8, 'g', 'qhlxgggqvg'],
        [11,14, 'x', 'ptqcgxnnhpxbgxlm'],
        [17,19, 'g', 'gggggggcgggbggggngg'],
        [10,19, 'q', 'qtjrqqwjvqqqknqbqqq'],
        [10,13, 'j', 'jjjjjjnjjljjsj'],
        [1,3, 'g', 'mggg'],
        [3,7, 'w', 'pwtwjdq'],
        [1,2, 'j', 'jjjp'],
        [9,13, 'z', 'pszzzglzhzzzzhz'],
        [1,2, 'j', 'fhhjxz'],
        [9,12, 'l', 'llllllllsltll'],
        [7,9, 'c', 'cxdvzcclccz'],
        [13,15, 'g', 'ggggggggfggggkgg'],
        [15,16, 'z', 'zjjbgzlxqzzsxzdxz'],
        [2,3, 'z', 'kxcszzzsrsccg'],
        [7,9, 't', 'sttwxgtwlbzbsffttjb'],
        [1,6, 'r', 'rnmrrrtrrl'],
        [4,7, 'm', 'pmmtmmq'],
        [5,7, 'f', 'lggcpdpf'],
        [16,19, 'j', 'jxjjxjfssrvlmjjfjjmq'],
        [2,8, 'w', 'wrwswcwvw'],
        [4,15, 'k', 'kkkpkkkkkkkkkkq'],
        [12,15, 's', 'xbssnshpsssgsbk'],
        [7,15, 'z', 'vzrzzczbhzzzzzzzhz'],
        [10,14, 'w', 'wwwwwwwwwtwwwwwwp'],
        [11,12, 'k', 'kkkkkkkkkkkkkckkkkq'],
        [15,16, 's', 'sfssvsssssssmspl'],
        [4,5, 'd', 'dddqd'],
        [5,7, 'h', 'phsblhnfhchb'],
        [8,11, 'x', 'rxxxbhxxxjxxxtgsc'],
        [11,13, 'x', 'xxxxxxqxxxnxvx'],
        [5,10, 'p', 'jbpzfmphpwpz'],
        [9,13, 'v', 'vvvvshvvgvsfqvvvv'],
        [4,7, 'r', 'rrzwrzdr'],
        [11,13, 'f', 'fffffxffffzfwf'],
        [13,14, 's', 'ssssssssssssss'],
        [2,11, 'c', 'czccdmkhhcvcc'],
        [7,11, 'w', 'wwsxwwwwwwwwj'],
        [7,9, 't', 'ttknmtxvttttnt'],
        [1,6, 'r', 'rrpjrrrr'],
        [5,9, 'v', 'vkvvjqvvbvtlv'],
        [1,5, 'q', 'mwvhpqqqcj'],
        [1,5, 'f', 'fffff'],
        [4,5, 'r', 'trrcv'],
        [10,12, 's', 'sssssssssssvss'],
        [4,5, 'd', 'drddzd'],
        [4,5, 'n', 'nnknl'],
        [10,12, 'x', 'xxxxfxxrzbxzvtxlxt'],
        [4,10, 'v', 'sbgsvssbnhmh'],
        [3,11, 'n', 'dnngqwnnjtnjjg'],
        [1,2, 'w', 'xdsvzdmzswwwwwwmgjw'],
        [6,8, 'h', 'whhhhmhbhh'],
        [2,18, 'w', 'wswwwwwwwwwwwwwwwwww'],
        [11,12, 'v', 'vvvvvvvvvvvv'],
        [7,10, 'v', 'vrhvvcvvvvvv'],
        [4,9, 'r', 'rrrrmzntrsgrrkhhr'],
        [4,5, 'v', 'vvvtvc'],
        [3,10, 't', 'ttnttwzgptr'],
        [2,3, 'c', 'gccrngp'],
        [2,3, 'b', 'bbbqx'],
        [1,7, 's', 'zsdlsjs'],
        [5,7, 'j', 'jjjjjjj'],
        [2,5, 'g', 'ggnhg'],
        [2,6, 'w', 'fwwkwhjqbwqw'],
        [1,6, 'w', 'wdgnjwqwqv'],
        [9,11, 'b', 'bbtksbbdxbpjbbbbb'],
        [12,15, 'k', 'kkkkkkkkkkkkkkk'],
        [1,6, 'b', 'bbbrbbb'],
        [6,7, 'g', 'gggggvs'],
        [8,14, 's', 'sssnwssrsssslcs'],
        [1,6, 'q', 'ngjprqqmdwgkjqvq'],
        [11,12, 'z', 'vzzkzzgzzzzzzz'],
        [3,4, 'n', 'nnnnnnnn'],
        [5,6, 'b', 'fbwbljf'],
        [11,18, 'h', 'hhhhhhhhhhshhhhhhlh'],
        [2,15, 'r', 'rrzgrzwrblrfwfrsd'],
        [6,11, 'n', 'zncnknknbgn'],
        [13,14, 'f', 'vwffftfffpffzfff'],
        [5,6, 'c', 'fcccbc'],
        [5,6, 'b', 'bxjbcpsbrgbgn'],
        [2,7, 'f', 'tffhrsf'],
        [7,12, 'g', 'ggggggtgggggg'],
        [4,5, 't', 'ktphttltctt'],
        [4,6, 'w', 'fwsgwh'],
        [7,8, 'm', 'mfmmmmmmm'],
        [4,5, 'z', 'gzjzzfjzzz'],
        [8,9, 'l', 'lvtllllllll'],
        [3,5, 'm', 'rsmmd'],
        [10,11, 'r', 'rrrrrrrrrlz'],
        [11,13, 'j', 'hhqtkwznghbfsbwpvrj'],
        [4,5, 'z', 'zjzndzrmqzlptg'],
        [13,16, 'm', 'mmhmmmmmmmmmpmrmmm'],
        [5,7, 'p', 'pppphpp'],
        [2,3, 's', 'zscgsj'],
        [14,15, 'h', 'hhhhhhhhhhhhhlhh'],
        [2,3, 'f', 'rffrtlxwfff'],
        [1,3, 'z', 'ptqlzzxskrjsnp'],
        [3,4, 't', 'ftttst'],
        [8,9, 't', 'thtttttpttm'],
        [11,13, 'g', 'qzhmgptdfwggqqc'],
        [6,9, 'f', 'nfffhfkffhf'],
        [2,3, 'w', 'qsxgww'],
        [11,12, 'd', 'ddddddddddddd'],
        [2,4, 'v', 'qsbvvv'],
        [8,13, 'z', 'zxczszkwxzgkz'],
        [2,4, 't', 'cbtt'],
        [2,5, 'q', 'clndcnv'],
        [8,12, 'f', 'kfnhqbfnnpntfsvxcx'],
        [2,3, 'd', 'gddtd'],
        [1,9, 'z', 'tztzzzdnm'],
        [3,7, 'h', 'hhhhhhhhh'],
        [5,6, 't', 'tttttvtttt'],
        [5,9, 'g', 'npzggdhvggpqgxwgvgsg'],
        [3,12, 'p', 'kwpptpplxrcgfxphpqbg'],
        [15,18, 'f', 'fffjffffffffffwffff'],
        [7,17, 'n', 'nnnnnnnnnnnnnnnnnnnn'],
        [5,10, 'd', 'dndddkddddx'],
        [1,7, 'v', 'cvhvsvhvv'],
        [5,7, 'f', 'fscrtxlz'],
        [1,14, 'b', 'bbbbbbbbbbbbbbb'],
        [1,11, 'n', 'nnlnxntnlxnnnktnnxb'],
        [13,18, 'p', 'pppzppppfqhppppzrp'],
        [7,8, 'h', 'hhhhzhhmqhh'],
        [16,17, 'r', 'rrrrwrrrrrrrrxrrrr'],
        [4,8, 'f', 'wfffgnff'],
        [15,16, 'j', 'jswvgtfhtffjgjjsxsdq'],
        [16,17, 'n', 'nnnsnnnnnnnnnnnnnnn'],
        [7,8, 'w', 'dxhcjvwwzwdddhhwwlj'],
        [1,13, 'h', 'ppshfshghphcq'],
        [5,15, 'b', 'cbxnbhbbjbhbbmbkvz'],
        [2,11, 'c', 'tdgcqlcccccthwmk'],
        [1,4, 'p', 'mpppp'],
        [1,4, 'x', 'xpzxxkzlrsgrbxpklcz'],
        [2,11, 'f', 'qffffgfffcgn'],
        [14,19, 'h', 'hhhhhhhhhhhhhsbkhhqh'],
        [9,12, 'h', 'hclhhhpsvhhfhh'],
        [2,6, 's', 'lqcppxlsfv'],
        [6,9, 'v', 'vvvvvnvvv'],
        [9,10, 'q', 'xqqqqqqqqqq'],
        [3,8, 'm', 'qmmcjmvmckrmm'],
        [4,9, 'h', 'hhhdhfhhs'],
        [1,14, 'r', 'vpsprlstjkrmmrpzqsz'],
        [6,7, 'g', 'ggggrlqg'],
        [7,10, 't', 'dtkttptttttt'],
        [3,4, 'n', 'vkkf'],
        [9,11, 'g', 'gflgwgggrgmmggg'],
        [3,19, 'l', 'blblmlrlllhbllwllll'],
        [12,13, 'x', 'gvxsxkrvdqbxx'],
        [11,12, 'b', 'bbbbdpdbbwls'],
        [2,13, 'n', 'nnnnnnnnsnnnrnnnnn'],
        [6,13, 'n', 'mfnnnnnkxnnnn'],
        [5,6, 'f', 'kxxfqnf'],
        [4,5, 'x', 'xxxxl'],
        [6,13, 'f', 'nsnxwrftkcgzffv'],
        [6,7, 'w', 'wwpwwxl'],
        [5,7, 'm', 'brvmmnw'],
        [1,4, 'r', 'rkbhnmdt'],
        [9,10, 'b', 'knbzbbfnfbbblrqbrbnj'],
        [2,5, 'v', 'vvvxvvxbw'],
        [3,5, 'q', 'qcsjq'],
        [7,15, 'c', 'gcdpccrcddccwccf'],
        [13,14, 'h', 'hhhhhhhhhhhhhh'],
        [10,11, 'l', 'rllllllllllpcs'],
        [10,11, 'w', 'wwwwwwwwwfw'],
        [2,7, 'f', 'fxtfffn'],
        [3,5, 'x', 'xxxkx'],
        [3,6, 'c', 'ccrrwbsj'],
        [1,4, 'g', 'gggggpgqgg'],
        [1,2, 't', 'vztj'],
        [4,11, 'c', 'zccccccccqcc'],
        [5,11, 'p', 'hbpzppdlppp'],
        [3,5, 'h', 'frhhhzhprz'],
        [4,7, 'd', 'mzdnddd'],
        [15,16, 't', 'gttttttttqttntttc'],
        [1,8, 'c', 'ccqcjbhpccczvfck'],
        [2,3, 'b', 'lztcb'],
        [4,5, 'd', 'ddddd'],
        [2,8, 'j', 'pwfjfdjjjjzkjcjrlwr'],
        [10,11, 'm', 'qmmmmmjnmpmmmmxn'],
        [10,17, 'f', 'ppbfdsjvpfhzccbwfr'],
        [4,8, 'c', 'cfnhqtcmcws'],
        [4,6, 'b', 'bbqxpfzqfvkpbhcbdfn'],
        [4,5, 'k', 'kkkkx'],
        [4,8, 'f', 'vpwfkfff'],
        [1,3, 't', 'ttxtvtthttg'],
        [3,4, 'j', 'fjjj'],
        [18,19, 'v', 'vvvvvvvvvvvvvgvvvxp'],
        [11,14, 'q', 'qqqqqqqqqqqqqq'],
        [2,3, 'p', 'ppplxprwvjmf'],
        [7,14, 'q', 'qpqxzqqqqqqgqmgqqgq'],
        [3,7, 'x', 'dqlxtkx'],
        [6,7, 'f', 'sfczgfffzfhffjkkf'],
        [1,4, 'x', 'xxxxfwxxxpmxd'],
        [4,5, 'b', 'jbbbbb'],
        [10,11, 'p', 'vrpvpppppppdppp'],
        [18,19, 'l', 'llllllllllllllllllll'],
        [4,10, 'v', 'jjzvnsfbbvqcdfq'],
        [16,18, 'd', 'ddddddddddddddddddd'],
        [13,14, 't', 'ftttdtkrdtktttlttkd'],
        [3,17, 'd', 'ddkddfldddddddddr'],
        [10,20, 'v', 'hfzhttvvnkxqvvhlvvvq'],
        [5,6, 't', 'tbwtszgwpntthtvttrsj'],
        [5,6, 's', 'ssshsstds'],
        [2,4, 'h', 'hhhb'],
        [6,7, 'b', 'bbsbfbb'],
        [2,12, 'n', 'znvqnslfhnwnqr'],
        [16,17, 'g', 'gggkggggggggggggl'],
        [4,12, 'j', 'vjqdjjjtsjdjv'],
        [14,16, 'j', 'jjjdjljjjjjjjjjjjp'],
        [4,14, 'd', 'dddddtqdddddddd'],
        [3,4, 'm', 'mpmm'],
        [7,8, 'c', 'ccccccdc'],
        [3,8, 'l', 'clllhnlllrzzgll'],
        [9,10, 'c', 'ccccccccbx'],
        [3,4, 'k', 'kkkj'],
        [5,12, 'r', 'rrrtjxhxzbrrf'],
        [4,6, 'w', 'wwwkwhww'],
        [7,9, 'm', 'fqrmrmmmmgmmmtmb'],
        [3,11, 'w', 'kwwnwwwghhgw'],
        [9,11, 'k', 'kkkkkkpkkkktvkkk'],
        [5,9, 'w', 'hwqjflkkwdqmwmcw'],
        [12,16, 'h', 'hmhmhhhkxhghhhhhhhhh'],
        [1,4, 'z', 'zjzlhjpft'],
        [1,6, 'd', 'dddqdd'],
        [1,9, 's', 'ssssssssss'],
        [2,4, 'd', 'wddf'],
        [7,9, 'k', 'nhzkkmkxkhkphkdkkd'],
        [12,15, 'm', 'khmmmmmmhgmmmmmmm'],
        [3,9, 'n', 'jnknnnnnn'],
        [6,8, 'g', 'ntgggfggmlrgcggf'],
        [12,15, 'g', 'gggghggggmgmggdgg'],
        [7,13, 'x', 'rxxxxxrxxxxxnqxwsxx'],
        [3,5, 'n', 'bnnbnnvdwnls'],
        [3,5, 'v', 'mvbnzk'],
        [2,8, 'n', 'npntnnnjnxknb'],
        [6,11, 't', 'ttftttlqtttt'],
        [5,7, 'g', 'ggggmgp'],
        [5,7, 'x', 'xxbjcxw'],
        [1,8, 'd', 'ddddldddddddwdddd'],
        [2,4, 's', 'csswjbfnjnm'],
        [3,4, 'm', 'mmmr'],
        [16,17, 'z', 'zzsspzjzzzzzznzzz'],
        [3,4, 'r', 'rvzpfr'],
        [3,5, 'p', 'wpgxpb'],
        [4,5, 'r', 'qlrrr'],
        [7,9, 'q', 'vqzzqqrqtf'],
        [6,14, 'c', 'qcfwcfcchcvzzgcl'],
        [2,11, 'r', 'brhlrbvrlrrr'],
        [7,13, 'l', 'lllllllllrlllll'],
        [2,7, 'w', 'twfwwdwvzwbw'],
        [4,5, 'z', 'zzzbzz'],
        [3,4, 'q', 'qzzt'],
        [3,11, 'h', 'hhhhhhhhhhhh'],
        [5,12, 'c', 'cdclccgcccxfczrlcc'],
        [5,11, 'p', 'lmgprpppvphpj'],
        [2,5, 'r', 'rgkqrdsrxlmddmkktpnr'],
        [1,4, 'm', 'zmgfmqmmmxfm'],
        [15,16, 'f', 'ffbffffffffffwvnf'],
        [19,20, 'l', 'ltllllllllllllllllhl'],
        [2,6, 'j', 'spthjkftw'],
        [3,10, 'r', 'rrrrrrfrrmrrrr'],
        [1,8, 'n', 'nndfhqxn'],
        [6,7, 'j', 'zjjjjjj'],
        [12,14, 'k', 'qvgcvhmzkkrcck'],
        [6,8, 'k', 'kkhbkhkkkk'],
        [10,12, 's', 'ssrssxssslsj'],
        [9,18, 'h', 'dsmxxwndhgjpztkqhh'],
        [5,6, 'm', 'mmmmlf'],
        [4,5, 'x', 'xxxlh'],
        [9,15, 'b', 'bbbcsgbdcbbrbrfbbbbb'],
        [6,15, 'j', 'nfbjrpjjqjjxsbjt'],
        [1,6, 'c', 'cncpkcfwcd'],
        [2,4, 'm', 'xmmhmjbcmdmm'],
        [4,11, 's', 'lhdssvkldhsqssdjgs'],
        [14,19, 't', 'ttttttdtttttlttttttt'],
        [2,4, 'x', 'gxxxbxk'],
        [2,6, 'k', 'kkpqkkkz'],
        [10,11, 'w', 'wwwqwwwwcgqwww'],
        [8,9, 's', 'sssssssss'],
        [2,4, 'v', 'vvvwsrb'],
        [12,16, 's', 'rtcsfwssdswthfpf'],
        [3,11, 'g', 'fgnggtlgbgd'],
        [2,5, 'c', 'ggccc'],
        [10,15, 'h', 'hhhhhhlhpghhshh'],
        [1,5, 'n', 'nlhqnj'],
        [7,10, 'f', 'fnfffffhffff'],
        [5,6, 't', 'tfttkvt'],
        [1,4, 'c', 'mgcsrv'],
        [10,17, 'g', 'bggpmggggpgggggwqh'],
        [3,7, 'p', 'pprvppp'],
        [5,8, 'n', 'xnnqndnznf'],
        [6,11, 'b', 'bbbbrbfbrcdb'],
        [3,10, 'k', 'pcfknlqkgkpzkknk'],
        [10,11, 'm', 'mmmmmmmmmmc'],
        [3,4, 'v', 'fwvvh'],
        [2,7, 'l', 'zlcvxwrhlnnlkhr'],
        [1,7, 'q', 'vqqqjqsqqqqvrqqq'],
        [6,8, 'd', 'ddddddddd'],
        [1,3, 'z', 'zkzlrz'],
        [5,11, 'w', 'wbfzwdwpwdfztsrxzcw'],
        [7,9, 's', 'qsssclssl'],
        [3,5, 'l', 'cvmlgk'],
        [9,12, 's', 'qsrssnsvsxshqsdtd'],
        [8,12, 'm', 'wmxsnmmmfwzmf'],
        [1,12, 'x', 'xxxxxdxxjxxdxxxxxx'],
        [4,10, 'r', 'rwrlbkkmqrxr'],
        [5,13, 'g', 'ggggggggghgggx'],
        [11,15, 'w', 'wwwwtwnwwwvwwft'],
        [9,10, 'q', 'qqqqqqqqwfq'],
        [6,13, 'q', 'qmhfqqxkmcjwqmc'],
        [2,8, 'r', 'rrrrcmrrrrq'],
        [12,14, 'm', 'mmmwmmmmmgmhmt'],
        [2,6, 't', 'ttvtctt'],
        [3,6, 'r', 'qcrrpsxjttqrrr'],
        [7,8, 'g', 'gggggggk'],
        [13,15, 'w', 'wwwwwwwwwwwwwww'],
        [8,12, 'p', 'qqphwpjmwppfpvwrp'],
        [7,10, 'c', 'cccccwtccc'],
        [8,11, 'w', 'kwtwrwwwwcqwww'],
        [9,19, 'z', 'zzzzzzzzzzzzzzzzzzz'],
        [4,5, 'q', 'qqqsq'],
        [6,9, 'c', 'cxfcccgcccpc'],
        [7,9, 'd', 'nddlddxdgddzd'],
        [3,12, 'q', 'qrghqxqjqqdwqqq'],
        [14,15, 'w', 'wwwwwwwwwwwwwqmwwww'],
        [14,15, 'c', 'frcwcctccrccccc'],
        [2,5, 'v', 'vqvvdvv'],
        [3,4, 'r', 'rsrr'],
        [16,18, 'd', 'dddddddddddddddtdxdd'],
        [4,7, 'b', 'bfbbbbsbj'],
        [14,15, 'b', 'bbgbbbbbbfbbmbbbmb'],
        [2,7, 'b', 'pbrsbbb'],
        [15,16, 'q', 'qqqsqqqqqqqbnqqqqq'],
        [6,14, 'k', 'rbvkkvqrxfklck'],
        [2,6, 'c', 'klccdm'],
        [2,3, 'b', 'bpbbs'],
        [4,13, 'p', 'cppjppppppppmvpppp'],
        [1,2, 'k', 'kqkpq'],
        [8,9, 'r', 'rrrrrhrkr'],
        [7,9, 't', 'tptftttgwtmt'],
        [8,12, 'g', 'gfhkgqggznqghqg'],
        [15,18, 'n', 'pnnnnnnnnnnnnnnnnnn'],
        [4,5, 'p', 'qpqpq'],
        [1,9, 'h', 'xhqhhhnthzmhhhrh'],
        [4,6, 'x', 'bzkxxxhxxwdzpkks'],
        [4,5, 'c', 'ccccc'],
        [9,10, 'v', 'vvvvvvvvvv'],
        [8,12, 'd', 'cdcxdzgddtcfdrxt'],
        [7,10, 'b', 'bbbsbpbbgbbnj'],
        [4,7, 'z', 'zznzzzq'],
        [1,5, 'z', 'zjbzzjdppsbvgbg'],
        [2,4, 'w', 'lwwwtvjwdjwsbps'],
        [1,2, 'z', 'bzbvbz'],
        [6,14, 'n', 'dnnnnqnnnnnnnn'],
        [15,18, 'r', 'rfbrrwqshczrnbxrvhzr'],
        [9,11, 'f', 'ffffffffpfz'],
        [1,4, 'k', 'rskn'],
        [5,6, 'n', 'njnnnb'],
        [3,5, 'z', 'zzzzz'],
        [7,8, 'n', 'nntnnnnn'],
        [8,14, 'k', 'kkkkkkfkkkkkkkkk'],
        [11,16, 'r', 'rrqrprrrrrrrrrsvrr'],
        [2,10, 'c', 'dncjfccpcccccccc'],
        [8,20, 'q', 'gztqpsqqvthwpfjlqxrq'],
        [6,16, 'n', 'nnnnnpnnnnnnnnbnnnnn'],
        [4,7, 'h', 'ghhhwzhhhhhh'],
        [10,12, 'z', 'zzqzzzcfxzzzwzz'],
        [1,3, 'k', 'tlkwlkskklxvnk'],
        [12,13, 'n', 'nnnqqnnnnnnfpn'],
        [1,3, 'l', 'lnlb'],
        [6,9, 'b', 'bvfkbrzbwdmbvbql'],
        [11,13, 'd', 'ddddtdwtjdkdqz'],
        [9,15, 'j', 'jjcljjjjqjvnjjfjjj'],
        [13,14, 'l', 'tpllllllllqlll'],
        [18,20, 'd', 'dddddddddddzdddddtdb'],
        [9,15, 'x', 'nxxxmnxxxxxxsxxxjwg'],
        [6,7, 'j', 'rjwvjzjjx'],
        [5,6, 'j', 'jjjjjjj'],
        [8,13, 't', 'ttfttttttttttt'],
        [6,16, 'f', 'ffrffxfffffffffmf'],
        [3,4, 'f', 'mhxk'],
        [4,9, 'w', 'lnwnwwvtvwjww'],
        [9,12, 'd', 'dwdddqddpdddd'],
        [11,16, 'q', 'qqqqqqqjzqqpqqlq'],
        [2,14, 'k', 'zkskkmkrwrdkskq'],
        [5,8, 'v', 'vqxmvxvvj'],
        [3,5, 'z', 'zpbwzhrzzwqxr'],
        [3,5, 'c', 'cccgc'],
        [6,9, 'v', 'vvvtbvvvvtj'],
        [5,6, 'f', 'fjwfgdfgtf'],
        [1,2, 's', 'svvsnsk'],
        [11,13, 'f', 'qfpwfmrcfcwfr'],
        [3,6, 'j', 'jjjxdd'],
        [3,6, 'n', 'kntwpnn'],
        [8,13, 'v', 'qgmgcrxvdvkbs'],
        [11,16, 'q', 'cqsqpqlzqqdhqcqrbgk'],
        [1,8, 't', 'pptttttt'],
        [11,13, 'g', 'ggggggggggkgqgg'],
        [4,5, 'g', 'gggsgg'],
        [10,11, 'p', 'rpppfppppmpppp'],
        [6,7, 'q', 'qqqqqqq'],
        [3,11, 'f', 'pgfftfflctfd'],
        [3,8, 's', 'lswnfsjjdsh'],
        [11,13, 'k', 'kkkkkkkkkkmksk'],
        [3,5, 'p', 'pppjpppg'],
        [3,4, 'z', 'zznrz'],
        [8,9, 'd', 'ntgdwtdmh'],
        [2,3, 'g', 'gggl'],
        [19,20, 'q', 'qqqqqxqqqqqqqqqqqqwd'],
        [4,11, 'n', 'ljgdnkgftmsvntnn'],
        [16,19, 't', 'tttttttttttttttttttt']]# num of 't's <= 16 and num of 't's >= 19 
    loop = 0
    for pas in passwords:
        count = pas[3].count(pas[2])
        if count >= pas[0] and count <= pas[1]:
            loop += 1
            print(loop)
def twoparttwo2020():
    password = [  
        [
        4,5,'m','m','m','p','t','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'r','r','s','z','c','h','r','r','r','z','g','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'w','d','g','q','t','w','w','k','w','w','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'w','l','d','s','l','p','w','b','b','q','w','p','w','t','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'s','s','s','z','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'l','l','l','m','j','x','l','b','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,11,'c','c','c','c','t','c','c','c','c','c','c','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,11,'l','t','l','l','l','l','l','l','p','l','l','l','z','j','l','l','g','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,8,'j','l','j','j','j','j','j','j','q','c','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'s','s','s','s','s','s','q','s','s','l','s','v','h','f','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'f','f','f','f','f','f','m','f','q','f','f','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'m','m','m','m','s','q','m','m','m','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,9,'w','d','w','z','v','s','t','t','j','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'l','l','l','l','l','f','l','h','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,13,'f','j','f','k','w','h','z','r','t','k','t','p','h','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'p','p','v','l','d','p','p','q','v','c','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,17,'s','s','s','s','s','s','s','s','s','t','s','s','s','s','s','s','s','c','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'k','z','l','w','h','c','w','k','r','c','k','w','k','s','k','x','k','g','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'n','n','n','n','n','n','n','w','n','c','n','n','j','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'g','g','k','w','z','b','w','h','g','m','g','r','q','q','l','k','s','s','w','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'d','d','r','p','b','h','d','v','w','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'d','d','l','m','p','h','v','w','b','n','n','d','d','r','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'m','m','m','z','m','m','m','p','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'x','x','d','c','x','h','k','q','q','x','z','n','x','w','h','t','x','d','x','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,14,'c','p','n','c','w','n','c','d','c','c','c','c','c','d','m','w','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'s','g','s','r','s','s','s','s','s','b','s','s','s','s','t','k','s','s','m','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'m','d','h','m','z','m','l','n','f','m','s','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'l','l','l','m','l','r','l','l','c','h','l','w','h','l','k','t','p','x','d','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'g','n','j','g','k','g','l','g','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,14,'v','v','v','v','v','m','w','v','k','v','t','q','v','g','x','v','v','v','l','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'h','h','h','h','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'l','d','f','r','m','s','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'n','n','k','k','n','n','k','r','f','l','k','p','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'w','d','w','w','w','w','w','w','l','w','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'h','x','n','h','h','h','r','v','w','p','n','k','m','h','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'l','l','l','l','l','l','k','l','r','l','l','r','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'d','l','d','r','v','t','d','d','r','d','d','v','d','q','g','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'p','b','x','p','q','p','l','q','t','q','z','h','j','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'t','b','m','l','t','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,10,'j','l','j','j','j','j','j','j','m','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'x','x','x','x','v','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'b','b','x','b','b','b','b','b','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'t','t','t','j','m','s','t','t','w','t','d','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'p','d','m','x','x','r','p','n','p','p','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'x','x','x','x','x','x','g','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'v','v','w','c','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'l','l','q','p','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,20,'p','p','s','x','q','n','p','f','p','n','m','p','s','p','p','p','p','p','p','s','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,18,'g','l','g','g','g','k','g','g','g','g','g','g','g','g','g','g','g','g','l','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'b','t','b','f','b','b','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'n','n','s','n','n','n','n','n','n','n','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'p','d','p','p','n','d','l','m','t','n','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,15,'q','t','q','q','q','q','q','q','q','q','q','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'r','r','r','r','r','r','r','r','r','r','r','r','r','b','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'s','s','h','s','s','s','f','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'l','m','l','g','h','d','l','h','w','f','b','c','q','m','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'k','m','l','w','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,17,'v','h','b','v','l','q','v','k','n','v','v','s','v','z','v','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'g','b','m','n','g','r','g','t','t','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'h','h','h','m','h','h','h','h','h','t','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,15,'m','n','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'k','k','k','k','k','k','k','k','k','k','j','n','f','c','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,8,'k','s','k','k','k','z','k','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'j','j','j','j','j','j','j','h','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'g','g','m','g','x','w','g','l','g','g','g','g','g','b','g','g','q','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'p','p','p','p','x','p','p','q','p','p','r','l','g','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'j','c','p','j','j','j','j','j','j','j','j','j','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,12,'l','l','n','b','l','z','b','d','m','p','w','w','r','b','m','n','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'d','d','d','d','h','d','m','c','r','d','d','n','d','d','n','d','d','j','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'g','k','g','h','q','f','s','g','g','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        18,20,'g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','n','g','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'q','r','k','q','l','q','f','z','v','w','q','q','q','k','s','n','t','q','d','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,16,'m','d','k','m','m','z','g','m','d','m','m','m','h','w','m','x','m','x','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'q','q','n','q','h','t','k','q','q','q','q','q','q','j','v','c','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'m','m','m','l','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,10,'b','b','j','f','k','m','b','l','m','b','b','t','v','x','z','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'c','c','c','l','d','c','c','s','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'k','d','z','b','k','k','s','r','k','k','k','b','k','w','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'r','r','r','r','r','r','r','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'g','q','g','g','g','t','g','n','l','s','z','g','g','g','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'g','g','g','s','g','j','f','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'n','n','n','n','n','n','n','n','n','g','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'c','f','t','c','h','c','g','c','v','l','g','z','c','k','d','r','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,15,'p','p','p','p','n','p','p','p','p','p','p','p','p','z','h','p','p','l','h','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'k','x','n','l','h','l','x','s','d','z','k','v','h','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,8,'m','m','m','m','b','m','q','m','n','f','m','t','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'d','s','d','d','d','d','d','c','j','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'b','f','n','j','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,14,'c','c','c','c','c','c','r','j','c','c','c','c','c','c','c','c','h','c','f','q','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'l','l','l','l','l','l','w','h','t','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'z','z','z','b','z','r','z','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,10,'n','n','c','n','z','n','x','z','c','w','v','c','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'f','x','p','k','f','f','x','m','l','w','t','g','z','j','p','p','c','d','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        19,20,'c','c','c','c','c','c','c','c','c','c','c','c','c','c','x','c','c','c','c','l','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,14,'w','w','w','l','m','w','w','f','p','w','w','z','j','d','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,17,'f','f','v','f','f','f','v','f','f','f','f','f','x','f','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'s','g','t','s','h','b','p','z','g','x','n','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'m','m','m','s','j','j','g','m','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,17,'x','x','x','x','x','x','x','x','w','x','x','x','x','x','x','h','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'f','k','g','f','j','m','b','c','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'k','w','k','k','n','m','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'s','g','r','s','g','s','k','j','n','s','m','s','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'q','q','q','q','q','q','p','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'f','f','f','f','b','f','b','f','f','f','f','f','j','f','f','f','c','f','f','k','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'q','q','q','q','q','k','n','q','q','c','m','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,18,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,10,'j','c','m','h','g','l','h','q','j','d','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'h','p','n','h','z','h','k','g','x','b','h','k','d','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'j','q','j','j','j','j','w','j','j','j','l','z','j','b','j','j','d','c','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'q','q','q','q','q','q','q','q','q','q','q','k','c','k','v','r','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,15,'f','f','k','f','f','f','f','f','f','f','s','f','c','k','n','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,17,'c','v','g','p','s','g','l','c','z','j','d','f','c','n','q','t','b','n','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'k','m','m','x','k','t','w','k','k','w','b','v','f','k','k','d','k','k','k','n','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'s','s','s','s','s','s','s','s','p','s','s','s','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'l','l','c','q','d','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'m','m','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'k','f','k','k','k','j','k','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,15,'g','g','q','l','g','d','s','g','g','g','g','g','x','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'r','j','v','n','k','h','h','r','r','r','v','r','s','f','x','k','r','t','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'f','f','f','r','f','f','f','f','f','f','f','f','q','p','k','l','l','f','x','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'d','g','j','v','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'x','h','x','x','x','r','x','q','w','x','x','j','x','x','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'k','w','d','k','k','k','d','f','t','t','q','k','d','k','n','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'x','x','x','x','v','x','h','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'c','c','c','s','c','l','c','c','c','c','f','m','c','d','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,17,'c','c','d','c','c','s','v','c','c','c','c','c','c','c','c','c','c','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'s','s','s','s','s','s','s','s','s','s','k','s','s','s','n','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'j','j','j','j','w','h','q','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'s','k','s','s','s','s','s','s','s','s','s','s','s','p','c','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'w','t','n','m','l','b','h','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'g','l','q','g','r','t','c','g','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,11,'b','d','r','r','w','h','b','w','z','q','d','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'r','v','r','n','v','d','t','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,8,'w','v','w','w','w','w','w','w','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'v','v','v','v','v','v','v','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,14,'t','s','x','t','x','h','d','x','c','w','q','d','g','r','t','q','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'w','p','t','g','s','d','w','g','h','v','j','w','m','w','b','g','r','q','q','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'l','l','l','l','l','g','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'n','n','p','n','n','b','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'h','m','x','h','h','h','w','h','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,15,'j','b','j','j','j','t','n','j','p','p','j','j','j','z','c','j','j','s','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,11,'r','s','r','k','k','h','r','r','c','w','r','b','r','p','t','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'t','q','t','t','w','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'t','t','f','h','t','l','d','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,15,'r','l','w','d','m','l','g','r','r','r','r','t','r','r','r','p','x','g','r','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'d','d','d','c','d','d','d','d','g','w','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'b','c','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'m','v','m','m','n','x','t','d','x','m','m','n','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'r','r','w','r','v','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,10,'s','s','s','s','x','s','f','s','s','s','s','s','w','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'v','k','v','l','x','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,17,'h','d','h','q','h','h','h','l','x','h','h','h','h','q','h','h','b','h','h','n','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'d','b','d','d','d','p','k','d','n','f','r','n','m','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'x','q','v','s','t','b','x','v','k','q','f','n','x','w','n','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,18,'m','m','l','m','p','n','m','m','s','t','m','m','l','m','c','m','b','m','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'t','t','q','c','t','t','w','w','t','t','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'m','g','m','v','l','m','m','m','q','m','t','p','f','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'p','p','p','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,17,'d','x','d','d','g','q','h','d','d','d','c','p','t','x','d','h','x','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,11,'f','f','f','f','f','f','f','f','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'r','d','m','s','r','n','z','t','g','r','r','l','v','g','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'r','r','r','r','r','r','r','r','r','r','r','v','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,9,'k','k','k','k','k','b','k','k','k','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'b','v','s','b','b','b','t','r','n','q','z','b','b','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,12,'j','s','j','g','j','n','j','m','h','j','g','c','j','j','c','n','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,15,'h','l','q','h','v','h','h','t','x','k','h','c','h','m','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,14,'l','s','l','l','s','f','l','l','l','l','l','l','l','l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'v','p','v','v','v','v','v','v','v','v','v','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'j','j','j','g','j','j','j','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'q','q','q','q','q','m','q','q','q','q','q','d','q','x','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'p','p','p','p','p','p','p','p','h','p','n','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'s','s','s','r','s','s','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,14,'j','j','j','j','j','j','j','j','j','j','j','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'j','j','t','x','j','d','j','m','j','x','j','j','j','r','j','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,16,'d','d','d','d','d','d','d','d','d','k','d','d','d','d','d','j','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'h','h','h','h','h','w','h','x','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,12,'h','h','h','p','h','w','j','h','j','h','h','h','h','h','n','h','h','b','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'m','m','m','m','j','x','h','p','k','m','m','h','m','t','t','j','d','m','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'c','c','x','c','v','g','t','c','c','t','t','w','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'r','b','c','r','r','w','z','n','b','g','t','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'t','f','p','t','t','l','t','t','x','j','w','c','q','m','t','b','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'b','d','m','x','k','b','r','g','p','j','q','t','l','n','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'r','r','d','r','f','p','r','q','p','r','k','g','w','p','x','r','r','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,13,'c','c','c','c','k','p','c','s','c','c','w','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'l','v','l','l','l','l','l','k','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,11,'x','x','x','x','j','x','x','x','x','v','x','t','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,12,'s','s','j','s','s','s','s','x','n','s','s','m','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'w','w','t','h','m','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'f','f','k','p','p','f','f','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'c','c','g','k','t','c','c','c','c','c','k','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'q','l','h','n','s','q','r','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'m','d','v','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'x','d','b','x','x','l','x','k','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,14,'d','d','d','s','d','j','s','l','p','k','f','d','d','x','j','j','j','k','d','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,16,'c','c','c','q','c','v','c','t','j','c','c','c','r','c','c','g','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'d','d','d','d','r','k','d','d','d','d','k','m','x','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'w','g','p','w','g','s','k','m','x','s','j','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'v','b','x','h','g','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'w','w','h','w','h','f','q','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'x','s','x','x','x','r','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'g','g','g','d','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'h','h','h','h','b','h','h','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'s','s','s','s','s','x','s','k','s','s','h','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'w','w','w','w','l','w','q','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'d','s','d','p','q','d','d','d','d','m','d','d','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'j','j','j','j','j','j','j','j','n','j','j','j','m','n','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,9,'p','p','v','z','s','t','c','c','l','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        18,19,'g','f','g','g','g','g','g','g','g','g','l','p','g','g','g','g','g','z','t','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,17,'z','z','z','z','z','n','z','z','z','z','f','z','z','v','z','t','z','h','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'j','p','j','j','k','j','k','j','j','j','g','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,12,'w','d','w','b','w','w','b','z','w','w','w','b','v','w','m','w','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'g','v','g','g','g','w','q','n','w','s','p','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,13,'w','w','w','w','w','w','w','c','z','w','n','w','t','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,11,'m','m','j','d','t','s','v','w','m','c','q','m','v','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'c','v','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,17,'k','w','s','k','k','k','k','k','k','k','k','g','j','k','z','k','k','k','g','m','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'g','m','g','h','g','r','n','g','j','g','g','v','j','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'p','p','p','p','s','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'v','v','v','v','v','v','r','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,14,'j','j','j','m','q','l','z','j','b','j','j','j','l','m','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,13,'f','f','k','b','n','f','f','f','f','f','f','f','f','p','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,9,'r','v','r','f','r','x','t','v','w','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'k','f','k','s','k','p','j','k','k','b','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,19,'d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','h','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,16,'s','s','w','t','m','g','s','w','s','s','f','w','s','x','p','s','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'s','s','s','s','s','s','s','s','s','s','s','s','l','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'q','w','v','z','v','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,14,'d','p','d','d','d','d','q','g','c','d','d','d','j','d','d','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'x','v','b','q','p','x','x','b','k','x','m','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'q','q','z','q','q','q','q','q','w','f','m','t','q','f','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,17,'l','m','d','l','c','l','l','l','l','h','r','l','l','l','h','p','l','l','c','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'q','q','q','q','q','q','s','t','c','g','c','x','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'x','t','x','t','x','h','x','x','m','x','h','x','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'c','c','c','c','c','c','c','p','p','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'v','v','m','v','m','v','v','v','v','v','v','v','v','x','v','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'r','r','r','r','r','r','z','r','r','g','l','r','r','r','r','k','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'s','s','s','b','s','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,17,'g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'g','s','g','v','g','t','g','g','h','m','t','x','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','v','z','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'n','n','n','n','n','q','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,15,'t','m','v','t','t','t','v','t','f','t','q','z','m','t','j','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'q','q','q','q','q','b','q','q','w','q','r','z','q','q','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,14,'h','h','j','h','h','h','c','h','h','h','h','j','h','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,15,'b','z','b','w','h','d','j','k','s','b','q','b','d','b','m','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,12,'r','m','r','n','g','g','r','w','z','r','h','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,16,'m','j','m','m','m','m','m','m','m','m','q','w','m','m','c','x','m','f','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'h','q','s','m','h','h','h','t','s','b','h','h','h','j','h','w','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'h','h','k','g','h','h','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'k','n','k','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'j','j','r','j','j','g','b','g','j','x','r','q','j','r','m','j','j','g','c','k','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'w','w','w','w','q','q','l','w','d','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'b','f','s','b','b','b','q','b','b','q','m','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,16,'n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'b','c','b','b','q','m','b','b','r','h','b','b','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'l','x','j','z','k','b','w','g','f','w','w','c','w','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'c','c','c','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'l','l','h','l','s','l','m','l','w','m','w','b','l','l','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'h','r','q','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'t','d','m','t','t','t','m','x','h','t','q','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,17,'n','n','n','x','c','n','n','c','n','n','v','g','c','n','n','r','n','r','m','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'x','x','x','m','x','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,10,'j','j','j','j','j','j','j','t','j','t','v','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'d','l','d','l','d','b','n','n','d','d','d','d','d','s','g','d','p','g','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,8,'n','n','s','j','v','h','n','c','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'f','f','f','f','f','f','s','s','f','f','x','f','f','f','h','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'q','k','w','n','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'k','k','r','k','c','k','l','k','h','k','s','p','q','m','q','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'k','d','k','l','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,14,'j','j','j','j','j','j','j','j','j','j','j','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'v','v','v','v','v','v','v','f','v','v','v','v','v','v','v','v','m','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'l','w','d','l','g','l','l','q','l','s','l','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'t','p','r','b','w','t','t','m','t','p','v','w','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,20,'c','c','w','c','c','t','q','c','c','t','h','c','c','r','p','c','c','c','c','c','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,12,'s','s','s','s','s','s','b','s','s','s','s','s','z','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'k','m','k','k','j','k','l','h','k','k','t','k','k','k','d','v','k','q','q','k','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'n','n','n','n','n','r','n','n','s','n','g','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'p','p','p','p','p','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,11,'f','m','v','m','d','f','m','d','w','f','f','f','f','f','w','f','r','j','f','q','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,16,'r','r','z','s','r','d','s','r','r','r','r','r','r','p','r','p','j','r','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'c','c','c','c','c','c','c','d','c','c','c','c','c','t','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,18,'n','n','n','n','n','n','n','n','n','n','n','n','n','c','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'r','r','v','r','r','d','h','f','l','c','r','t','w','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,9,'p','p','r','p','c','z','p','b','p','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'q','q','q','q','q','c','k','s','q','q','t','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'d','x','x','d','p','m','d','b','v','d','d','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'j','j','j','l','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'n','n','r','n','n','n','s','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'w','p','n','w','k','w','d','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'w','w','l','w','g','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,14,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,15,'k','k','k','k','k','f','s','k','k','h','k','k','k','q','p','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'b','b','b','b','b','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'r','j','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'h','h','t','k','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'g','g','g','g','g','g','g','g','g','g','g','g','g','g','v','g','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,18,'s','s','s','s','s','s','s','s','s','s','s','g','s','s','s','s','s','s','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'m','p','k','n','g','m','m','p','j','m','x','m','m','m','m','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'f','r','s','m','x','v','s','g','h','d','l','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'z','z','v','z','h','z','z','c','z','d','v','z','k','z','z','g','h','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,18,'v','v','v','v','v','v','v','v','v','v','v','v','v','v','j','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'t','t','t','t','t','t','m','t','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'j','h','j','w','x','g','b','j','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'k','k','k','k','k','k','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,13,'d','d','d','p','g','d','f','d','d','d','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'v','v','q','v','q','k','r','j','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'h','h','j','h','h','n','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'v','j','v','v','s','r','g','s','v','f','q','l','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'m','m','m','m','m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'f','f','f','n','f','p','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'b','b','b','b','b','b','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'p','p','p','j','w','q','p','j','b','n','p','p','p','w','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'l','l','l','d','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'g','g','v','g','q','g','g','t','g','g','g','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'x','j','x','x','x','x','x','w','x','q','q','v','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'w','l','w','w','g','b','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'d','j','c','d','m','g','k','m','f','v','v','l','q','p','h','b','d','d','v','h','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,12,'s','s','s','s','s','l','s','s','s','s','s','s','n','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'p','c','j','n','p','p','j','l','l','x','b','r','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'n','j','m','z','j','h','t','t','n','k','k','g','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'t','v','r','g','t','r','g','j','r','d','m','t','c','f','z','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'l','l','l','l','l','l','n','m','l','v','l','d','l','l','l','r','w','m','l','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,16,'m','m','b','d','m','m','m','m','m','m','h','m','s','m','m','m','m','t','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'z','z','s','z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'h','h','h','h','q','h','r','b','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'n','r','l','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,19,'x','x','x','x','c','x','x','x','v','x','x','x','x','x','x','x','x','x','x','k','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,10,'r','r','c','c','r','r','r','h','r','r','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'h','h','h','h','d','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'g','h','g','f','z','p','m','p','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'x','x','x','q','h','h','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'m','j','m','m','m','m','z','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'j','b','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'q','g','q','s','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'g','g','g','g','g','m','b','g','h','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'f','f','n','f','d','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'q','q','p','q','t','d','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'t','p','t','c','t','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'d','p','d','d','v','d','d','d','s','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'f','f','f','f','t','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'b','b','b','d','b','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,17,'f','f','g','f','c','k','c','d','f','f','f','f','t','f','f','x','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'w','w','w','k','x','s','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,12,'l','h','v','g','q','m','b','q','l','r','n','z','l','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'f','s','z','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'q','s','q','q','q','q','n','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'p','p','p','v','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'c','c','w','s','c','b','k','g','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,12,'s','s','s','s','f','s','s','s','s','p','s','f','s','g','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'t','j','s','t','t','t','g','s','t','s','t','t','g','h','z','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'j','j','j','j','j','t','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'k','f','f','k','d','k','t','k','k','h','b','b','w','k','k','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,15,'k','k','k','k','k','k','z','k','k','k','c','b','k','k','k','k','k','k','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,17,'w','w','w','g','w','n','n','k','s','w','w','p','q','w','k','w','d','h','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,20,'l','w','l','l','l','l','l','s','l','l','l','l','l','r','l','l','l','l','l','l','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'r','r','r','r','f','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'l','f','l','l','l','n','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'s','s','s','s','s','s','s','s','s','s','s','s','c','w','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'r','z','p','q','r','r','r','r','r','f','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,13,'h','x','h','h','f','h','z','c','h','h','j','h','h','t','d','r','h','h','z','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'b','b','b','b','b','n','r','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,12,'f','t','f','f','j','c','j','t','l','n','v','g','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'g','g','t','g','k','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,14,'n','n','n','n','n','n','n','b','r','n','n','n','p','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,17,'j','j','j','j','j','j','j','j','j','j','j','j','d','j','j','v','j','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,13,'r','b','r','g','r','r','r','f','r','m','f','r','r','x','r','g','r','r','r','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,13,'v','v','w','v','j','s','f','t','z','k','v','c','x','v','d','b','x','f','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,19,'f','f','f','f','f','f','f','f','f','f','m','f','f','f','f','f','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'g','v','g','g','x','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,16,'m','c','s','c','k','d','f','x','g','l','f','p','z','m','r','h','c','m','b','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,15,'z','g','z','q','j','z','c','z','z','z','z','j','z','z','h','j','b','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'w','w','w','w','l','w','w','w','w','w','w','w','w','h','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'j','c','j','j','d','j','j','j','j','s','j','j','j','k','j','j','j','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,15,'w','w','w','w','q','w','w','z','w','w','m','w','w','t','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'p','p','p','j','c','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,10,'f','f','f','j','f','f','r','f','f','f','s','g','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,19,'q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'g','g','m','g','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,14,'s','f','p','s','s','s','d','m','s','s','d','s','g','s','g','v','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'m','m','m','m','m','m','m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'c','f','c','g','n','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'t','t','t','c','g','t','t','t','r','t','t','t','t','t','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'v','v','v','r','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'w','x','w','p','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,12,'d','t','r','d','h','r','q','l','q','w','r','l','s','r','d','f','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'n','b','b','n','n','n','z','r','n','n','j','d','n','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,10,'w','w','w','w','r','w','d','w','j','g','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'d','d','d','d','d','j','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'p','p','p','q','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,19,'f','d','f','b','j','g','f','f','m','p','v','n','k','h','f','w','j','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'k','k','k','k','k','k','k','k','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'t','v','q','t','x','t','x','t','v','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'c','c','c','c','c','l','c','c','c','c','c','c','c','t','c','c','t','w','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,13,'x','t','m','x','x','z','x','k','l','x','g','z','x','x','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'b','b','b','b','r','b','b','b','b','b','b','b','b','b','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'h','g','m','z','h','h','h','h','m','r','h','q','h','h','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'k','k','k','k','k','k','k','q','k','c','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'v','p','g','v','d','v','v','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,19,'f','f','f','f','f','f','f','f','f','f','f','f','x','f','f','f','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'p','m','p','h','t','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'t','c','t','t','t','v','w','t','n','t','q','t','t','t','t','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'t','x','n','t','r','z','x','t','l','n','w','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,18,'l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'c','z','c','z','p','c','f','d','z','b','l','n','k','c','v','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'z','f','z','z','z','m','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'f','t','d','c','f','f','p','f','f','w','q','l','f','f','f','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'h','h','h','h','h','c','h','h','h','h','s','h','h','h','h','h','d','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'m','m','s','m','m','m','k','m','m','m','j','m','m','m','m','z','m','m','n','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'s','n','h','b','s','c','s','g','c','s','s','x','s','r','s','s','s','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,17,'q','q','q','v','q','q','q','h','q','r','k','q','q','q','q','g','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'t','v','q','t','b','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'t','w','f','d','r','s','r','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'f','f','f','f','f','z','d','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,13,'r','p','m','r','t','k','v','d','c','r','x','r','n','r','z','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,18,'r','w','r','r','q','r','r','c','r','r','l','r','j','m','r','r','k','r','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,17,'j','j','j','j','j','j','j','j','c','j','j','j','j','j','j','x','j','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'h','z','m','h','h','l','m','h','h','h','d','h','h','h','h','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,15,'l','l','l','l','l','l','n','l','f','l','l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'n','n','n','f','n','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'s','s','s','s','s','s','s','s','s','l','s','s','s','s','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'k','k','d','k','j','k','k','k','s','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'z','g','z','z','m','z','h','d','p','l','n','w','w','v','l','s','j','n','z','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,15,'r','r','v','m','r','b','s','r','t','r','f','d','q','r','r','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'l','l','l','l','l','l','l','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'g','d','n','g','g','x','h','g','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'f','f','f','t','f','f','k','d','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'r','r','r','r','v','r','p','r','b','r','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'q','q','w','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'h','m','z','h','p','w','n','k','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'m','m','m','l','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,15,'v','v','j','p','k','v','d','z','v','z','d','l','k','l','p','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'r','r','r','g','g','v','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,13,'d','d','w','r','p','d','s','d','j','h','l','d','d','q','d','d','h','d','w','d','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'r','f','v','r','r','s','p','r','r','m','r','r','r','j','g','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'s','z','s','r','s','s','v','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'d','d','f','d','w','t','c','v','g','v','c','d','f','d','q','d','w','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,12,'n','r','h','n','j','n','n','d','n','f','n','w','q','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'l','h','v','l','x','l','c','n','c','l','q','l','l','r','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,14,'l','l','l','l','l','l','l','l','l','l','j','l','l','l','p','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,10,'b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,11,'q','q','q','q','q','q','q','q','t','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'r','r','r','r','r','r','r','x','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'k','j','k','k','k','z','s','m','b','t','n','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,17,'r','r','r','r','r','r','r','l','r','p','r','r','d','r','r','r','r','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'t','d','f','g','n','v','t','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'v','q','v','v','d','s','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'l','l','l','t','l','r','l','l','j','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'m','m','d','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,18,'t','t','t','t','t','t','t','t','t','t','t','t','t','j','t','x','t','t','w','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'b','b','b','b','b','b','b','b','b','b','b','p','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'b','b','w','n','b','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'t','t','f','d','t','l','t','s','t','d','f','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,10,'z','z','z','f','z','z','z','z','t','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'q','q','q','q','q','q','q','q','m','q','n','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,11,'r','r','z','r','r','r','r','z','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'k','k','k','k','k','l','k','l','b','k','m','k','l','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,18,'l','s','l','l','l','l','l','b','l','l','l','l','l','l','l','l','l','c','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,14,'s','s','s','s','s','s','s','s','s','s','w','s','s','s','s','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'s','h','w','s','s','s','s','g','j','s','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'g','f','b','g','g','x','g','t','b','n','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'z','t','z','z','z','h','z','j','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'g','g','g','g','g','g','g','c','r','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,20,'g','g','r','g','g','h','j','c','n','l','m','k','s','z','x','r','g','t','g','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,16,'n','p','r','q','n','w','n','n','g','b','g','t','j','s','v','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'z','z','s','z','l','g','q','d','g','t','q','b','z','z','l','p','k','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,8,'f','f','f','f','t','f','f','n','n','f','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,18,'s','j','r','d','g','s','s','s','z','d','x','k','z','h','l','s','f','z','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'l','l','l','l','l','l','l','b','p','l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'l','l','l','l','l','b','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'b','b','b','b','b','w','b','b','b','l','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'g','g','d','w','h','d','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'v','j','n','f','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'h','h','h','h','h','h','x','h','h','h','m','z','h','b','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'r','w','b','r','r','r','r','x','g','w','l','v','w','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'m','g','x','m','p','m','m','m','g','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'h','h','h','h','h','z','h','h','h','h','j','h','n','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,13,'g','k','z','k','z','t','g','n','l','b','q','h','l','g','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'z','z','k','t','z','z','z','z','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'q','p','q','r','x','q','q','h','f','p','g','l','w','q','t','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'f','p','f','f','v','f','b','t','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'l','t','l','l','j','j','l','l','l','n','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,17,'f','f','l','f','f','p','f','f','f','f','d','f','q','f','f','s','c','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'q','b','q','x','q','r','q','r','r','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'l','l','l','l','n','l','l','f','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'r','x','r','g','r','r','j','r','r','r','k','g','r','r','q','r','n','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,19,'r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        18,19,'w','l','b','q','r','k','d','w','w','w','q','g','r','k','l','c','w','x','w','w','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'n','n','n','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,13,'b','b','b','b','b','b','b','b','b','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'k','h','k','b','f','s','k','q','k','j','k','t','w','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'c','t','l','v','m','t','f','c','p','c','c','w','w','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'r','r','z','z','r','s','p','m','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,11,'g','g','g','h','z','g','g','l','g','g','g','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'p','p','b','p','w','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'q','q','q','r','q','q','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,13,'m','m','m','m','w','x','m','m','l','m','n','v','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'p','p','p','p','l','q','p','f','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,15,'t','t','t','t','t','t','t','c','t','t','t','l','t','c','t','g','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'m','c','m','n','h','j','q','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'m','m','z','j','m','t','m','m','m','m','m','d','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,10,'j','j','z','g','j','c','j','j','j','j','s','p','j','j','j','j','j','g','j','m','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'r','v','m','x','t','r','r','n','r','x','n','n','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,16,'h','h','h','h','h','h','q','h','f','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'z','k','c','m','k','z','m','z','p','z','t','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'j','j','j','j','j','j','j','j','j','j','z','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'x','x','x','k','m','x','x','c','x','x','v','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','g','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'w','w','w','w','w','w','g','q','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'d','d','k','d','p','m','c','d','d','j','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,12,'s','s','s','s','s','s','s','s','s','s','s','s','v','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,10,'q','f','c','p','w','t','g','q','q','q','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'w','w','w','w','w','g','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,11,'q','q','q','q','q','q','q','q','n','q','q','b','q','q','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'d','d','d','d','w','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'x','q','x','c','g','x','x','x','x','v','d','x','d','k','z','x','x','x','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'k','k','q','c','s','j','x','s','z','v','s','c','f','v','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'d','m','g','d','d','d','d','d','h','k','d','q','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'x','x','j','x','x','l','j','l','s','f','r','f','n','h','s','x','x','l','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,9,'g','x','g','s','x','g','t','g','g','g','x','m','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'p','t','p','p','k','n','p','t','k','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'z','g','z','z','b','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'p','p','p','g','p','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'f','f','z','f','f','f','f','f','f','f','f','f','f','f','f','f','w','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'t','t','z','t','t','v','q','l','t','f','x','t','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'v','v','h','q','v','z','p','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'f','f','m','f','f','f','t','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,13,'d','d','x','r','d','g','d','d','d','d','r','d','d','d','d','q','p','g','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'r','r','r','r','r','r','n','l','n','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'t','b','t','t','t','w','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'g','g','g','g','g','g','g','g','g','g','g','h','g','b','l','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,19,'r','q','k','g','r','v','f','n','s','r','w','z','r','q','s','r','h','r','r','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,17,'j','j','j','j','j','j','j','j','j','j','j','n','j','j','j','h','j','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,9,'t','b','t','m','r','b','c','g','t','t','j','h','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'n','n','n','n','n','n','n','n','n','v','n','n','n','n','n','n','z','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'l','l','l','t','l','l','l','g','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'f','f','l','b','f','p','h','v','w','f','d','f','f','j','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'z','l','s','z','z','z','z','z','z','z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,9,'k','l','v','z','k','k','h','k','k','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'j','f','m','r','j','c','c','s','j','r','z','j','q','k','f','v','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'x','x','x','x','x','v','m','x','x','x','x','c','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'c','w','c','c','c','c','c','c','c','j','x','c','v','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'l','s','b','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'x','x','n','v','l','n','x','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'f','n','f','f','c','c','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'p','v','p','p','p','p','p','p','r','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'d','v','f','c','q','m','d','d','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'b','b','b','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,13,'n','n','n','n','n','n','n','n','n','n','n','n','n','w','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'q','z','q','q','q','q','q','q','q','q','q','p','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'g','g','b','g','g','g','g','d','g','g','l','g','m','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,13,'b','w','b','b','b','x','n','b','b','q','b','b','b','b','k','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'g','g','g','g','w','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,9,'r','v','n','q','v','v','h','p','r','z','m','b','h','r','c','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'m','m','m','m','m','m','m','m','m','m','p','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'c','c','g','r','b','c','c','d','b','c','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,8,'r','r','b','v','r','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,11,'d','d','d','d','d','j','d','m','d','d','f','h','v','d','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'k','z','j','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,11,'w','w','t','w','w','w','w','w','w','w','w','s','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'b','b','k','b','b','b','b','f','b','b','x','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'w','w','w','n','j','s','w','w','m','g','b','w','r','w','w','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,18,'j','j','j','j','j','j','j','j','j','k','j','j','j','j','j','j','j','j','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'t','t','t','t','t','t','v','w','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'v','w','v','v','v','b','v','v','v','v','v','v','v','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,20,'d','d','d','d','d','d','d','d','d','d','d','d','d','h','d','d','d','d','d','d','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,12,'q','q','d','q','q','q','q','q','q','q','q','q','x','q','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'w','r','j','d','s','w','w','w','w','w','w','q','m','m','p','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'b','b','b','b','b','b','b','b','b','x','c','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'q','q','q','q','w','x','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,15,'n','n','n','m','n','n','n','n','n','n','c','n','n','n','n','v','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,17,'f','f','n','f','f','f','f','f','f','f','f','f','f','f','f','f','c','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'p','k','r','p','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,10,'c','c','v','s','c','c','c','l','w','c','c','r','c','j','j','c','l','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'t','f','p','n','h','t','m','t','q','t','v','w','c','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,13,'r','r','r','x','r','r','r','r','r','r','f','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'l','l','l','l','l','l','w','l','l','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,15,'n','d','n','n','n','n','n','n','h','s','x','g','n','n','h','s','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,16,'b','b','b','b','b','b','b','c','b','b','b','n','b','w','k','b','s','b','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'g','q','h','l','x','g','g','g','q','v','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,14,'x','p','t','q','c','g','x','n','n','h','p','x','b','g','x','l','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        17,19,'g','g','g','g','g','g','g','g','c','g','g','g','b','g','g','g','g','n','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,19,'q','q','t','j','r','q','q','w','j','v','q','q','q','k','n','q','b','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,13,'j','j','j','j','j','j','j','n','j','j','l','j','j','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'g','m','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'w','p','w','t','w','j','d','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'j','j','j','j','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,13,'z','p','s','z','z','z','g','l','z','h','z','z','z','z','h','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'j','f','h','h','j','x','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'l','l','l','l','l','l','l','l','l','s','l','t','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'c','c','x','d','v','z','c','c','l','c','c','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,15,'g','g','g','g','g','g','g','g','g','f','g','g','g','g','k','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'z','z','j','j','b','g','z','l','x','q','z','z','s','x','z','d','x','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'z','k','x','c','s','z','z','z','s','r','s','c','c','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'t','s','t','t','w','x','g','t','w','l','b','z','b','s','f','f','t','t','j','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'r','r','n','m','r','r','r','t','r','r','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'m','p','m','m','t','m','m','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'f','l','g','g','c','p','d','p','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,19,'j','j','x','j','j','x','j','f','s','s','r','v','l','m','j','j','f','j','j','m','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,8,'w','w','r','w','s','w','c','w','v','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,15,'k','k','k','k','p','k','k','k','k','k','k','k','k','k','k','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,15,'s','x','b','s','s','n','s','h','p','s','s','s','g','s','b','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,15,'z','v','z','r','z','z','c','z','b','h','z','z','z','z','z','z','z','h','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,14,'w','w','w','w','w','w','w','w','w','w','t','w','w','w','w','w','w','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'k','k','k','k','k','k','k','k','k','k','k','k','k','k','c','k','k','k','k','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'s','s','f','s','s','v','s','s','s','s','s','s','s','m','s','p','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'d','d','d','d','q','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'h','p','h','s','b','l','h','n','f','h','c','h','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,11,'x','r','x','x','x','b','h','x','x','x','j','x','x','x','t','g','s','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'x','x','x','x','x','x','x','q','x','x','x','n','x','v','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,10,'p','j','b','p','z','f','m','p','h','p','w','p','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,13,'v','v','v','v','v','s','h','v','v','g','v','s','f','q','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'r','r','r','z','w','r','z','d','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'f','f','f','f','f','f','x','f','f','f','f','z','f','w','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,11,'c','c','z','c','c','d','m','k','h','h','c','v','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,11,'w','w','w','s','x','w','w','w','w','w','w','w','w','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'t','t','t','k','n','m','t','x','v','t','t','t','t','n','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'r','r','r','p','j','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'v','v','k','v','v','j','q','v','v','b','v','t','l','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'q','m','w','v','h','p','q','q','q','c','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'f','f','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'r','t','r','r','c','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'s','s','s','s','s','s','s','s','s','s','s','s','v','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'d','d','r','d','d','z','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'n','n','n','k','n','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'x','x','x','x','x','f','x','x','r','z','b','x','z','v','t','x','l','x','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'v','s','b','g','s','v','s','s','b','n','h','m','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'n','d','n','n','g','q','w','n','n','j','t','n','j','j','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'w','x','d','s','v','z','d','m','z','s','w','w','w','w','w','w','m','g','j','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'h','w','h','h','h','h','m','h','b','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,18,'w','w','s','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'v','v','v','v','v','v','v','v','v','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'v','v','r','h','v','v','c','v','v','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,9,'r','r','r','r','r','m','z','n','t','r','s','g','r','r','k','h','h','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'v','v','v','v','t','v','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,10,'t','t','t','n','t','t','w','z','g','p','t','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'c','g','c','c','r','n','g','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'b','b','b','b','q','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'s','z','s','d','l','s','j','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'j','j','j','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'g','g','g','n','h','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'w','f','w','w','k','w','h','j','q','b','w','q','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'w','w','d','g','n','j','w','q','w','q','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'b','b','b','t','k','s','b','b','d','x','b','p','j','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,15,'k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'b','b','b','b','r','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'g','g','g','g','g','g','v','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,14,'s','s','s','s','n','w','s','s','r','s','s','s','s','l','c','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'q','n','g','j','p','r','q','q','m','d','w','g','k','j','q','v','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'z','v','z','z','k','z','z','g','z','z','z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'n','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'b','f','b','w','b','l','j','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,18,'h','h','h','h','h','h','h','h','h','h','h','s','h','h','h','h','h','h','l','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,15,'r','r','r','z','g','r','z','w','r','b','l','r','f','w','f','r','s','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'n','z','n','c','n','k','n','k','n','b','g','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'f','v','w','f','f','f','t','f','f','f','p','f','f','z','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'c','f','c','c','c','b','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'b','b','x','j','b','c','p','s','b','r','g','b','g','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'f','t','f','f','h','r','s','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,12,'g','g','g','g','g','g','g','t','g','g','g','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'t','k','t','p','h','t','t','l','t','c','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'w','f','w','s','g','w','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'m','m','f','m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'z','g','z','j','z','z','f','j','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'l','l','v','t','l','l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'m','r','s','m','m','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'r','r','r','r','r','r','r','r','r','r','l','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'j','h','h','q','t','k','w','z','n','g','h','b','f','s','b','w','p','v','r','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'z','z','j','z','n','d','z','r','m','q','z','l','p','t','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,16,'m','m','m','h','m','m','m','m','m','m','m','m','m','p','m','r','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'p','p','p','p','p','h','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'s','z','s','c','g','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'h','h','h','h','h','h','h','h','h','h','h','h','h','h','l','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'f','r','f','f','r','t','l','x','w','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'z','p','t','q','l','z','z','x','s','k','r','j','s','n','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'t','f','t','t','t','s','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'t','t','h','t','t','t','t','t','p','t','t','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'g','q','z','h','m','g','p','t','d','f','w','g','g','q','q','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'f','n','f','f','f','h','f','k','f','f','h','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'w','q','s','x','g','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'d','d','d','d','d','d','d','d','d','d','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'v','q','s','b','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,13,'z','z','x','c','z','s','z','k','w','x','z','g','k','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'t','c','b','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'q','c','l','n','d','c','n','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'f','k','f','n','h','q','b','f','n','n','p','n','t','f','s','v','x','c','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'d','g','d','d','t','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'z','t','z','t','z','z','z','d','n','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'t','t','t','t','t','t','v','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'g','n','p','z','g','g','d','h','v','g','g','p','q','g','x','w','g','v','g','s','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,12,'p','k','w','p','p','t','p','p','l','x','r','c','g','f','x','p','h','p','q','b','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,18,'f','f','f','f','j','f','f','f','f','f','f','f','f','f','f','w','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,17,'n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,10,'d','d','n','d','d','d','k','d','d','d','d','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'v','c','v','h','v','s','v','h','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'f','f','s','c','r','t','x','l','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,14,'b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,11,'n','n','n','l','n','x','n','t','n','l','x','n','n','n','k','t','n','n','x','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,18,'p','p','p','p','z','p','p','p','p','f','q','h','p','p','p','p','z','r','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'h','h','h','h','h','z','h','h','m','q','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'r','r','r','r','r','w','r','r','r','r','r','r','r','r','x','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,8,'f','w','f','f','f','g','n','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'j','j','s','w','v','g','t','f','h','t','f','f','j','g','j','j','s','x','s','d','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'n','n','n','n','s','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'w','d','x','h','c','j','v','w','w','z','w','d','d','d','h','h','w','w','l','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,13,'h','p','p','s','h','f','s','h','g','h','p','h','c','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,15,'b','c','b','x','n','b','h','b','b','j','b','h','b','b','m','b','k','v','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,11,'c','t','d','g','c','q','l','c','c','c','c','c','t','h','w','m','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'p','m','p','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'x','x','p','z','x','x','k','z','l','r','s','g','r','b','x','p','k','l','c','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,11,'f','q','f','f','f','f','g','f','f','f','c','g','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,19,'h','h','h','h','h','h','h','h','h','h','h','h','h','h','s','b','k','h','h','q','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'h','h','c','l','h','h','h','p','s','v','h','h','f','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'s','l','q','c','p','p','x','l','s','f','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'v','v','v','v','v','v','n','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'q','x','q','q','q','q','q','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'m','q','m','m','c','j','m','v','m','c','k','r','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,9,'h','h','h','h','d','h','f','h','h','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,14,'r','v','p','s','p','r','l','s','t','j','k','r','m','m','r','p','z','q','s','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'g','g','g','g','g','r','l','q','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'t','d','t','k','t','t','p','t','t','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'n','v','k','k','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'g','g','f','l','g','w','g','g','g','r','g','m','m','g','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,19,'l','b','l','b','l','m','l','r','l','l','l','h','b','l','l','w','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'x','g','v','x','s','x','k','r','v','d','q','b','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,12,'b','b','b','b','b','d','p','d','b','b','w','l','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,13,'n','n','n','n','n','n','n','n','n','s','n','n','n','r','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'n','m','f','n','n','n','n','n','k','x','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'f','k','x','x','f','q','n','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'x','x','x','x','x','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'f','n','s','n','x','w','r','f','t','k','c','g','z','f','f','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'w','w','w','p','w','w','x','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'m','b','r','v','m','m','n','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'r','r','k','b','h','n','m','d','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'b','k','n','b','z','b','b','f','n','f','b','b','b','l','r','q','b','r','b','n','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'v','v','v','v','x','v','v','x','b','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'q','q','c','s','j','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,15,'c','g','c','d','p','c','c','r','c','d','d','c','c','w','c','c','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'l','r','l','l','l','l','l','l','l','l','l','l','p','c','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'w','w','w','w','w','w','w','w','w','w','f','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'f','f','x','t','f','f','f','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'x','x','x','x','k','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'c','c','c','r','r','w','b','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'g','g','g','g','g','g','p','g','q','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'t','v','z','t','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,11,'c','z','c','c','c','c','c','c','c','c','q','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'p','h','b','p','z','p','p','d','l','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'h','f','r','h','h','h','z','h','p','r','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'d','m','z','d','n','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'t','g','t','t','t','t','t','t','t','t','q','t','t','n','t','t','t','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,8,'c','c','c','q','c','j','b','h','p','c','c','c','z','v','f','c','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'b','l','z','t','c','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'d','d','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,8,'j','p','w','f','j','f','d','j','j','j','j','z','k','j','c','j','r','l','w','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'m','q','m','m','m','m','m','j','n','m','p','m','m','m','m','x','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,17,'f','p','p','b','f','d','s','j','v','p','f','h','z','c','c','b','w','f','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,8,'c','c','f','n','h','q','t','c','m','c','w','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'b','b','b','q','x','p','f','z','q','f','v','k','p','b','h','c','b','d','f','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'k','k','k','k','k','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,8,'f','v','p','w','f','k','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'t','t','t','x','t','v','t','t','h','t','t','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'j','f','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        18,19,'v','v','v','v','v','v','v','v','v','v','v','v','v','v','g','v','v','v','x','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,14,'q','q','q','q','q','q','q','q','q','q','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'p','p','p','p','l','x','p','r','w','v','j','m','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,14,'q','q','p','q','x','z','q','q','q','q','q','q','g','q','m','g','q','q','g','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'x','d','q','l','x','t','k','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'f','s','f','c','z','g','f','f','f','z','f','h','f','f','j','k','k','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'x','x','x','x','x','f','w','x','x','x','p','m','x','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'b','j','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'p','v','r','p','v','p','p','p','p','p','p','p','d','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        18,19,'l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'v','j','j','z','v','n','s','f','b','b','v','q','c','d','f','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,18,'d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'t','f','t','t','t','d','t','k','r','d','t','k','t','t','t','l','t','t','k','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,17,'d','d','d','k','d','d','f','l','d','d','d','d','d','d','d','d','d','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,20,'v','h','f','z','h','t','t','v','v','n','k','x','q','v','v','h','l','v','v','v','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'t','t','b','w','t','s','z','g','w','p','n','t','t','h','t','v','t','t','r','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'s','s','s','s','h','s','s','t','d','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'h','h','h','h','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'b','b','b','s','b','f','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,12,'n','z','n','v','q','n','s','l','f','h','n','w','n','q','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'g','g','g','g','k','g','g','g','g','g','g','g','g','g','g','g','g','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,12,'j','v','j','q','d','j','j','j','t','s','j','d','j','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,16,'j','j','j','j','d','j','l','j','j','j','j','j','j','j','j','j','j','j','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,14,'d','d','d','d','d','d','t','q','d','d','d','d','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'m','m','p','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'c','c','c','c','c','c','c','d','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'l','c','l','l','l','h','n','l','l','l','r','z','z','g','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'c','c','c','c','c','c','c','c','c','b','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'k','k','k','k','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,12,'r','r','r','r','t','j','x','h','x','z','b','r','r','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'w','w','w','w','k','w','h','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'m','f','q','r','m','r','m','m','m','m','g','m','m','m','t','m','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'w','k','w','w','n','w','w','w','g','h','h','g','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'k','k','k','k','k','k','k','p','k','k','k','k','t','v','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,9,'w','h','w','q','j','f','l','k','k','w','d','q','m','w','m','c','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,16,'h','h','m','h','m','h','h','h','k','x','h','g','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'z','z','j','z','l','h','j','p','f','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'d','d','d','d','q','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'s','s','s','s','s','s','s','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'d','w','d','d','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'k','n','h','z','k','k','m','k','x','k','h','k','p','h','k','d','k','k','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,15,'m','k','h','m','m','m','m','m','m','h','g','m','m','m','m','m','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,9,'n','j','n','k','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'g','n','t','g','g','g','f','g','g','m','l','r','g','c','g','g','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,15,'g','g','g','g','g','h','g','g','g','g','m','g','m','g','g','d','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,13,'x','r','x','x','x','x','x','r','x','x','x','x','x','n','q','x','w','s','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'n','b','n','n','b','n','n','v','d','w','n','l','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'v','m','v','b','n','z','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,8,'n','n','p','n','t','n','n','n','j','n','x','k','n','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'t','t','t','f','t','t','t','l','q','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'g','g','g','g','g','m','g','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,7,'x','x','x','b','j','c','x','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,8,'d','d','d','d','d','l','d','d','d','d','d','d','d','w','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'s','c','s','s','w','j','b','f','n','j','n','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'m','m','m','m','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,17,'z','z','z','s','s','p','z','j','z','z','z','z','z','z','n','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'r','r','v','z','p','f','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'p','w','p','g','x','p','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'r','q','l','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'q','v','q','z','z','q','q','r','q','t','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,14,'c','q','c','f','w','c','f','c','c','h','c','v','z','z','g','c','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,11,'r','b','r','h','l','r','b','v','r','l','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,13,'l','l','l','l','l','l','l','l','l','l','r','l','l','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'w','t','w','f','w','w','d','w','v','z','w','b','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'z','z','z','z','b','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'q','q','z','z','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'h','h','h','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,12,'c','c','d','c','l','c','c','g','c','c','c','x','f','c','z','r','l','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'p','l','m','g','p','r','p','p','p','v','p','h','p','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'r','r','g','k','q','r','d','s','r','x','l','m','d','d','m','k','k','t','p','n','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'m','z','m','g','f','m','q','m','m','m','x','f','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'f','f','f','b','f','f','f','f','f','f','f','f','f','f','w','v','n','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        19,20,'l','l','t','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','h','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'j','s','p','t','h','j','k','f','t','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,10,'r','r','r','r','r','r','r','f','r','r','m','r','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,8,'n','n','n','d','f','h','q','x','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'j','z','j','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'k','q','v','g','c','v','h','m','z','k','k','r','c','c','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'k','k','k','h','b','k','h','k','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'s','s','s','r','s','s','x','s','s','s','l','s','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,18,'h','d','s','m','x','x','w','n','d','h','g','j','p','z','t','k','q','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'m','m','m','m','m','l','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'x','x','x','x','l','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,15,'b','b','b','b','c','s','g','b','d','c','b','b','r','b','r','f','b','b','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,15,'j','n','f','b','j','r','p','j','j','q','j','j','x','s','b','j','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,6,'c','c','n','c','p','k','c','f','w','c','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'m','x','m','m','h','m','j','b','c','m','d','m','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,11,'s','l','h','d','s','s','v','k','l','d','h','s','q','s','s','d','j','g','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,19,'t','t','t','t','t','t','t','d','t','t','t','t','t','l','t','t','t','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'x','g','x','x','x','b','x','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'k','k','k','p','q','k','k','k','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'w','w','w','w','q','w','w','w','w','c','g','q','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'s','s','s','s','s','s','s','s','s','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'v','v','v','v','w','s','r','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,16,'s','r','t','c','s','f','w','s','s','d','s','w','t','h','f','p','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'g','f','g','n','g','g','t','l','g','b','g','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'c','g','g','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,15,'h','h','h','h','h','h','h','l','h','p','g','h','h','s','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'n','n','l','h','q','n','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'f','f','n','f','f','f','f','f','h','f','f','f','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'t','t','f','t','t','k','v','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'c','m','g','c','s','r','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,17,'g','b','g','g','p','m','g','g','g','g','p','g','g','g','g','g','w','q','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,7,'p','p','p','r','v','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,8,'n','x','n','n','q','n','d','n','z','n','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,11,'b','b','b','b','b','r','b','f','b','r','c','d','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,10,'k','p','c','f','k','n','l','q','k','g','k','p','z','k','k','n','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'m','m','m','m','m','m','m','m','m','m','m','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'v','f','w','v','v','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'l','z','l','c','v','x','w','r','h','l','n','n','l','k','h','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,7,'q','v','q','q','q','j','q','s','q','q','q','q','v','r','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,8,'d','d','d','d','d','d','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'z','z','k','z','l','r','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,11,'w','w','b','f','z','w','d','w','p','w','d','f','z','t','s','r','x','z','c','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'s','q','s','s','s','c','l','s','s','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'l','c','v','m','l','g','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'s','q','s','r','s','s','n','s','v','s','x','s','h','q','s','d','t','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'m','w','m','x','s','n','m','m','m','f','w','z','m','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,12,'x','x','x','x','x','x','d','x','x','j','x','x','d','x','x','x','x','x','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,10,'r','r','w','r','l','b','k','k','m','q','r','x','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,13,'g','g','g','g','g','g','g','g','g','g','h','g','g','g','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,15,'w','w','w','w','w','t','w','n','w','w','w','v','w','w','f','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'q','q','q','q','q','q','q','q','q','w','f','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,13,'q','q','m','h','f','q','q','x','k','m','c','j','w','q','m','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,8,'r','r','r','r','r','c','m','r','r','r','r','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,14,'m','m','m','m','w','m','m','m','m','m','g','m','h','m','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'t','t','t','v','t','c','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'r','q','c','r','r','p','s','x','j','t','t','q','r','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'g','g','g','g','g','g','g','g','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,15,'w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'p','q','q','p','h','w','p','j','m','w','p','p','f','p','v','w','r','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'c','c','c','c','c','c','w','t','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,11,'w','k','w','t','w','r','w','w','w','w','c','q','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,19,'z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'q','q','q','q','s','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'c','c','x','f','c','c','c','g','c','c','c','p','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'d','n','d','d','l','d','d','x','d','g','d','d','z','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,12,'q','q','r','g','h','q','x','q','j','q','q','d','w','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'w','w','w','w','w','w','w','w','w','w','w','w','w','w','q','m','w','w','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'c','f','r','c','w','c','c','t','c','c','r','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,5,'v','v','q','v','v','d','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'r','r','s','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,18,'d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','t','d','x','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'b','b','f','b','b','b','b','s','b','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        14,15,'b','b','b','g','b','b','b','b','b','b','f','b','b','m','b','b','b','m','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,7,'b','p','b','r','s','b','b','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,16,'q','q','q','q','s','q','q','q','q','q','q','q','b','n','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,14,'k','r','b','v','k','k','v','q','r','x','f','k','l','c','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,6,'c','k','l','c','c','d','m','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'b','b','p','b','b','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,13,'p','c','p','p','j','p','p','p','p','p','p','p','p','m','v','p','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'k','k','q','k','p','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'r','r','r','r','r','r','h','r','k','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,9,'t','t','p','t','f','t','t','t','g','w','t','m','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'g','g','f','h','k','g','q','g','g','z','n','q','g','h','q','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,18,'n','p','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'p','q','p','q','p','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,9,'h','x','h','q','h','h','h','n','t','h','z','m','h','h','h','r','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,6,'x','b','z','k','x','x','x','h','x','x','w','d','z','p','k','k','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'c','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,10,'v','v','v','v','v','v','v','v','v','v','v','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,12,'d','c','d','c','x','d','z','g','d','d','t','c','f','d','r','x','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,10,'b','b','b','b','s','b','p','b','b','g','b','b','n','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'z','z','z','n','z','z','z','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,5,'z','z','j','b','z','z','j','d','p','p','s','b','v','g','b','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,4,'w','l','w','w','w','t','v','j','w','d','j','w','s','b','p','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'z','b','z','b','v','b','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,14,'n','d','n','n','n','n','q','n','n','n','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        15,18,'r','r','f','b','r','r','w','q','s','h','c','z','r','n','b','x','r','v','h','z','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,11,'f','f','f','f','f','f','f','f','f','p','f','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,4,'k','r','s','k','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'n','n','j','n','n','n','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'z','z','z','z','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        7,8,'n','n','n','t','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,14,'k','k','k','k','k','k','k','f','k','k','k','k','k','k','k','k','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,16,'r','r','r','q','r','p','r','r','r','r','r','r','r','r','r','s','v','r','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,10,'c','d','n','c','j','f','c','c','p','c','c','c','c','c','c','c','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,20,'q','g','z','t','q','p','s','q','q','v','t','h','w','p','f','j','l','q','x','r','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,16,'n','n','n','n','n','n','p','n','n','n','n','n','n','n','n','b','n','n','n','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,7,'h','g','h','h','h','w','z','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,12,'z','z','z','q','z','z','z','c','f','x','z','z','z','w','z','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'k','t','l','k','w','l','k','s','k','k','l','x','v','n','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        12,13,'n','n','n','n','q','q','n','n','n','n','n','n','f','p','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,3,'l','l','n','l','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'b','b','v','f','k','b','r','z','b','w','d','m','b','v','b','q','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'d','d','d','d','d','t','d','w','t','j','d','k','d','q','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,15,'j','j','j','c','l','j','j','j','j','q','j','v','n','j','j','f','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        13,14,'l','t','p','l','l','l','l','l','l','l','l','q','l','l','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        18,20,'d','d','d','d','d','d','d','d','d','d','d','d','z','d','d','d','d','d','t','d','b','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,15,'x','n','x','x','x','m','n','x','x','x','x','x','x','s','x','x','x','j','w','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'j','r','j','w','v','j','z','j','j','x','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'j','j','j','j','j','j','j','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,13,'t','t','t','f','t','t','t','t','t','t','t','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,16,'f','f','f','r','f','f','x','f','f','f','f','f','f','f','f','f','m','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'f','m','h','x','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,9,'w','l','n','w','n','w','w','v','t','v','w','j','w','w','0','0','0','0','0','0','0','0','0'
        ],
        [
        9,12,'d','d','w','d','d','d','q','d','d','p','d','d','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,16,'q','q','q','q','q','q','q','q','j','z','q','q','p','q','q','l','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,14,'k','z','k','s','k','k','m','k','r','w','r','d','k','s','k','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,8,'v','v','q','x','m','v','x','v','v','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'z','z','p','b','w','z','h','r','z','z','w','q','x','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'c','c','c','c','g','c','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,9,'v','v','v','v','t','b','v','v','v','v','t','j','0','0','0','0','0','0','0','0','0'
        ],
        [
        5,6,'f','f','j','w','f','g','d','f','g','t','f','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,2,'s','s','v','v','s','n','s','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'f','q','f','p','w','f','m','r','c','f','c','w','f','r','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'j','j','j','j','x','d','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,6,'n','k','n','t','w','p','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,13,'v','q','g','m','g','c','r','x','v','d','v','k','b','s','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,16,'q','c','q','s','q','p','q','l','z','q','q','d','h','q','c','q','r','b','g','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        1,8,'t','p','p','t','t','t','t','t','t','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'g','g','g','g','g','g','g','g','g','g','g','k','g','q','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,5,'g','g','g','g','s','g','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        10,11,'p','r','p','p','p','f','p','p','p','p','m','p','p','p','p','0','0','0','0','0','0','0','0','0'
        ],
        [
        6,7,'q','q','q','q','q','q','q','q','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,11,'f','p','g','f','f','t','f','f','l','c','t','f','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,8,'s','l','s','w','n','f','s','j','j','d','s','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        11,13,'k','k','k','k','k','k','k','k','k','k','k','m','k','s','k','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,5,'p','p','p','p','j','p','p','p','g','0','0','0','0','0','0','0','0','0'
        ],
        [
        3,4,'z','z','z','n','r','z','0','0','0','0','0','0','0','0','0'
        ],
        [
        8,9,'d','n','t','g','d','w','t','d','m','h','0','0','0','0','0','0','0','0','0'
        ],
        [
        2,3,'g','g','g','g','l','0','0','0','0','0','0','0','0','0'
        ],
        [
        19,20,'q','q','q','q','q','q','x','q','q','q','q','q','q','q','q','q','q','q','q','w','d','0','0','0','0','0','0','0','0','0'
        ],
        [
        4,11,'n','l','j','g','d','n','k','g','f','t','m','s','v','n','t','n','n','0','0','0','0','0','0','0','0','0'
        ],
        [
        16,19,'t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','0','0','0','0','0','0','0','0','0','0'
        ]]
    loop = 0
    for pas in password:
        if pas[2] == pas[pas[0]+2] and pas[2] == pas[pas[1]+2]:
            print('no')
        elif pas[2] != pas[pas[0]+2] and pas[2] != pas[pas[1]+2]:
            print('no')
        else:
            loop += 1
    print(loop)