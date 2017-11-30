import json
import random
import string

alphabet = string.digits + string.ascii_uppercase  # + string.punctuation


class ArbitraryStruct:
    def __init__(self, special_string, depth_levels=range(2, 5),
                 nodes_count=(2, 4), min_special_string_deep=3):
        """
        Determines the initial parameters of the structure
        :param special_string:
        :param depth_levels:
        :param nodes_count:
        :param min_special_string_deep:
        """
        # Possible values of nodes/branches numbers
        self.nodes_count = nodes_count
        self.special_string = special_string
        # Levels depth between minimum(3) and maximum(5)
        self.depth = random.choice(depth_levels)

        # Depth on which can occur special string
        self.sstr_depth = min_special_string_deep
        # Creation of structure
        self.struct = self.structure(self.depth, random.choice(self.nodes_count))

    def __str__(self):
        """
        JSON compatible representation of resulting structure
        """
        return json.dumps(self.struct, indent=4, separators=(',', ': '))

    def structure(self, depth_level, nodes_count):
        """
        Method for creation of arbitrary structure
        with parameters defined in the __init__
        """
        # Count of containers which will be located on this depth_level
        # in the structure(Minimal 1 for intermediate layers)
        containers_count = random.randrange(1, nodes_count)
        # If this is the deepest level, then there will be no containers
        if not depth_level:
            containers_count = 0
        # Generating of list with random location of containers(0) and strings(1)
        containers = [1] * containers_count + [0] * (nodes_count - containers_count)
        random.shuffle(containers)
        # Next condition statement determines the type of result (list or dict)
        # Internal for loop iterates through "container" list and for
        # containers recursively call the "structure" method to generate deeper
        # levels of structure
        if bool(random.getrandbits(1)):
            return [self.random_str(depth_level) if not container
                    else self.structure(depth_level - 1, random.choice(self.nodes_count))
                    for container in containers]
        else:
            return {self.random_str(depth_level): self.random_str(depth_level)
                    if not container
                    else self.structure(depth_level - 1, random.choice(self.nodes_count))
                    for container in containers}

    def random_str(self, depth):
        """
        Creation of (pseudo)randomly generated or unique string
        """
        # Chance of returning unique string instead of random is depends on
        # depth of structure. While depth is under sstr_depth (Minimal depth)
        # chance of special string is equal to 0. For the deepest layer "depth"
        # will be 0, so "2**0=1" and "not random.choice(range(1))" will be True
        if (self.depth - depth + 1) >= self.sstr_depth and \
                not random.choice(range(2 ** depth)):
            self.sstr_depth = float('inf')
            return self.special_string
        # Random string is generating from alphabet with digits, uppercase
        # letters and punctuation symbols
        return ''.join(random.choice(alphabet) for _ in range(random.choice([2, 5])))


if __name__ == "__main__":
    struct = ArbitraryStruct('I am Red Hat')
    print(struct)
