# once i have the dictionary, I will use the ffg to generate the word cloud image

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
coud.to_file("myfile.jpg")
