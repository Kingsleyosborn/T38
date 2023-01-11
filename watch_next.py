import spacy

# get the most similar one
def check_sim(description):
    nlp = spacy.load('en_core_web_md')
    description = nlp(description)
    chance = 0
    # get the most similar line and return
    for line in content:
        similarity = nlp(line).similarity(description)
        if similarity > chance:
            chance = similarity
            output = line
    return output


f = open("movies.txt", "r+", encoding="utf-8")
content = f.readlines()
f.close()
print("We will help you to find a movie that you describe most alike!")
description = input("Please describe your movie:")
most_suit_one = check_sim(description)
suit_list = most_suit_one.split(" :")
print(f"The most similar movie is {suit_list[0]}")



