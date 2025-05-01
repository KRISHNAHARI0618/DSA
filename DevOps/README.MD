## Shell Scripting

- For accessing the virtual machine ```ssh -i priavte-key username@publicip```
- keygeneration ```ssh-keygen -t rsa 2048 -f peddireddydevOps```
- *.ssh* directory --> create a file called config

```
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/peddireddy.pem

Host github.com-t
  HostName github.com
  User git
  IdentityFile ~/.ssh/peddireddy.pem
```
- How to push existing directory to github


```
git init **Initializes the git repo in local**
create a repo in git hub server
git commit -m "commit id "
git branch -M main
git remote add origin github-repo-url
git push -u origin main

```

## Shebang #!/bin/bash/
- How to excute the scripts we need to give shebang

## Concepts :
- Variables
  - var1=$1, var2=$2 echo "$2"
- Data Types
  - We dont have data types in shell script 
  - Boolean 
    - 0 --> Failure
    - 1 --> Success
  - Array = ("shell" "bash" "zsh" "sh" "ksh")
- Conditions
- Loops
- Functions

## read command 
- Read command will read the data from terminal and it will store data in variable
- 
- 