# Totally Random Roulette
Roulette game engine algorithm that ensures no possible win condition for end user by use of pseudorandom value manipulation and "sneaky" random number generation specifications.  

ie:  
`# if user inputs 0 as "bet"`  
`NUMBER_GEN = random.randint(1,36)`  
`# pseudorandom number generation for randint(0+1,36) to ensure 0 is not chosen, thus eliminating end user win condition`  

The source for Totally Random Roulette is 100% native Python and is free for uncredited public use.  

## Common Errors
`Error: (Traceback) No module found named colorama`  
Solution:  
`pip install colorama`  
  
`Error (Import)` or `Error (Traceback)`  
`No module found named Fore` or `No module found named fore`  
Note the capitalization of Fore (fore) and:  
`pip install Fore` or `pip install fore`  
If this doesn't work, you may need to try:  
`from colorama install Fore` or `from colorama install fore`  
  
If issues persist, you can contact me: jxcobvfx@outlook.com
