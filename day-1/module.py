class Day1:
    @classmethod
    def calculate_calibration_value(self, line_of_text):
        first = None
        last = None
        
        for character_index in range(len(line_of_text)):
            character = line_of_text[character_index]
            
            if character.isdigit():
                last = character
                if first == None:
                    first = last

        if first == None:
            return 0
    
        return int(first + last)

    @classmethod
    def sum_calibration_values(self, multiline_text):
        # split into multiple lineslines = multiline_text.splitlines()
        lines = list(filter(None, multiline_text.splitlines()))
        
        # run calculate calibration value
        calibration_values = map(Day1.calculate_calibration_value, lines)
        
        # sum all calibration values
        return sum(calibration_values)