# Python Trivy Report Parse
Python 3 class to parse [Trivy][trivy_website] [json report file][trivy_output_docs] and create useful messages that can be used for an alert message.


## Quick example
```sh
# Create report with image that has vulnerabilities
trivy -q image --format json -o report.json alpine:3.15.0

# Run example python file
python3 example.py
```

[trivy_website]: https://trivy.dev
[trivy_output_docs]: https://aquasecurity.github.io/trivy/v0.48/docs/configuration/reporting/#file