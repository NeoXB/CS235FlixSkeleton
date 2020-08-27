class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__actor_colleague = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def actor_colleague(self) -> list:
        return self.__actor_colleague

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        if (self.__actor_full_name == None and other.__actor_full_name != None):
            return "None" < other.__actor_full_name
        elif (other.__actor_full_name == None and self.__actor_full_name != None):
            return self.__actor_full_name < "None"
        elif (self.__actor_full_name != None and other.__actor_full_name != None):
            return self.__actor_full_name < other.__actor_full_name
        else:
            return "None" < "None"

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if not isinstance(colleague, Actor):
            raise Exception("Only Actors can be added as colleagues")
        self.__actor_colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if not isinstance(colleague, Actor):
            return False
        else:
            return colleague in self.__actor_colleague
