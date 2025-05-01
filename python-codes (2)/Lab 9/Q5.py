ls=["Shivam", "Maharshi", "Yagna", "Soham", "Darshil"]

ls2=list(filter(lambda n:len(n)>=8, ls))

print(f"Here is original list: {ls}\nHere is list of memebers with >=8 characters: {ls2}")
