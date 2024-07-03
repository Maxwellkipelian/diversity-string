def solution(N):
    import string
    alphabet = string.ascii_lowercase 

k = min(26, N) # type: ignore

q = N // k # type: ignore
r = N % k # type: ignore

result = (alphabet[:k] * q) + alphabet[:r] # type: ignore

return result
Examples
print(solution(10))
print(solution(7))
print(solution(40)) 