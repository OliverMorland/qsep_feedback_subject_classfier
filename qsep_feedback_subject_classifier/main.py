import phrase_classifier

if __name__ == "__main__":
    # phrase_classifier.create_dataset(samples_per_category=500)
    feed_back_classifier = phrase_classifier.Classifier()
    ans = feed_back_classifier.classify_text("they hung up on me!")
    print(ans)