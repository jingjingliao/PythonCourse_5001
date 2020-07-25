import re


class DataAnalysis:
    """keep counts of how many times each language shows up in a data item,
    and how many times each 2-letter country top-level domain signifier
    shows up in an email address"""
    def __init__(self, file):
        self.file = file
        self.total_count = 0
        self.language_counts = {}
        self.top_level_county = {}
        self.read_data(file)

    def read_data(self, file_name):
        """read the data, get the kinds of languages and its counts,
        get the kinds of countries and its counts"""
        INDEX_ZERO = 0
        LANGUAGE = "language"

        country_pattern = r"\.([a-z]{2})[,\t\n]"
        language_index = 0
        try:
            f = open(file_name)
        except FileNotFoundError:
            print("Can't find", file_name)
            return

        line_list = f.readline().strip().split(",")
        for i in range(len(line_list)):
            if line_list[i] == LANGUAGE:
                language_index = i
                break

        for line in f:
            self.total_count += 1  # count the total languages(countries)

            match_country = re.findall(country_pattern, line)
            if match_country:
                if match_country[INDEX_ZERO] in self.top_level_county:
                    self.top_level_county[match_country[INDEX_ZERO]] += 1
                else:
                    self.top_level_county[match_country[INDEX_ZERO]] = 1

            line_split = line.strip().split(",")
            if line_split[language_index] in self.language_counts:
                self.language_counts[line_split[language_index]] += 1
            else:
                self.language_counts[line_split[language_index]] = 1

    def top_n_lang_freqs(self, N):
        self.language_counts = {key: self.language_counts[key]/self.total_count
                                for key in self.language_counts.keys()}

        sorted_language_counts = sorted(
                                        self.language_counts.items(),
                                        key=lambda x: x[1],
                                        reverse=True)

        return sorted_language_counts[:N]

    def top_n_country_tlds_freqs(self, N):
        self.top_level_county = {
                            key: self.top_level_county[key]/self.total_count
                            for key in self.top_level_county.keys()}

        sorted_top_level_county = sorted(
                                        self.top_level_county.items(),
                                        key=lambda x: x[1],
                                        reverse=True)

        return sorted_top_level_county[:N]
