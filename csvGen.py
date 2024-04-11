from LLM.gemini import Gemini
import csv

class Generator_csv:
    def __init__(self):
        self.llm = Gemini()

    def generate_csv(self, data, output_path):
        prompt = f'''
        System Message : You are an AI assistant that generates csv files and doesn't talk

        Instruction : You should go through the information of the below company and return me a csv in the format(Email,First Name,Last Name,Company,Description)
        To craft an email of a person use this method (firstname.lastname@companywebsite)

        Information : {data}

        '''
        result = self.llm.get_response(prompt)
        lines = result.split('\n')

        with open(output_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for line in lines:
                fields = line.split(',')
                csv_writer.writerow(fields)

        print("CSV file has been created successfully.")
        return True