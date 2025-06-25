arn = "arn:aws:iam::123456789012:user/johndoe"

print(arn.split("/")) # split by "/" output: ['arn:aws:iam:123456789012:user', 'johndoe']

print(arn.split("/")[0]) # output first part: 'arn:aws:iam:123456789012:user'

print(arn.split("/")[1]) # output second part: 'johndoe'