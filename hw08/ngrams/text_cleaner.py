class TextCleaner:
    """carry out the text pre-processing
    (switching to lowercase, eliminating puntuation)"""
    def __init__(self):
        self.new_line = None
        self.text = []

    def clean_file(self, file):
        for line in file:
            self.new_line = line.strip().lower()
            self.new_line = self.new_line.replace('(', "").replace(')', "")
            self.new_line = self.new_line.replace('"', "")
            self.new_line = self.new_line.replace('-', "")
            self.new_line = self.new_line.replace("mr.", "mr")
            self.new_line = self.new_line.replace("dr.", "dr")
            self.new_line = self.new_line.replace("mrs.", "mrs")
            self.new_line = self.new_line.replace(",", " COMMA")
            split_line = self.new_line.split(" ")
            if split_line != ['']:
                for each in split_line:
                    if each == "":
                        continue
                else:
                    self.text.append(split_line)
