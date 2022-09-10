# Matrix Rotation/Imaging
----

Remember: the shape with the origin and it’s relationship are unchanged!


1.  Imaging
    1.  ![[Archive/面试资料/Programming/_resources/Matrix_Rotation_Imaging.resources/unknown_filename.png]]
        1.  Imaging by function y=x, point (x,y) projects to (x’,y’)
        2.  The triangle of origin, (x,y) and axis is unchanged, thus it’s in same shape of that contains (x’, y’) => **x’= y, y’ = x**
    2.  ![[Archive/面试资料/Programming/_resources/Matrix_Rotation_Imaging.resources/unknown_filename.1.png]]
        1.  Imaging by function y = 1 - x, point (x, y) projects to (x’, y’)
        2.  The origin projects to (n, n), thus x’ + y = n, y’ + x = n => **x’ = n - y, y’ = n - x**
    3.  ![[Archive/面试资料/Programming/_resources/Matrix_Rotation_Imaging.resources/unknown_filename.4.png]]
        1.  Imaging vertically, origin projects to (0, n), thus **x’ = x, y’ = n - y**
    4.  ![[Archive/面试资料/Programming/_resources/Matrix_Rotation_Imaging.resources/unknown_filename.3.png]]
        1.  Imaging horizontally, origin projects to (n, 0), thus **x’ = n - x, y’ = y**
2.  Rotation
    1.  ![[Archive/面试资料/Programming/_resources/Matrix_Rotation_Imaging.resources/unknown_filename.2.png]]
    2.  Clock-wise 90: from (x, y) to (a, b) 
        1.  origin rotate to (0, n) => **a = y, b = n - x**
    3.  Reverse Clockwise 90: from (x, y) to (c, d)
        1.  origin rotate to (n, 0) => c = n - y, d = x
    4.  Clock-wise 180: from (x, y) to (e, f)
        1.  origin rotate to (n, n) => e = n - x, f = n - y
3.  Imaging to Rotation
    1.  ![[Archive/面试资料/Programming/_resources/Matrix_Rotation_Imaging.resources/unknown_filename.5.png]]
    2.  Given point (x, y), it’s imaging point by y=x is (x’, y’)
    3.  Clock-wise 90 point (a, b) is the vertically imaging point of (x’, y’) => **Clock-wise 90 <=> (y=x) imaging + vertically imaging**
    4.  Reverse clock-wise 90 points (c, d), it’s horizontally imaging point of (x’, y’) => **Reverse Clock-wise 90 <=> (y=x) imaging + horizontally imaging**
    5.  Clock-wise 180 point (e, f), it’s (y=1-x) imaging point of (x’, y’) => **Clock-wise** 180 <=> (y=x) imaging + (y=1-x) imaging
4.  



----

- Date: 2019-02-13
- Tags: #Interview/Programing 



