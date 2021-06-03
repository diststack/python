class Flight:

     def __init__(self,number):
         if not number[:2].isalpha:
             raise ValueError("no airline code")
         self._number = number

     def number(self):
         return self._number
