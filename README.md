## Recaptchav3py

This package provides a basic solver function for 
Google's Recaptcha V3.

## Requirements 

Python 3.7+

Main dependencies:
  <ul>
    <li>requests for handling the HTTP rqeuests.</li>
    <li>re for handling regex text searches.</li>
  </ul>

## Installation

```bash
pip install recaptchav3py
```

## Usage

```python
from recaptchav3py import RecaptchaV3Solver


# Solve Recaptcha V3 without using your own anchor URL
solver_without_custom_url = RecaptchaV3Solver()

print(solver_without_custom_url.solve())

# This is what a Recaptcha V3 anchor url should look like
custom_anchor_url = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lc31pYUAAAAACSh0pZlRjRiKHqdrExHgdlhrNoh&co=aHR0cHM6Ly93d3cubWludG9zLmNvbTo0NDM.&hl=en&v=vP4jQKq0YJFzU6e21-BGy3GP&size=invisible&badge=bottomleft&cb=gbid8icu4p7u'

# Or solve it using your own anchor URL for improved accuracy and integrity
solver_with_custom_url = RecaptchaV3Solver(
    anchor_url=custom_anchor_url,
)

print(solver_with_custom_url.solve())
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
