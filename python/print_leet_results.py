
class PrintResults():

    def print_results(self, data):
        print("")
        for k, v in data.items():
            print(f"{k} = {v}")
        # Determine the pass/fail results if they are not in the input data
        if 'output' in data.keys() and 'expected' in data.keys() and 'result' not in data.keys():
            result = 'Pass' if data['output'] == data['expected'] else 'Fail'
            print(f"result={result}")

