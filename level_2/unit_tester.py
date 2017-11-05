def unit_test(function_to_test, test_input, expected_output):
    try:
        number_of_inputs = len(test_input)
        if type(test_input) == list: function_output = function_to_test(test_input)
        elif number_of_inputs == 1: function_output = function_to_test(test_input)
        elif number_of_inputs == 2: function_output = function_to_test(test_input[0], test_input[1])
        elif number_of_inputs == 3: function_output = function_to_test(test_input[0], test_input[1], test_input[2])
        
    except Exception as error:
        print("Error occurred with test input: [{0}] value: {1}\nError Message: {2}\nCorrect the error and try again.\n"
        .format(type(test_input), test_input, error))
    else:
        test = function_output == expected_output
        print(unit_test_response(test, test_input, function_output, expected_output))
      
def unit_test_response(correct, test_input, function_output, expected_output): 
    score = "Test Passed" if correct else "Test Failed" 
    return "{0}\nInput: {1}\nExpected Output: {2}\nFunction Output: {3}\n".format(score, test_input, expected_output, function_output)

def run_unit_tests(function_to_test, test_list):  
    for test_tuple in test_list:
        test_input, expected_output = test_tuple
        unit_test(function_to_test, test_input, expected_output)

class UnitTester:
  def __init__(self, function, tests):
    self.function_to_test = function
    self.test_list = tests

  def run(self):
    run_unit_tests(self.function_to_test, self.test_list)