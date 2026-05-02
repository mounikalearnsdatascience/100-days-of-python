def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_score = (
        combined_names.count('t') +
        combined_names.count('r') +
        combined_names.count('u') +
        combined_names.count('e')
    )
    
    love_score = (
        combined_names.count('l') +
        combined_names.count('o') +
        combined_names.count('v') +
        combined_names.count('e')
    )
    
    final_score = int(str(true_score) + str(love_score))
    
    print(final_score)
  
calculate_love_score("Kanye West", "Kim Kardashian")
