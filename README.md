# z2a

Guess what three words have in common. BUT! The letters of each work are initiall hidden. The letters are revealed in reverse alphabetical order.

Starting with 'z', if 'z' is in the word then that letter is filled in. Then 'y', then 'x' and so on.

e.g.
For Zoe, you would first see
```
_ _ _
```

So Next you would see
```
Z _ _
```

Then
```
Z o _
```

And finally
```
Z o e
```

This is based on a mini-game from the BBC TV series House of Games hosted by Richard Osman

## Implementation Notes
This first version is pretty basic:

- It uses tqdm as a visual countdown timer for each letter
- It uses ANSI escape sequences for colours and for clearing the screen. I grabbed these codes off of Stackoverflow but I can't find the link so apologies to the original author. The plan is to use something like (colorama)[https://github.com/tartley/colorama] and (terminaltables)[https://robpol86.github.io/terminaltables/index.html] for nicer formatting in the future
- Other than that it's basic python code - my python is rusty so this is a good way to get going again
