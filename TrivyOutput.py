import json
import os.path

class TrivyOutput:
    ''' Load the report json file after checking if it exists 
    '''
    @staticmethod
    def __loadJsonFile(filepath: str):
        check_file = os.path.exists(filepath)

        if check_file is False:
            return False

        f = open(filepath)
        data = json.load(f)
        f.close()

        return data

    ''' Get the json output and make some use of it by grouping the
    vulnerabilities into levels and using emoji to define the highest level.
    Returns a message in the form of an array of lines that can be used in a
    notification
    '''
    def parseOutput(filepath: str):
        data = TrivyOutput.__loadJsonFile(filepath)
        if data is False:
            return False

        crit = []
        high = []
        med = []
        msg_lines = []
        
        for i in data['Results']:
            if 'Vulnerabilities' in i:
                for vuln in i['Vulnerabilities']:
                    match vuln['Severity']:
                        case "CRITICAL":
                            crit.append(vuln)
                        case "HIGH":
                            high.append(vuln)
                        case "MEDIUM":
                            med.append(vuln)
                        case _:
                            print(vuln['VulnerabilityID'] + ' vulnerability level is unknown')

        icon = ':white_check_mark:'
        if (len(med) > 0):
            icon = ':bell:'
            msg_lines.append('Found ' + str(len(med)) +  ' medium vulnerabilities')

        if (len(high) > 0):
            icon = ':warning:'
            msg_lines.append('Found ' + str(len(high)) +  ' high vulnerabilities')

        if (len(crit) > 0):
            icon = ':siren:'
            msg_lines.append('Found ' + str(len(crit)) +  ' critical vulnerabilities')

        msg_lines.insert(0, icon + ' Scan results for ' + data['ArtifactName'])

        return msg_lines;