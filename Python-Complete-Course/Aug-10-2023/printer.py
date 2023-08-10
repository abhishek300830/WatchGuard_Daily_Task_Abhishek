class PrinterError(RuntimeError):
    pass

class Printer:
    def __init__(self,pages_per_s:float,capacity:int) -> None:
        self.pages_per_s =pages_per_s
        self._capacity = capacity
    
    def print(self,pages):
        if pages>self._capacity:
            raise PrinterError("Printer doesn't have enough capacity")
        self._capacity -= pages
        
        return f"Printed {pages} Pages in {pages/self.pages_per_s:.2f} seconds."
    
    