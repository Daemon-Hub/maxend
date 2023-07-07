def ispalindrome(string: str) -> bool:
	return True if string == string[::-1] else False


strings = ["лепсспел", "helloworld", "abcba"]
for s in strings:
	print(s, " - ", ispalindrome(s))
