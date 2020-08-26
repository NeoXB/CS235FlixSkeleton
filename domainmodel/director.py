class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        return other.__director_full_name == self.__director_full_name

    def __lt__(self, other):
        if (self.__director_full_name == None and other.__director_full_name != None):
            return "None" < other.__director_full_name
        elif (other.__director_full_name == None and self.__director_full_name != None):
            return self.__director_full_name < "None"
        elif (self.__director_full_name != None and other.__director_full_name != None):
            return self.__director_full_name < other.__director_full_name
        else:
            return "None" < "None"

    def __hash__(self):
        return hash(self.__director_full_name)
