
def neural(out)
    # Vectorize the words and Create a common word dataframe
    cvec = CountVectorizer()
    cv_fit = cvec.fit_transform(out['tweet'])
    word_list = cvec.get_feature_names();
    count_list = cv_fit.toarray().sum(axis=0)
    word_dict = dict(zip(word_list,count_list))
    cleaned_df = pd.DataFrame(cv_fit.toarray(), columns= word_list)
    counter = Counter()
    counter.update(word_dict)

    # The maximum number of words to be used. (most frequent)
    MAX_NB_WORDS = 50000

    MAX_SEQUENCE_LENGTH = 280 # First 280 words in each tweet

    EMBEDDING_DIM = 100
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)  # instantiating Tokenizer
    tokenizer.fit_on_texts(out['tweet'].values)  #fit text to values
    word_index = tokenizer.word_index  # replaces every word
    X = tokenizer.texts_to_sequences(out['tweet'].values) # adds index # of every word in a title
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)   # pads each post so every title has 280 length
    model = tf.keras.models.load_model('./saved_model/lstm_rnn_model_')

    # Model Predictions
    ls = []
    for ea_tweet in out['tweet']:
        new_post = [ea_tweet]
        seq = tokenizer.texts_to_sequences(new_post)
        padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
        pred = model.predict(padded)
        # ls.append(pred)
        labels = [0, 1]
        ls.append(labels[np.argmax(pred)])

    return print(ls)

neural(out)
