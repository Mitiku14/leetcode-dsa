class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
     
        kelvin = celsius * 1.80 + 32.00
        fahrenheit = celsius + 273.15
        return [fahrenheit, kelvin]
        
