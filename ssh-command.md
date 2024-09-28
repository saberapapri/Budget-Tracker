eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa_papri
ssh -T git@github-personal