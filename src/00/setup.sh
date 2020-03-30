#!/bin/bash -e


PYTHON_VERSION=3.7.5


function ask_yes_no {
  while true; do
    echo
    read -t 60 -p "$* [y/n]: " ANS || return 1

    case $ANS in
      [Yy]*)
        return 0
        ;;
      [Nn]*)
        return 1
        ;;
      *)
        printf "\e[31mPlease enter y or n\e[0m\n"
        ;;
    esac
  done
}


# install pyenv
if [ ! -e ~/.pyenv ];then
  echo "Installing pyenv..."
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
  echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bash_profile
fi


# install python
if [ ! -e "${HOME}"/.pyenv/versions/${PYTHON_VERSION} ];then
  if ask_yes_no "Start install Python ${PYTHON_VERSION} OK? "; then
    ~/.pyenv/bin/pyenv install ${PYTHON_VERSION}
    ~/.pyenv/bin/pyenv global ${PYTHON_VERSION}
    ~/.pyenv/bin/pyenv rehash
    ~/.pyenv/shims/pip install -U pip
  fi
else
  echo "Python ${PYTHON_VERSION} is already installed."
fi

