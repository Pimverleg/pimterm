# pimterm

pimterm can be used to find the linux command you need.
for example:

### using the short notation
```bash
pimterm c "how do I ping example.com?"
ping example.com
```

### using the long notation
```bash
pimterm command "how do i remove a file"
rm filename
```

## You can also ask reqular questions:

### using the short notation
```bash
pimterm q  "who is cleopatra?"
Cleopatra was the last active ruler of the Ptolemaic Kingdom of Egypt.
```

### using the long notation
```bash
pimterm question  "what is the capital of the netherlands?"
Amsterdam
```


### Notes

## intallation
Make sure to add your chatgpt key to your system

```bash
pimterm c "how do i add my chatgpt key to my linux instalation?"
echo "export OPENAI_API_KEY='YOUR_API_KEY'" >> ~/.bashrc
```




The ai will try to return only the command needed. Somtimes when the ai feels explenation is needed it will add it in plain text.