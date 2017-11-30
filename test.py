import assignment
import json




import unittest


def nested_structure_info(struct, level):
    """
    Provides information about the expanded structure
    "elements_info" - list with all elements and their location
    "layers" - list of nested layers in structure
    """
    # determination of the type of structure
    if isinstance(struct, list):
        struct = enumerate(struct)
    if isinstance(struct, dict):
        struct = struct.iteritems()

    nested_layers = []
    elements_info = []
    # for loop through the structure to get its contents (elements_info)
    # and form list (nested_layers) of possible nested instances
    for key, value in struct:
        if isinstance(value, basestring):
            elements_info.append((level, key, value))
        elif isinstance(value, dict):
            elements_info.append((level, 'DICT', len(value)))
            nested_layers.append(value)
        elif isinstance(value, list):
            elements_info.append((level, 'LIST', len(value)))
            nested_layers.append(value)

    layers_info = elements_info[:]
    layers = [elements_info[:]]
    # Getting information from nested instances
    for value in nested_layers:
        elements, layers = nested_structure_info(value, level + 1)
        elements_info.extend(elements)
        layers.append(layers_info)
    return elements_info, layers


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.test_class = assignment.ArbitraryStruct('I am Red Hat')
        self.test_class_elements, self.test_class_layers = nested_structure_info(self.test_class.struct, 0)

    def tearDown(self):
        self.test_class = None

    def test_special_string(self):
        """Special string is in structure"""
        self.assertIn(True, ['I am Red Hat' in inst
                             for inst in self.test_class_elements], 'missing special string')

    def test_special_string_depth(self):
        """Special string is lying under 2nd(on 3rd or deeper) nested levels"""
        self.assertIn(True, [('I am Red Hat' in inst and inst[0] >= 2)
                             for inst in self.test_class_elements], 'special string live < 3 (nested) levels deep')

    def test_containers(self):
        """Presence of container instances"""
        self.assertIn(True, [('LIST' in inst or 'DICT' in inst)
                             for inst in self.test_class_elements], 'missing sequence or mapping instances')

    def test_branches_numbers(self):
        """Numbers of branches for each node"""
        self.assertIn(True, [len(inst) == 2 or len(inst) == 4
                             for inst in self.test_class_layers], 'wrong number of branches')

    def test_levels_deep(self):
        """Maximum depth level for the structure"""
        self.assertTrue(max(map(lambda x: x[0], self.test_class_elements)) <= 4,
                        'depth of the structure is out of allowed range')

    def test_output_form(self):
        """Check the correctness of translation in JSON"""
        self.assertTrue(json.loads(self.test_class.__str__()) == self.test_class.struct,
                        'wrong output form')


if __name__ == '__main__':
    unittest.main()
