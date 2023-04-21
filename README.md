# Ex1_NewSpace

## חלק 1 


האלגוריתם שבחרנו הינו התאמת תכונת תמונה באמצעות Scale-Invariant Feature Transform (SIFT) ו-Brute-Force Matcher (BFMatcher) ב-OpenCV. <br />

סקירה קצרה של שלבי האלגוריתם: <br />

טען שתי תמונות בגווני אפור (img1 ו-img2) מנתיבי קבצים. <br />

שנה את גודל התמונות למחצית מהגודל המקורי שלהן באמצעות הפונקציה cv2.resize() .על מנת להקל על זמן החישוב. <br />

אתחל את גלאי התכונה SIFT באמצעות cv2.SIFT_create(). <br />

זיהוי נקודות מפתח ומחשב מתארים עבור שתי התמונות באמצעות פונקציית detector.detectAndCompute(), אשר מוצאת נקודות מפתח ומחשבת את המתארים שלהן. <br />

אתחול ה-BFMatcher באמצעות cv2.BFMatcher(cv2.NORM_L2, crossCheck=True), אשר מחשב את המרחקים הזוגיים בין המתארים. <br /> 

התאם את המתארים בין שתי התמונות באמצעות הפונקציה matcher.match(), המחזירה רשימה של התאמות. <br />

הדפס את הקואורדינטות של נקודות המפתח המותאמות עבור כל התאמה. <br />

מיין את ההתאמות לפי מרחק באמצעות הפונקציה sorted() ומקש כ-x.distance עבור כל התאמה.
 <br />
צייר את ההתאמות בין התמונות באמצעות הפונקציה cv2.drawMatches(), היוצרת תמונה עם נקודות מפתח מותאמות. <br />

הצג את נקודות המפתח המתואמות בחלון באמצעות הפונקציה cv2.imshow() .
 <br />
בסך הכל, קוד זה מדגים כיצד להשתמש ב-SIFT וב-BFMatcher עבור התאמת תכונות בתמונות ולדמיין את נקודות המפתח המותאמות. <br />

## חלק 2 
 חלק זה ממשנו בקובץ part2.py <br />
תחילה נטען את התמונות בעזרת ספרייה cv2 . נחפש נקודות מפתח , נמיר את התמונה לגוונים של אפור. נחפש את הפיקסלים שהם לבנים בטווח שבין 230 ל255 , מוצאים את הכוכבים בעזרת  findcontours() ומדפסים את הכמות הכוכבים שמצאנו . לאחר מכאן צובעים את כל הכוכבים שנמצאו באדום  על מנת שנוכל למצוא את הכוכבים בתמונה. מדפיסים את כל הכוכבים קורדינאטות X ,Y  רדיוס ובהירות. <br />

![image](https://user-images.githubusercontent.com/92544909/233650975-eb508fa3-7b84-4103-b600-601a55e3a038.png)  <br />  <br />
עוברים על תקיית התמונות ועבור כל תמונה נציג את מיקומם של הכוכבים על ציר הx,y את עוצמתם, והרדיוס של כל כוכב  . <br />  <br />
![image](https://user-images.githubusercontent.com/92544909/233651849-13b36973-bf62-4b66-8547-3f6884107510.png) <br />


## חלק 3 
בחלק זה ממשנו את חלק 1 בקובץ part3.py <br />
אנו מגרילים 2 תמונות מתקיית התמונות באופן רנדומלי. <br />
ותמונות אלה אנו מריצים את חלק 1 של האלגוריתם. מציגים את ההתאמות עם קווים. <br />  
תמונה לדוגמא לתוצאות של התאמה בין 2 תמונות. <br />
![image](https://user-images.githubusercontent.com/92544909/233663304-d559d40a-855b-4fd7-b9bb-54f78ec47a95.png) <br />

  ## how to download  <br />
- To download the task from GitHub, you should navigate to the top level of the project , and then a green "Code" download button will be visible on the right.
   Choose the Download ZIP option from the Code pull-down menu. That ZIP file will contain the entire repository content.
  ## how to use  <br />
- After you download the task at zip you need to extract  the zip file , then you need 
  to open IDE and run the files ,then you need to start the main at the file you want then he will start . 
