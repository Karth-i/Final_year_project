# -*- coding: utf-8 -*-
"""Working_interface.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/187v9ms9vIa47yZEhZDcUTC8Jz8C-xaxE
"""
sentiment = 0



from google.colab import drive
drive.mount('/content/drive')

model_path = r'/content/drive/My Drive/your_folder/model1'  # Update with the correct path
loaded_model = keras.models.load_model(model_path)

loaded_model

#path=  r"https://colab.research.google.com/drive/1LKT64aVQ2fNVJZ1OJz4e4loF3vJE2e7W?usp=drive_link"

# Function to extract English words from the chat history
def extract_english_words(text):
    english_words = []
    english_pattern = re.compile(r'\b[a-zA-Z]+\b')
    english_words = english_pattern.findall(text)
    return english_words

# Function to process the uploaded chat history
def process_whatsapp_file(file_path):
    user_messages = defaultdict(list)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_user = None
    for line in lines:
        parts = line.split(' - ')
        if len(parts) > 1:
            user_message = parts[1].strip()
            user_parts = user_message.split(': ')
            if len(user_parts) > 1:
                user = user_parts[0].strip()
                message = ': '.join(user_parts[1:]).strip()

                if user != current_user:
                    current_user = user
                    if not user_messages[current_user]:
                        user_messages[current_user] = []

                english_words = extract_english_words(message)
                user_messages[current_user].extend(english_words)

    return user_messages,sentiment

# Function to predict the sentiment of the chat history
def predict_sentiment(chat_history):
    # Preprocess the chat history
    inputs = tokenizer(chat_history, return_tensors="pt", truncation=True, padding=True, max_length=150, return_attention_mask=True)
    input_ids = inputs['input_ids'].to('cuda')
    attention_mask = inputs['attention_mask'].to('cuda')

    # Use the saved model1 to predict the sentiment
    # predictions = loaded_model.predict(tf.expand_dims(input_ids, axis=0))
    # predicted_labels = np.argmax(predictions, axis=1)

    return 0

# Streamlit interface
st.title("Chat Sentiment Analysis")

uploaded_file = st.file_uploader("Upload your chat history (.txt)")

if uploaded_file is not None:
    # Process the uploaded chat history
    user_messages = process_whatsapp_file(uploaded_file)

    # Predict the sentiment of the chat history
    sentiment = predict_sentiment(" ".join(user_messages["Karthi"]))

    # Display the predicted sentiment
    if sentiment == 0:
        st.write("The predicted sentiment is positive.")
    elif sentiment == 1:
        st.write("The predicted sentiment is neutral.")
    else:
        st.write("The predicted sentiment is negative.")

#!streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py





