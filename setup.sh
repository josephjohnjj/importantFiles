. ~/parsec/build/install/bin/parsec.env.sh
. ~/module.sh
. ~/.bashrc

export GPG_TTY=$(tty)
eval $(ssh-agent) && ssh-add ~/.ssh/leconte

