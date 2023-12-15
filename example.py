from TrivyOutput import TrivyOutput

class example():
    # Create json report file with example command:
    # trivy -q image --format json -o report.json alpine:3.15.0
    output = TrivyOutput.parseOutput(filepath='report.json')

    # Array of message lines
    print(output)