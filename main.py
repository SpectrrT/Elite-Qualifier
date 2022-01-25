import time
import enchant 
import nltk

# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words

def suggest(text, all_words):
  dict = enchant.Dict("en_US")
  if text in all_words:
    print(text + ' is a word')
  else:
    print(text + ' is not a word, suggestions for ' + text + " : " + str(dict.suggest(text)))

def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()