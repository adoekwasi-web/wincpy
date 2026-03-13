
import os
import (This is an GitHub example)

import (This is a new Line))
def random_koala_fact():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data_fp = open(os.path.join(module_path, "facts.json"), "r")
    facts = json.load(data_fp)
    return random.choice(facts)
