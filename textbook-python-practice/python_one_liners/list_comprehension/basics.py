employees = {'Maddalena': 125273, 'Ortensia': 259803, 'Blondelle': 266566, 'Gratia': 56735, 'Olivie': 70653, 'Hyacinthe': 29398, 'Lillian': 192504, 'Elisabet': 204009, 'Olenka': 35155, 'Annabela': 142851, 'Gilbertina': 61829, 'Brandise': 279204, 'Rene': 184396, 'Dotti': 168738, 'Patrizia': 176930, 'Jo-Ann': 130816, 'Paulita': 101756, 'Madelle': 278333, 'Sydel': 46727, 'Betti': 109717, 'Bunnie': 26503, 'Angel': 245538, 'Tallou': 62598, 'Tobey': 81379, 'Chrystel': 236241, 'Barbabra': 252281, 'Chiarra': 131410, 'Theodora': 193158, 'Deirdre': 255832, 'Flori': 128953, 'Dyan': 243440, 'Zita': 90356, 'Aridatha': 213799, 'Gretchen': 48030, 'Iseabal': 156188, 'Ruthy': 72257, 'Dottie': 47478, 'Stefania': 219529, 'Brena': 279280, 'Salaidh': 223891, 'Dulce': 133612, 'Latrena': 179392, 'Celeste': 105644, 'Cristin': 96724, 'Flore': 256659, 'Sibbie': 53104, 'Heloise': 192541, 'Lorinda': 85114, 'Selene': 275843, 'Shawna': 260661}

class EmployeeAnalyzer:
    def __init__(self, employees):
        self.employees = employees
        
    def top_earner_long(self):
        top_earners = []
        for key, val in employees.items():
            if val >= 100000:
                top_earners.append((key,val))
        return top_earners

    def top_earner_one_line(self):
        
        return [(key, val) for key, val in employees.items() if val >= 100000]

# should return: True
analyzer = EmployeeAnalyzer(employees)
print(analyzer.top_earner_long() == analyzer.top_earner_one_line())

# ================================================================================================================

search_engine_text = "Using list information to find words with High Information Value. Search engines rank textual information according to its relevance to a user query. To accomplish this, search engines analyze the content of the text to be searched. All text consists of words. Some words provide a lot of information about the content of the text—and others don’t. Examples for the former are words like white, whale, Captain, Ahab (Do you know the text?). Examples for the latter are words like is, to, as, the, a, or how, because most texts contain those words. Filtering out words that don’t contribute a lot of meaning is common practice when implementing search engines. A simple heuristic is to filter out all words with three characters or less."


class HighInformationWord:
    def __init__(self, search_engine_text):
        self.search_engine_text = search_engine_text
    
    # one-liner creates a list of lists by using two nested list comprehension expressions:
        # 1. inner list comprehension [x for x in line.split() if len(x) > 3] uses the split() function to divide the a given line into a sequence of words. It then iterates over each of the words x and add them to the list if they have more than 3 characters
        # 2. the outer list comprehension expression `for line in search_engine_text.split('\n')` creates the string line used in the previous statement again, it uses the split() function to divide the text on the newline characters \n.
    def high_information_words_long(self):
        high_information = []
        # Split the text into lines
        lines = search_engine_text.split('\n')
        # Iterate over each line
        for line in lines:
            words = line.split()  # Split the line into words
            filtered_words = []  # List to hold words longer than 3 characters
            # Iterate over each word in the line
            for word in words:
                if len(word) > 3:  # Check if the word length is greater than 3
                    filtered_words.append(word)  # Add the word to the filtered list
            high_information.append(filtered_words)  # Add the filtered words to the main list
        
        return high_information
    
    def high_information_words(self):
        
        return [[x for x in line.split() if len(x) > 3] for line in search_engine_text.split('\n')]

# should return true
high_information = HighInformationWord(search_engine_text)
print(high_information.high_information_words() == high_information.high_information_words_long())


# ================================================================================================================



