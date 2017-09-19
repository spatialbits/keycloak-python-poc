import jwt

TEST_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJROVN1N2NuVFpsTGlOVTF1TFZuaFdOMFBldGtrbjhOQlB2bWFSQUNpeGVBIn0.eyJqdGkiOiIyMDk4YzY0Ni1lZDUyLTQ0MmYtODJhOC1hYWE1ZjliYWVkZTkiLCJleHAiOjE1MDU4MzgzMjAsIm5iZiI6MCwiaWF0IjoxNTA1ODM3NzIwLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvYXV0aC9yZWFsbXMvbWFzdGVyIiwiYXVkIjoic2VjdXJpdHktYWRtaW4tY29uc29sZSIsInN1YiI6IjAxM2EyYmQzLTdlYTQtNDNhYi1hNjU3LWJiN2UxNTczZThmYiIsInR5cCI6IkJlYXJlciIsImF6cCI6InNlY3VyaXR5LWFkbWluLWNvbnNvbGUiLCJub25jZSI6ImRiYTBjZDk0LWNjNGYtNGU4My04ZWM3LTJkMGExMWQzODcyZiIsImF1dGhfdGltZSI6MTUwNTgzNzcyMCwic2Vzc2lvbl9zdGF0ZSI6IjQ4NDY2ZWMyLWI1ZWUtNDQyOC05N2IyLTJkMWRjNTc1NjhhZiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOltdLCJyZXNvdXJjZV9hY2Nlc3MiOnt9LCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJkZW1vdXNlciIsImVtYWlsIjoiZGVtb3VzZXJAdXNncy5nb3YifQ.aqlC8lUsD07af13BQmoOMb3eVQp3uL7lTcq8m8sGfuTKdtj924zPA9FN8ZxDk9zvQjs7oD61JoQcTJuryDAN9bh2JBcQkSfVIhb4rPBgLBH6_2hn-js2GqzHGxZnVz8RaLbGGF6Cmsw3vFMHMXgkZU1mZNLox_W309Ovvny-JCN0aW9KQH3SPGyjTmgKGsIE55JZk87Dx93ADaIsRMTSS5XXR9RJVvkhqgJ7Fb0M_QUB08JVTQm1MNVmiWouzBFypRdiD2Gq2X9XdT9HmjMBM1d7YDoketStQe2O7-aywHFp3uGyqkWo073V845FJor68BOepHF6WVoteSlVsm6rog'
PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqIiwEvm6rBa/9DbBU5HqVriuPyW6oxdD7yn9vampqpWAGnFUncUfN8sns/nflxUgSnCet9x+F62EUjU226v0GOsBmz9rLQ0c1LMvNse2ZiZSVz+w7RLqz31BZAJenOx0h0Oq05bbIMl/Pe/kDUtB5jSb41fWgEye+kQBic+8jTQFJWpA+7kOKQwmF580S9KDdOl5eiKmvXQ++opeVEraf79c8EuDLQVWnJUcVxKB4leIjFsul2Q6HZfB8WvWW6f5yppy/7F9Fp1JoELT7QaOWjDr2XC3r36F+Jl21YQv9jCQ8MgTJanTa6lhEgKCpnbieKItMMocvsoa2eNq0cltTwIDAQAB
-----END PUBLIC KEY-----
'''
open_token = jwt.decode(TEST_TOKEN, PUBLIC_KEY, audience='security-admin-console')
print(open_token)