with open("test.txt",'r') as f, open('output.txt','w') as fw:
      text = f.read()
      result_string = ''

      words = ["artdoo", "Rina", "mahal"]
      text2 = text.split(".")
      for itemIndex in range(len(text2)):
          for word in words:
              if word in text2[itemIndex]:
                  if text2[itemIndex][0] ==' ':
                      print(text2[itemIndex][1:])
                      result_string += text2[itemIndex][1:]+'. '
                      break
                  else:
                      print(text2[itemIndex])
                      result_string += text2[itemIndex]
                      break
   
