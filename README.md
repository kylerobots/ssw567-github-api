# ssw567-github-api

[![Build Status](https://app.travis-ci.com/kylerobots/ssw567-github-api.svg?branch=HW05a_Mocking)](https://app.travis-ci.com/kylerobots/ssw567-github-api)

A SSW 567 project to retrieve information from GitHub's API.

This provides a function that, given a username, will return a dictionary containing the list of repositories that
user has and the number of commits per each repository. An example usage is shown below.

```
from get_user_info import getUserInfo

result = getUserInfo('kylerobots')
print(result)
```

This would print something like this:
```
{'algorithms': 30, 'ground-texture-sim': 30, 'hello-ssw567': 2, 'k-armed-bandit': 30, 'kylerobots.github.io': 30, 'manual-image-transformation': 30, 'mnist-viewer': 30, 'ssw567-github-api': 1, 'ssw567-triangle-classification': 10, 'ssw567-triangle-qa': 16, 'turtlesim_teleop': 30}
```
