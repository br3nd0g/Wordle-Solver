# Wordle-Solver
A small python programme that helps solve the daily Wordle (at https://www.nytimes.com/games/wordle/index.html) with user input

It receive the letters known from users and the letters' positions (if the user knows the position), and then searches through a .txt file of all english 5 letter words to find suitable words. 

It is rather messy in my opinion, and i think i could make it more effective. I am sure there is a better way to do it but this was my solution lol :)

Try it [here](https://replit.com/@brendawg/Automatic-Wordle-Solver?v=1).

## Next Steps
I probably will update this to make it somewhat better, and if i think of a better way to do it i will probably implement that. ~~I am probably gonna add something that lets you input letters that you know *aren't* in the word, so it can filter the results down even more.~~

### Updates
I added an extra loop and input which takes the letters the user knows aren't in the word, and checks every word to make sure it doesn't contain them.
