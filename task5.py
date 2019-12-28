a = int(input())
answer = ""

for i in range(a):
	word1 = input()
	word2 = input()
	w1 = set(word1)
	w2 = set(word2)
	res = w1.intersection(w2)
	if len(res) > 0:
		answer = answer + "YES "
	else:
		answer = answer + "NO "

for i in answer.split():
	print(i)