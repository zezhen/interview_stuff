'''
https://leetcode.com/problems/gray-code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:


Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1


Example 2:


Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        if n == 0: return [0]
        if n == 1: return [0, 1]

        ans = [0,1,3,2]
        if n == 2: return ans

        for i in xrange(3, n+1):
            size = len(ans)
            for j in xrange(size-1, -1, -1):
                ans.append((1<<(i-1)) + ans[j])
        return ans

s = Solution()
print s.grayCode(11) == [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,21,23,22,18,19,17,16,48,49,51,50,54,55,53,52,60,61,63,62,58,59,57,56,40,41,43,42,46,47,45,44,36,37,39,38,34,35,33,32,96,97,99,98,102,103,101,100,108,109,111,110,106,107,105,104,120,121,123,122,126,127,125,124,116,117,119,118,114,115,113,112,80,81,83,82,86,87,85,84,92,93,95,94,90,91,89,88,72,73,75,74,78,79,77,76,68,69,71,70,66,67,65,64,192,193,195,194,198,199,197,196,204,205,207,206,202,203,201,200,216,217,219,218,222,223,221,220,212,213,215,214,210,211,209,208,240,241,243,242,246,247,245,244,252,253,255,254,250,251,249,248,232,233,235,234,238,239,237,236,228,229,231,230,226,227,225,224,160,161,163,162,166,167,165,164,172,173,175,174,170,171,169,168,184,185,187,186,190,191,189,188,180,181,183,182,178,179,177,176,144,145,147,146,150,151,149,148,156,157,159,158,154,155,153,152,136,137,139,138,142,143,141,140,132,133,135,134,130,131,129,128,384,385,387,386,390,391,389,388,396,397,399,398,394,395,393,392,408,409,411,410,414,415,413,412,404,405,407,406,402,403,401,400,432,433,435,434,438,439,437,436,444,445,447,446,442,443,441,440,424,425,427,426,430,431,429,428,420,421,423,422,418,419,417,416,480,481,483,482,486,487,485,484,492,493,495,494,490,491,489,488,504,505,507,506,510,511,509,508,500,501,503,502,498,499,497,496,464,465,467,466,470,471,469,468,476,477,479,478,474,475,473,472,456,457,459,458,462,463,461,460,452,453,455,454,450,451,449,448,320,321,323,322,326,327,325,324,332,333,335,334,330,331,329,328,344,345,347,346,350,351,349,348,340,341,343,342,338,339,337,336,368,369,371,370,374,375,373,372,380,381,383,382,378,379,377,376,360,361,363,362,366,367,365,364,356,357,359,358,354,355,353,352,288,289,291,290,294,295,293,292,300,301,303,302,298,299,297,296,312,313,315,314,318,319,317,316,308,309,311,310,306,307,305,304,272,273,275,274,278,279,277,276,284,285,287,286,282,283,281,280,264,265,267,266,270,271,269,268,260,261,263,262,258,259,257,256,768,769,771,770,774,775,773,772,780,781,783,782,778,779,777,776,792,793,795,794,798,799,797,796,788,789,791,790,786,787,785,784,816,817,819,818,822,823,821,820,828,829,831,830,826,827,825,824,808,809,811,810,814,815,813,812,804,805,807,806,802,803,801,800,864,865,867,866,870,871,869,868,876,877,879,878,874,875,873,872,888,889,891,890,894,895,893,892,884,885,887,886,882,883,881,880,848,849,851,850,854,855,853,852,860,861,863,862,858,859,857,856,840,841,843,842,846,847,845,844,836,837,839,838,834,835,833,832,960,961,963,962,966,967,965,964,972,973,975,974,970,971,969,968,984,985,987,986,990,991,989,988,980,981,983,982,978,979,977,976,1008,1009,1011,1010,1014,1015,1013,1012,1020,1021,1023,1022,1018,1019,1017,1016,1000,1001,1003,1002,1006,1007,1005,1004,996,997,999,998,994,995,993,992,928,929,931,930,934,935,933,932,940,941,943,942,938,939,937,936,952,953,955,954,958,959,957,956,948,949,951,950,946,947,945,944,912,913,915,914,918,919,917,916,924,925,927,926,922,923,921,920,904,905,907,906,910,911,909,908,900,901,903,902,898,899,897,896,640,641,643,642,646,647,645,644,652,653,655,654,650,651,649,648,664,665,667,666,670,671,669,668,660,661,663,662,658,659,657,656,688,689,691,690,694,695,693,692,700,701,703,702,698,699,697,696,680,681,683,682,686,687,685,684,676,677,679,678,674,675,673,672,736,737,739,738,742,743,741,740,748,749,751,750,746,747,745,744,760,761,763,762,766,767,765,764,756,757,759,758,754,755,753,752,720,721,723,722,726,727,725,724,732,733,735,734,730,731,729,728,712,713,715,714,718,719,717,716,708,709,711,710,706,707,705,704,576,577,579,578,582,583,581,580,588,589,591,590,586,587,585,584,600,601,603,602,606,607,605,604,596,597,599,598,594,595,593,592,624,625,627,626,630,631,629,628,636,637,639,638,634,635,633,632,616,617,619,618,622,623,621,620,612,613,615,614,610,611,609,608,544,545,547,546,550,551,549,548,556,557,559,558,554,555,553,552,568,569,571,570,574,575,573,572,564,565,567,566,562,563,561,560,528,529,531,530,534,535,533,532,540,541,543,542,538,539,537,536,520,521,523,522,526,527,525,524,516,517,519,518,514,515,513,512,1536,1537,1539,1538,1542,1543,1541,1540,1548,1549,1551,1550,1546,1547,1545,1544,1560,1561,1563,1562,1566,1567,1565,1564,1556,1557,1559,1558,1554,1555,1553,1552,1584,1585,1587,1586,1590,1591,1589,1588,1596,1597,1599,1598,1594,1595,1593,1592,1576,1577,1579,1578,1582,1583,1581,1580,1572,1573,1575,1574,1570,1571,1569,1568,1632,1633,1635,1634,1638,1639,1637,1636,1644,1645,1647,1646,1642,1643,1641,1640,1656,1657,1659,1658,1662,1663,1661,1660,1652,1653,1655,1654,1650,1651,1649,1648,1616,1617,1619,1618,1622,1623,1621,1620,1628,1629,1631,1630,1626,1627,1625,1624,1608,1609,1611,1610,1614,1615,1613,1612,1604,1605,1607,1606,1602,1603,1601,1600,1728,1729,1731,1730,1734,1735,1733,1732,1740,1741,1743,1742,1738,1739,1737,1736,1752,1753,1755,1754,1758,1759,1757,1756,1748,1749,1751,1750,1746,1747,1745,1744,1776,1777,1779,1778,1782,1783,1781,1780,1788,1789,1791,1790,1786,1787,1785,1784,1768,1769,1771,1770,1774,1775,1773,1772,1764,1765,1767,1766,1762,1763,1761,1760,1696,1697,1699,1698,1702,1703,1701,1700,1708,1709,1711,1710,1706,1707,1705,1704,1720,1721,1723,1722,1726,1727,1725,1724,1716,1717,1719,1718,1714,1715,1713,1712,1680,1681,1683,1682,1686,1687,1685,1684,1692,1693,1695,1694,1690,1691,1689,1688,1672,1673,1675,1674,1678,1679,1677,1676,1668,1669,1671,1670,1666,1667,1665,1664,1920,1921,1923,1922,1926,1927,1925,1924,1932,1933,1935,1934,1930,1931,1929,1928,1944,1945,1947,1946,1950,1951,1949,1948,1940,1941,1943,1942,1938,1939,1937,1936,1968,1969,1971,1970,1974,1975,1973,1972,1980,1981,1983,1982,1978,1979,1977,1976,1960,1961,1963,1962,1966,1967,1965,1964,1956,1957,1959,1958,1954,1955,1953,1952,2016,2017,2019,2018,2022,2023,2021,2020,2028,2029,2031,2030,2026,2027,2025,2024,2040,2041,2043,2042,2046,2047,2045,2044,2036,2037,2039,2038,2034,2035,2033,2032,2000,2001,2003,2002,2006,2007,2005,2004,2012,2013,2015,2014,2010,2011,2009,2008,1992,1993,1995,1994,1998,1999,1997,1996,1988,1989,1991,1990,1986,1987,1985,1984,1856,1857,1859,1858,1862,1863,1861,1860,1868,1869,1871,1870,1866,1867,1865,1864,1880,1881,1883,1882,1886,1887,1885,1884,1876,1877,1879,1878,1874,1875,1873,1872,1904,1905,1907,1906,1910,1911,1909,1908,1916,1917,1919,1918,1914,1915,1913,1912,1896,1897,1899,1898,1902,1903,1901,1900,1892,1893,1895,1894,1890,1891,1889,1888,1824,1825,1827,1826,1830,1831,1829,1828,1836,1837,1839,1838,1834,1835,1833,1832,1848,1849,1851,1850,1854,1855,1853,1852,1844,1845,1847,1846,1842,1843,1841,1840,1808,1809,1811,1810,1814,1815,1813,1812,1820,1821,1823,1822,1818,1819,1817,1816,1800,1801,1803,1802,1806,1807,1805,1804,1796,1797,1799,1798,1794,1795,1793,1792,1280,1281,1283,1282,1286,1287,1285,1284,1292,1293,1295,1294,1290,1291,1289,1288,1304,1305,1307,1306,1310,1311,1309,1308,1300,1301,1303,1302,1298,1299,1297,1296,1328,1329,1331,1330,1334,1335,1333,1332,1340,1341,1343,1342,1338,1339,1337,1336,1320,1321,1323,1322,1326,1327,1325,1324,1316,1317,1319,1318,1314,1315,1313,1312,1376,1377,1379,1378,1382,1383,1381,1380,1388,1389,1391,1390,1386,1387,1385,1384,1400,1401,1403,1402,1406,1407,1405,1404,1396,1397,1399,1398,1394,1395,1393,1392,1360,1361,1363,1362,1366,1367,1365,1364,1372,1373,1375,1374,1370,1371,1369,1368,1352,1353,1355,1354,1358,1359,1357,1356,1348,1349,1351,1350,1346,1347,1345,1344,1472,1473,1475,1474,1478,1479,1477,1476,1484,1485,1487,1486,1482,1483,1481,1480,1496,1497,1499,1498,1502,1503,1501,1500,1492,1493,1495,1494,1490,1491,1489,1488,1520,1521,1523,1522,1526,1527,1525,1524,1532,1533,1535,1534,1530,1531,1529,1528,1512,1513,1515,1514,1518,1519,1517,1516,1508,1509,1511,1510,1506,1507,1505,1504,1440,1441,1443,1442,1446,1447,1445,1444,1452,1453,1455,1454,1450,1451,1449,1448,1464,1465,1467,1466,1470,1471,1469,1468,1460,1461,1463,1462,1458,1459,1457,1456,1424,1425,1427,1426,1430,1431,1429,1428,1436,1437,1439,1438,1434,1435,1433,1432,1416,1417,1419,1418,1422,1423,1421,1420,1412,1413,1415,1414,1410,1411,1409,1408,1152,1153,1155,1154,1158,1159,1157,1156,1164,1165,1167,1166,1162,1163,1161,1160,1176,1177,1179,1178,1182,1183,1181,1180,1172,1173,1175,1174,1170,1171,1169,1168,1200,1201,1203,1202,1206,1207,1205,1204,1212,1213,1215,1214,1210,1211,1209,1208,1192,1193,1195,1194,1198,1199,1197,1196,1188,1189,1191,1190,1186,1187,1185,1184,1248,1249,1251,1250,1254,1255,1253,1252,1260,1261,1263,1262,1258,1259,1257,1256,1272,1273,1275,1274,1278,1279,1277,1276,1268,1269,1271,1270,1266,1267,1265,1264,1232,1233,1235,1234,1238,1239,1237,1236,1244,1245,1247,1246,1242,1243,1241,1240,1224,1225,1227,1226,1230,1231,1229,1228,1220,1221,1223,1222,1218,1219,1217,1216,1088,1089,1091,1090,1094,1095,1093,1092,1100,1101,1103,1102,1098,1099,1097,1096,1112,1113,1115,1114,1118,1119,1117,1116,1108,1109,1111,1110,1106,1107,1105,1104,1136,1137,1139,1138,1142,1143,1141,1140,1148,1149,1151,1150,1146,1147,1145,1144,1128,1129,1131,1130,1134,1135,1133,1132,1124,1125,1127,1126,1122,1123,1121,1120,1056,1057,1059,1058,1062,1063,1061,1060,1068,1069,1071,1070,1066,1067,1065,1064,1080,1081,1083,1082,1086,1087,1085,1084,1076,1077,1079,1078,1074,1075,1073,1072,1040,1041,1043,1042,1046,1047,1045,1044,1052,1053,1055,1054,1050,1051,1049,1048,1032,1033,1035,1034,1038,1039,1037,1036,1028,1029,1031,1030,1026,1027,1025,1024]